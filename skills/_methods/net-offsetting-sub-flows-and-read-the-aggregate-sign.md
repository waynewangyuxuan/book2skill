---
name: Net offsetting sub-flows and read the aggregate sign
kind: reasoning
category: macro-systems
one_liner: Decompose a headline flow into sub-flows that cancel, then read the sign of the net aggregate rather than any single gross sub-account; and when one cause acts through several same-direction channels, add them.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch02¶21, ch03¶5, ch07¶12]
promoted: 2026-06-14
status: promoted
---

# Net offsetting sub-flows and read the aggregate sign

## When to use
When a headline number is cited as evidence but it bundles gross sub-flows that partly or fully cancel, or when one cause is credited through only its most obvious channel.

## Method
1. Decompose the headline flow into its gross sub-accounts.
2. Net the ones that offset each other.
3. Read the sign and size of the net aggregate, not the largest gross sub-account.
4. Conversely, when a single cause pushes the same direction through multiple channels, sum them rather than counting only the obvious one.

## Inputs -> Outputs
Inputs: a headline flow; its sub-account breakdown. Outputs: the net aggregate (sign + size), with offsetting and reinforcing channels labeled.

## Failure modes / assumptions
- Mislabeling a reinforcing channel as offsetting (or vice versa) flips the conclusion.
- Sub-account data may be incomplete.

## Worked example
A large gross inflow is shown to be nearly cancelled by a matching outflow, so the net effect on the balance is small and the alarm misplaced.
