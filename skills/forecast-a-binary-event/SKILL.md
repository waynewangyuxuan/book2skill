---
name: forecast-a-binary-event
description: Use when estimating the probability that a binary real-world event resolves YES (prediction-market / judgmental forecasting). A gated procedure — anchor on an outside-view base rate, adjust by inside-view evidence, red-team the estimate, account for dynamics and the resolution deadline, then output a calibrated probability. Assembled from book2skill reasoning methods. Triggers: "what's the probability that X", "will X happen by <date>", forecasting a yes/no market.
---

# Forecast a binary event

Turn a question + resolution rules into a calibrated P(YES). Follow the steps in order; each names the method it applies (provenance in `../_methods/`).

## Spine
A good probability is an **outside-view base rate, adjusted by inside-view evidence, then stress-tested for the ways it could be wrong** — not a gut number and not a story fitted to one vivid scenario.

## Procedure
1. **Frame & find the reference class.** Restate exactly what resolves YES (per the rules). Put the event in the *narrowest reference class whose base rate you can estimate*, and start from that base rate — not from the specific story. (`match-the-reference-class-to-the-positions-scope`; `find-a-structural-isomorphism-and-transfer-the-precedent`)
2. **Inside view: the load-bearing variable.** Identify the one or two variables that actually decide this case; ignore the rest. Name the decisive variable you *cannot* observe — your uncertainty lives there. (`reduce-framework-to-load-bearing-variable`; `find-the-decisive-variable-the-method-cannot-measure`; `analyze-by-progressive-resolution-of-complexity`)
3. **Adjust from the base rate** by the inside-view evidence — *move it, don't replace it.* Strong specific evidence shifts more; thin evidence shifts little. Don't anchor on the vivid scenario.
4. **Red-team the estimate** before committing:
   - Reasoning from the outcome / a survivor set? Find the denominator. (`test-conclusions-for-selection-on-the-outcome-bias`; `correct-survivorship-by-expected-cost`)
   - Is the case for YES (or NO) *unfalsifiable* — does any evidence get re-explained to fit? (`detect-claims-immunized-against-falsification`; `catch-hindsight-relabeling-and-overconfident-counterfactuals`)
   - Does an "inevitable" mechanism quietly depend on hidden enabling conditions? (`enumerate-the-hidden-enabling-conditions-of-an-inevitable-mechanism`)
   - Are you *predicting* or just *organizing* what you already believe? (`separate-frameworks-that-predict-from-those-that-only-organize`)
5. **Dynamics & deadline.** Does the rule require something to *happen by a date*? Systems correct asymmetrically (slow to clear gluts), trends/advantages decay. Discount any "it'll happen soon." (`assume-asymmetric-correction-speed-in-oversupplied-systems`; `discount-advantage-by-its-decay-clock`; `model-every-channel-by-which-an-outcome-erodes`)
6. **Calibrate & output.** Convert to a probability you'd bet at. Keep honest uncertainty — avoid 0.02 / 0.98 unless the rules nearly force it; avoid both false confidence and false balance. (`propagate-uncertainty-before-trusting-a-forecast-driven-decision`)

## Guardrails
- The base rate is the anchor; the story only adjusts it.
- A longer analysis is not a better one — decisiveness toward the right number is the goal.
