---
name: classify-interaction-into-canonical-game
kind: reasoning
category: competitive-interaction
one_liner: Match a strategic interaction to a small library of well-studied archetypes and import the known solution set instead of deriving from scratch; if none fits and players are many, infer there are no real barriers.
source_book: [Competition Demystified]
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [historian, teacher, trader]
source_anchors: [ch01¶101, ch01¶103, ch08¶21, ch08¶40, ch08¶42, ch11¶25, ch11¶45]
promoted: 2026-06-13
status: promoted
---

## When to use
You confront a strategic interaction among a small number of identifiable actors and are tempted to analyze it from first principles.

## Method
1. Keep a small library of canonical interaction archetypes and their solved dynamics. Two cover the large majority of cases:
   - Repeated price/quality rivalry over a reversible variable → prisoner's-dilemma archetype (large joint gains from cooperation, strong private incentive to defect; default attractor is the mutually-worst non-cooperative equilibrium, which is sticky).
   - Capacity/entry rivalry over a long-lived commitment → entry-preemption archetype (sequential, committed, hard-to-reverse moves).
2. Diagnose which archetype fits using a cue (is the contest over a reversible variable or a durable commitment?), and treat each archetype as a reference class carrying accumulated outcomes — retrieve the precedent rather than re-deriving it.
3. State the archetype's default predicted outcome, then look for the case-specific forces pulling toward or away from it.
4. Only build a bespoke model if no template fits. If more than ~half a dozen serious actors are involved and no archetype fits cleanly, infer there are probably no real barriers and that detailed interaction analysis is superfluous — default to operating efficiently.

## Inputs → Outputs
- Inputs: a competitive interaction + its participants + the reversibility of the contested variable.
- Outputs: an archetype label, the precedent base-rate outcome, and the case-specific deviations from it (or a "no barriers, model from scratch / just operate" verdict).

## Failure modes / assumptions
- Forcing a poor fit imports the wrong precedent.
- Archetypes organize and predict but rarely "solve" a real situation exactly.
- The default attractor can be overridden by structural/tactical interventions.

## Worked example (illustrative, single)
An industry with a long history of debilitating price wars points to the prisoner's-dilemma toolkit; one where every firm's expansion habitually triggered matching expansions points to the preemption tree — and the precedent outcome is your starting prediction, not a blank-slate derivation.
