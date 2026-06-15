---
name: Size a hidden transfer as rate-gap times affected stock
kind: reasoning
category: macro-systems
one_liner: Monetize an implicit subsidy or tax as (fair rate - administered rate) times the affected stock as a share of base, summing separate gaps and reporting a range.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch04¶37, ch02¶14]
promoted: 2026-06-14
status: promoted
---

# Size a hidden transfer as rate-gap times affected stock

## When to use
When a price or rate is administered away from its fair level and you want to quantify the resulting implicit transfer.

## Method
1. Estimate the fair (market/opportunity) rate and the administered rate; take the gap.
2. Identify the affected stock and express it as a share of the relevant base.
3. Multiply gap by affected stock to size the transfer.
4. Sum independent gaps (across instruments) and report a range, not a point.
5. When converting a rate change into a paired surcharge/subsidy, compute both directions via the reciprocal — they are not symmetric.

## Inputs -> Outputs
Inputs: fair rate; administered rate; affected stock; base. Outputs: a sized implicit transfer, as a range.

## Failure modes / assumptions
- The "fair rate" is itself an estimate; sensitivity-test it.
- Double-counting across overlapping instruments inflates the total.

## Worked example
A suppressed deposit rate applied to the household deposit stock is monetized as several percent of output transferred per year, reported as a range.
