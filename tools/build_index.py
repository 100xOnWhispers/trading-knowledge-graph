#!/usr/bin/env python3
"""Build INDEX.md from note front matter and validate the repository.

Usage: python3 tools/build_index.py [--check-only]

Checks each note under topics/*/notes/ against CONVENTIONS.md: required front
matter keys, allowed values, required body headings, and that any referenced
PDF exists and really is a PDF. Writes INDEX.md and VALIDATION.md at the root.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_KEYS = [
    "title", "authors", "year", "venue", "url", "pdf", "access",
    "source_type", "evidence_grade", "topic", "asset_class", "horizon", "tags",
]
ALLOWED = {
    "access": {"full-text", "abstract-only", "secondary"},
    "source_type": {"peer-reviewed", "working-paper", "industry-research",
                    "practitioner", "documentation", "book"},
    "evidence_grade": {"A", "B", "C", "D"},
    "asset_class": {"crypto", "futures", "equities", "fx", "options", "multi"},
    "horizon": {"tick", "seconds", "minutes", "hours", "daily", "multi-day", "n/a"},
}
HEADINGS = [
    "## Key insight", "## Method", "## Data and sample", "## Reported results",
    "## Signal construction", "## Relevance to SOL perpetuals at minutes to hours",
    "## Caveats",
]


def parse_front_matter(text):
    """Return (dict, body) or (None, text) when there is no front matter."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    meta = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        value = m.group(2).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[m.group(1)] = value.strip()
    return meta, text[end + 4:]


def is_pdf(path):
    try:
        with open(path, "rb") as fh:
            return b"%PDF" in fh.read(1024)
    except OSError:
        return False


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def main():
    notes, problems = [], defaultdict(list)
    referenced_pdfs = set()
    for path in sorted(ROOT.glob("topics/*/notes/*.md")):
        rel = path.relative_to(ROOT).as_posix()
        meta, body = parse_front_matter(path.read_text(encoding="utf-8", errors="replace"))
        if meta is None:
            problems[rel].append("no front matter")
            continue
        for key in REQUIRED_KEYS:
            if not meta.get(key):
                problems[rel].append(f"missing key: {key}")
        for key, allowed in ALLOWED.items():
            if meta.get(key) and meta[key] not in allowed:
                problems[rel].append(f"{key} has unexpected value: {meta[key]!r}")
        if meta.get("url") and not meta["url"].startswith("http"):
            problems[rel].append(f"url is not a web address: {meta['url']!r}")
        topic_dir = path.parts[-3]
        if meta.get("topic") and meta["topic"] != topic_dir:
            problems[rel].append(f"topic {meta['topic']!r} does not match folder {topic_dir!r}")
        pdf = meta.get("pdf", "none")
        has_pdf = False
        if pdf and pdf.lower() != "none":
            pdf_path = ROOT / pdf
            referenced_pdfs.add(pdf_path.resolve())
            if not pdf_path.is_file():
                problems[rel].append(f"pdf not found: {pdf}")
            elif not is_pdf(pdf_path):
                problems[rel].append(f"file is not a PDF: {pdf}")
            else:
                has_pdf = True
        for heading in HEADINGS:
            if heading not in body:
                problems[rel].append(f"missing section: {heading}")
        words = len(body.split())
        if words < 150:
            problems[rel].append(f"very short note ({words} words)")
        notes.append({**meta, "file": rel, "topic_dir": topic_dir, "has_pdf": has_pdf, "words": words})

    orphan_pdfs = [p.relative_to(ROOT).as_posix() for p in sorted(ROOT.glob("sources/**/*.pdf"))
                   if p.resolve() not in referenced_pdfs]
    bad_files = [p.relative_to(ROOT).as_posix() for p in sorted(ROOT.glob("sources/**/*"))
                 if p.is_file() and p.suffix.lower() == ".pdf" and not is_pdf(p)]
    topics = sorted(p.name for p in (ROOT / "topics").iterdir() if p.is_dir())
    no_synthesis = [t for t in topics if not (ROOT / "topics" / t / "SYNTHESIS.md").is_file()]

    # Same work noted under more than one topic (matched on normalized title).
    by_title = defaultdict(list)
    for n in notes:
        key = re.sub(r"[^a-z0-9]+", " ", n.get("title", "").lower()).strip()
        if key:
            by_title[key].append(n["file"])
    duplicates = {k: v for k, v in by_title.items() if len(v) > 1}

    report = ["# Validation report", "",
              f"- Notes: {len(notes)}",
              f"- Notes with a downloaded PDF: {sum(n['has_pdf'] for n in notes)}",
              f"- Notes with problems: {len(problems)}",
              f"- Topics without SYNTHESIS.md: {len(no_synthesis)}",
              f"- PDFs not referenced by any note: {len(orphan_pdfs)}",
              f"- Files named .pdf that are not PDFs: {len(bad_files)}",
              f"- Works noted under more than one topic: {len(duplicates)}", ""]
    for label, counter in (("Access", Counter(n.get("access", "?") for n in notes)),
                           ("Evidence grade", Counter(n.get("evidence_grade", "?") for n in notes)),
                           ("Source type", Counter(n.get("source_type", "?") for n in notes))):
        report.append(f"**{label}:** " + ", ".join(f"{k} {v}" for k, v in sorted(counter.items())))
        report.append("")
    if problems:
        report += ["## Problems by note", ""]
        for rel, items in sorted(problems.items()):
            report.append(f"- `{rel}`: " + "; ".join(items))
        report.append("")
    for title, items in (("Topics without SYNTHESIS.md", no_synthesis),
                         ("PDFs not referenced by any note", orphan_pdfs),
                         ("Files named .pdf that are not PDFs", bad_files)):
        if items:
            report += [f"## {title}", ""] + [f"- `{i}`" for i in items] + [""]
    if duplicates:
        report += ["## Works noted under more than one topic", ""]
        for files in duplicates.values():
            report.append("- " + ", ".join(f"`{f}`" for f in files))
        report.append("")
    report_text = "\n".join(report)
    print(report_text)
    if "--check-only" in sys.argv:
        return

    (ROOT / "VALIDATION.md").write_text(report_text + "\n", encoding="utf-8")

    out = ["# Index of source notes", "",
           "Generated by `tools/build_index.py`. Do not edit by hand.", "",
           f"{len(notes)} notes across {len(topics)} topics; "
           f"{sum(n['has_pdf'] for n in notes)} have a downloaded PDF.", "",
           "Evidence grades: A peer-reviewed or replicated with out-of-sample tests or costs; "
           "B serious empirical work without replication; C limited evidence; "
           "D practitioner claim without rigorous test. See `CONVENTIONS.md`.", "",
           "## Topics", "", "| Topic | Notes | PDFs | Synthesis |", "|---|---|---|---|"]
    per_topic = defaultdict(list)
    for n in notes:
        per_topic[n["topic_dir"]].append(n)
    for t in topics:
        synth = f"[synthesis](topics/{t}/SYNTHESIS.md)" if t not in no_synthesis else "missing"
        out.append(f"| [{t}](#{t}) | {len(per_topic[t])} | {sum(n['has_pdf'] for n in per_topic[t])} | {synth} |")
    out.append("")
    for t in topics:
        out += [f"## {t}", "", "| Year | Authors | Title | Type | Grade | Access | Horizon | PDF |",
                "|---|---|---|---|---|---|---|---|"]
        for n in sorted(per_topic[t], key=lambda n: (n.get("year", ""), n.get("authors", ""))):
            pdf = f"[pdf]({n['pdf']})" if n["has_pdf"] else ""
            out.append("| " + " | ".join([
                cell(n.get("year", "")), cell(n.get("authors", "")),
                f"[{cell(n.get('title', n['file']))}]({n['file']})",
                cell(n.get("source_type", "")), cell(n.get("evidence_grade", "")),
                cell(n.get("access", "")), cell(n.get("horizon", "")), pdf]) + " |")
        out.append("")
    (ROOT / "INDEX.md").write_text("\n".join(out), encoding="utf-8")
    print(f"\nWrote INDEX.md and VALIDATION.md ({len(notes)} notes).")


if __name__ == "__main__":
    main()
