---
name: detect-moat-by-two-signal-convergence
kind: decision
category: competitive-advantage
one_liner: Confirm a durable competitive advantage only when market-share stability AND sustained returns above the cost of capital agree, then name the structural source as a cross-check.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant, trader, historian, teacher]
source_anchors: [ch01¶115, ch04¶4, ch04¶6, ch04¶8, ch04¶10, ch04¶15, ch04¶16, ch04¶86, ch04¶89, ch09¶22, ch10¶24]
promoted: 2026-06-13
status: promoted
---

## When to use
Before betting on, investing behind, or defending a market position — whenever you must decide if it is structurally protected or merely a transient lead that competition will erode. Run before any valuation that assumes excess returns persist.

## Method
1. **Map and bound the arena first.** Segment the field, list the meaningful players per segment, and draw boundaries by competitor-roster overlap: merge sub-areas where the same dominant players recur, keep separate those whose leaders differ. Getting the boundary wrong invalidates every downstream test.
2. **Require two independent signals that must agree:**
   - Signal A — share stability: over a multi-year window (≥5, ideally ~10 years), renormalize tracked competitors' shares and compute each firm's average absolute share change. Calibrated screens (recalibrate per domain): can't count the serious players on one hand → assume no barrier; average drift > ~5pp → no barrier; ≤ ~2pp → strong barrier.
   - Signal B — sustained return on capital: compute ROIC over the window and compare to the risk-matched cost-of-capital hurdle (the spread, not the absolute level, is what matters). Persistently well above the hurdle → advantage; hovering near it → none.
3. **Read agreement and disagreement as information.** Both point the same way → verdict. Stable share + ROIC ≈ hurdle, or churning share + high ROIC → the edge is temporary or execution-driven, not structural.
4. **Name the structural source** (proprietary cost, customer captivity, economies of scale, regulation) as a cross-check. Metrics that pass with no nameable source are likely transient or good management.
5. **De-aggregate buried segments.** If the protected market sits inside a diversified entity, do not trust blended financials — read a focused pure-play comparable as the segment proxy.

## Inputs → Outputs
- Inputs: per-segment competitor rosters; multi-year share data; multi-year ROIC (or margin + capital intensity); risk-matched cost of capital; pure-play comparables.
- Outputs: a per-segment moat / no-moat / management-only verdict, the named source, and a confidence note (do the two signals agree?).

## Failure modes / assumptions
- Neither high returns alone nor stable share alone is sufficient — both gates must pass.
- ROIC is unreliable for asset-light models (tiny/negative/intangible-heavy capital); cross-check with return-on-sales.
- Renormalized share can hide the whole group losing to outside substitutes — check the group's absolute trajectory.
- A short window can mistake luck for structure.

## Worked example (illustrative, single)
A category whose leaders' shares moved under ~2pp over a decade with ROIC far above the cost of capital passes both signals — a strong moat, confirmed by naming scale-plus-captivity as the source. A neighboring category whose shares swung ~15pp with clustered ordinary margins fails both — no moat.
