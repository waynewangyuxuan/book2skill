---
name: explore-data-visually-before-modeling
kind: decision
category: causal-and-statistical-hygiene
one_liner: Plot the candidate relationship first to see whether a pattern exists and what shape it takes; if nothing is visible, abort the modeling effort rather than fitting noise.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Before fitting any model to a hypothesized relationship.

## Method
1. Plot the raw data for the candidate relationship first.
2. Read whether a relationship exists at all and what shape it has (linear, curved, none).
3. If no pattern is visible, abort the modeling effort and conclude "no signal" rather than over-fitting.
4. If a pattern exists, let its shape decide whether to model directly, transform first, or stop.

## Inputs → Outputs
- Inputs: the raw candidate data.
- Outputs: a go/transform/stop decision and the relationship's shape.

## Failure modes / assumptions
- Fitting a model to data with no visible structure.
- Forcing a pattern onto ambiguous data.

## Worked example (illustrative, single)
A scatter plot shows no relationship between two variables, so the practitioner abandons the regression instead of reporting a spurious coefficient.
