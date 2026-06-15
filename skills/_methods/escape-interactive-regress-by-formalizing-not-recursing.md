---
name: escape-interactive-regress-by-formalizing-not-recursing
kind: reasoning
category: competitive-interaction
one_liner: When reasoning about a rival's reaction spirals into infinite regress, stop recursing and switch tools — impose simplifying assumptions and lay out a small payoff structure.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch08¶15]
promoted: 2026-06-13
status: promoted
---

## When to use
When anticipating another agent's response leads to "my move depends on their reaction, which depends on their read of my move..." with no bottom.

## Method
1. Recognize the regress: each added level of "what they think I think" buys no new clarity.
2. Stop thinking one level deeper. The cure for regress is not more recursion.
3. Switch representation: impose explicit simplifying assumptions (finite choices per player) and lay the interaction out as a small payoff structure.
4. Analyze the structure for stable outcomes instead of chasing nested expectations.

## Inputs → Outputs
- Input: an interactive decision trapped in mutual-anticipation regress.
- Output: a finite formalized representation (payoff layout) ready for equilibrium analysis.

## Failure modes / assumptions
- Failure: continuing to recurse, or over-simplifying away the choices that actually matter.
- Assumption: the interaction can be reduced to a manageable set of actions and payoffs without losing its essence.
