---
name: estimate-segment-return-from-a-synthetic-balance-sheet
kind: decision
category: valuation
one_liner: Recover a business's true return on capital when segment financials are unreported by building assets as %-of-sales, netting spontaneous liabilities, and dividing margin by capital intensity.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch09¶22, ch10¶24]
promoted: 2026-06-13
status: promoted
---

## When to use
When you need a ROIC for a business unit or industry whose capital base isn't separately reported (diversified parent, private segment), and only margins plus industry knowledge are available.

## Method
1. Estimate each asset line as a % of sales from industry knowledge (cash, receivables, inventory, PP&E) and sum to total assets-as-%-of-sales.
2. Subtract spontaneous (non-interest-bearing) liabilities — payables, accruals — as a % of sales to get net capital required as a % of sales.
3. Convert margin to return: ROIC ≈ operating margin ÷ (capital ÷ sales). Low capital intensity multiplies a modest margin into a high return.
4. **Robustness check:** redo with the capital estimate doubled. If the conclusion (moat / no moat) survives, the estimate is decision-grade despite its roughness.

## Inputs → Outputs
- Inputs: operating margin; industry-informed asset and spontaneous-liability ratios to sales; tax rate if converting pre/after-tax.
- Outputs: an estimated ROIC with an explicit sensitivity band, usable in the moat-detection skill.

## Failure modes / assumptions
- Garbage-in on the asset ratios propagates; the doubling check exists precisely because the inputs are guesses.
- Off-balance-sheet intangibles and operating leases can understate true capital — note them.
- Best for low-capital businesses where the margin→ROIC leverage is large and the verdict is robust to error.

## Worked example (illustrative, single)
A media business with assets ~15% of sales and spontaneous liabilities ~5% has ~10% capital-to-sales; a 12–13% operating margin then implies a ~120–130% pretax ROIC — and even doubling the capital estimate leaves it above 60%, so the moat verdict is robust.
