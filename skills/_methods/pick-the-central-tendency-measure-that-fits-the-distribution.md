---
name: pick-the-central-tendency-measure-that-fits-the-distribution
kind: reasoning
category: causal-and-statistical-hygiene
one_liner: Before using any "average," identify whether it is mean/median/mode and inspect the distribution shape, since on a skewed distribution they diverge materially — and treat a large mean-vs-median gap in a peer group as an outlier detector.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Any time you rely on an "average" of a metric, especially across a peer group or skewed population.

## Method
1. Determine which average is in play — mean, median, or mode.
2. Inspect the distribution shape; on a skewed distribution the three diverge and the wrong one misleads.
3. Choose the measure that fits the distribution and the decision (median for skew, mean for additive/symmetric).
4. Compute both mean and median of a peer-group statistic; treat a material gap between them as a signal that an outlier is skewing the group, then investigate it.

## Inputs → Outputs
- Inputs: a metric across a population; its distribution.
- Outputs: the appropriate central-tendency measure plus any flagged outlier.

## Failure modes / assumptions
- Quoting a mean on a heavily skewed distribution.
- Missing an outlier that the mean-median gap would have revealed.

## Worked example (illustrative, single)
A peer-group "average margin" mean sits far above the median; the gap traces to one giant outlier, and the median is used instead.
