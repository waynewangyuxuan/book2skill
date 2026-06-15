---
name: express-a-model-estimate-as-an-uncertainty-band
kind: reasoning
category: forecasting-and-probability
one_liner: Read a fit through paired statistics (variance explained + standard error), run sensitivity on the soft high-leverage inputs, diagnose and remove residual structure, and state a range rather than a false-precise point.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Stating and acting on an estimate produced by a fitted model.

## Method
1. Read the fit through paired statistics — variance explained and standard error — not a single point.
2. Plot residuals against time to detect serial correlation; add lagged terms to remove it, since uncorrected autocorrelation overstates reliability.
3. Run sensitivity on the soft, high-leverage inputs.
4. State a range, with the inputs that move it, rather than a false-precise central number.

## Inputs to Outputs
- Inputs: a fitted model; its residuals; its soft inputs.
- Outputs: an estimate as a range with explained-variance, standard error, and sensitivity.

## Failure modes / assumptions
- Quoting a point estimate as if it were certain.
- Ignoring autocorrelation and overstating reliability.

## Worked example (illustrative, single)
A practitioner finds residual serial correlation, adds a lag, and then states the forecast as a band with its driving sensitivities.
