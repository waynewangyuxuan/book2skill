---
name: decompose-movement-into-expectations-versus-substance
kind: reasoning
category: behavioral-and-sentiment
one_liner: Split any price/valuation change into the multiple-change (psychology/expectations) and the metric-change (realized results), measure the lead/lag between them, and after de-benchmarking, separate the market anticipating a revision from the realized revision to act on the lead time.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Attributing why a price or valuation moved, and timing action around revisions.

## Method
1. Subtract the benchmark's co-movement to isolate the idiosyncratic change.
2. Decompose the idiosyncratic move into change in the multiple (expectations/psychology) and change in the underlying metric (results).
3. Split the metric piece further into the market anticipating a revision vs the realized revision.
4. Measure the lead/lag between the expectation-shift and the realized result.
5. Use the measured lead time to act early, orienting monitoring to trend-changes rather than isolated data points.

## Inputs to Outputs
- Inputs: a price/valuation series; the benchmark; the underlying metric.
- Outputs: an attribution into expectations vs results, with the lead/lag and an entry timing.

## Failure modes / assumptions
- Attributing a benchmark-driven move to the member.
- Confusing anticipation with realization and acting late.

## Worked example (illustrative, single)
A move is found to be 80% multiple-expansion ahead of any results; the practitioner reads it as anticipation and positions before the realized revision.
