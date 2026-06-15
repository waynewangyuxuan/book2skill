---
name: quantify-effective-scope-from-correlation-structure
kind: reasoning
category: analytic-method
one_liner: Items driven by one common factor collapse into roughly one unit of work and one bet; measure pairwise correlation over a long window to size real workload and real diversification, not nominal count.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
When a set of items looks large by count and you need to know how much of it is genuinely independent — for sizing workload, diversification, or true edge.

## Method
1. Compute pairwise correlation of the items' time series over a long window as the computable proxy for "driven by the same thing."
2. Cluster highly-correlated items; treat each cluster as approximately one unit of work and one bet.
3. Re-derive effective scope from the cluster count, not the nominal item count.
4. Use the freed capacity for truly orthogonal items.

## Inputs → Outputs
- Inputs: time series for each item; a long observation window.
- Outputs: correlation clusters → effective (independent) scope count.

## Failure modes / assumptions
- Short windows make correlation unstable; needs enough cycles.
- A common factor can change over time, so re-estimate periodically.

## Worked example (illustrative, single)
A dozen items that all move with one cyclical driver collapse to roughly one effective unit; the practitioner reallocates the saved effort to an uncorrelated name.
