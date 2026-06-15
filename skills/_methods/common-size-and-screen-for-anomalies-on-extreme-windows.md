---
name: common-size-and-screen-for-anomalies-on-extreme-windows
kind: reasoning
category: analytic-method
one_liner: Re-express every line as a percent of a common base, plot the multi-period series, and concentrate anomaly-hunting on the periods of most extreme outcome — causal drivers and discontinuities reveal themselves at the tails, not in typical periods.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Examining a set of statements or time series to surface anomalies, drivers, and discontinuities.

## Method
1. Normalize each item to a percent of a common base so levels become comparable.
2. Build a multi-period series and graph it so anomalies and discontinuities jump out visually.
3. Concentrate anomaly-hunting on the episodes of most extreme over- and under-performance — drivers reveal themselves at the tails.
4. Investigate each flagged deviation back to its cause, grading findings by source durability.

## Inputs → Outputs
- Inputs: statement lines or series; a common base; a long history.
- Outputs: a common-sized, graphed series with flagged anomalies and their causes.

## Failure modes / assumptions
- Studying average periods, where drivers are muddy, instead of the extremes.
- Comparing un-normalized levels across different-sized entities.

## Worked example (illustrative, single)
Common-sizing reveals one cost line spiking only in the worst two periods, pinpointing the driver that average years hid.
