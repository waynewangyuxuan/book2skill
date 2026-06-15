---
name: size-a-sample-by-cycle-count-with-a-reliability-floor
kind: decision
category: forecasting-and-probability
one_liner: Set a historical/sample size by the number of full cycles it must span — not a fixed calendar length — and pre-commit a minimum count required for the precision your decision needs.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Choosing how much history or how many observations to use for an analysis governed by cyclical behavior.

## Method
1. Identify the relevant cycle length in the data.
2. Set the sample/history size by the number of full cycles it must span to be representative, not by a fixed calendar length.
3. Pre-commit a minimum observation count required for the precision the decision needs.
4. If the available data cannot span enough cycles or clear the floor, discount the conclusion accordingly.

## Inputs to Outputs
- Inputs: the cycle length; required precision; available data.
- Outputs: a cycle-spanning sample size with a pre-committed reliability floor.

## Failure modes / assumptions
- Using a calendar window that captures only part of one cycle.
- Drawing strong conclusions below the reliability floor.

## Worked example (illustrative, single)
A practitioner extends the history to span three full cycles rather than the convenient five recent years that covered only an upswing.
