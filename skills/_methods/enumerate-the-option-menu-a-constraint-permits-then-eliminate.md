---
name: Enumerate the option menu a constraint permits, then eliminate
kind: decision
category: analytic-method
one_liner: When an identity forces a fixed total adjustment, list the complete mutually-exclusive ways to balance it, confirm exhaustiveness, strike the infeasible ones, and corner the residual outcome.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, teacher, trader, historian]
source_anchors: [ch06¶28, ch06¶31, ch07¶33, ch07¶34, ch09¶30, ch09¶32]
promoted: 2026-06-14
status: promoted
---

# Enumerate the option menu a constraint permits, then eliminate

## When to use
When a binding identity forces some total adjustment and you want to forecast which outcome the system lands on.

## Method
1. From the identity, derive the complete set of mutually-exclusive ways the required adjustment can occur.
2. Confirm the set is exhaustive — nothing else can balance the constraint.
3. Strike each option blocked by another binding constraint or by infeasibility.
4. Whatever survives is the forced outcome; bet on the residual.

## Inputs -> Outputs
Inputs: the binding identity; the candidate adjustment paths; the eliminating constraints. Outputs: the cornered residual outcome.

## Failure modes / assumptions
- Missing an option breaks the exhaustiveness and can corner the wrong outcome.
- Combinations of options may be feasible even if each alone is marginal.

## Worked example
An economy that must rebalance is shown to have only three arithmetic routes; two are politically blocked, cornering the third as the forecast.
