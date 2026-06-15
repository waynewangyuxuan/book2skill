---
name: stress-test-a-statistic-against-framing-manipulation
kind: reasoning
category: causal-and-statistical-hygiene
one_liner: Treat the framing choices behind any presented number — start date, baseline, ratio base, percent-vs-point, denominator — as adversarially-selected free parameters; reclaim each, hold them fixed across all claims, and re-derive the number under neutral framing.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, skeptic, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Whenever an interested party presents a statistic, trend, or comparison and you must judge what it really shows.

## Method
1. Never let the presenter choose the analysis window — assume endpoints were picked to flatter; probe the period just outside the shown window.
2. Reclaim the denominator and the ratio base — for any percentage ask "off of what base?" and distinguish percent change from point change.
3. Check additive-vs-percent and the numeraire used.
4. Hold window, base, and definitions fixed across every claim being compared.
5. Re-derive the number under neutral framing and compare to the presented one.

## Inputs → Outputs
- Inputs: a presented statistic with its framing choices.
- Outputs: the neutrally-framed value and the size of the framing distortion.

## Failure modes / assumptions
- Accepting the presenter's window or denominator as given.
- Confusing a point move with a percent move.

## Worked example (illustrative, single)
A "+40% since the trough" headline shrinks to a modest gain once the window is extended back across the prior peak the presenter excluded.
