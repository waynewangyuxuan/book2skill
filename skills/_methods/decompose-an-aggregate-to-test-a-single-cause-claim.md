---
name: Decompose an aggregate to test a single-cause claim
kind: reasoning
category: causal-and-statistical-hygiene
one_liner: A single-cause explanation must move every component of an aggregate; decompose it and reject the cause if it can only touch one slice while others drive the total, then re-attribute by true incidence.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, skeptic, teacher, historian]
source_anchors: [ch02¶36, ch04¶32]
promoted: 2026-06-14
status: promoted
---

# Decompose an aggregate to test a single-cause claim

## When to use
Before accepting a behavioral or single-cause explanation for a movement in an aggregate composed of distinct parts.

## Method
1. Decompose the aggregate into its components (by sector, actor, or account).
2. Test whether the proposed mechanism can move every component, or only one.
3. Reject the explanation if the aggregate is driven by components the mechanism cannot touch.
4. Second pass: trace each non-obvious component to its funding source — accounting location can differ from economic incidence, so re-attribute to the true bearer.

## Inputs -> Outputs
Inputs: an aggregate; its component breakdown; the proposed cause. Outputs: pass/fail on the explanation plus a corrected attribution by incidence.

## Failure modes / assumptions
- Components may be interdependent.
- The breakdown data may be missing, forcing estimates.

## Worked example
A "consumers got thrifty" story for a falling aggregate is rejected once decomposition shows the move came from a component consumer behavior cannot reach.
