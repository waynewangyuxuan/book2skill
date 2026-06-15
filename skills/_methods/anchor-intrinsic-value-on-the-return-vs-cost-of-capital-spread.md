---
name: anchor-intrinsic-value-on-the-return-vs-cost-of-capital-spread
kind: reasoning
category: valuation
one_liner: Measure value creation as the spread between returns on incremental capital and the cost of that capital, since value (and empirically the price change) tracks that spread — not growth or absolute return level.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Estimating whether and how much an entity is creating value, and what should drive its valuation.

## Method
1. Compute the return on incremental capital deployed.
2. Compute the cost of that capital on a risk-matched basis.
3. Measure value creation as the spread between the two, not the absolute return level or the growth rate.
4. Recognize that price change empirically tracks that spread; growth funded below the cost of capital destroys value.

## Inputs to Outputs
- Inputs: return on incremental capital; risk-matched cost of capital.
- Outputs: the value-creation spread and its sign.

## Failure modes / assumptions
- Crediting growth that earns below its cost of capital.
- Using an absolute return level without the cost-of-capital comparison.

## Worked example (illustrative, single)
An entity growing fast but earning below its cost of capital is shown to be destroying value despite rising reported earnings.
