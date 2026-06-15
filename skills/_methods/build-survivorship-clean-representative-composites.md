---
name: build-survivorship-clean-representative-composites
kind: reasoning
category: epistemic-hygiene
one_liner: Apply survivorship and representativeness corrections uniformly when building any historical series or composite — include the members that exited, choose weighting so one giant cannot dominate, and reconstruct baselines from the full population including the failed.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, quant, skeptic, teacher, trader]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Constructing a historical series, index, peer composite, or base rate where dropped-out members would otherwise vanish from view.

## Method
1. Identify the full population of members across the period, including those that exited, failed, or were excluded for convenience.
2. Include the exited members in the series rather than the survivors only.
3. Choose a weighting scheme that prevents one giant member from dominating the composite.
4. Reconstruct any historical baseline or expectation from the full population, using the forward expectations that prevailed at each point rather than realized actuals on survivors.
5. Apply these corrections uniformly, not only where it is conventional to mention them.

## Inputs → Outputs
- Inputs: the member roster including exits; period; weighting options.
- Outputs: a survivorship-clean, representative composite or base rate.

## Failure modes / assumptions
- Building a series only from members that still exist, fabricating a phantom advantage.
- Letting one dominant member drive the composite.

## Worked example (illustrative, single)
A peer composite that quietly drops delisted failures looks far healthier than the survivorship-clean version that retains them.
