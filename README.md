# Crypto perpetuals trading: research repository

A literature base for a bot that trades crypto perpetual futures directionally on horizons of minutes to hours. The reference instrument is the SOL perpetual on Kalshi. This repository holds research only; there is no trading code here.

## Where to start

1. `synthesis/OVERVIEW.md`: a map of the field and what moves prices at these horizons.
2. `synthesis/SIGNALS.md`: a ranked backlog of candidate signals and methods, with the evidence behind each.
3. `INDEX.md`: every source note, grouped by topic, with evidence grades and links to downloaded PDFs.
4. `topics/<topic>/SYNTHESIS.md`: what one topic's literature says, taken together.

## Layout

| Path | Contents |
|---|---|
| `topics/<NN-slug>/notes/` | One markdown note per source: key insight, method, data, results, signal construction, relevance, caveats |
| `topics/<NN-slug>/SYNTHESIS.md` | Topic-level synthesis |
| `sources/<NN-slug>/` | Raw open-access PDFs, named to match their notes. Kept on the local machine only and excluded from git; in a fresh clone the `pdf` links are dead and `tools/build_index.py` reports them as missing. Each note's `url` records where its PDF came from |
| `synthesis/` | Cross-topic documents |
| `CONVENTIONS.md` | Note template, evidence grades and grounding rules |
| `explorations/` | Dated question lists and the assessments written from them. Not indexed, so conclusions drawn from the corpus are never retrieved as if they were sources |
| `tools/build_index.py` | Rebuilds `INDEX.md` and `VALIDATION.md`, and checks notes and PDFs |
| `tools/kb.py` | Builds and queries a local search index and concept graph over the notes, syntheses and PDF text |

## How to read the evidence

Each note carries an `evidence_grade` from A (peer-reviewed or replicated, with out-of-sample tests or realistic costs) to D (practitioner claim with no rigorous test), and an `access` field saying whether the note was written from the full text, the abstract only, or a secondary description. Treat abstract-only and secondary notes as pointers to read, not as verified summaries.

Notes were written by research agents from sources fetched on 2026-11-22. Check a note against its source before relying on a specific number.

## Maintaining

After adding or editing notes, run:

```
python3 tools/build_index.py
```

## Searching and exploring

`tools/kb.py` builds a local index in `.kb/` (derived; delete it and rebuild at any time). It needs `pdftotext` from poppler and a virtual environment:

```
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/kb.py build --project ../jup-charts   # --project also indexes a codebase's markdown, to compare research with what is built
.venv/bin/python tools/kb.py build --encoder BAAI/bge-small-en-v1.5   # a smaller encoder: about a minute
```

Nothing is sent anywhere: text extraction, full-text ranking, embeddings and re-ranking all run on this machine.

### Model weights

The weights live inside this folder, in `.kb/models`, and nowhere else on the machine. `tools/kb.py` sets `HF_HOME` to that path before it loads anything, so the usual `~/.cache/huggingface` is not used. Set `HF_HOME` yourself to keep them somewhere else.

| Model | Used for | Size on disk |
|---|---|---|
| `BAAI/bge-large-en-v1.5` | Default encoder: one 1,024-number vector per chunk and per query | 1.3 GB |
| `BAAI/bge-reranker-v2-m3` | Cross-encoder that re-scores the 40 best candidates of each query | 2.3 GB |
| `BAAI/bge-small-en-v1.5` | Optional faster encoder (`--encoder BAAI/bge-small-en-v1.5`) | 0.1 GB |

A model is downloaded from Hugging Face the first time a command needs it, and only then. Once all three are present, searching works with no network: `HF_HUB_OFFLINE=1 .venv/bin/python tools/kb.py search "..."`. The files are in the Hugging Face cache layout (`.kb/models/hub/models--BAAI--<name>/snapshots/<revision>/`, with the bytes in `.kb/models/hub/blobs`).

`.kb/` is in `.gitignore`, so the weights, vectors and index are never committed. They are also not backed up with the notes: deleting `.kb/` costs a 3.7 GB download and about ten minutes of rebuilding, and nothing else. To move the index to another machine without downloading again, copy `.kb/` whole.

The vectors are tied to the encoder that made them. Each encoder has its own `vectors-<name>.npy`, and `.kb/encoder.txt` names the one in use.

How search works. Each PDF is converted to text and cut into chunks of about 350 tokens by page, leaving out reference lists and number-only tables; notes are one chunk per section and syntheses one per heading. Every chunk gets a vector from a local encoder (default `BAAI/bge-large-en-v1.5`, about 6 minutes for 32,000 chunks on an Apple M-series GPU) and an entry in a SQLite full-text index. A query is ranked both ways, the two rankings are merged by reciprocal rank, and the 40 best candidates are re-scored by a cross-encoder (`BAAI/bge-reranker-v2-m3`), whose score from 0 to 1 is what is printed. Vectors sit in one NumPy file per encoder and are compared exhaustively, which is exact and takes milliseconds at this size. A rebuild re-embeds only chunks whose text changed, and `embed --encoder NAME` switches encoder without touching the rest.

| Command | What it answers |
|---|---|
| `search "question" [--kind paper] [--topic 04,28] [--grade AB] [--full]` | Passages from notes, PDF text, syntheses and project docs, ranked by keyword and meaning together. Several questions can be given at once. |
| `ask questions.txt --out DIR [--floor 0.5]` | A reading pack for a file of questions: each question's ten best passages in full, each passage printed once, passages below the relevance floor left out |
| `show <part of a note slug>` | One note with its tags, the signals it supports, what it cites and is cited by, and its nearest notes |
| `hubs` | Works that the other downloaded papers cite most |
| `bridges` | Pairs of notes from distant topics that say closely related things and are not linked |
| `tags` | Concepts that span the most topics |
| `orphans` | Graded notes that describe a signal and are absent from `synthesis/SIGNALS.md` |
| `gaps` | Signal notes least similar to anything in the indexed project docs |
| `path A B` | The chain of tags, citations and synthesis links between two notes |

The graph is built only from what the repository states: front-matter tags and topics, links in the synthesis documents, the candidate-signal tables, and citations found by matching each note's title in the text of the other PDFs. A search hit from a PDF is the source text; a hit from a note is an agent's summary of it. Rebuild after adding notes.
