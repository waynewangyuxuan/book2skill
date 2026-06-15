---
name: book2skill-trace-playbook
description: Sub-skill of book2skill. Reconstruct the book's analytical PROCEDURE (its orchestration logic) as a playbook — spine plus gated, dependency-ordered steps that reference the atomic methods. A control-flow / decision-tree reading, distinct from per-perspective open-coding. This is the high-value product. Invoked by the book2skill orchestrator.
---

# book2skill-trace-playbook

Extract the book's **编排逻辑** — the latent analytical procedure it teaches — as a playbook (schema = `Contracts/playbook.md`). The atomic methods are its nodes; this is the graph that connects them.

## Why a separate pass
`book2skill-read-perspective` harvests atoms and deliberately ignores book structure. The playbook is the *connective tissue*: which method when, what gates, what depends on what. It needs a different reading — trace the author's decision procedure, don't harvest tricks. Note: book TOC (surface order) ≠ the procedure (latent control flow); extract the latter.

## Input
- `book-text/` (+ `thesis.md`)
- the run's atomic methods (`skills-raw/`) — to reference as each step's `uses`

## Procedure
1. **Spine**: the controlling principle the whole method organizes around (1–2 sentences).
2. **Procedure**: the ordered/branching steps a practitioner follows. Per step: goal, which atomic methods it `uses`, inputs from prior steps, the **gate/branch** condition, output.
3. **Gates & dependencies**: mark where the procedure stops/switches track (e.g., "no barrier → value at reproduction cost, stop") and which step requires which.
4. **Whole-failure**: when the procedure as a whole (the spine) misleads.

## Output
One (or a few) playbook file(s) per book (schema = `Contracts/playbook.md`), written into the run, promoted to `Playbooks/`.

## Guardrails
- Reference atoms by name; don't restate them — the playbook is the graph, not the nodes.
- A playbook is the **eval unit** (run it on a case → outcome); keep it executable, not a summary.
