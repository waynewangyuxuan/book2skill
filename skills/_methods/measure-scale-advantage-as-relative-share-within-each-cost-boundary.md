---
name: measure-scale-advantage-as-relative-share-within-each-cost-boundary
kind: decision
category: competitive-advantage
one_liner: Compute scale advantage from relative share inside the boundary where a given fixed cost actually stays fixed — never from absolute size.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch03¶5, ch03¶24, ch05¶74]
promoted: 2026-06-13
status: promoted
---

## When to use
When evaluating whether a player has a real economies-of-scale advantage, or sizing one.

## Method
1. Model cost as fixed + (variable × volume), so average cost = variable + fixed/volume. The advantage comes only from the share gap that lets a player spread fixed cost over more units than rivals.
2. For each fixed-cost category, find its **relevant boundary** by asking: over what territory does this particular fixed cost stay fixed? (e.g. a delivery radius for logistics, a media market for advertising, a manager's reachable cluster for supervision, a product line for R&D.)
3. Measure the player's share within each cost's own boundary — not a single company-wide size figure.
4. Conclude there is a scale advantage only where the player has higher relative share inside a boundary where fixed costs remain proportionately large.

## Inputs → Outputs
- Input: a player's cost structure and its share figures by region/segment.
- Output: per-cost-category scale-advantage assessment based on in-boundary relative share.

## Failure modes / assumptions
- Failure: citing total/global size as proof of scale advantage when fixed costs pool locally.
- Assumption: you can locate the boundary for each fixed cost; if the market is huge relative to fixed costs, the advantage may be negligible.
