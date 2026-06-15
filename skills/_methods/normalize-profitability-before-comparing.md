---
name: normalize-profitability-before-comparing
kind: decision
category: valuation
one_liner: Convert reported earnings into a clean, comparable return by stripping financing/tax/one-off noise and choosing the right capital base, so profitability means the same thing across firms and years.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch02¶22, ch04¶58, ch04¶91, ch04¶95]
promoted: 2026-06-13
status: promoted
---

## When to use
Before comparing two firms' (or two years') profitability, or before feeding a profit figure into a moat test or valuation — whenever the headline number is net income or a single year's ROIC.

## Method
1. **Strip to operating earnings.** Start from EBIT, not net income — remove interest, taxes, and non-operating/extraordinary items so financing structure and tax games don't distort comparison.
2. **Smooth the lumps.** Average recurring "extraordinary" charges over the current + several prior years and fold that average back in; they reflect real operating decisions deferred into one year.
3. **Pick the right denominator — and use two.** Express as margin (÷ revenue) AND return (÷ invested capital); the two expose different distortions.
4. **Guard the capital base.** If invested capital is near-zero, negative, or dominated by off-balance-sheet intangibles, ROIC is a measurement artifact — for asset-light businesses lean on margin instead.
5. **Un-blend mixed pools.** If a cash hoard or unrelated segment dilutes the return, subtract the cash's own earnings (cash × a safe rate) from income and the cash from capital, then divide remaining operating earnings by remaining operating capital to recover the core business's true return.
6. **Benchmark relatively.** Judge the cleaned return against the risk-matched opportunity cost of capital; the spread (return − hurdle) is the meaningful quantity, not the absolute level.

## Inputs → Outputs
- Inputs: multi-year income statement, balance sheet, cash balance, a safe rate, the risk-matched hurdle rate.
- Outputs: adjusted operating margin, adjusted ROIC, and the un-blended core-business return where applicable.

## Failure modes / assumptions
- Over-smoothing can hide a genuine structural decline; inspect the trend, not just the average.
- A "capital" denominator at historical book can mislead vs reproduction value.
- Un-blending assumes you can cleanly attribute earnings to cash vs operations; rough but far better than the blended headline.

## Worked example (illustrative, single)
A firm reported ~15% blended ROIC. Removing a large cash pile (earning a low safe rate) from both earnings and capital revealed the operations themselves returned roughly 49% — the moat was hidden by balance-sheet structure.
