---
name: triangulate-with-independent-estimators-and-treat-divergence-as-diagnostic
kind: reasoning
category: analytic-method
one_liner: Estimate the same quantity by two or more methodologically independent paths and route the decision by their agreement; a gap is a signal to investigate, not noise to average away, and a large divergence means dig deeper.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, skeptic, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Producing or validating an estimate where a single method could be confidently wrong.

## Method
1. Estimate the target quantity by two or more methodologically independent paths (e.g., top-down and bottom-up).
2. Compare the results.
3. Treat agreement as corroboration and route the decision by it.
4. Treat a gap as a diagnostic signal to investigate the source of disagreement — do not simply average the two; a large divergence means dig deeper.
5. Reconcile granular forecasts against an independent whole-system total; an implausible total exposes hidden assumptions.

## Inputs to Outputs
- Inputs: the target quantity; two+ independent estimation methods.
- Outputs: a corroborated estimate or a located source of disagreement.

## Failure modes / assumptions
- Averaging two divergent estimates instead of investigating why they differ.
- Methods that are not actually independent (shared inputs) giving false agreement.

## Worked example (illustrative, single)
A bottom-up sum and a top-down total disagree by a third; investigating the gap surfaces a double-counted segment.
