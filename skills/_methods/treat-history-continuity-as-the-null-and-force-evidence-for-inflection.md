---
name: treat-history-continuity-as-the-null-and-force-evidence-for-inflection
kind: reasoning
category: forecasting-and-probability
one_liner: Overlay the forward projection on the full historical series, make continuity the null, and require explicit causal justification for any break from the historical range/trend — imposing deceleration/saturation by default and treating an unjustified hockey-stick as a self-bias warning.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Sanity-checking any forward projection, especially one that extrapolates a recent extreme.

## Method
1. Graph the projection continuous with the full long historical series.
2. Make history-continuity the null hypothesis.
3. Reject straight-line extrapolation of extremes; impose deceleration/saturation by default and bound scenarios to the long-run range.
4. Require explicit causal justification for any break from the historical range or trend; treat a range-break as needing extraordinary evidence.
5. Read an unjustified hockey-stick as a self-bias warning.

## Inputs to Outputs
- Inputs: a forward projection; the full historical series.
- Outputs: a continuity-checked projection, with any inflection justified or removed.

## Failure modes / assumptions
- Extrapolating a transient spike into a permanent trend.
- A genuine structural break that the continuity null would wrongly suppress (require the evidence, then accept it).

## Worked example (illustrative, single)
A projected sharp acceleration is overlaid on a decade of stable history; with no causal story for the break, the practitioner flattens it toward the historical range.
