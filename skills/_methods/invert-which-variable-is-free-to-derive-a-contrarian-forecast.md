---
name: Invert which variable is free to derive a contrarian forecast
kind: reasoning
category: forecasting-and-probability
one_liner: When a required differential cannot come from the consensus-favored term, hold the achievable term fixed and solve the identity for the other free variable — yielding the estimate consensus misses.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch04¶30, ch04¶61, ch03¶37]
promoted: 2026-06-14
status: promoted
---

# Invert which variable is free to derive a contrarian forecast

## When to use
When consensus pins the adjustment on one term of an identity, but that term is constrained, so the adjustment must fall elsewhere.

## Method
1. Write the identity and the required total adjustment.
2. Show the consensus-favored term cannot supply it (it is capped or already maxed).
3. Hold that term at its achievable value and solve the identity for the remaining free variable.
4. Report the implied value of the free variable as the contrarian forecast.
5. For a goal-seeking actor, note a higher return on the stock reduces the flow needed to hit the target, freeing current activity — the opposite of a reward-for-postponement read.

## Inputs -> Outputs
Inputs: the identity; the required adjustment; the constraint on the favored term. Outputs: the implied value of the free variable.

## Failure modes / assumptions
- The constraint on the favored term must be real, not assumed.
- More than one variable may be free; pin the others first.

## Worked example
Consensus expects rebalancing via rising consumption, but with consumption growth capped, solving the identity forces a sharp fall in the investment rate instead.
