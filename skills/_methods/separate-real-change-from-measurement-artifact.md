---
name: Separate real change from measurement artifact
kind: reasoning
category: macro-systems
one_liner: A reported gain/loss may be an accounting recognition, a moving-numeraire illusion, or a nominal move rather than a real change; price a loss at the moment of the mispriced transaction, and deflate any nominal move by the relevant differential before sizing it.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, skeptic, teacher, trader]
source_anchors: [ch02¶25, ch02¶26, ch02¶27, ch02¶30, ch03¶43, ch08¶59]
promoted: 2026-06-14
status: promoted
---

# Separate real change from measurement artifact

## When to use
When a number is cited as a real gain or loss but may be an accounting recognition, a unit-of-account illusion, or merely nominal.

## Method
1. Classify the reported change: accounting recognition (delayed recognition of an earlier real event), moving-numeraire illusion (the measuring unit changed), or nominal move.
2. For losses, price them at the moment of each mispriced transaction using the gap to true value; later mark-to-market only recognizes them, and delaying recognition grows the cumulative real loss.
3. Confirm denomination invariants: a face-value obligation is unchanged in its own unit by a rate move — reject any story that requires the invariant to change.
4. Deflate any nominal move by the relevant differential (productivity, inflation gap) before judging its real size.

## Inputs -> Outputs
Inputs: a reported change; the relevant invariant and differential. Outputs: the real change (possibly zero) with the artifact named.

## Failure modes / assumptions
- Confusing accounting-value swings (which can be real) with face-value changes (which cannot).
- The invariant and differential must be correctly identified.

## Worked example
A headline currency-translation "loss" is shown to be a numeraire artifact once the asset and its uses reprice by the same factor, leaving real value unchanged.
