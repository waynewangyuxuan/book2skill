---
name: Classify an intervention as level-changing vs composition-only
kind: decision
category: macro-systems
one_liner: Ask whether an intervention moves the conserved netting variable; if it only reshuffles who fills constant demand, predict ~zero aggregate change (theater) and locate the real effect in distribution, efficiency, or risk.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, skeptic, teacher, trader]
source_anchors: [ch05¶25, ch05¶31, ch05¶33, ch07¶12]
promoted: 2026-06-14
status: promoted
---

# Classify an intervention as level-changing vs composition-only

## When to use
When a proposed intervention claims to move an aggregate balance but may only reshuffle composition.

## Method
1. Identify the conserved netting variable that pins the aggregate.
2. Ask: does the intervention change that variable, or only reallocate which counterparty fills fixed demand?
3. If composition-only, predict ~zero change in the aggregate and call it theater.
4. Locate the true effect in distribution, efficiency, or risk.
5. Note that an intra-pool swap hands funds to a counterparty who redeploys them inside the pool, conserving the aggregate (only spreads reprice).

## Inputs -> Outputs
Inputs: the intervention; the conserved variable. Outputs: level-changing vs composition-only verdict, plus where the real effect lands.

## Failure modes / assumptions
- Second-round effects can be non-trivial even when the aggregate is unchanged.
- Requires correctly identifying the netting variable.

## Worked example
A program that swaps which institution holds a balance is shown to leave the aggregate untouched, so its only real effect is on who bears the risk.
