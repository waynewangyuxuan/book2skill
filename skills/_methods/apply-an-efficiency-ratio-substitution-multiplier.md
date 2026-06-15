---
name: Apply an efficiency-ratio substitution multiplier
kind: reasoning
category: macro-systems
one_liner: When a more-efficient channel is displaced by a less-efficient one to hold an outcome constant, the less-efficient channel must over-compensate (>1:1), which can flip the sign of a related side quantity.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch08¶33]
promoted: 2026-06-14
status: promoted
---

# Apply an efficiency-ratio substitution multiplier

## When to use
When one mechanism is replaced by a less-efficient one to keep some outcome fixed, and you must track a side quantity that the substitution affects.

## Method
1. Establish the relative efficiency of the two channels at producing the outcome.
2. Compute the substitution ratio: the less-efficient channel needs more than one unit per displaced unit.
3. Apply the >1:1 multiplier to the side quantity.
4. Check whether the over-compensation reverses the side quantity's expected sign.

## Inputs -> Outputs
Inputs: the two channels; their relative efficiency; the held-constant outcome. Outputs: the over-compensation multiplier and the side-quantity effect (possibly sign-flipped).

## Failure modes / assumptions
- Relative efficiency is often uncertain.
- The substitution may be incomplete, softening the multiplier.

## Worked example
Replacing an efficient funding channel with an inefficient one to hold output constant forces enough extra borrowing that the debt stock rises instead of falling.
