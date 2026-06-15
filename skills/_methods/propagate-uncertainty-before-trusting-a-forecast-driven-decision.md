---
name: propagate-uncertainty-before-trusting-a-forecast-driven-decision
kind: decision
category: forecasting-and-probability
one_liner: A chain of point-estimate projections feels like analysis; ask which forecast error reverses the recommendation, and how likely it is.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [skeptic]
source_anchors: [ch07¶17, ch16¶20]
promoted: 2026-06-13
status: promoted
---

## When to use
When an irreversible commitment is justified by multi-year quantitative projections (demand curves, cost curves, terminal values), or when a method is praised for "segregating reliable from unreliable information."

## Method
1. Treat each projection as a *distribution*, not a number; carry a plausible range.
2. Identify which forecast error would *reverse* the recommendation, and estimate how likely that error is. (Often the surprise that kills the thesis is the market growing *faster* than expected, not slower.)
3. When a method claims to avoid unreliable inputs (e.g. refusing to forecast growth), check whether it truly removed the uncertainty or just buried it in a different assumption (e.g. "current earnings persist forever"). A quieter bet is still a bet.
4. Stress the decision against both ends of each range before committing irreversibly.

## Inputs → Outputs
- In: a decision + its underlying projections/assumptions.
- Out: the decision-reversing error for each input, its likelihood, and whether the recommendation is robust or fragile to forecast error.

## Failure modes / assumptions
- You still need *some* forecast; the skill is sensitivity analysis, not forecast nihilism.
- Ranges can be gamed (too wide = everything fragile, too narrow = false comfort); anchor them to historical variability where possible.
