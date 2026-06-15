---
name: separate-cause-from-symptom-then-falsify-with-the-time-series
kind: reasoning
category: causal-and-statistical-hygiene
one_liner: Check that a proposed remedy targets the actual causal lever (not a correlated surface feature), then kill or confirm causal stories by testing their time-series prediction.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch02¶5, ch05¶44]
promoted: 2026-06-13
status: promoted
---

## When to use
When a popular remedy is prescribed for a problem, or a tidy "the cause is X" story circulates, and you must decide whether to believe it.

## Method
1. Name the surface feature the remedy/story addresses (Y) and the variable that actually controls the outcome (X).
2. Trace the causal chain: does pulling Y actually move the outcome, or does the outcome stay controlled by X? If the lever is the wrong one, the remedy fails even when it "works" on Y.
3. Derive the time-series prediction the causal story implies: if X drives the result, the X-metric should have moved in step as the result moved.
4. Check the actual history. If the metric moved opposite to the story (got worse while results improved), reject the story regardless of its intuitive appeal.

## Inputs → Outputs
- Input: a remedy or causal claim plus historical data on the relevant metrics.
- Output: a verdict — lever correct/incorrect, and story confirmed/falsified by the temporal evidence.

## Failure modes / assumptions
- Failure: accepting a story on plausibility without checking whether its metric actually tracked the outcome.
- Assumption: the implied time-series is observable; if not, the test is weaker and you rely on the causal-chain step alone.
