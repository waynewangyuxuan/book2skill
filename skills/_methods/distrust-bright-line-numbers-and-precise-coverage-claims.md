---
name: distrust-bright-line-numbers-and-precise-coverage-claims
kind: decision
category: causal-and-statistical-hygiene
one_liner: Round cutoffs and suspiciously exact percentages usually launder a judgment call into an objective fact.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [skeptic]
source_anchors: [ch04¶15, ch08¶43]
promoted: 2026-06-13
status: promoted
---

## When to use
When a diagnostic hinges on a numeric threshold ("above X% = advantage; below Y% = none") or a confident coverage statistic ("80–90% of cases fit this model").

## Method
1. For each threshold, ask: where did this number come from, and what's the false-positive/false-negative behavior of cases sitting *just* on either side? A round, single-number, long-window cutoff usually encodes the author's judgment.
2. Test a borderline case: does an instance one point on the "other" side actually behave differently, or is the line cosmetic?
3. For coverage percentages, check the source. If it's intuition ("our informal impression"), recognize it as fake quantification — the honest version is "often." Ask how the denominator (all cases) was even enumerated; if it can't be, the percentage is rhetorical.

## Inputs → Outputs
- In: a thresholded test or coverage claim.
- Out: the cutoff treated as a tunable knob with its sensitivity, and any precision-theater statistics downgraded to qualitative language.

## Failure modes / assumptions
- Some thresholds are empirically calibrated and defensible — ask for the calibration before dismissing.
- Don't swing to "all numbers are arbitrary"; the target is *unjustified* precision, not quantification per se.
