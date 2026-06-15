---
name: validate-the-assumptions-feeding-a-model-not-the-machinery
kind: decision
category: forecasting-and-probability
one_liner: Spend the bulk of effort confirming the inputs that drive a model via outside evidence rather than elaborating the model itself — an intricate model with wrong inputs forecasts no better, and complexity is often avoidance of the real assumption risk.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, skeptic, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Deciding where to spend modeling effort, when there is a temptation to add machinery instead of validating inputs.

## Method
1. Identify the inputs that actually drive the model's output.
2. Spend the bulk of effort confirming those inputs against outside evidence.
3. Recognize that elaborating tooling feels productive but does nothing to validate assumptions — treat added complexity as avoidance.
4. Keep the model as simple as the decision allows; complexity raises update time, error risk, and the cost for others to inherit it.

## Inputs to Outputs
- Inputs: a model; its driving assumptions; available outside evidence.
- Outputs: externally-validated inputs and a model no more complex than needed.

## Failure modes / assumptions
- Polishing the model while leaving its key inputs unverified.
- Adding rows/factors as a proxy for rigor.

## Worked example (illustrative, single)
Rather than refine an elaborate model, a practitioner spends the week verifying its single load-bearing demand assumption with field checks.
