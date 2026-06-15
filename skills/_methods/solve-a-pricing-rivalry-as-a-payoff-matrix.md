---
name: solve-a-pricing-rivalry-as-a-payoff-matrix
kind: decision
category: competitive-interaction
one_liner: Turn a small-number price rivalry into a payoff matrix with computed cells, then find the stable outcome by the no-unilateral-improvement test.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch08¶27, ch08¶38]
promoted: 2026-06-13
status: promoted
---

## When to use
When a few identifiable competitors compete on a quickly-adjustable, repeatable variable (price, discount, ad spend, features) and you need to predict the stable outcome and whether it can be improved.

## Method
1. **Enumerate actions.** List each rival's discrete choices (e.g. two price points).
2. **Compute every cell.** Payoff = unit margin × volume, using an explicit demand-split rule (e.g. the low-price firm wins a disproportionate share). Quantify, don't narrate.
3. **Adjust for real motives.** If a player values market share or "beating the rival" over profit, rewrite that player's payoffs before solving.
4. **Equilibrium test.** For each cell, ask whether either player can raise its own payoff by changing only its own action while the other holds. The cell(s) where no unilateral switch helps are the stable (Nash) outcomes — often jointly worse than mutual cooperation.
5. **Use the verdict.** If the equilibrium is unfavorable, look to change the game (pre-commit to matching, alter payoffs) rather than play it straight.

## Inputs → Outputs
- Inputs: each rival's action set, unit margins, a demand-split assumption, any non-profit motives.
- Outputs: the filled payoff matrix and the identified stable outcome(s) with their payoffs.

## Failure modes / assumptions
- The demand-split parameter drives the answer; state it explicitly and sensitivity-test it.
- Matrix form fits simultaneous/repeatable moves only; for sequential, hard-to-reverse capacity moves use the backward-induction tree.
- Assuming pure profit-maximization when a rival is share- or ego-driven produces the wrong equilibrium.

## Worked example (illustrative, single)
Two retailers choosing between a $115 and $105 basket (COGS $75): matching at $115 yields $200 each, but each can grab $210 by undercutting, so the only stable cell is both at $105 earning $150 — jointly worse, yet no one can unilaterally improve by raising price.
