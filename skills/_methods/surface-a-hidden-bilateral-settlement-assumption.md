---
name: Surface a hidden bilateral-settlement assumption
kind: reasoning
category: macro-systems
one_liner: A confident "no direct link, so no effect" secretly assumes pairwise settlement; allow network settlement and trace through the conserved netting variable, and the effect returns.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [skeptic, teacher, quant]
source_anchors: [ch05¶18, ch05¶20, ch05¶22]
promoted: 2026-06-14
status: promoted
---

# Surface a hidden bilateral-settlement assumption

## When to use
When an argument concludes "these two parties don't interact directly, therefore one cannot affect the other," and flows actually settle through a wider network.

## Method
1. Name the unstated assumption — usually that settlement is pairwise.
2. Replace it with the real structure: flows clear through a network into a conserved aggregate.
3. Trace the effect through the network rather than from any single pairwise overlap.
4. Pin the endpoint on the conserved netting variable, which the network must satisfy.

## Inputs -> Outputs
Inputs: a no-effect claim; the true settlement network; the conserved variable. Outputs: the restored effect, traced through the network.

## Failure modes / assumptions
- Requires that the network genuinely connects the parties through the conserved aggregate.
- Real frictions may attenuate the network channel; size it, don't just assert it.

## Worked example
"We don't trade much with them, so their policy can't hit our balance" fails once you route the effect through the shared global pool both parties settle into.
