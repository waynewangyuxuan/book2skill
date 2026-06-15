---
name: choose-nodes-that-reveal-the-whole-system
kind: decision
category: analytic-method
one_liner: When you can only study a few items in a network, pick the ones positioned to reveal the most information about their neighbors, treating coverage choice as an information-maximization problem.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Choosing which few items to cover deeply within a larger interconnected network you cannot fully study.

## Method
1. Map the network and each candidate item's connections to its neighbors.
2. Estimate how much information about its neighbors each candidate would reveal if studied.
3. Pick the nodes positioned to reveal the most about the rest of the system (hubs, suppliers, bottlenecks).
4. Treat the coverage choice as information-maximization, not equal sampling.

## Inputs to Outputs
- Inputs: the network; each node's connectivity and information yield.
- Outputs: a coverage set chosen to illuminate the whole system.

## Failure modes / assumptions
- Covering isolated items that reveal nothing about the rest.
- Mis-estimating which nodes are genuinely revealing.

## Worked example (illustrative, single)
Limited to a few names, a practitioner covers a key supplier whose order book illuminates a dozen downstream items rather than a peripheral one.
