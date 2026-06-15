---
name: reduce-model-dimensionality-by-triaging-drivers
kind: decision
category: analytic-method
one_liner: Regress the output on all candidate inputs to find which independently drive it, forecast only those independent drivers, and derive any variable empirically tied to a driver above a fit threshold instead of forecasting both.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Building a forecast model with many candidate inputs, where forecasting all of them is wasteful.

## Method
1. Regress the output on all candidate inputs to find which independently drive it.
2. Concentrate forecasting effort on the genuinely independent drivers.
3. For any variable empirically tied to a driver above a fit threshold, derive it from the driver rather than forecasting it separately.
4. Auto-link the dependent variables to their primary driver so the model has fewer free forecasts to get wrong.

## Inputs to Outputs
- Inputs: candidate inputs; a multivariate fit; a dependence threshold.
- Outputs: a reduced set of independent drivers to forecast, with the rest derived.

## Failure modes / assumptions
- Forecasting variables that are just functions of a driver, doubling the error.
- A dependence relationship that breaks out-of-sample.

## Worked example (illustrative, single)
A practitioner finds three of eight inputs are independent drivers and derives the other five from them, shrinking the forecast surface.
