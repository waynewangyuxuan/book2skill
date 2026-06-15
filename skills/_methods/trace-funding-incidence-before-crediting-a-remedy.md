---
name: Trace funding incidence before crediting a remedy
kind: decision
category: macro-systems
one_liner: A remedy funded by the same party it is meant to help nets to ~zero and will not move the target; only a transfer funded by a different party changes the aggregate.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, skeptic, teacher]
source_anchors: [ch02¶40, ch02¶41, ch03¶20]
promoted: 2026-06-14
status: promoted
---

# Trace funding incidence before crediting a remedy

## When to use
When evaluating whether a transfer, subsidy, or program will move an aggregate, and the naive view counts only the benefit side.

## Method
1. Identify the beneficiary sector and the funding sector.
2. If the beneficiary funds its own benefit (its own taxes or borrowing), net the two: the effect on the aggregate is ~zero.
3. A real shift requires the cost to fall on a different sector.
4. Predict the aggregate change as benefit minus funding incidence.

## Inputs -> Outputs
Inputs: the transfer; who benefits; who funds. Outputs: net effect on the aggregate.

## Failure modes / assumptions
- Timing mismatches (cost felt before benefit) can flip the short-run sign.
- Requires correctly identifying who ultimately pays.

## Worked example
A consumption-boosting program financed by taxing the same households nets to roughly zero and leaves the aggregate unchanged.
