---
name: detect-bias-via-the-directional-consistency-of-your-revisions
kind: reasoning
category: epistemic-hygiene
one_liner: Audit the sign-run of your successive estimate revisions against your stated thesis; a persistent drift opposite the thesis is a measurable signal of bias or thesis failure, not a sequence of independent updates.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Reviewing whether your own estimate revisions reveal a hidden bias or a broken thesis.

## Method
1. Log the sign of each successive revision to your estimate.
2. Compare the run of signs against your stated thesis direction.
3. Treat a persistent drift opposite the thesis as a measurable signal — either creeping bias or a failing thesis, not independent noise.
4. Investigate the drift rather than continuing to make small same-direction revisions.

## Inputs to Outputs
- Inputs: the time-ordered signs of your revisions; the stated thesis direction.
- Outputs: a bias/thesis-failure flag from the revision sign-run.

## Failure modes / assumptions
- Treating a long one-directional run of revisions as a series of independent updates.
- Ignoring the drift because each step felt justified.

## Worked example (illustrative, single)
Six straight downward revisions against a bullish thesis flag that the thesis is wrong, prompting a from-scratch re-decision.
