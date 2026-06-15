---
name: normalize-then-threshold-for-overextension
kind: decision
category: behavioral-and-sentiment
one_liner: Convert a raw series into a bounded normalized indicator with overbought/oversold thresholds, scale band width to each item's volatility, and require size-and-persistence (debounce) to confirm a breach before acting.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Building a mean-reversion or overextension indicator from a raw price/level series.

## Method
1. Convert the raw series into a bounded normalized indicator (e.g., scaled to a fixed range).
2. Set overbought/oversold thresholds on the normalized scale.
3. Scale the band width to each item's own volatility so the thresholds mean the same thing across items.
4. Require a breach to clear both a size and a persistence (debounce) test before treating it as a confirmed signal.

## Inputs to Outputs
- Inputs: a raw series; per-item volatility; size and persistence rules.
- Outputs: a calibrated overbought/oversold indicator with debounced breaches.

## Failure modes / assumptions
- Acting on a single-bar breach that immediately reverts.
- Using one band width across items of very different volatility.

## Worked example (illustrative, single)
A volatile item and a calm item get different band widths; only a sustained, large breach in either fires the signal.
