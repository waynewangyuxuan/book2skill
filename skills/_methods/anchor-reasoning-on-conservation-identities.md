---
name: Anchor reasoning on conservation identities
kind: reasoning
category: macro-systems
one_liner: Build conclusions on relationships that are true by definition (sums-to-zero, balance, total=parts) so they inherit deductive certainty, and label each step as identity-deduction (certain) vs behavioral-assumption (uncertain).
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, teacher, trader, historian, skeptic]
source_anchors: [ch01¶36, ch01¶37, ch01¶39, ch01¶41, ch09¶3, ch09¶7, ch05¶16]
promoted: 2026-06-14
status: promoted
---

# Anchor reasoning on conservation identities

## When to use
When a domain has a small set of accounting/conservation identities that must hold by construction, and you want conclusions that cannot be disputed empirically — or you want to backstop a forecast against constraints it cannot violate.

## Method
1. Enumerate the relationships that are true by definition (sum to zero, balance, total = parts).
2. Use them as hard filters: reject any proposed story that would require violating one.
3. Propagate only logically-necessary steps from the identities; mark each conclusion as identity-deduction (certain) vs behavioral-assumption (uncertain).
4. Present identity-deductions as deductively valid, outranking conflicting single-variable regression evidence.

## Inputs -> Outputs
Inputs: candidate identities; a hypothesis or forecast. Outputs: filtered hypothesis set, each conclusion stamped with a certainty label.

## Failure modes / assumptions
- Misidentifying an approximate relationship as an exact identity.
- Over-claiming certainty when a hidden behavioral assumption was smuggled into the derivation.

## Worked example
A claimed outcome is faded because it requires a closed-system balance to fail to sum to zero; the identity-deduction outranks the regression that supported the claim.
