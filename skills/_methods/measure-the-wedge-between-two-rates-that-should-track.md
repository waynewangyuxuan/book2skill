---
name: Measure the wedge between two rates that should track
kind: reasoning
category: macro-systems
one_liner: Define an equilibrium where two growth rates should match, then treat their cumulative gap — summarized as a ratio of cumulative growth multiples — as the lever that transfers share between parties.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch03¶16, ch04¶32]
promoted: 2026-06-14
status: promoted
---

# Measure the wedge between two rates that should track

## When to use
When two series ought to grow together in equilibrium and a sustained divergence is quietly redistributing share between two parties.

## Method
1. State the equilibrium null: rate A should equal rate B over the long run.
2. Measure the sustained wedge (A minus B) and its cumulative effect on shares.
3. Summarize a long window by the ratio of cumulative growth multiples (e.g. one series x2 vs another x3) — cleaner than annual rates.
4. Treat the wedge as the measurable driver of the downstream aggregate.

## Inputs -> Outputs
Inputs: two tracking series; the equilibrium null. Outputs: the cumulative wedge and the implied share transfer.

## Failure modes / assumptions
- The equilibrium null may not hold structurally.
- A temporary wedge differs from a regime change; check persistence.

## Worked example
Wages growing slower than productivity over decades is summarized by the cumulative-multiple gap, which equals the share transferred from labor to capital.
