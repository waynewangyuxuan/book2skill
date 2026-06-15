---
name: Convert a target into a required rate and gate against the ceiling
kind: decision
category: forecasting-and-probability
one_liner: Translate a stated target into the per-period differential growth rate it demands over the horizon, then benchmark that rate against the most the system has ever achieved; if it exceeds the historical ceiling, the plan is infeasible and the assumptions must change.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, teacher, trader]
source_anchors: [ch04¶15, ch04¶56, ch04¶57, ch04¶59, ch04¶61]
promoted: 2026-06-14
status: promoted
---

# Convert a target into a required rate and gate against the ceiling

## When to use
When an official target or forecast is asserted, and you want to test its arithmetic plausibility before debating its merits.

## Method
1. Translate the target (a change in one quantity's share of a total) into the differential growth rate it must sustain over the horizon.
2. Benchmark that required rate against the historical achievable maximum for the system.
3. If the required rate exceeds the ceiling, declare the plan infeasible — its assumptions must change.
4. Attribute past competence only to the specific lever that produced prior wins; a new goal needing a different lever earns no such credit.

## Inputs -> Outputs
Inputs: the target; the horizon; the historical rate ceiling. Outputs: the required rate and a feasible/infeasible verdict.

## Failure modes / assumptions
- The historical ceiling may be exceeded by a genuine regime change — require it to be named.
- The translation must use the correct base and horizon.

## Worked example
A consumption-share target is converted into the household-income growth rate it requires, which exceeds anything ever sustained, so the target is faded.
