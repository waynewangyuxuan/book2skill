---
name: classify-decisions-by-interaction-dependence
kind: decision
category: competitive-interaction
one_liner: Sort decisions into strategic vs operational by asking whether the outcome depends on other agents' reactions, not on size or money.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch01¶32]
promoted: 2026-06-13
status: promoted
---

## When to use
When you must triage a large list of decisions and decide which deserve scarce high-level attention and which can be delegated to execution.

## Method
1. For each decision ask one question: does the result depend on the actions/reactions of other independent agents?
2. If yes → label it **strategic**: it demands you model and anticipate others.
3. If it hinges only on your own execution quality → label it **operational**: optimize it internally and delegate.
4. Allocate top-level attention only to the strategic set; refuse to spend it on operational items however large their budget.

## Inputs → Outputs
- Input: a list of pending decisions.
- Output: a partition into strategic (interaction-dependent) vs operational (execution-dependent), with attention routed accordingly.

## Failure modes / assumptions
- Failure: using size/cost/hours as the dividing line — a huge investment can still be operational, a small choice can be strategic.
- Assumption: you can identify whether other agents' responses materially move the outcome; in murky cases default to treating it as strategic.

## Worked example (illustrative, single)
Choosing which theater of a conflict to engage first depends on the opponent's response → strategic; building a facility well depends on your own execution → operational.
