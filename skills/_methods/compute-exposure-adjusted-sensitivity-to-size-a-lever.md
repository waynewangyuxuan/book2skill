---
name: compute-exposure-adjusted-sensitivity-to-size-a-lever
kind: reasoning
category: analytic-method
one_liner: Multiply an output's raw sensitivity to a driver by the fraction of the entity actually exposed to that driver to get the lever's true size, so headline sensitivities are not over-applied.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Sizing how much a driver actually moves an output when only part of the entity is exposed to it.

## Method
1. Estimate the output's sensitivity to the driver on the exposed portion.
2. Estimate the fraction of the entity actually exposed to that driver.
3. Multiply the two to get the true, exposure-adjusted lever size.
4. Use the adjusted figure, not the headline sensitivity, in scenarios and attribution.

## Inputs to Outputs
- Inputs: raw sensitivity to a driver; exposed fraction of the entity.
- Outputs: the exposure-adjusted lever size.

## Failure modes / assumptions
- Applying a sensitivity measured on the exposed slice to the whole entity.
- Mis-estimating the exposed fraction.

## Worked example (illustrative, single)
A driver moves the exposed segment sharply, but that segment is only a fifth of the entity, so the true earnings lever is a fifth of the headline figure.
