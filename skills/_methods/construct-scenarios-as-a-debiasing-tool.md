---
name: construct-scenarios-as-a-debiasing-tool
kind: reasoning
category: forecasting-and-probability
one_liner: Build explicit upside/base/downside cases specifically to surface your own confirmation bias, vary only the two-to-four highest-leverage drivers, bound the tails to history-anchored plausibility, sanity-check against structural trade-offs, and refine the spread rather than a false-precise central point.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Producing a forecast or valuation where a single point estimate would silently encode your prior.

## Method
1. Mandate explicit upside, base, and downside cases as a debiasing device — a single point forecast hides your confirmation bias.
2. Build the scenarios by moving only the two-to-four highest-impact drivers; the outcome spread matters more than a precise central point.
3. Bound the tails to a defensible historical range; require justification to break it, and attach explicit probabilities.
4. Sanity-check each scenario against the domain's structural trade-offs — a case where every variable improves at once is almost certainly unrealistic.

## Inputs to Outputs
- Inputs: the base case; the highest-leverage drivers; their historical ranges.
- Outputs: a probability-weighted scenario set with a defensible spread.

## Failure modes / assumptions
- A single point forecast that encodes the prior.
- A scenario where every variable improves at once, ignoring trade-offs.

## Worked example (illustrative, single)
A downside case built by stressing only the two key drivers reveals a far wider loss than the comfortable central forecast implied.
