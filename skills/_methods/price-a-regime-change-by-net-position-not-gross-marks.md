---
name: Price a regime change by net position, not gross marks
kind: decision
category: macro-systems
one_liner: Judge winners and losers of a managed-price regime change by each entity's NET exposure to the moving variable, not gross holdings or accounting marks; the defender of a wrong price accumulates real losses continuously, so "they can't afford to let it move" is backwards.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [trader, teacher]
source_anchors: [ch02¶25, ch02¶26, ch02¶30]
promoted: 2026-06-14
status: promoted
---

# Price a regime change by net position, not gross marks

## When to use
When a managed price (a peg, a controlled rate or level) is expected to move and you must work out who actually gains or loses, and the second-order behavioral consequences.

## Method
1. For each affected entity, compute its NET position (long minus short) in the moving variable, not gross holdings.
2. Distinguish accounting loss from economic loss: a mark on a large gross stash is irrelevant if real purchasing power is unchanged; find the genuinely mismatched balance sheets.
3. Distinguish real from realized loss: if the managed price is wrong, the real loss is incurred at every transaction at the wrong price, not at the eventual re-mark — so the defender's delay deepens its own hole.
4. Build the consequence map: sectors gaining purchasing power raise activity, those losing it cut; derive the aggregate behavioral shift from the transfer map, not sentiment.

## Inputs -> Outputs
Inputs: the regime change; each entity's net exposure; a view on whether the price is mispriced. Outputs: a winner/loser map by net position, a corrected directional read, and a sector-level behavioral forecast.

## Failure modes / assumptions
- Net exposure is hard to measure with implicit exposures; approximate and stress-test.
- The real-vs-realized logic depends on conviction the price is genuinely wrong.

## Worked example
A holder of a huge gross foreign stash is wrongly called the loser from an appreciation; netting shows it is long real goods, and only the mismatched defender of the peg loses, flipping the directional read.
