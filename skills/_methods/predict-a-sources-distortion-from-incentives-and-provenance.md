---
name: predict-a-sources-distortion-from-incentives-and-provenance
kind: reasoning
category: research-process-and-sourcing
one_liner: Before trusting any source or dataset, trace who funds or benefits from it and model which way it bends — provenance is a prior on bias, and opacity is itself a signal.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, skeptic, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Whenever you receive externally-supplied data, a forecast, or testimony and must weight its reliability before using it.

## Method
1. Identify who funded the data's collection or who benefits from the claim, before examining its content.
2. Model the direction the incentive bends the figure; any funder unlike you likely shaped it toward their interest.
3. Treat polish and specificity as orthogonal to honesty — do not infer trust from production quality.
4. Treat opacity (refusal to expose provenance or method) as an adverse signal in itself.
5. Discount the input by the modeled bias rather than rejecting or accepting it wholesale.

## Inputs → Outputs
- Inputs: a source/dataset; its funder and beneficiary; its transparency level.
- Outputs: a directional bias estimate and a discounted weight.

## Failure modes / assumptions
- Trusting a number because it is precise and well-formatted.
- Failing to ask who paid for it.

## Worked example (illustrative, single)
A glossy industry study funded by the parties it flatters is down-weighted on provenance before its content is even read.
