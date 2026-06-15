---
name: project-moat-erosion-as-the-market-grows
kind: decision
category: competitive-advantage
one_liner: Treat market growth as the enemy of a scale moat and compute how fast the fixed-cost gap decays and the shrinking share an entrant needs to break in.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶44, ch03¶29]
promoted: 2026-06-13
status: promoted
---

## When to use
When a scale-based incumbent operates in a growing market and you must decide whether its advantage will hold or melt — or when judging whether to enter a large/fast-growing market.

## Method
1. Model each player's scale moat as fixed_cost ÷ revenue (fixed cost as a % of sales).
2. As the market grows, fixed costs stay constant while variable costs scale with volume, so the fixed-cost-as-%-of-sales gap between leader and entrant decays roughly inversely with market size (market doubles → gap halves; 10× → ~1/10).
3. Compute the entrant's break-in share = (fixed_cost ÷ acceptable-gap%) ÷ market_size. A larger market lowers the share an entrant needs to reach a tolerable cost gap, eroding the moat.
4. For unprotected markets generally, model the steady state as economic profit → 0 (ROIC converging to the cost of capital): treat any current above-hurdle return as transient and forecast toward the equilibrium, not the peak.

## Inputs → Outputs
- Inputs: each player's fixed costs, current market size and growth, the cost-gap an entrant can tolerate.
- Outputs: projected decay of the cost gap over time and the entrant's required break-in share at each market size.

## Failure modes / assumptions
- Holds only where the advantage is *scale-based*; pure-captivity or input-cost advantages are not eroded by market growth this way.
- Assumes fixed costs truly stay fixed as the market grows (new geographies/lines can re-inflate them).
- The "inverse with size" relation is a back-of-envelope approximation, not a precise law.

## Worked example (illustrative, single)
With $100k fixed cost, a leader/entrant fixed-cost-%-of-sales gap of 16% halves to 8% when the market doubles and falls to ~1.6% at 10× — and the entrant's required break-in share drops from ~20% in a small market to ~5% in a market four times larger.
