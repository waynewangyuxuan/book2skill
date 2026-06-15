---
name: pick-a-model-representation-by-whether-move-order-matters
kind: decision
category: analytic-method
one_liner: Choose matrix vs tree representation with one diagnostic — does the sequence/timing of moves change the outcome?
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch08¶21, ch11¶22]
promoted: 2026-06-13
status: promoted
---

## When to use
When you are about to formalize an interactive decision and must pick a representation.

## Method
1. Ask the single diagnostic: does the sequence or timing of moves change the outcome?
2. If moves are simultaneous, repeatable, and reversible (e.g. adjustable prices/features) → use the **payoff-matrix** form.
3. If moves are sequential with long-lived, hard-to-reverse commitments (e.g. building capacity, entering a market) → use the **decision-tree** form.
4. Match the representation to the temporal structure before doing any analysis.

## Inputs → Outputs
- Input: a description of the interaction and its move timing/reversibility.
- Output: the appropriate representation (matrix or tree) selected on principle.

## Failure modes / assumptions
- Failure: forcing a sequential commitment problem into a matrix, or a reversible repeated game into a tree.
- Assumption: the interaction is cleanly one type; mixed cases may need both, but pick the dominant temporal feature first.
