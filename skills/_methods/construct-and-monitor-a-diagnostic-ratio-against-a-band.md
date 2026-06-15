---
name: construct-and-monitor-a-diagnostic-ratio-against-a-band
kind: reasoning
category: analytic-method
one_liner: Build a ratio that pairs two related quantities that should track, read its level against an interpretive band and its trend over time as a quality/early-warning signal, and flag a sustained departure as one of the two being managed.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [quant, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Monitoring an entity for quality deterioration or manipulation using two measures that should move together.

## Method
1. Pair two quantities that reflect one underlying reality and should track each other.
2. Form their ratio and define an interpretive band of normal values.
3. Read the ratio's level against the band and its trend over time as a quality or early-warning signal.
4. Treat a sustained departure of the ratio from its norm as a flag that one of the two is being managed — then test whether a stale numerator or denominator is about to move and close the gap on its own before acting.

## Inputs → Outputs
- Inputs: two should-track quantities; an interpretive band.
- Outputs: a monitored diagnostic ratio with breach/early-warning flags.

## Failure modes / assumptions
- Trading the gap when a stale component is simply about to update.
- Choosing two quantities that need not actually track.

## Worked example (illustrative, single)
Reported earnings and operating cash diverge persistently; the ratio breaches its band, flagging accrual management for investigation.
