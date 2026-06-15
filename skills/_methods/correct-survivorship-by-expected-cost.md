---
name: correct-survivorship-by-expected-cost
kind: reasoning
category: epistemic-hygiene
one_liner: Value a class of hit-or-miss bets against expected cost = success cost ÷ success probability, so the invisible failures sit in the denominator — correcting the survivorship bias that fabricates a phantom advantage.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant, historian, teacher]
source_anchors: [ch17¶60]
promoted: 2026-06-13
status: promoted
---

## When to use
Estimating the return on any class of risky, repeatable initiatives where most attempts fail and only the winners are visible afterward — brand launches, drug pipelines, new-product portfolios, exploration, venture bets.

## Method
1. Identify the full population of attempts in the class, including the failed/abandoned ones that have dropped out of view.
2. Estimate the success probability p for a single attempt (base it on the full population, not on survivors, which overstate p).
3. Compute the expected cost of producing one success = investment_in_a_winner ÷ p (equivalently, total category spend per winner).
4. Return = PV(future net income from the winner) ÷ expected cost. Divide by the re-inflated cost, never by the winner's spend alone.
5. Compare to the cost of capital: if the corrected return merely matches the hurdle, the activity is *not* a competitive advantage, however impressive the winners look in isolation. Use this to reject "successful X earn huge returns ⇒ creating X is a moat" claims.

## Inputs → Outputs
- Inputs: success probability, the investment in a successful instance (or total category spend per success), PV of the winner's income stream, cost of capital.
- Outputs: a survivorship-corrected ROI and a verdict on whether the activity confers an advantage or merely returns the cost of capital.

## Failure modes / assumptions
- The success probability is the hard input and is easy to overestimate from survivors; base it on the full population.
- A corrected return above the hurdle can still be a real advantage (e.g. scale lets you spread creation costs) — the correction tests the *claim*, it doesn't deny all advantages.
- Assumes failed attempts' costs are knowable or estimable.

## Worked example (illustrative, single)
If only one in four attempts succeeds, the return is the PV of the winner's net income divided by four times the actual spend on the winner — usually collapsing an apparently stellar return down toward the ordinary cost of capital, exposing the "advantage" as a survivorship illusion.
