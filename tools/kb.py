#!/usr/bin/env python3
"""Search index and concept graph over this repository. Runs locally: no key, no network after the first build.

    .venv/bin/python tools/kb.py build [--project DIR] [--also FILE ...] [--encoder NAME]
    .venv/bin/python tools/kb.py embed --encoder NAME            switch encoder without rebuilding the rest
    .venv/bin/python tools/kb.py search "what happens after a liquidation cascade" [-k 8] [--kind paper]
                                        [--topic 04,28] [--grade AB] [--horizon minutes,hours] [--full]
    .venv/bin/python tools/kb.py ask questions.txt --out DIR     a reading pack: top passages per question, each once
    .venv/bin/python tools/kb.py show kim-2026-quarter-hour      a note with everything linked to it
    .venv/bin/python tools/kb.py hubs                            works the other sources cite most
    .venv/bin/python tools/kb.py bridges                         close note pairs from distant topics
    .venv/bin/python tools/kb.py tags                            concepts that span several topics
    .venv/bin/python tools/kb.py orphans                         graded signals the ranked backlog never links
    .venv/bin/python tools/kb.py gaps                            signals furthest from the project's own docs
    .venv/bin/python tools/kb.py path A B                        how two notes or tags connect

What is indexed (`kind`): `note` (one chunk per section), `paper` (the text of each downloaded
PDF, by page), `synthesis` (topic and cross-topic documents) and, with --project, `project`
(the markdown of a codebase, so the research can be compared with what is already built).

Search is hybrid: SQLite full-text ranking and a local embedding model, merged by reciprocal
rank, and the merged candidates are then re-scored by a local cross-encoder. Any
sentence-transformers model name works as the encoder; each encoder's vectors are kept, so
switching back costs nothing. The graph is built from what the repository already states, with no model guessing:
front-matter tags and topics, links from synthesis documents, the candidate-signal tables, and
citations found by looking for each note's title in every other paper's text.

Everything derived lives in `.kb/` and can be deleted and rebuilt. Needs `pdftotext` (poppler)
and the packages in tools/requirements.txt.
"""
import argparse
import hashlib
import os
import json
import re
import sqlite3
import subprocess
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

from build_index import parse_front_matter

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / ".kb"
os.environ.setdefault("HF_HOME", str(KB / "models"))
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
ENCODER = "BAAI/bge-large-en-v1.5"  # a few minutes for 32,000 chunks on an M-series GPU
FAST = "BAAI/bge-small-en-v1.5"  # about a minute; slightly weaker
RERANKER = "BAAI/bge-reranker-v2-m3"
CHUNK = 1500  # characters, about 350 tokens: inside the embedding model's 512-token window
SKIP_DIRS = {"node_modules", ".venv", ".git", "build", "dist", ".pytest_cache", ".secrets", ".agents", ".claude", "kalshi"}
STOP = set("a an and are as at be by do does for from how in is it of on or that the to what when which with".split())
META = ("topic", "evidence_grade", "horizon", "asset_class", "year", "source_type", "access", "tags")


def norm(text):
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def pack(paragraphs, limit=CHUNK):
    """Join paragraphs into chunks of at most `limit` characters, cutting an oversized one at sentence ends."""
    out, buf = [], ""
    for p in paragraphs:
        while len(p) > limit:
            cut = max(p.rfind(". ", 0, limit) + 1, limit // 2) if ". " in p[:limit] else limit
            paragraphs_head, p = p[:cut].strip(), p[cut:].strip()
            if buf:
                out.append(buf)
                buf = ""
            out.append(paragraphs_head)
        if buf and len(buf) + len(p) + 1 > limit:
            out.append(buf)
            buf = ""
        buf = f"{buf}\n{p}" if buf else p
    return out + ([buf] if buf else [])


def sections(body):
    """(heading, text) pairs of a markdown body. Text before the first heading has an empty heading."""
    parts = re.split(r"(?m)^(#{1,3} .+)$", body)
    pairs = [("", parts[0])] + [(parts[i].lstrip("# ").strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
    return [(h, t.strip()) for h, t in pairs if t.strip()]


def markdown_chunks(body):
    for heading, text in sections(body):
        for piece in pack([p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]):
            yield heading, piece


def pdf_text(pdf):
    out = KB / "text" / pdf.relative_to(ROOT / "sources").with_suffix(".txt")
    if not out.exists() or out.stat().st_mtime < pdf.stat().st_mtime:
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), str(out)], capture_output=True, timeout=300)
        except subprocess.TimeoutExpired:
            pass
        if not out.exists():
            out.write_text("")
    return out.read_text(encoding="utf-8", errors="replace")


def paper_chunks(text):
    """(page label, text) pairs. Leaves out fragments, number tables and reference lists."""
    pieces = []  # (page, paragraph)
    for number, page in enumerate(text.split("\f"), 1):
        page = re.sub(r"-\n(?=[a-z])", "", page)
        pieces += [(number, re.sub(r"\s+", " ", p).strip()) for p in re.split(r"\n\s*\n", page) if p.strip()]
    total, seen, start, buf = sum(len(p) for _, p in pieces) or 1, 0, None, []
    out = []

    def flush():
        for piece in pack(buf):
            letters = sum(c.isalpha() for c in piece)
            listing = len(re.findall(r"\b(?:19|20)\d\d\b", piece)) >= 10 and piece.count(",") >= 15
            if len(piece) >= 200 and letters >= 0.45 * len(piece) and not (listing and seen > 0.4 * total):
                out.append((f"p.{start}", piece))

    size = 0
    for page, paragraph in pieces:
        if buf and size + len(paragraph) > CHUNK:
            flush()
            buf, size = [], 0
        if not buf:
            start = page
        buf.append(paragraph)
        size += len(paragraph) + 1
        seen += len(paragraph)
    if buf:
        flush()
    return out


def collect(project, also, skip):
    """Every document as (fields, [(section, text), ...]), and the full text of each paper for citation matching."""
    docs, full = [], {}
    notes = []
    for path in sorted(ROOT.glob("topics/*/notes/*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8", errors="replace"))
        if meta is None:
            continue
        key = f"{path.parts[-3]}/{path.stem}"
        fields = {"key": key, "path": path.relative_to(ROOT).as_posix(), "title": meta.get("title", path.stem),
                  **{k: meta.get(k, "") for k in META}, "authors": meta.get("authors", ""), "pdf": meta.get("pdf", "none")}
        fields["topic"] = path.parts[-3]
        notes.append(fields)
        docs.append(({**fields, "kind": "note"}, sections(body)))
    with ThreadPoolExecutor(8) as pool:
        wanted = [n for n in notes if n["pdf"].lower() != "none" and (ROOT / n["pdf"]).is_file()]
        for n, text in zip(wanted, pool.map(lambda n: pdf_text(ROOT / n["pdf"]), wanted)):
            full[n["key"]] = text
            docs.append(({**n, "kind": "paper", "path": n["pdf"]}, paper_chunks(text)))
    for path in sorted(ROOT.glob("topics/*/SYNTHESIS.md")) + sorted((ROOT / "synthesis").glob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        topic = path.parts[-2] if path.name == "SYNTHESIS.md" else ""
        docs.append(({"kind": "synthesis", "key": rel, "path": rel, "title": f"Synthesis: {topic or path.stem}",
                      "topic": topic}, list(markdown_chunks(path.read_text(encoding="utf-8")))))
    files = [Path(f).resolve() for f in also or []]
    if project:
        base = Path(project).resolve()
        files += [p for p in sorted(base.rglob("*.md")) if not set(p.relative_to(base).parts[:-1]) & skip]
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        chunks = list(markdown_chunks(text)) if path.suffix == ".md" else [("", c) for c in pack(text.split("\n\n"))]
        docs.append(({"kind": "project", "key": str(path), "path": str(path), "title": f"Project: {path.name}", "topic": ""},
                     chunks))
    return docs, notes, full


def device():
    import torch

    return "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"


def encoder(name):
    import torch
    from sentence_transformers import SentenceTransformer

    half = {"torch_dtype": torch.float16} if device() != "cpu" else {}
    model = SentenceTransformer(name, device=device(), model_kwargs=half)
    model.max_seq_length = 512
    return model


def encode_query(model, name, query):
    """Query-side prompt: the model's own when it defines one, the BGE instruction for BGE models."""
    if "query" in (model.prompts or {}):
        return model.encode(query, prompt_name="query", normalize_embeddings=True)
    prompt = "Represent this sentence for searching relevant passages: " if "bge" in name.lower() else ""
    return model.encode(prompt + query, normalize_embeddings=True)


def store(name):
    slug = name.replace("/", "--")
    return KB / f"vectors-{slug}.npy", KB / f"hashes-{slug}.txt"


def embed(db, name):
    """Unit vectors for every chunk, reusing the vector of any text this encoder has embedded before."""
    texts = [f"{title}. {section}\n{text}" for title, section, text in db.execute(
        "SELECT title, section, text FROM chunks JOIN docs ON docs.id=doc ORDER BY chunks.id")]
    keys = [hashlib.sha1(t.encode()).hexdigest() for t in texts]
    vectors_path, hashes_path = store(name)
    cache = dict(zip(hashes_path.read_text().split(), np.load(vectors_path))) if vectors_path.exists() else {}
    todo = sorted((i for i, k in enumerate(keys) if k not in cache), key=lambda i: len(texts[i]))
    print(f"embedding {len(todo)} of {len(texts)} chunks with {name}", flush=True)
    if todo:
        model = encoder(name)
        for at in range(0, len(todo), 2048):
            part = todo[at:at + 2048]
            for i, vector in zip(part, model.encode([texts[i] for i in part], batch_size=32, normalize_embeddings=True)):
                cache[keys[i]] = vector
            print(f"  {at + len(part)}", flush=True)
    np.save(vectors_path, np.array([cache[k] for k in keys], dtype=np.float32))
    hashes_path.write_text("\n".join(keys))
    (KB / "encoder.txt").write_text(name)  # the index switches to this encoder only once every vector exists


def note_links(path, text):
    """Keys of the notes a markdown file links to."""
    found = []
    for target in re.findall(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)", text):
        parts = (path.parent / target).resolve().parts
        if len(parts) >= 3 and parts[-2] == "notes":
            found.append(f"{parts[-3]}/{Path(parts[-1]).stem}")
    return found


def table_rows(text, heading):
    """Cells of each body row of the first table under a `## heading`."""
    block = re.search(rf"(?ms)^## {re.escape(heading)}.*?$(.*?)(?=^## |\Z)", text)
    rows = [re.split(r"(?<!\\)\|", line.strip().strip("|")) for line in (block.group(1) if block else "").splitlines()
            if line.lstrip().startswith("|")]
    return [[c.strip() for c in r] for r in rows[2:]]


def build_graph(db, notes, full):
    nodes, edges = {}, set()
    known = {n["key"] for n in notes}
    for n in notes:
        nodes[n["key"]] = ("note", n["title"], {k: n[k] for k in ("topic", "evidence_grade", "horizon", "year")})
        nodes[f"topic:{n['topic']}"] = ("topic", n["topic"], {})
        edges.add((n["key"], f"topic:{n['topic']}", "in_topic"))
        for tag in filter(None, (t.strip().lower() for t in n["tags"].split(","))):
            nodes[f"tag:{tag}"] = ("tag", tag, {})
            edges.add((n["key"], f"tag:{tag}", "tagged"))
    by_title = defaultdict(list)
    for n in notes:
        by_title[norm(n["title"])].append(n["key"])
    same = {k: set(group) for group in by_title.values() for k in group}
    edges |= {(a, b, "same_work") for group in by_title.values() for a in group for b in group if a < b}
    # A paper cites a note's work when that work's title appears in the paper's text. A short title
    # also needs its first author's surname just before it.
    targets = [(norm(n["title"]), norm(n["authors"].split(",")[0].split(";")[0]), n["key"]) for n in notes]
    for key, text in full.items():
        flat = norm(text)
        for title, surname, other in targets:
            if other in same[key] or len(title) < 12:
                continue
            at = flat.find(title, len(title) + 200)  # past the paper's own title block
            if at >= 0 and (len(title) >= 25 or (surname and surname in flat[max(0, at - 200):at])):
                edges.add((key, other, "cites"))
    for path in sorted(ROOT.glob("topics/*/SYNTHESIS.md")) + sorted((ROOT / "synthesis").glob("*.md")):
        text, rel = path.read_text(encoding="utf-8"), path.relative_to(ROOT).as_posix()
        nodes[f"doc:{rel}"] = ("doc", rel, {})
        edges |= {(f"doc:{rel}", k, "mentions") for k in note_links(path, text) if k in known}
        ranked = path.name == "SIGNALS.md"
        for row in table_rows(text, "All candidates, best first" if ranked else "Candidate signals and methods"):
            if len(row) < 5:
                continue
            name = row[1] if ranked else row[0]
            ident = f"rank:{int(row[0]):02d}" if ranked and row[0].isdigit() else f"signal:{path.parts[-2]}:{name[:60]}"
            fields = ({"rank": row[0], "predicts": row[2], "inputs": row[3], "grade": row[4], "risk": row[5]} if ranked
                      else {"inputs": row[1], "horizon": row[2], "grade": row[3], "topic": path.parts[-2]})
            nodes[ident] = ("ranked" if ranked else "signal", name, fields)
            edges |= {(ident, k, "supports") for k in note_links(path, row[-1]) if k in known}
    db.executemany("INSERT INTO nodes VALUES(?,?,?,?)", [(i, k, label, json.dumps(m)) for i, (k, label, m) in nodes.items()])
    db.executemany("INSERT INTO edges VALUES(?,?,?)", sorted(edges))
    print("graph:", dict(Counter(k for k, _, _ in nodes.values())), dict(Counter(e[2] for e in edges)))


def build(args):
    KB.mkdir(exist_ok=True)
    docs, notes, full = collect(args.project, args.also, SKIP_DIRS | set(args.skip or []))
    empty = [d["key"] for d, chunks in docs if d["kind"] == "paper" and not chunks]
    if empty:
        print(f"{len(empty)} PDFs gave no text (scanned or protected):", ", ".join(empty))
    path = KB / "kb.sqlite"
    path.unlink(missing_ok=True)
    db = sqlite3.connect(path)
    db.executescript("""
        CREATE TABLE docs(id INTEGER PRIMARY KEY, kind, key, path, title, topic, grade, horizon, asset, year, source_type, access, tags);
        CREATE TABLE chunks(id INTEGER PRIMARY KEY, doc INTEGER, section, text);
        CREATE VIRTUAL TABLE fts USING fts5(title, text, content='', tokenize='porter unicode61');
        CREATE TABLE nodes(id PRIMARY KEY, kind, label, meta);
        CREATE TABLE edges(src, dst, kind);
        CREATE INDEX edges_src ON edges(src); CREATE INDEX edges_dst ON edges(dst); CREATE INDEX chunks_doc ON chunks(doc);
    """)
    count = 0
    for number, (d, chunks) in enumerate(docs):
        db.execute("INSERT INTO docs VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            number, d["kind"], d["key"], d["path"], d["title"], d.get("topic", ""), d.get("evidence_grade", ""),
            d.get("horizon", ""), d.get("asset_class", ""), d.get("year", ""), d.get("source_type", ""), d.get("access", ""),
            d.get("tags", "")))
        for section, text in chunks:
            db.execute("INSERT INTO chunks VALUES(?,?,?,?)", (count, number, section, text))
            db.execute("INSERT INTO fts(rowid, title, text) VALUES(?,?,?)", (count, f"{d['title']} {section}", text))
            count += 1
    build_graph(db, notes, full)
    db.commit()
    print("chunks:", dict(db.execute("SELECT kind, count(*) FROM chunks JOIN docs ON docs.id=doc GROUP BY kind").fetchall()))
    embed(db, args.encoder)


def embed_only(args):
    embed(sqlite3.connect(KB / "kb.sqlite"), args.encoder)


def active():
    return (KB / "encoder.txt").read_text().strip()


def load():
    if not (KB / "kb.sqlite").exists() or not (KB / "encoder.txt").exists():
        sys.exit("No index yet. Run: .venv/bin/python tools/kb.py build")
    db = sqlite3.connect(KB / "kb.sqlite")
    db.row_factory = sqlite3.Row
    vectors = np.load(store(active())[0], mmap_mode="r")
    if len(vectors) != db.execute("SELECT count(*) FROM chunks").fetchone()[0]:
        sys.exit(f"The vectors of {active()} do not match the index. Run: tools/kb.py embed --encoder {active()}")
    return db, vectors


def allowed(db, args):
    """Ids of the chunks whose document passes the filters."""
    where, values = ["1"], []
    for column, value in (("kind", args.kind), ("horizon", args.horizon), ("asset", args.asset)):
        if value:
            items = value.split(",")
            where.append(f"{column} IN ({','.join('?' * len(items))})")
            values += items
    if args.topic:
        where.append("(" + " OR ".join("topic LIKE ?" for _ in args.topic.split(",")) + ")")
        values += [f"{t}%" for t in args.topic.split(",")]
    if args.grade:
        where.append(f"grade IN ({','.join('?' * len(args.grade))})")
        values += list(args.grade)
    sql = f"SELECT chunks.id FROM chunks JOIN docs ON docs.id=doc WHERE {' AND '.join(where)}"
    return np.array([r[0] for r in db.execute(sql, values)], dtype=np.int64)


class Finder:
    """Hybrid retrieval: full-text and embedding rankings merged by reciprocal rank, then a cross-encoder."""

    def __init__(self, args):
        self.db, self.vectors = load()
        self.ids = allowed(self.db, args)
        self.keep = set(self.ids.tolist())
        self.model = encoder(active())
        self.judge = None
        if not args.no_rerank:
            from sentence_transformers import CrossEncoder

            self.judge = CrossEncoder(RERANKER, device=device(), max_length=512)

    def find(self, query, k, per_doc, pool):
        """Up to k (row, score) pairs, best first. One work filed under several topics is returned once."""
        scores = defaultdict(float)
        sims = self.vectors[self.ids] @ np.asarray(encode_query(self.model, active(), query), dtype=np.float32)
        for rank, i in enumerate(self.ids[np.argsort(-sims)[:60]]):
            scores[int(i)] += 1 / (60 + rank)
        words = [w for w in re.findall(r"[A-Za-z0-9]+", query) if w.lower() not in STOP and len(w) > 1]
        if words:
            hits = self.db.execute("SELECT rowid FROM fts WHERE fts MATCH ? ORDER BY bm25(fts, 3.0, 1.0) LIMIT 400",
                                   (" OR ".join(f'"{w}"' for w in words),))
            for rank, i in enumerate([r[0] for r in hits if r[0] in self.keep][:60]):
                scores[i] += 1 / (60 + rank)
        order = sorted(scores.items(), key=lambda kv: -kv[1])
        fetch = "SELECT chunks.id AS chunk, * FROM chunks JOIN docs ON docs.id=doc WHERE chunks.id=?"
        if self.judge:
            order = order[:pool]
            rows = [self.db.execute(fetch, (i,)).fetchone() for i, _ in order]
            marks = self.judge.predict([(query, f"{r['title']}. {r['section']}\n{r['text']}") for r in rows], batch_size=16)
            order = sorted(((i, float(s)) for (i, _), s in zip(order, marks)), key=lambda kv: -kv[1])
        out, per, texts = [], Counter(), set()
        for i, score in order:
            row = self.db.execute(fetch, (i,)).fetchone()
            if per[row["doc"]] >= per_doc or row["text"] in texts:
                continue
            texts.add(row["text"])
            per[row["doc"]] += 1
            out.append((row, score))
            if len(out) >= k:
                break
        return out, words


def search(args):
    finder = Finder(args)
    for query in args.query:
        print(f"\n=== {query}")
        found, words = finder.find(query, args.k, args.per_doc, args.pool)
        for shown, (row, score) in enumerate(found, 1):
            text = row["text"]
            if not args.full:
                at = min([p for p in (text.lower().find(w.lower()) for w in words) if p >= 0] or [0])
                text = ("…" if at > 80 else "") + " ".join(text[max(0, at - 80):max(0, at - 80) + args.width].split()) + "…"
            tag = " ".join(x for x in (row["grade"], str(row["year"]), row["horizon"], row["topic"]) if x)
            print(f"[{shown}] {score:.4f} {row['kind']:9} {tag}\n    {row['title']}\n    {row['path']} :: {row['section']}\n    {text}")


def ask(args):
    """Answer a file of questions with a reading pack: each question's best passages in full, each passage once.

    Lines of the file that start with `#` are headings and are copied through. A passage that an
    earlier question already printed is listed by its id only. A passage the cross-encoder scores
    below --floor is left out, so a question the corpus cannot answer shows as such.
    """
    finder = Finder(args)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    parts, seen, number, total = [[]], {}, 0, 0
    for line in Path(args.questions).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            block = [f"\n{line}"]
        else:
            number += 1
            found, _ = finder.find(line, args.k, args.per_doc, args.pool)
            found = [(row, score) for n, (row, score) in enumerate(found) if score >= args.floor or n == 0]
            block = [f"\n## Q{number}. {line}"]
            for row, score in found:
                slug = Path(row["path"]).stem if row["kind"] != "synthesis" else row["path"]
                tag = " ".join(x for x in (row["kind"], row["grade"], str(row["year"] or ""), row["horizon"], row["topic"][:2]) if x)
                head = f"[C{row['chunk']}] {score:.2f} {tag} {slug} :: {row['section']}"
                if row["chunk"] in seen:
                    block.append(f"{head} (text under Q{seen[row['chunk']]})")
                else:
                    seen[row["chunk"]] = number
                    block.append(f"{head}\n{' '.join(row['text'].split())}")
            if found and found[0][1] < args.floor:
                block.insert(1, f"(nothing scored above {args.floor}; the best passage follows)")
        size = sum(len(x) + 1 for x in block)
        if parts[-1] and sum(len(x) + 1 for x in parts[-1]) + size > args.part:
            parts.append([])
        parts[-1] += block
        total += size
    for n, part in enumerate(parts, 1):
        (out / f"pack-{n:02d}.md").write_text("\n".join(part) + "\n", encoding="utf-8")
    print(f"{number} questions, {len(seen)} passages, {total:,} characters in {len(parts)} files under {out}")


def note_vectors(db, vectors, wanted=("Key insight", "Method", "Signal construction")):
    """One unit vector per note: the mean of its chosen sections."""
    rows = db.execute("SELECT docs.key, chunks.id FROM chunks JOIN docs ON docs.id=doc WHERE kind='note' AND section IN "
                      f"({','.join('?' * len(wanted))})", wanted).fetchall()
    groups = defaultdict(list)
    for key, i in rows:
        groups[key].append(i)
    keys = sorted(groups)
    m = np.array([np.asarray(vectors[groups[k]]).mean(axis=0) for k in keys])
    return keys, m / np.linalg.norm(m, axis=1, keepdims=True)


def graph(db):
    nodes = {r["id"]: r for r in db.execute("SELECT * FROM nodes")}
    out, into = defaultdict(lambda: defaultdict(list)), defaultdict(lambda: defaultdict(list))
    for src, dst, kind in db.execute("SELECT src, dst, kind FROM edges"):
        out[src][kind].append(dst)
        into[dst][kind].append(src)
    return nodes, out, into


def describe(nodes, key):
    n = nodes[key]
    m = json.loads(n["meta"])
    if n["kind"] != "note":
        return f"{key}  {n['label']}"
    return f"{m['evidence_grade']} {m['year']} {m['horizon']:9} {key}\n      {n['label']}"


def ranked_by(into, key):
    return sorted(s for s in into[key]["supports"] if s.startswith("rank:"))


def show(args):
    db, vectors = load()
    nodes, out, into = graph(db)
    keys, m = note_vectors(db, vectors)
    for key in [k for k in keys if args.name in k]:
        print("\n" + describe(nodes, key))
        print("  tags:", ", ".join(t[4:] for t in out[key]["tagged"]))
        for label, items in (("supports", [f"{s}  {nodes[s]['label']}" for s in sorted(into[key]["supports"])]),
                             ("mentioned in", sorted(d[4:] for d in into[key]["mentions"])),
                             ("same work as", sorted(out[key]["same_work"] + into[key]["same_work"])),
                             ("cites", sorted(out[key]["cites"])), ("cited by", sorted(into[key]["cites"]))):
            if items:
                print(f"  {label}:\n    " + "\n    ".join(items))
        sims = m @ m[keys.index(key)]
        near = [(keys[j], sims[j]) for j in np.argsort(-sims)[1:9]]
        print("  nearest notes:\n    " + "\n    ".join(f"{s:.2f} {k}" for k, s in near))


def hubs(args):
    db, _ = load()
    nodes, out, into = graph(db)
    groups = {}
    for key in (k for k, n in nodes.items() if n["kind"] == "note"):
        group = sorted({key, *out[key]["same_work"], *into[key]["same_work"]})
        groups.setdefault(group[0], set()).update(c for g in group for c in into[g]["cites"])
    for key, citing in sorted(groups.items(), key=lambda kv: -len(kv[1]))[:args.k]:
        topics = Counter(c.split("/")[0][:2] for c in citing)
        print(f"{len(citing):3} cited by; topics {dict(topics.most_common(6))}; backlog {ranked_by(into, key) or '-'}\n    "
              + describe(nodes, key))


def centred(m, mean=None):
    """Remove the direction every vector shares, so cosine spreads out and compares content."""
    m = m - (m.mean(axis=0) if mean is None else mean)
    return m / np.linalg.norm(m, axis=1, keepdims=True)


def bridges(args):
    """Note pairs from topics that are far apart, each among the other's nearest notes, with no stated link.

    A pair is scored by how much closer the two notes are than each is to the other's topic as a
    whole. Notes by the same first author are skipped: those are usually one work filed twice.
    """
    db, vectors = load()
    nodes, out, into = graph(db)
    keys, m = note_vectors(db, vectors)
    m = centred(m)
    sims = m @ m.T
    topics = [k.split("/")[0] for k in keys]
    names = sorted(set(topics))
    member = np.array([[t == name for t in topics] for name in names], dtype=np.float32)
    to_topic = sims @ (member / member.sum(axis=1, keepdims=True)).T  # note by topic: mean similarity
    index = np.array([names.index(t) for t in topics])
    between = (member / member.sum(axis=1, keepdims=True)) @ to_topic  # topic by topic
    far = between <= np.median(between[~np.eye(len(names), dtype=bool)])
    excess = sims - (to_topic[:, index] + to_topic[:, index].T) / 2
    near = np.argsort(-sims, axis=1)[:, 1:args.near + 1]
    linked = {(a, b) for a in keys for kind in ("cites", "same_work") for b in out[a][kind]}
    grades = [json.loads(nodes[k]["meta"])["evidence_grade"] for k in keys]
    shown = 0
    for flat in np.argsort(-excess, axis=None):
        i, j = divmod(int(flat), len(keys))
        if i >= j or not far[index[i], index[j]] or j not in near[i] or i not in near[j]:
            continue
        if grades[i] not in args.grade or grades[j] not in args.grade:
            continue
        if keys[i].split("/")[1].split("-")[0] == keys[j].split("/")[1].split("-")[0]:
            continue
        if (keys[i], keys[j]) in linked or (keys[j], keys[i]) in linked:
            continue
        if set(ranked_by(into, keys[i])) & set(ranked_by(into, keys[j])):
            continue
        print(f"\n+{excess[i, j]:.2f} closer than their topics (similarity {sims[i, j]:.2f})\n    "
              + describe(nodes, keys[i]) + "\n    " + describe(nodes, keys[j]))
        shown += 1
        if shown >= args.k:
            break


def tags(args):
    db, _ = load()
    nodes, out, into = graph(db)
    rows = []
    for key, n in nodes.items():
        if n["kind"] == "tag":
            notes = into[key]["tagged"]
            rows.append((len({k.split("/")[0] for k in notes}), len(notes), n["label"], notes))
    for spread, count, label, notes in sorted(rows, reverse=True)[:args.k]:
        ranked = sum(bool(ranked_by(into, k)) for k in notes)
        print(f"{spread:2} topics {count:3} notes {ranked:3} in backlog  {label}")


def orphans(args):
    """Graded notes that describe a signal and are not linked from the ranked backlog."""
    db, _ = load()
    nodes, out, into = graph(db)
    rows = db.execute("SELECT docs.key, text, grade, horizon FROM chunks JOIN docs ON docs.id=doc WHERE kind='note' "
                      "AND section='Signal construction'").fetchall()
    shown = 0
    for key, text, grade, horizon in sorted(rows, key=lambda r: (r[2], r[0])):
        if grade not in args.grade or text.lower().startswith("not a signal") or (args.horizon and horizon not in args.horizon.split(",")):
            continue
        if ranked_by(into, key) or any(ranked_by(into, k) for k in out[key]["same_work"] + into[key]["same_work"]):
            continue
        local = [s for s in into[key]["supports"] if s.startswith("signal:")]
        print(describe(nodes, key) + f"\n      topic table: {'yes' if local else 'no'}; cited by {len(into[key]['cites'])}\n      "
              + " ".join(text.split())[:args.width])
        shown += 1
    print(f"\n{shown} notes")


def gaps(args):
    """Signal notes whose closest passage in the project's own docs is the least similar."""
    db, vectors = load()
    nodes, out, into = graph(db)
    project = db.execute("SELECT chunks.id, docs.path, section FROM chunks JOIN docs ON docs.id=doc WHERE kind='project'").fetchall()
    if not project:
        sys.exit("No project documents in the index. Rebuild with --project DIR.")
    keys, m = note_vectors(db, vectors, ("Key insight", "Signal construction"))
    theirs = np.asarray(vectors[[r[0] for r in project]])
    mean = np.vstack([m, theirs]).mean(axis=0)
    sims = centred(m, mean) @ centred(theirs, mean).T
    signal = {k: t for k, t in db.execute("SELECT docs.key, text FROM chunks JOIN docs ON docs.id=doc WHERE kind='note' "
                                          "AND section='Signal construction'")}
    shown = 0
    for i in np.argsort(sims.max(axis=1)):
        key, meta = keys[i], json.loads(nodes[keys[i]]["meta"])
        if meta["evidence_grade"] not in args.grade or signal.get(key, "").lower().startswith("not a signal"):
            continue
        if args.horizon and meta["horizon"] not in args.horizon.split(","):
            continue
        best = project[int(sims[i].argmax())]
        print(f"{sims[i].max():.2f} nearest: {Path(best[1]).name} :: {best[2][:50]}; backlog {ranked_by(into, key) or '-'}\n    "
              + describe(nodes, key) + "\n      " + " ".join(signal.get(key, "").split())[:args.width])
        shown += 1
        if shown >= args.k:
            break


def path(args):
    import networkx as nx

    db, _ = load()
    g = nx.Graph()
    g.add_edges_from((s, d, {"kind": k}) for s, d, k in db.execute("SELECT src, dst, kind FROM edges WHERE kind != 'in_topic'"))
    ends = []
    for name in (args.a, args.b):
        found = [n for n in g if name in n]
        if not found:
            sys.exit(f"nothing matches {name!r}")
        ends.append(min(found, key=len))
    try:
        steps = nx.shortest_path(g, *ends)
    except nx.NetworkXNoPath:
        sys.exit("no path")
    for a, b in zip(steps, steps[1:]):
        print(f"{a}\n   --{g[a][b]['kind']}--")
    print(steps[-1])


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("--project", help="also index the markdown of this codebase as kind `project`")
    b.add_argument("--also", nargs="*", help="more project files to index")
    b.add_argument("--skip", nargs="*", help="more directory names to leave out of --project")
    e = sub.add_parser("embed", help="embed the existing chunks with another encoder and switch to it")
    for parser in (b, e):
        parser.add_argument("--encoder", default=ENCODER, help=f"sentence-transformers model (default {ENCODER}; {FAST} is quick)")
    s = sub.add_parser("search")
    s.add_argument("query", nargs="+", help="one or more questions, each answered separately")
    s.add_argument("--full", action="store_true", help="print whole chunks")
    q = sub.add_parser("ask", help="write a reading pack for a file of questions")
    q.add_argument("questions", help="text file, one question per line; lines starting with # are headings")
    q.add_argument("--out", required=True, help="directory for the pack files")
    q.add_argument("--part", type=int, default=150_000, help="most characters per pack file")
    q.add_argument("--floor", type=float, default=0.05, help="leave out passages the cross-encoder scores below this")
    for parser in (s, q):
        parser.add_argument("--kind", help="note, paper, synthesis, project (comma-separated)")
        parser.add_argument("--topic", help="topic number prefixes, comma-separated")
        parser.add_argument("--asset", help="asset classes, comma-separated")
        parser.add_argument("--per-doc", type=int, default=2, help="most chunks shown from one document")
        parser.add_argument("--no-rerank", action="store_true", help="skip the cross-encoder; scores are then rank-fusion scores")
        parser.add_argument("--pool", type=int, default=40, help="candidates the cross-encoder re-scores")
    sub.add_parser("show").add_argument("name")
    for name in ("hubs", "bridges", "tags", "orphans", "gaps"):
        sub.add_parser(name)
    pa = sub.add_parser("path")
    pa.add_argument("a")
    pa.add_argument("b")
    for name, parser in sub.choices.items():
        parser.add_argument("-k", type=int, default={"search": 8, "ask": 10}.get(name, 25))
        parser.add_argument("--grade", default="" if name in ("search", "ask") else "AB", help="evidence grades, e.g. AB")
        parser.add_argument("--horizon", help="horizons, comma-separated")
        parser.add_argument("--width", type=int, default=320, help="characters of text shown")
        parser.add_argument("--near", type=int, default=15, help="bridges: each note must be among the other's N nearest")
    args = p.parse_args()
    {"build": build, "embed": embed_only, "search": search, "ask": ask, "show": show, "hubs": hubs, "bridges": bridges, "tags": tags, "orphans": orphans,
     "gaps": gaps, "path": path}[args.command](args)


if __name__ == "__main__":
    main()
