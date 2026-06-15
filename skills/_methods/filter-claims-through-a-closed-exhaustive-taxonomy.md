---
name: filter-claims-through-a-closed-exhaustive-taxonomy
kind: reasoning
category: epistemic-hygiene
one_liner: Reduce a sprawling list of claimed somethings to a small MECE set of buckets and use it as a falsification filter — anything fitting no bucket is suspect.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [teacher]
source_anchors: [ch01¶62, ch02¶35]
promoted: 2026-06-13
status: promoted
---

## When to use
When a field is cluttered with many supposed instances of a category (advantages, causes, risks) and you need to separate real ones from pseudo ones.

## Method
1. Derive the small closed set of structurally distinct types the category can take (aim for mutually exclusive, collectively exhaustive).
2. Add an explicit residual bucket for rare special cases.
3. For each claimed instance, force it into exactly one bucket.
4. Flag anything that fits no bucket as a likely pseudo-instance to be re-examined or discarded.

## Inputs → Outputs
- Input: a long list of claimed instances of a category.
- Output: each instance classified or flagged; the flagged ones exposed as suspect.

## Failure modes / assumptions
- Failure: a taxonomy that is not actually exhaustive, so real instances get wrongly flagged.
- Assumption: the category genuinely reduces to a few structural types; validate the taxonomy before trusting the filter.
