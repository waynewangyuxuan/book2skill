---
name: book2skill-abstract-to-method
description: Sub-skill of book2skill. Abstract a perspective's open-coding codes into atomic method cards, enforcing the RAG firewall (strip the book's examples, keep only the transferable method). These are atomic methods (the vocabulary), not assembled skills. Invoked by the book2skill orchestrator (Stage C).
---

# book2skill-abstract-to-method (Stage C)

Code → atomic **method card**, with the RAG firewall. Grammar = **reasoning / decision**.
(These are the *atoms* — the vocabulary. The assembled "skill" is the playbook; see `book2skill-trace-playbook`.)

## Input
`codes/<persp>.jsonl` (schema = `Contracts/code.md`).

## Procedure
- Merge codes expressing the same underlying method.
- Write each as a method card (schema = `Contracts/skill.md`): `name` (verb-led, content-agnostic), `kind` (reasoning|decision), Method, failure modes, optional single Worked example.
- **🔥 firewall**: if a candidate can't be stated without naming the book's specific example → reframe or drop.

## Output
`skills-raw/<persp>-NNN.md` (raw atomic method cards; promoted later to `Methods/`).

## Guardrails
- Known leak: companies smuggled in as reference-class labels inside Method (catch disguised examples).
- Decision lenses compress, reasoning lenses proliferate — don't split one method into three.
- This step produces **atoms only**; the orchestration connecting them is `book2skill-trace-playbook`.
