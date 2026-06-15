---
name: verify-comparability-before-comparing-two-series
kind: decision
category: causal-and-statistical-hygiene
one_liner: Run a comparability checklist — seasonality, inflation, period basis, definitional consistency, revision vintage — before computing any rate or appending two data series, and pin the denominator's period and basis before comparing.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Before comparing, ratioing, or concatenating two data series that may not be measured on the same basis.

## Method
1. Run a comparability checklist: seasonality, inflation/deflation, period basis (e.g., trailing vs forward), definitional consistency, and revision vintage.
2. Deflate nominal series by the relevant differential before sizing any move.
3. Pin the denominator's period and basis before comparing ratios.
4. Reconstruct history with as-of-then data, not later-revised figures, and keep time-relative metrics on a continuously rolling forward window.
5. Only after comparability is confirmed, compute the rate or append the series.

## Inputs → Outputs
- Inputs: two series with their definitions, periods, and vintages.
- Outputs: a comparable pair (or a documented adjustment), or a refusal to compare.

## Failure modes / assumptions
- Comparing a nominal series to a real one, or trailing to forward.
- Using revised figures as if they were known at the time.

## Worked example (illustrative, single)
Two growth rates look divergent until one is found to be on a forward basis and the other trailing; rebased, they agree.
