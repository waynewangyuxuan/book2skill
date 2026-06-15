---
name: match-the-axis-scale-to-additive-vs-multiplicative-change
kind: reasoning
category: analytic-method
one_liner: Plot quantities that compound or span orders of magnitude on a log scale so equal proportional changes render as equal distances, and reserve linear scale for additive quantities — then read a log-log slope as a percent-per-percent elasticity.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Visualizing or fitting a quantity that grows multiplicatively or spans wide ranges.

## Method
1. Classify the quantity as additive vs multiplicative / wide-range.
2. Use a logarithmic axis for multiplicative or wide-range quantities so equal proportional changes appear as equal distances; reserve linear axes for additive quantities.
3. When a relationship is curved or spans orders of magnitude, log-transform to linearize it before fitting.
4. Re-read the transformed coefficients: a log-log slope is a percent-per-percent elasticity, not a level effect.

## Inputs → Outputs
- Inputs: a quantity or relationship; its growth character.
- Outputs: the correct axis/scale and a correctly-interpreted slope.

## Failure modes / assumptions
- Reading a linear plot of a compounding series as decelerating when it is steady growth.
- Misinterpreting a log-log slope as a level coefficient.

## Worked example (illustrative, single)
A compounding series looks like an explosive hockey-stick on a linear axis but a straight line on a log axis, revealing constant growth.
