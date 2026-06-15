---
name: gate-correlation-behind-a-causal-mechanism-or-confounder-check
kind: reasoning
category: causal-and-statistical-hygiene
one_liner: Treat any measured correlation as a hypothesis, not license to forecast — require a plausible causal mechanism or rule out a confounder before predictive use, and read conflicting or null single-variable studies as evidence of an omitted co-moving variable.
source_book: [Best Practices for Equity Research Analysts, The Great Rebalancing]
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher]
source_anchors: [ch01¶16, ch01¶54, ch01¶55, ch01¶56, ch03¶39, ch03¶44]
promoted: 2026-06-14
status: promoted
---

## When to use
Before relying on a correlation to predict, screen, or trade — especially a strong, convenient co-movement.

## Method
1. Treat the correlation as a hypothesis to be tested for mechanism or confounding, not as a conclusion.
2. Require a plausible causal mechanism before acting; spurious co-movement is common.
3. Look for an omitted confounder that could drive both series.
4. When single-variable studies conflict or show nothing, suspect offsetting co-moving variables (a confound or feedback) rather than concluding no relationship exists.
5. Prefer structural-identity reasoning over a narrow regression where one is available.

## Inputs → Outputs
- Inputs: a measured correlation; candidate mechanisms and confounders.
- Outputs: a go/no-go on predictive use, with the mechanism or the disqualifying confounder named.

## Failure modes / assumptions
- Forecasting off a correlation with no mechanism.
- Concluding "no effect" from a null when a confound is masking it.

## Worked example (illustrative, single)
Two series co-move tightly until a practitioner finds both are driven by a common cyclical factor, voiding the predictive use of one for the other.
