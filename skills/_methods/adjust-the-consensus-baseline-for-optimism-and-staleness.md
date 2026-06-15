---
name: adjust-the-consensus-baseline-for-optimism-and-staleness
kind: reasoning
category: behavioral-and-sentiment
one_liner: Before treating a gap from consensus as evidence, audit the reference itself — correct for built-in upward bias, count how many real estimates compose it, and check whether it is stale, thinly-sampled, or apples-to-oranges.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Before reading signal from your divergence from an aggregated consensus or reference estimate.

## Method
1. Characterize the reference's reliability: its sample size, freshness, accuracy-weighting, and definitional consistency.
2. Correct for known structural optimism (built-in upward bias) in the aggregate.
3. Count how many genuine, independent estimates actually compose it — a thin baseline is not a real reference class.
4. Check whether it is stale or apples-to-oranges before treating any gap from it as evidence.

## Inputs to Outputs
- Inputs: an aggregated consensus/reference; its composition and vintage.
- Outputs: an adjusted, reliability-rated baseline against which divergence is meaningful.

## Failure modes / assumptions
- Diverging from a stale or thin baseline and calling it edge.
- Ignoring the systematic optimism bias in the aggregate.

## Worked example (illustrative, single)
A "consensus" turns out to rest on two stale estimates; the practitioner refuses to treat the gap as edge until a fresh, broad baseline is rebuilt.
