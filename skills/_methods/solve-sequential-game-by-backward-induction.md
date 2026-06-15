---
name: solve-sequential-game-by-backward-induction
kind: decision
category: competitive-interaction
one_liner: Model an irreversible, sequential entry/capacity decision as a tree with base-case-relative payoffs, then fold it back from the leaves so your first move accounts for every rational downstream response.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant, teacher, historian]
source_anchors: [ch11¶20, ch11¶22, ch11¶24, ch11¶25]
promoted: 2026-06-13
status: promoted
---

## When to use
When decisions are sequential and hard to reverse (entering a market, adding plant/capacity, opening stores) and timing/commitment matters — distinct from quickly-adjustable, repeatable price moves (use a payoff matrix for those).

## Method
1. **Build the tree forward.** Branch each player's choices in time order (e.g. Enter/Don't; then incumbent Accept/Resist; then aggressor Persist/Withdraw).
2. **Set a zero base case.** Assign the no-action outcome a payoff of 0 to each player; score every leaf as the incremental gain/loss relative to that base. Adjust leaves for non-monetary motives.
3. **Fold back (backward induction).** Start at the last decision node, pick the deciding player's payoff-maximizing branch, replace the node with that payoff, and recurse toward the root. Each earlier player chooses anticipating the already-solved rational continuation.
4. **Read the predicted path.** The folded-back choices trace the likely outcome — which often reverses naive forward optimism (entering looks good until you trace the opponent's forced response). Commit only if the folded-back path is profitable for you.
5. **Simulate when complex.** Beyond toy size, war-game it with people in each role, given their motives and history. If you must track more than ~6 meaningful players, that itself signals no barriers — skip game analysis and default to operational efficiency.

## Inputs → Outputs
- Inputs: ordered decision nodes, each player's options, incremental leaf payoffs, known motives/history.
- Outputs: the predicted equilibrium path and the entry/response recommendation.

## Failure modes / assumptions
- Backward induction assumes rational, payoff-maximizing players with known motives — irrational or relative-performance-driven players break it; adjust payoffs first.
- Leaf payoffs are estimates; the fold-back is only as good as them.
- Reasoning forward to a "solution" instead of rolling back, or using absolute instead of base-relative payoffs, is the classic error.

## Worked example (illustrative, single)
If the aggressor will rationally withdraw (+0.2 beats −2), the defender prefers resisting (−1 beats −2), so the aggressor — foreseeing a −1/−1 standoff — declines to enter at all. The discretion emerges from folding the tree back, not from forward guessing.
