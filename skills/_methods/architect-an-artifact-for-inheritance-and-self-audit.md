---
name: architect-an-artifact-for-inheritance-and-self-audit
kind: decision
category: analytic-method
one_liner: Build any artifact that will outlive its author for handoff from day one — isolate inputs from logic from outputs, preserve assumption history, embed redundant cross-computations as self-audits, and clean defects as you find them — or pay a rebuild tax.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Building a model, dataset, or analytical artifact that others will inherit or that you will maintain over time.

## Method
1. Separate changeable parameters from derivation logic from outputs, each in its own place.
2. Never overwrite past parameter values; preserve the assumption history.
3. Document provenance of every input.
4. Embed redundant cross-computations — compute a key quantity two independent ways that must agree, so any discrepancy instantly flags an error.
5. Clean small logical and cosmetic defects the moment you notice them; deferred defects compound until a full rebuild is needed.
6. Default to simplicity for maintainability and transferability.

## Inputs to Outputs
- Inputs: the artifact's parameters, logic, and outputs.
- Outputs: an inheritable artifact with isolated inputs, preserved history, and built-in self-checks.

## Failure modes / assumptions
- Tangling parameters into formulas so no one can update it.
- Overwriting assumptions and losing the audit trail.

## Worked example (illustrative, single)
A model computes one total two ways on separate tabs; when they diverge after an edit, the error is caught instantly instead of shipping.
