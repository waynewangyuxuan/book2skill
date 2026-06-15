---
name: book2skill-read-perspective
description: Sub-skill of book2skill. Open-code a book through ONE reader perspective (drawn from the roster) into a codes.jsonl, applying novelty pressure and a saturation stop. Parametrized by perspective; invoked once per perspective (in parallel) by the book2skill orchestrator (Stage B).
---

# book2skill-read-perspective (Stage B — parametrized open coding)

Grounded-theory open coding. **Takes one perspective** (from `…/Book-Skill-Distillation/skills/roster.md`) + anchored text, codes close to the text. The perspective is a parameter; this skill body does not change as the roster evolves.

## Inputs
- `book-text/` (+ `thesis.md`)
- one perspective persona (identity / hunting question / extract / ignore / kind lean) from `roster.md`

## Procedure
- Walk chapters in reading order (default: by chapter; split overlong chapters into ~4k-token windows). Reading order may follow the book — anti-TOC comes from multi-perspective + abstraction, not from shuffling.
- Per chunk, emit 0..n **codes** appended to `codes/<persp>.jsonl` (schema = `Contracts/code.md`).
- Carry a running list of already-extracted codes and apply **novelty pressure**: each pass, extract something not yet captured and non-obvious.
- **Saturation**: stop this perspective after K consecutive chunks with no new distinct code (v1 K=2; known not to trigger on long books — v2 candidate: rolling marginal-novelty gate).

## Output
`codes/<persp>.jsonl`.

## Guardrails
- `transferable_method` must strip the book's example (RAG firewall starts here).
- `[¶1]` is a header, not body; don't fabricate numbers from missing tables.
