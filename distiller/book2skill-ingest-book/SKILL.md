---
name: book2skill-ingest-book
description: Sub-skill of book2skill. Convert a book file (epub/pdf) into anchored per-chapter text plus a one-paragraph thesis, as the source material for a book2skill run. Invoked by the book2skill orchestrator (Stage A).
---

# book2skill-ingest-book (Stage A)

Turn a book into extractable, traceable source text.

## Input
A book file (epub / pdf).

## Procedure
- epub = zip + XHTML: take content chapters in spine order, strip HTML. pdf: extract text, split by chapter.
- Write per-chapter `book-text/ch01.md …`, prefixing each paragraph with a `[¶N]` anchor (1-based within chapter) so skills can cite `ch03¶12`. Skip / clearly mark front & back matter (TOC, copyright, index); don't number them as content chapters.
- Read intro + conclusion and write `thesis.md` (≤120 words: the book's **core argument**, NOT its table of contents) — this tunes perspectives downstream.

## Output
`book-text/ch*.md`, `thesis.md`. (code anchors per `Contracts/code.md`.)

## Guardrails
- Tables/figures embedded as images are lost; note this in `book-text/_folder`… and downstream must not fabricate numbers from missing tables.
- Each chapter's `[¶1]` is usually a running header, not body.
