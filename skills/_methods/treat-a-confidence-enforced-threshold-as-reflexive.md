---
name: Treat a confidence-enforced threshold as reflexive
kind: reasoning
category: macro-systems
one_liner: For thresholds enforced by collective belief, the line is crossed when enough participants believe it is — analyze the belief/credibility variable as the trigger, not a fixed balance-sheet ratio.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, teacher, trader]
source_anchors: [ch06¶7, ch06¶17]
promoted: 2026-06-14
status: promoted
---

# Treat a confidence-enforced threshold as reflexive

## When to use
When a solvency/stability threshold is treated as a fixed numeric ratio, but the actual failure is triggered by a loss of collective confidence.

## Method
1. Identify whether the threshold is mechanically fixed or enforced by participants' beliefs.
2. If belief-enforced, model the trigger as the credibility variable, not the ratio.
3. Locate the tipping point at the belief threshold — crossed when enough participants believe it is crossed.
4. Predict nonlinearity: gradual deterioration then abrupt break.

## Inputs -> Outputs
Inputs: the threshold; the credibility/belief variable. Outputs: the reflexive trigger and a nonlinear trajectory.

## Failure modes / assumptions
- Belief dynamics are hard to measure; use credibility proxies.
- Some thresholds really are mechanical.

## Worked example
A funding run is forecast off the market's confidence variable rather than a fixed leverage ratio, because the run starts when enough lenders expect others to pull.
