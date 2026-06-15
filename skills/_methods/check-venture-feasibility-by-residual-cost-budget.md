---
name: check-venture-feasibility-by-residual-cost-budget
kind: decision
category: valuation
one_liner: Test whether a new product can be made profitably by anchoring to the price the market will bear, stacking known per-unit costs, and solving for the budget the uncertain cost must fit inside.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch07¶19, ch07¶20]
promoted: 2026-06-13
status: promoted
---

## When to use
When launching a new product whose final price is constrained by an existing alternative and one cost component (e.g. manufacturing) is still uncertain — and you must judge feasibility before committing.

## Method
1. **Anchor the price.** Take the incumbent/substitute's price and apply the willingness-to-pay premium your product justifies to set the ceiling price the market will bear.
2. **Stack the known costs.** Sum the per-unit costs you already know (royalties, promotion, distribution, packaging).
3. **Solve for the residual.** Residual budget = ceiling price − known costs. This is the maximum the uncertain cost item may be.
4. **Compare.** If your best estimate of the achievable uncertain cost < residual, the venture clears the price–cost hurdle; if not, it doesn't — regardless of how attractive the market looks.

## Inputs → Outputs
- Inputs: anchor price of the substitute, WTP premium, known per-unit cost components, an engineering estimate of the uncertain cost.
- Outputs: the allowable cost ceiling for the uncertain item and a feasibility verdict.

## Failure modes / assumptions
- The WTP premium is the soft input; bound it with a range and re-test.
- Feasibility ≠ profitability with a moat — clearing the price–cost hurdle says nothing about whether competition will later erode the margin (pair with the moat-detection skill).
- Assumes the anchor price and its trajectory are reasonably forecastable.

## Worked example (illustrative, single)
A new product anchored to a ~$9 substitute price × a 30% quality premium gave an ~$11–12 ceiling; subtracting ~$7 of known costs and ~$1.18 packaging left ~$2.82 for manufacturing, and since achievable cost was ~$1.44, the venture was feasible on price–cost grounds.
