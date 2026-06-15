---
name: choose-push-vs-pull-intake-by-signal-vs-completeness
kind: decision
category: research-process-and-sourcing
one_liner: Match each information stream's architecture to your state — pull cuts noise but needs expertise and may miss things; push guarantees completeness but invites overload — and decide per stream what to collect, where it sources, and how it is stored for retrieval.
source_book: Best Practices for Equity Research Analysts
source_run: best-practices-equity-research-v1
extraction_contract: v1
perspective_origin: [historian, teacher]
source_anchors: [ch01¶16]
promoted: 2026-06-14
status: promoted
---

## When to use
Designing the information-gathering system that feeds your analysis.

## Method
1. Before building, decide for each stream: what to collect, where it sources from, and how it is stored for later retrieval.
2. Choose push (complete but noisy) vs pull (high-signal but may miss things) per stream, calibrated to your expertise and volume — pull demands enough domain knowledge to know what to ask for.
3. Tag captured items at capture time with a small controlled vocabulary so you can later pull everything on a cross-cutting theme.
4. Score each incoming item by impact-to-decision × proven source reliability and spend attention on the product; let low-low items go unread.

## Inputs → Outputs
- Inputs: candidate streams; your expertise and volume tolerance.
- Outputs: a per-stream push/pull design with a tagging and triage scheme.

## Failure modes / assumptions
- Defaulting all streams to push and drowning in noise.
- Using pull where you lack the expertise to know what to request.

## Worked example (illustrative, single)
A high-volume commodity feed is set to pull-on-demand while a rare expert source is set to push, each tagged at capture for later theme retrieval.
