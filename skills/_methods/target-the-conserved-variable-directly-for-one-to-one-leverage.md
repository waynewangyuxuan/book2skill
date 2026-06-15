---
name: Target the conserved variable directly for one-to-one leverage
kind: decision
category: macro-systems
one_liner: To actually move a conserved aggregate, act directly on the conserved variable for 1:1 transmission; proxy interventions get absorbed, and many distinct policies collapse to one underlying lever.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch05¶33, ch05¶41, ch03¶3, ch03¶19, ch03¶20]
promoted: 2026-06-14
status: promoted
---

# Target the conserved variable directly for one-to-one leverage

## When to use
When you want to move a conserved aggregate and are choosing among instruments, some of which only touch it indirectly.

## Method
1. Identify the conserved variable that pins the aggregate.
2. Classify each candidate instrument by whether it changes that variable directly or via a proxy.
3. Prefer the direct reallocation: it transmits ~1:1.
4. Expect proxy interventions to be partly or fully absorbed by offsetting adjustments.
5. Recognize that several differently-named policies may all operate the same underlying lever, so picking among them is mostly cosmetic.

## Inputs -> Outputs
Inputs: the conserved variable; the instrument set. Outputs: a ranked instrument list by transmission efficiency.

## Failure modes / assumptions
- A "direct" lever may carry larger political/transition costs.
- Absorption of proxies can be partial, not total.

## Worked example
To shift a consumption share, a direct income transfer transmits nearly 1:1 while an interest-rate nudge is largely absorbed by offsetting behavior.
