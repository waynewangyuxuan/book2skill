---
name: net-first-mover-against-vintage-penalty
kind: decision
category: competitive-interaction
one_liner: Decide whether moving first pays by netting the learning-curve cost saving against the vintage penalty (later entrants buy cheaper, newer capacity) and find the volume where the edge expires.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [historian, quant]
source_anchors: [ch07¶19, ch07¶32, ch07¶64, ch07¶69]
promoted: 2026-06-13
status: promoted
---

## When to use
Evaluating a pioneer investment in a new product/process and judging whether being first confers a durable cost advantage or just an early, decaying lead.

## Method
1. **Learning term (+):** estimate the first mover's variable-cost saving from cumulative-volume experience vs a fresh entrant.
2. **Vintage term (−):** estimate the capital-cost penalty the first mover carries because later entrants buy cheaper, more efficient equipment. Put capital on a per-unit footing — annualize capex over its depreciation life at the cost of capital, then divide by annual capacity — so it is comparable to variable cost.
3. **Net them per unit:** net advantage = learning saving − vintage penalty. If negative, going first loses.
4. **Find the expiry volume:** the advantage shrinks as the entrant accumulates experience and disappears once it reaches the cumulative volume where the learning curve flattens. Fast market growth lets entrants reach that volume quickly — so a large, fast-growing market is the *worst* case for a pioneer; a slow/niche market preserves the lead longest.

## Inputs → Outputs
- Inputs: variable-cost-vs-cumulative-volume curve, capex by vintage, depreciation life, cost of capital, annual capacity, market growth rate.
- Outputs: per-unit net first-mover advantage and the time/volume at which it expires.

## Failure modes / assumptions
- Without some customer captivity, even a real cost edge doesn't stop customers leaving once the entrant catches up.
- Assumes the learning curve genuinely flattens and that later vintages are cheaper — verify both.
- A large fast-growing market being the worst case for a pioneer is the opposite of common intuition.

## Worked example (illustrative, single)
A pioneer's first-generation plant cost ~$2.50/unit of capacity vs ~$1.12 for a later entrant's third-generation plant (a ~$1.38 vintage penalty), while accumulated volume gave a ~$1.33 variable-cost edge — roughly offsetting — and the net advantage vanished once entrants reached ~50M cumulative units.
