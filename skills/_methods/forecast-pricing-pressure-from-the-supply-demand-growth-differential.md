---
name: forecast-pricing-pressure-from-the-supply-demand-growth-differential
kind: reasoning
category: forecasting-and-probability
one_liner: Compute the compound growth-rate spread between supply and demand over time; the widening or narrowing gap is the leading driver of pricing power, margins, and returns.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Forecasting pricing power and margins in a market driven by the balance of supply and demand growth.

## Method
1. Estimate the compound growth rate of demand and of supply separately over the forecast horizon.
2. Compute the spread between them.
3. Read a demand-over-supply gap as pricing power building and the reverse as pricing pressure.
4. Use the trajectory of the gap (widening vs narrowing) as the leading driver of margins and returns, ahead of the realized price.

## Inputs to Outputs
- Inputs: demand growth rate; supply growth rate; horizon.
- Outputs: the supply-demand growth spread and its pricing/margin implication.

## Failure modes / assumptions
- Forecasting demand carefully but ignoring the supply response.
- Treating a one-period imbalance as durable.

## Worked example (illustrative, single)
Demand is set to grow faster than supply for several years; the widening gap forecasts strengthening pricing power before it shows in reported margins.
