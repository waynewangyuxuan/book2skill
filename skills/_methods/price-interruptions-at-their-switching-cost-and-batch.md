---
name: price-interruptions-at-their-switching-cost-and-batch
kind: decision
category: research-process-and-sourcing
one_liner: Charge each interruption its refocus-time × frequency as a fixed tax, batch reactive inputs into scheduled windows, and lower monitoring cadence to the decision horizon rather than the data's update rate.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Designing your day around deep analytical work that is repeatedly broken by reactive inputs and status-checking.

## Method
1. Treat every context switch as a large fixed cost = refocus-time × frequency, not a free micro-action.
2. Silence push alerts; batch reactive communications into a few scheduled windows.
3. Match monitoring frequency to your decision horizon, not the data's update rate — frequent outcome-checking amplifies anxiety and overtrading.
4. Pre-budget time for any unbounded interaction and prepare graceful exits.

## Inputs → Outputs
- Inputs: your interruption log; decision horizon.
- Outputs: a batched-intake schedule and a horizon-matched review cadence.

## Failure modes / assumptions
- Under-monitoring a genuinely fast-moving driver because cadence was set too low.
- Treating all interruptions as equal when some are real catalysts.

## Worked example (illustrative, single)
A practitioner moves from continuous alert-checking to two batched windows a day and a weekly review; output quality rises and churn falls.
