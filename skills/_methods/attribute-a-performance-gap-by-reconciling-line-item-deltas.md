---
name: attribute-a-performance-gap-by-reconciling-line-item-deltas
kind: decision
category: analytic-method
one_liner: Explain why one firm out-earns peers by decomposing the margin into cost categories as %-of-sales and requiring the per-line deltas to sum to the total gap.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch05¶22, ch05¶68, ch05¶71]
promoted: 2026-06-13
status: promoted
---

## When to use
When a firm is more profitable than its peers and you need to know *which* functions drive it (and whether the advantage is structural and defensible) rather than accepting a single-cause story.

## Method
1. Express every cost category as a % of sales for the target firm and for the peer/industry average.
2. Subtract line by line to get a delta per category; positive deltas are sources of advantage, negative ones are costs incurred elsewhere (e.g. lower prices raise COGS%).
3. **Closure test:** the sum of the per-line deltas must reconcile to the total operating-margin gap. If it doesn't, the explanation is incomplete or hand-waving.
4. For locally-fixed costs sold per-impression (advertising, broadcast, distribution routes), reframe the delta as cost-per-customer = posted cost ÷ your penetration in the covered area; greater local density mechanically divides the cost — quantify the moat as the inverse of local share.
5. **Longitudinal variant:** track the firm's own margin/ROIC over time, locate the peak-and-decline inflection, and align it with the operational change (e.g. geographic dispersion) that coincided — using the firm as its own control.

## Inputs → Outputs
- Inputs: cost-category breakdown (% of sales) for the firm and peers; for the local variant, posted media/route costs and local penetration; for the longitudinal variant, a margin/ROIC time series.
- Outputs: ranked sources of the advantage, a reconciliation check, and identification of which variable drives erosion over time.

## Failure modes / assumptions
- A favorable line can be offset by an unfavorable one (low prices → high COGS%); never read one line in isolation.
- Requires comparable cost classifications across firms; mismatched accounting breaks the reconciliation.
- Correlation in the longitudinal variant is suggestive, not proof; corroborate with a structural mechanism.

## Worked example (illustrative, single)
A discount retailer's ~3-point margin edge reconciled to lower inbound-logistics, advertising, and supervision costs (summing to 4–5 points), partly offset by a higher COGS% from its lower prices — and the advertising edge traced to ~3× greater local store density driving ~1/3 the ad cost per sales dollar.
