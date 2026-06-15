---
name: stress-test-a-terminal-value-before-trusting-it
kind: decision
category: valuation
one_liner: Treat a perpetuity terminal value as a high-sensitivity estimate — run ±1% on the discount and growth rates, and refuse to add a value that swings several-fold to your reliable near-term cash flows.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch16¶18, ch16¶20]
promoted: 2026-06-13
status: promoted
---

## When to use
Whenever a valuation leans on a perpetuity terminal value of the form TV = CF ÷ (R − G), and that terminal value is a large share of the total.

## Method
1. Compute the base TV = CF ÷ (R − G).
2. **Sensitivity sweep.** Recompute at R ±1% and G ±1% in the adverse and favorable directions. Because the denominator (R − G) is small, modest input errors produce multiplicative swings (commonly a ~3:1 range).
3. If the resulting range is wide and TV dominates the overall value, distrust the point estimate — do not combine this unreliable figure with reliable near-term cash flows as though they were equal quality (good + bad information → bad information).
4. Prefer a no-growth Earnings Power Value as the reliable backbone, and treat growth value as a separate, explicitly-uncertain tranche rather than burying it in a single TV.

## Inputs → Outputs
- Inputs: first post-terminal cash flow CF, discount rate R, perpetual growth rate G.
- Outputs: a TV range under ±1% perturbation and a judgment on whether the valuation is reliable enough to act on.

## Failure modes / assumptions
- Assumes a stable perpetuity is even appropriate; if the business won't stabilize, the formula is invalid regardless of sensitivity.
- A narrow band doesn't validate the inputs — garbage CF still yields garbage TV.
- The ±1% sweep is a fragility probe, not a confidence interval.

## Worked example (illustrative, single)
With CF $120M, R 10%, G 6%, TV = $3B; shifting to (R 9%, G 7%) gives $6B and (R 11%, G 5%) gives $2B — a 3:1 range from 1-point input moves, showing why such a TV must not be trusted as a precise addend.
