---
name: set-a-target-ratio-conditioned-on-its-fundamental-drivers
kind: reasoning
category: forecasting-and-probability
one_liner: Regress a historical ratio on its fundamental drivers and pick a target level consistent with the drivers' current values, rather than defaulting to the historical average — and before trading a ratio's deviation, test whether a stale numerator or denominator is about to close the gap itself.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Setting a target level for a ratio (a multiple, margin, or other ratio) and deciding whether a current deviation is actionable.

## Method
1. Regress the historical ratio on its fundamental drivers.
2. Pick the target level consistent with the drivers' current values, not the unconditional historical average.
3. Before acting on a deviation from the target, decompose it into inputs-wrong vs price-wrong.
4. Test whether a stale numerator or denominator is about to move and close the gap on its own before trading it.

## Inputs to Outputs
- Inputs: the historical ratio; its fundamental drivers; current driver values.
- Outputs: a driver-conditioned target ratio and an actionable-deviation test.

## Failure modes / assumptions
- Reverting to the historical average when drivers have structurally shifted.
- Trading a deviation that a stale component is about to erase.

## Worked example (illustrative, single)
A multiple sits below its historical average, but conditioned on weaker current drivers the target is also lower, so the apparent cheapness vanishes.
