---
name: book2skill-promote-to-registry
description: Sub-skill of book2skill. Govern a run's raw outputs into the canonical registries — atomic methods to Methods/, assembled playbooks to Playbooks/ — collapsing duplicates, re-applying the firewall, and stamping provenance. Invoked by the book2skill orchestrator (final stage).
---

# book2skill-promote-to-registry

Govern raw outputs into the canonical registries, with provenance (selective coding).

## Input
- `skills-raw/*` (atomic method cards) + `taxonomy-v0.md` (merge groups)
- the run's playbook(s) from `book2skill-trace-playbook`

## Procedure
- **Atoms → `Methods/`**: collapse each merge group into one canonical method (union `source_anchors` + `perspective_origin`); promote singletons directly. Re-apply the 🔥 firewall (clear brand names even from worked-example slots). **Cross-book**: dedup onto an existing canonical method, don't create a new one.
- **Playbooks → `Playbooks/`**: promote each playbook; re-point its step `uses` to the canonical method names in `Methods/`.
- Write provenance frontmatter on both (schema = `Contracts/provenance.md`).

## Output
`Distilled-Artifact/Methods/*` + `Distilled-Artifact/Playbooks/*` + backfilled run entry `promoted_to_registry`.

## Guardrails
- Write only into `Methods/` and `Playbooks/`; `runs/` is immutable.
