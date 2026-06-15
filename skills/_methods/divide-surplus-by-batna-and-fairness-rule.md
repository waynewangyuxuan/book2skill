---
name: divide-surplus-by-batna-and-fairness-rule
kind: decision
category: competitive-interaction
one_liner: Run any cooperative negotiation in two phases — first maximize the joint pie, then divide only the surplus above the sum of BATNAs by the fairness rule that keeps the split defection-proof.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher, trader]
source_anchors: [ch14¶18, ch14¶22, ch14¶55, ch14¶58, ch14¶61, ch14¶62, ch14¶63, ch14¶66, ch14¶68, ch14¶22]
promoted: 2026-06-13
status: promoted
---

## When to use
Negotiating or predicting the outcome of any alliance, supplier/customer relationship, value-chain split, or coalition where parties both create and split value — and you need a *stable* division, not just an efficient one.

## Method
1. **Phase 1 — grow the pie (never reverse the order).** Exhaust all win-win moves that expand total attainable value without any party sacrificing; identify the efficiency frontier beyond which no one gains without another losing. Premature haggling over slices forecloses joint gains. (To find the ceiling and your own role, run the single-coordinator thought experiment.)
2. **Phase 2 — compute each party's threat point / BATNA:** the payoff it gets if cooperation collapses and it pursues its best alternative. No party accepts less than this (individual-rationality floor).
3. **Find the divisible surplus** = total joint value − Σ(BATNAs). Only this is up for division.
4. **Apply the capture rule first:** a party whose outside option is set by free entry (no barrier) is competed down to its cost of capital and captures none of the surplus, however much value it helps create — the barrier-protected chokepoint claims it. Start from outside options, not from effort or "partnership" language.
5. **Then apply the fairness rules, in order, to the surplus** (where "fair" = defection-proof, not moral):
   - Individual rationality — no party below its BATNA.
   - Symmetry — among parties each indispensable and essentially alike, split the surplus equally regardless of size or power.
   - Linear invariance — among peers sharing one horizontal segment, split in proportion to relative economic strength.
6. **Forecast durability from fairness-compliance.** A split that lets one party grab more than these rules allow is unstable regardless of current power — a shortchanged party defects or enables a rival, and one defection can cascade the whole arrangement into collapse. If you hold the advantage, cap your own take at the fair share; the fair split is the profit-maximizing split over time.

## Inputs → Outputs
- Inputs: the set of win-win moves; each party's BATNA and barrier status; whether parties are complementary-indispensable or same-segment peers.
- Outputs: the maximized joint value, the divisible surplus, each party's predicted stable share, and a flag on any grievance that would destabilize the deal.

## Failure modes / assumptions
- "Partner with a dominant player and prosper" is a delusion: a replaceable contributor is pinned to its cost of capital regardless of how much value it adds.
- BATNA estimation is the crux; misjudging your own threat point leads to over-claiming and collapse.
- The split must be *perceived* fair, not merely efficient; assumes transfers between parties are feasible.

## Worked example (illustrative, single)
Two complementary, equally-indispensable links in a chain with a $10M joint maximum and BATNAs of $2M and $4M split the $4M surplus equally (+$2M each) → $4M and $6M. A dominant integrator that instead grabbed a disproportionate slice from replaceable-but-resentful complementors saw them defect to a rival the moment one became credible — the unfair split, not the market, ended the arrangement.
