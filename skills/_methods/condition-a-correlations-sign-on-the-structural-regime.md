---
name: Condition a correlation's sign on the structural regime
kind: decision
category: causal-and-statistical-hygiene
one_liner: The same input can produce opposite outputs in different structural regimes; trace a "universal" correlation to its mechanism, identify the moderating variable, and never port the correlation across regimes where that mechanism's premise breaks.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [skeptic, quant, teacher]
source_anchors: [ch03¶32, ch03¶33, ch03¶34, ch03¶38, ch03¶39, ch04¶47]
promoted: 2026-06-14
status: promoted
---

# Condition a correlation's sign on the structural regime

## When to use
Before transplanting a correlation or textbook intuition from one system to another with different structure.

## Method
1. Trace the correlation to the mechanism that gives it its sign.
2. Identify the moderating/structural variable that mechanism depends on (e.g. where wealth is held, how a rate transmits).
3. Check whether that premise holds in the target regime.
4. If the premise breaks, expect the sign to flip; do not port the relationship.

## Inputs -> Outputs
Inputs: a correlation; its mechanism; the target regime's structure. Outputs: the expected sign in the target regime (possibly inverted).

## Failure modes / assumptions
- Requires correctly naming the moderating variable.
- Multiple mechanisms may operate; net them.

## Worked example
A rate cut that stimulates consumption where households are net borrowers is shown to depress it where households are net fixed-rate savers, so the sign inverts.
