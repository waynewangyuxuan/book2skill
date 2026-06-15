---
name: map-dependencies-to-discover-leading-indicators
kind: reasoning
category: analytic-method
one_liner: Chart everything your subject depends on and everything that depends on it, decompose backward from the outcome you care about to its earliest observable root driver, and read adjacent nodes as early-warning signals.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Looking for leading indicators of a subject whose outcome you want to anticipate.

## Method
1. Chart the subject's full dependency graph: everything it depends on (upstream) and everything that depends on it (downstream).
2. Decompose backward from the outcome you care about to the earliest observable root driver.
3. Instrument that root driver and the adjacent upstream nodes.
4. Read movements in those adjacent nodes as early-warning signals before the outcome itself moves.

## Inputs to Outputs
- Inputs: the subject; its upstream and downstream dependencies.
- Outputs: a set of instrumented leading indicators.

## Failure modes / assumptions
- Watching the outcome directly instead of its leading drivers.
- A dependency that is correlated but not causal (cross-check with mechanism).

## Worked example (illustrative, single)
A practitioner instruments an upstream supplier's order intake as a lead indicator that moves weeks before the subject's reported demand.
