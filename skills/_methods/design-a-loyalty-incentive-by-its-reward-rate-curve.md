---
name: design-a-loyalty-incentive-by-its-reward-rate-curve
kind: decision
category: competitive-advantage
one_liner: Distinguish a real switching-cost lock-in from a disguised discount by the shape of the reward function — accelerating rewards on cumulative volume create loyalty; a flat per-unit reward is just a price cut.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch08¶54]
promoted: 2026-06-13
status: promoted
---

## When to use
When designing or auditing a loyalty/rewards program and you must judge whether it actually suppresses price competition or merely gives margin away.

## Method
1. Write down the reward as a function of purchase volume.
2. **Flat per-unit reward → no loyalty effect.** Mathematically it equals a uniform price discount: the customer is just as free to defect.
3. **Accelerating reward rate (rises with cumulative purchases) → genuine lock-in.** It builds a convex switching penalty: defecting forfeits the high marginal earn rate, so customers concentrate purchases and competitors gain less by undercutting.
4. Tie rewards to *cumulative*, not current, volume, and add expiry/sunset on balances so loyalty must be continuously re-earned.
5. Verdict: only the accelerating-on-cumulative form changes competitive dynamics; everything else is a discount in disguise.

## Inputs → Outputs
- Inputs: the proposed reward schedule (rate vs cumulative volume), expiry rules.
- Outputs: a verdict on whether the program creates lock-in or just erodes margin, plus the design fix (make the curve convex, base it on cumulative volume).

## Failure modes / assumptions
- Customers holding balances across several providers neutralize lock-in; cross-program alliances re-flatten the effective curve.
- Assumes rewards are valuable enough that customers concentrate purchases to chase the accelerating tier.
- A convex curve still fails if the underlying product has no other captivity and rivals copy the program.

## Worked example (illustrative, single)
A rewards scheme that awards the same units per unit purchased is economically a flat discount; one where the earn rate accelerates with cumulative volume (plus sunset expiry) penalizes defection and actually concentrates a customer's spending on one provider.
