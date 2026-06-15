---
name: attribute-a-gap-to-named-quantified-drivers
kind: reasoning
category: analytic-method
one_liner: Convert an unexplained difference between two figures into a sum of contributions from specific named variables (a variance bridge), and locate the single assumption responsible for a disagreement by decomposing the gap until you can name it.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Explaining why two figures differ — your estimate vs another's, this period vs last, actual vs forecast.

## Method
1. State the total unexplained gap between the two figures.
2. Decompose it into contributions from specific named variables, each quantified.
3. Require the per-variable contributions to sum to the total gap (a closed variance bridge).
4. When the gap is a disagreement with another analyst, decompose until you can name the exact assumption causing it, then debate that single assumption.

## Inputs to Outputs
- Inputs: two figures; the candidate driving variables.
- Outputs: a variance bridge attributing the gap to named, summing contributions.

## Failure modes / assumptions
- A bridge whose parts do not sum to the total (a hidden driver remains).
- Attributing the gap to a vague cause instead of a named variable.

## Worked example (illustrative, single)
A forecast miss is bridged into volume, price, and cost contributions that sum exactly to the miss, isolating price as the culprit.
