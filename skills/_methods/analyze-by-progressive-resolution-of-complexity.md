---
name: analyze-by-progressive-resolution-of-complexity
kind: reasoning
category: analytic-method
one_liner: Begin any complex analysis with the coarsest model that could answer the question, add detail only where the first pass shows it matters, and re-simplify whenever the picture turns intractable.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch04¶140]
promoted: 2026-06-13
status: promoted
---

## When to use
At the start of any analysis of a complex system, and whenever an in-progress analysis becomes unwieldy.

## Method
1. Start with the coarsest model that could plausibly answer the question (few segments, one dominant factor).
2. Run the first pass and see where it reveals that more detail actually matters.
3. Add complexity only at those points; treat complexity as a cost to be justified, not a default.
4. Whenever the picture becomes intractable, deliberately step back and simplify again.
5. Maintain clarity as the binding constraint — an intractable diagram is a failure even if comprehensive.

## Inputs → Outputs
- Input: a complex problem and a question to answer.
- Output: the simplest sufficient model, selectively elaborated only where it changes the answer.

## Failure modes / assumptions
- Failure: front-loading every factor and producing an unusable everything-connected picture.
- Assumption: the question is well-posed enough that a coarse model can be tested and refined toward it.
