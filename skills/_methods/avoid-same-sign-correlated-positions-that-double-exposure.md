---
name: Avoid same-sign correlated positions that double exposure
kind: decision
category: forecasting-and-probability
one_liner: Don't build a position whose value is positively correlated with your own underlying fortunes — it wins twice and loses twice; quantify the correlation and prefer negative/zero-correlation positions.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, trader]
source_anchors: [ch07¶16, ch07¶52]
promoted: 2026-06-14
status: promoted
---

# Avoid same-sign correlated positions that double exposure

## When to use
When building or evaluating a position relative to an existing base exposure (a portfolio, a balance sheet, a country's reserves).

## Method
1. Estimate the correlation between the candidate position and your existing base state.
2. If positive, recognize the position doubles exposure (gain-gain / loss-loss) and amplifies volatility.
3. Prefer positions with negative or zero correlation to the base state to dampen volatility.
4. Override only if expected return is large enough to justify the concentrated risk.

## Inputs -> Outputs
Inputs: the candidate position; the base exposure; their correlation. Outputs: a keep/avoid decision and a volatility assessment.

## Failure modes / assumptions
- Correlations are unstable and regime-dependent.
- A same-sign position may still be justified by sufficient expected return.

## Worked example
A commodity exporter holding reserves in the same commodity-linked assets is shown to double its exposure, losing on both reserves and exports when the price falls.
