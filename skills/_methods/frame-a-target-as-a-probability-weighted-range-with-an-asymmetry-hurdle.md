---
name: frame-a-target-as-a-probability-weighted-range-with-an-asymmetry-hurdle
kind: decision
category: forecasting-and-probability
one_liner: Express the estimate as probabilities over a base plus history-bounded tails, convert the range into an upside-to-downside ratio, and only commit when it clears a preset asymmetry hurdle — direction without asymmetry is rejected.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Deciding whether to commit to a position once you have a scenario range, not just a directional view.

## Method
1. Express the estimate as probabilities over a base plus bounded upside/downside tails, capping tail magnitudes to empirical history.
2. Convert the range into an upside-to-downside ratio.
3. Set a minimum asymmetry hurdle in advance.
4. Only commit when the ratio clears the hurdle; reject a correct direction that lacks favorable asymmetry.

## Inputs to Outputs
- Inputs: a probability-weighted scenario range; a preset asymmetry hurdle.
- Outputs: a go/no-go sizing decision based on payoff asymmetry.

## Failure modes / assumptions
- Acting on direction alone when downside roughly equals upside.
- Tails not bounded to history, inflating the apparent asymmetry.

## Worked example (illustrative, single)
A view is directionally right but its upside-to-downside ratio sits below the hurdle, so the practitioner passes.
