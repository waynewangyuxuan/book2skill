---
name: screen-cooperation-scope-by-joint-payoff-variance
kind: decision
category: competitive-interaction
one_liner: Decide whether cooperation is even worth pursuing by summing all players' payoffs per outcome — a varying joint sum means surplus to share; a constant sum means a zero-sum game with nothing to negotiate.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher]
source_anchors: [ch11¶53, ch11¶63]
promoted: 2026-06-13
status: promoted
---

## When to use
After laying out a competitive interaction (matrix or tree), as a first screen to decide whether to pursue a cooperative/bargaining strategy or accept that the game is adversarial.

## Method
1. For every outcome, compute the sum of all players' payoffs, including non-monetary values where they matter.
2. Inspect the variation in that joint total:
   - Joint total varies → positive-sum structure; a Pareto-superior cooperative target exists, so steer toward the highest-joint-sum outcome.
   - Joint total is constant → constant/zero-sum game; cooperation yields nothing, expect unrelenting rivalry.
3. Link structure to behavior: invariant joint totals typically arise where actors care about relative performance (share, beating rivals) — a cultural red flag predicting remorseless competition. Rewrite payoffs to include such motives before reading the variance.
4. Cross-check with player count: needing more than ~6 meaningful profiles to model the game signals no real barriers, making direct-interaction analysis moot.

## Inputs → Outputs
- Inputs: the payoff for each player in each outcome of the matrix/tree, including soft motives.
- Outputs: a cooperate-able vs inherently-adversarial verdict and, if cooperate-able, the joint-maximizing target outcome.

## Failure modes / assumptions
- Must include non-profit motives; a relative-performance culture can make an objectively variable-sum game behave constant-sum.
- Identifying the highest-joint cell doesn't make it reachable — sustaining it needs a fair, enforced division (see the surplus-division skill).
- Assumes payoffs are estimable across outcomes.

## Worked example (illustrative, single)
In a two-firm pricing matrix the joint payoff is highest when both hold high prices and lowest when both cut — that variation signals real room to cooperate; had every cell summed to the same total, the rivalry would be zero-sum with nothing to negotiate.
