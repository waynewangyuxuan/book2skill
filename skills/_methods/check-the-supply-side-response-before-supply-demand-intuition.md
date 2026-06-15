---
name: Check the supply-side response before supply-demand intuition
kind: reasoning
category: causal-and-statistical-hygiene
one_liner: "More demand raises price" only holds if supply is held constant; if the same force that adds demand also raises supply, the net price effect can be zero — state the ceteris-paribus clause and test it.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, skeptic, teacher]
source_anchors: [ch08¶32, ch08¶33]
promoted: 2026-06-14
status: promoted
---

# Check the supply-side response before supply-demand intuition

## When to use
Before trusting a comparative-static claim like "more demand for X raises its price."

## Method
1. State the implicit ceteris-paribus clause (supply held constant).
2. Ask whether the same shock that raised demand also moves supply.
3. If supply rises by a comparable amount, the net price effect is muted or zero.
4. When a more-efficient channel is displaced by a less-efficient one to hold an outcome constant, apply the efficiency-ratio multiplier (>1:1): the less-efficient channel over-compensates, which can flip a related quantity's sign.

## Inputs -> Outputs
Inputs: a supply-demand claim; the shock; the supply response. Outputs: the corrected net price/quantity effect.

## Failure modes / assumptions
- The supply response may lag, restoring the naive sign short-run.
- Requires estimating both elasticities.

## Worked example
A claim that rising demand for a safe asset must raise its price fails once the same flows are shown to expand its supply in step.
