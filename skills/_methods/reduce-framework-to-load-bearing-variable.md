---
name: reduce-framework-to-load-bearing-variable
kind: reasoning
category: analytic-method
one_liner: Turn an intractable equal-weight multi-factor model into an ordered decision tree by finding the one factor whose absence makes the rest irrelevant, and analyzing it first.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [historian, teacher]
source_anchors: [ch01¶40, ch01¶41]
promoted: 2026-06-13
status: promoted
---

## When to use
You face an established but unwieldy framework with several factors presented as equally important, and applying all at once is intractable.

## Method
1. List the framework's factors.
2. For each, run the absence test: "if this were removed, would the others lose most of their force?" The factor whose removal collapses the rest is the candidate gating variable.
3. Analyze and resolve the dominant factor first; escalate to the remaining factors only if it is present. This converts an N-variable model into an ordered decision tree (one primary driver, the rest as second-order modifiers).
4. Sanity-check against the base rate: durable, long-surviving frameworks usually reduce to one primary cause plus modifiers, not many co-equal forces. A framework that resists reduction is either genuinely multi-causal or not yet mature.

## Inputs → Outputs
- Inputs: a multi-factor model + the domain it describes.
- Outputs: a ranked framework with a single gating factor first and a simpler analysis sequence (start with the primary, add complexity only as needed).

## Failure modes / assumptions
- Assumes one factor really dominates; some systems are irreducibly multi-causal — forcing a single driver oversimplifies ("as simple as possible, but not simpler"). If two are co-dominant, keep both at the top.
- The dominant factor may differ by context.
- Risk of motivated reduction: picking the factor you already favor rather than the one the absence-test selects.
