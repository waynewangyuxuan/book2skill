---
name: Zero out a residual term for an exact proxy
kind: reasoning
category: analytic-method
one_liner: Adopt a simplifying assumption that nullifies one term of an identity so a hard-to-measure target equals a directly observable quantity exactly, giving a faster high-frequency read.
source_book: The Great Rebalancing
source_run: great-rebalancing-v1
extraction_contract: v1
perspective_origin: [quant, trader]
source_anchors: [ch02¶20, ch02¶21]
promoted: 2026-06-14
status: promoted
---

# Zero out a residual term for an exact proxy

## When to use
When a target quantity is hard or slow to measure but sits in an identity with an observable quantity plus a term you can argue is negligible.

## Method
1. Write the identity linking the unobservable target to the observable plus a residual term.
2. Justify setting the residual to ~zero (e.g. other private flows net out, or are small/estimable).
3. Read the observable as a same-period proxy for the target.
4. Correct for contamination: when the residual is in fact non-trivial (e.g. anticipatory positioning), net it out before trusting the proxy.

## Inputs -> Outputs
Inputs: the identity; the observable series; an estimate of the residual. Outputs: a real-time proxy for the target, residual-adjusted.

## Failure modes / assumptions
- Large uncounted residual flows break the clean mirror.
- The observable may settle through a hidden venue; find where the quantity actually accumulates.

## Worked example
An authority that absorbs unlimited quantity at a fixed price has reserve changes that mirror the underlying flow imbalance once speculative inflows are netted out.
