---
name: require-time-to-convergence-not-just-a-valuation-gap
kind: decision
category: valuation
one_liner: A correct mispricing judgment is only actionable if the gap closes within your horizon and is not an artifact of a stale denominator about to move on its own; decouple correctness of the conclusion from timing of action, since "right but early" is indistinguishable from wrong.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, skeptic, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
When you have judged something mispriced and are deciding whether and when to act.

## Method
1. Confirm the valuation gap is real, not an artifact of a stale numerator/denominator about to move and close the gap on its own.
2. Require the gap to close within your decision horizon, with a correction mechanism and survivability.
3. Decouple the correctness of the conclusion from the timing of action — use one method for the call and a separate signal to time entry.
4. Treat "right but early" as operationally indistinguishable from wrong, and don't fight a containing regime for a single correct unit.

## Inputs to Outputs
- Inputs: a judged mispricing; its convergence mechanism and horizon; an entry-timing signal.
- Outputs: a go/wait decision separating the call from its timing.

## Failure modes / assumptions
- Holding a correct view past your horizon and being ruined by the wait.
- Mistaking a stale-denominator artifact for a real gap.

## Worked example (illustrative, single)
A gap is real but has no catalyst within the horizon; the practitioner shelves the call and waits for a timing signal rather than bleeding early.
