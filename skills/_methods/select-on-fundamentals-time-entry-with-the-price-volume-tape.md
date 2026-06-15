---
name: select-on-fundamentals-time-entry-with-the-price-volume-tape
kind: decision
category: behavioral-and-sentiment
one_liner: Use fundamentals to pick what to own and the market's price/volume verdict to time entry — wait for confirmation, weight a move's significance by the participation accompanying it, and treat sharp divergence between the two as a mandate for deeper work.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Combining a fundamental selection process with market-based entry timing.

## Method
1. Use fundamentals to decide what to own.
2. Use the market's price/volume tape to time the entry, waiting for confirmation rather than catching a falling knife.
3. Weight a move's significance by the participation/activity accompanying it — confirm a signal with an independent intensity measure.
4. Budget for the unrecoverable portion of the move that occurs before a lagging confirmation fires.
5. Treat a sharp divergence between your fundamental view and the tape as a mandate for deeper work, not an instant override.

## Inputs to Outputs
- Inputs: a fundamental selection; price and volume; an intensity confirm.
- Outputs: a confirmed entry timing and a divergence flag.

## Failure modes / assumptions
- Acting before confirmation and catching the falling knife.
- Letting the tape override fundamentals without investigating the divergence.

## Worked example (illustrative, single)
A fundamentally chosen name is bought only once price firms on rising volume; an unconfirmed earlier dip is left alone.
