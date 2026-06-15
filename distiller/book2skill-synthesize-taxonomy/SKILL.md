---
name: book2skill-synthesize-taxonomy
description: Sub-skill of book2skill. Cluster a run's raw skills bottom-up into an emergent taxonomy, find cross-perspective merge groups, and write the run-log of process findings. Invoked by the book2skill orchestrator (Stage D–E).
---

# book2skill-synthesize-taxonomy (Stage D–E)

Cluster across perspectives into a taxonomy + dedup + run-log. **Bottom-up; no preset categories.**

> This is a **similarity clustering** (for dedup + navigation), **NOT** the book's orchestration logic. The orchestration (which method when, gates, dependencies) is `book2skill-trace-playbook`'s job — a different, more valuable structure.

## Input
`skills-raw/*`.

## Procedure
- Cluster bottom-up into emergent categories (don't impose a preset taxonomy) → `taxonomy-v0.md`.
- Cross-perspective dedup → merge groups (list members + a canonical name; **do not delete files**).
- Write `run-log.md`: per-perspective yield, interrogation of process anomalies, recommendations for v2 / the roster.

## Output
`taxonomy-v0.md`, `run-log.md` (shapes = `Contracts/taxonomy.md`).

## Guardrails
- Category is an output, not an input; never use the book's TOC as the taxonomy.
