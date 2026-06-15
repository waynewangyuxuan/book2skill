---
name: Define a quantity as an arithmetic residual
kind: reasoning
category: macro-systems
one_liner: Express a behavioral-looking variable as the leftover of two larger measured flows so it cannot be moved in isolation, then bound its move via the components' marginal propensities.
source_book: [The Great Rebalancing]
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch01¶8, ch02¶5, ch05¶9]
promoted: 2026-06-14
status: promoted
---

# Define a quantity as an arithmetic residual

## When to use
When a variable is commonly treated as a free behavioral input (a "choice" or "preference") but is in fact pinned by an accounting definition.

## Method
1. Write the variable explicitly as `residual = aggregate_A - aggregate_B`, where A and B are larger, separately measured flows.
2. Conclude the residual cannot be changed in isolation — any move requires moving A or B.
3. Use the components' marginal propensities to sign and bound the residual: if a shock changes A, the induced change in B is smaller by the relevant marginal fraction, so the residual absorbs the difference.

## Inputs -> Outputs
Inputs: a target variable; the two aggregates that define it; component marginal propensities. Outputs: a forced relationship showing the residual's movement is derivative, with a signed bound.

## Failure modes / assumptions
- Assumes the definition is a true identity, not an approximation.
- Fails if the "aggregates" are themselves endogenous to the residual in a way that breaks the decomposition.

## Worked example
A rate framed as a matter of thrift is rewritten as production minus consumption, showing it cannot be lifted without changing one of those two larger flows.
