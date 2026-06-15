---
name: estimate-a-mixed-population-from-pure-play-samples
kind: reasoning
category: analytic-method
one_liner: When the true signal is local/granular but the data is aggregated and dilutes it, read the most narrowly-focused "pure play" actors as a clean proxy for the segment's economics.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [historian]
source_anchors: [ch04¶16]
promoted: 2026-06-13
status: promoted
---

## When to use
The phenomenon you want to measure is fine-grained (local, per-segment), but available data is aggregated across many activities and dilutes the signal.

## Method
1. Recognize the dilution: combined/conglomerate reporting averages away where value is actually created.
2. Find the most narrowly-focused single-purpose actors ("pure plays") operating only in the segment of interest.
3. Use their unmixed results as a proxy estimate for the segment's true economics.
4. Triangulate across several pure-play comparables to reduce idiosyncratic noise.

## Inputs → Outputs
- In: an aggregated dataset + a target sub-population + a set of focused comparables.
- Out: a de-diluted estimate of the sub-population's economics.

## Failure modes / assumptions
- Pure plays may be unrepresentative (smaller, differently financed); adjust for their idiosyncrasies.
- Few or no pure plays may exist for some segments.
- Accounting quirks (e.g. intangible-heavy balance sheets) can still distort even a focused comparable.
