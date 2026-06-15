---
name: value-in-reliability-tranches
kind: decision
category: valuation
one_liner: Value a business in ordered tranches of rising uncertainty — asset reproduction value, then no-growth earnings power, then growth — never blending reliable with speculative inputs, and credit growth only behind a verified barrier.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant, teacher, trader, historian]
source_anchors: [ch16¶18, ch16¶20, ch16¶31, ch16¶46, ch16¶54, ch16¶57, ch16¶58, ch16¶60, ch16¶88, ch16¶93, ch16¶99, ch16¶21]
promoted: 2026-06-13
status: promoted
---

## When to use
Valuing a company or project, or setting a buy/sell discipline, where a standard discounted-cash-flow result is dominated by a speculative terminal value and you want the uncertainty made visible.

## Method
1. **Refuse to blend reliability levels.** Combining high-confidence near-term cash flows with a low-confidence terminal value into one summed figure yields an unreliable number — the bad-input errors dominate ("good info + bad info = bad info"). Segregate into tranches and reason about each separately.
2. **Tranche 1 — Asset value (most reliable, no forecast).** Reproduction cost if the industry is viable, else liquidation value. Walk the balance sheet from most-certain (cash, securities) to least-certain (intangibles = spend to recreate them); the more value in intangibles, the lower your confidence. This is the floor that survives if the moat evaporates.
3. **Tranche 2 — Earnings Power Value (no growth).** EPV = normalized, debt-neutral, no-growth sustainable earnings ÷ cost of capital. Normalize first: smooth recurring "nonrecurring" charges over several years, normalize cyclical margins, replace accounting depreciation with maintenance capex, apply a sustainable tax rate. Excluding growth keeps this far more reliable.
4. **Franchise value = EPV − asset value, and let the comparison diagnose the situation:** EPV > assets → a franchise gap, real *only* if you can name a sustainable barrier (sanity-check it as a franchise margin: are the advantages plausibly worth that many margin points?); EPV ≈ assets → commodity, no moat; assets > EPV → value-destroying management.
5. **Tranche 3 — Growth (least reliable).** Credit growth value *only* when EPV > assets and a barrier exists. Without a moat, growth merely returns the cost of capital (neutral) or, with weak management, destroys value — size it at zero or negative. The moat, not the growth rate, decides whether growth is worth paying for.
6. **Anchor the margin of safety to the most reliable applicable tier.** Value the enterprise first, then subtract debt — a fixed enterprise-value error lands entirely on the thin equity residual, so leverage magnifies equity uncertainty; present the enterprise band before deriving equity.

## Inputs → Outputs
- Inputs: balance sheet (reproduction/liquidation), normalized debt-neutral earnings, cost of capital, sales, a moat verdict, industry growth, debt, current price.
- Outputs: three stacked values of increasing uncertainty, a moat/commodity/bad-management diagnosis, a growth-value gate, a franchise-margin sanity check, and a tier-anchored buy discipline with its (magnified) equity error band.

## Failure modes / assumptions
- A ±1% error in terminal-value assumptions can swing a DCF 2–3×; the fix is segregation by reliability, not better forecasting.
- Crediting franchise value or growth without naming a barrier is the core error.
- Using reproduction value where liquidation value applies (or vice versa) corrupts the floor — the industry-viability judgment comes first.
- Equity-level errors are magnified by leverage; reason at the enterprise level first.

## Worked example (illustrative, single)
A firm with $1,200M reproduction assets and $240M after-tax earnings at a 10% cost of capital has a $2,400M EPV; the implied ~20% pretax franchise margin on $1,000M sales is real only if the moat is plausibly worth ~20 margin points — otherwise value it at assets. A no-moat firm reinvesting at 8% against a 10% cost of capital destroys value as it grows, so its growth is priced at zero or less.
