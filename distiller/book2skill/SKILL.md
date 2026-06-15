---
name: book2skill
description: Use when distilling reusable analysis capability from a book — the "book2skill" pipeline. Orchestrates ingest → multi-perspective open-coding → atomic-method abstraction (with RAG firewall) → similarity clustering → playbook (orchestration) extraction → promotion, producing one attributed immutable run plus the book's playbook(s) and atomic methods. Triggers include "run book2skill on <book>", "distill skills from this book", "extract skills from <book>".
---

# book2skill — orchestrator (entrypoint)

One book in → one attributed, immutable **run** + its **playbook(s)** (the assembled skill) + its **atomic methods** (the parts). Run every stage in subagents so book text never floods the main context.

## Locations (relative to this repo root)
- Book file(s): provided by you (the path you pass in)
- Runs: `runs/<date>-<book>-<ver>/`
- Method registry (atoms, vocabulary): `skills/_methods/`
- Playbook registry (assembled skills, eval unit): `skills/`
- Roster (config): `distiller/roster.md`
- Data contracts: `distiller/contracts/{code,skill,playbook,taxonomy,provenance}.md`

## Procedure
1. Open a run dir; write its folder-entry config (book / `extraction_contract` / roster version / params) per `Contracts/provenance.md`.
2. **book2skill-ingest-book** → `book-text/` (anchored) + `thesis.md`.
3. For each perspective in `roster.md`, run **book2skill-read-perspective** in **PARALLEL** → `codes/<persp>.jsonl`.
4. **book2skill-abstract-to-method** per perspective → `skills-raw/` (atomic method cards).
5. **book2skill-synthesize-taxonomy** → `taxonomy-v0.md` + `run-log.md` (similarity clusters for dedup/nav — **not** the orchestration).
6. **book2skill-trace-playbook** → the book's playbook(s): spine + gated steps referencing the atoms. ← **the high-value product**.
7. **book2skill-promote-to-registry** → atoms to `Methods/`, playbooks to `Playbooks/`; backfill run entry.

## Guardrails
- All stages in subagents; only compact summaries return to the caller.
- **Two products**: atomic methods (vocabulary, retrieved top-k, not blanket-injected) + playbook(s) (the assembly, the eval unit). The playbook is the point; atoms are its parts.
- Runs are immutable; to change method, bump `extraction_contract` + start a NEW run.
- Feed `run-log.md` findings (saturation / firewall / roster) back into the sub-skills + `roster.md` (二阶 loop).
