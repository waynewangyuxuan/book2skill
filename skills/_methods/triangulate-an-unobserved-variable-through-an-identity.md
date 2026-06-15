---
name: Triangulate an unobserved variable through an identity
kind: reasoning
category: analytic-method
one_liner: When two observed quantities jointly imply an extreme value of a third via a constraint, infer the third's magnitude without measuring it — and treat the co-occurrence as an anomaly signal.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch04¶3, ch04¶4, ch04¶23, ch04¶24]
promoted: 2026-06-14
status: promoted
---

# Triangulate an unobserved variable through an identity

## When to use
When two facts seem mutually exclusive under your model, or when a third quantity is unmeasured but two measured quantities pin it through a constraint.

## Method
1. Write the identity relating the two observed quantities to the unobserved third.
2. Solve for the third; its implied value is a deduction, not an estimate.
3. If the implied value is extreme or paradoxical, read the co-occurrence as an anomaly that demands explanation rather than dismissal.

## Inputs -> Outputs
Inputs: two observed quantities; the binding identity. Outputs: the deduced magnitude of the third quantity plus an anomaly flag.

## Failure modes / assumptions
- The identity must hold exactly.
- Measurement error in the observed quantities propagates into the inferred third.

## Worked example
Two simultaneously-high reported figures that "should" trade off are reconciled only by an extreme implied value of a hidden flow, which becomes the thing to investigate.
