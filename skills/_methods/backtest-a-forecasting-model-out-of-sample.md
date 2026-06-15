---
name: backtest-a-forecasting-model-out-of-sample
kind: reasoning
category: forecasting-and-probability
one_liner: Refit a predictive model on a truncated history ending at a past point and score its prediction of the subsequent known period under strict pseudo-out-of-sample replay; expect failure at the inflections that actually matter and budget trust accordingly.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, skeptic, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Validating any predictive model before relying on its forward forecast.

## Method
1. Truncate the history at a past point; fit only on data available then.
2. Predict the subsequent known period and score the prediction (strict pseudo-out-of-sample replay).
3. Note that models reliably fit stable stretches and break at the inflections that actually drive decisions — concentrate the test there.
4. Budget trust in the live forecast according to the model's measured behavior at past inflections, not its in-sample fit.

## Inputs → Outputs
- Inputs: a model; a held-out later period; past inflection points.
- Outputs: an out-of-sample score and a regime-change fragility read.

## Failure modes / assumptions
- Trusting in-sample fit as evidence of predictive skill.
- Leaking later information into the truncated fit.

## Worked example (illustrative, single)
A model with excellent in-sample fit is shown to miss every past turning point in pseudo-out-of-sample replay, so its forward call is heavily discounted.
