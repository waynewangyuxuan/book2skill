---
name: treat-a-threshold-as-an-anomaly-detector-never-a-verdict
kind: decision
category: causal-and-statistical-hygiene
one_liner: A tripwire (a screen, a bright-line ratio, a flagged outlier) fires on both wrongdoing and ordinary causes; enumerate the benign generators and rule them out before escalating, and apply class-conditioned thresholds with documented structural exceptions.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, skeptic]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
When a numeric screen or threshold flags an item and you must decide whether it indicates a real problem.

## Method
1. Treat the threshold breach as an anomaly detector, never a verdict.
2. Enumerate the benign generators that could trip the same wire (accounting choices, structural features, timing).
3. Rule out the benign causes before escalating to a wrongdoing conclusion.
4. Condition the threshold on the item's class and carry explicit structural exceptions, plus a materiality-and-recurrence test.

## Inputs to Outputs
- Inputs: a flagged item; the threshold; the benign generators of a breach.
- Outputs: an escalate-or-clear decision after ruling out benign causes.

## Failure modes / assumptions
- Treating a screen hit as proof of wrongdoing.
- Using one threshold across classes that legitimately differ.

## Worked example (illustrative, single)
An outlier ratio trips the screen but is explained by a one-time structural change; the practitioner clears it rather than escalating.
