# book2skill — roadmap / TODO

Consolidated from the design docs. Priority follows Wayne's call that **eval is the most
important problem** ("我们不好对skill做eval，但是我们需要对skill做eval"). Sources:
[`distiller/pipeline-v2.md`](distiller/pipeline-v2.md) ·
[`eval/eval-system-v1.md`](eval/eval-system-v1.md) ·
[`eval/in-domain-study/FINDINGS.md`](eval/in-domain-study/FINDINGS.md).

Status: ☐ todo · ◐ in progress · ✅ done

---

## ✅ Done (this round)
- ✅ Public repo delivered (4 skills on a 250-method library); deliverable submitted.
- ✅ In-domain study (4 large-caps): playbook adds discipline **but inherits source-book worldview** (Disney false negative).
- ✅ Design specs written: pipeline v2, eval-system v1.

---

## Phase 1 — Eval Engine A + start Engine B's clock  ← **do first** (fastest payoff, serves everything else)
Engine A (backtest, history-driven) is immediately useful, diagnostic, and is what makes the
composition experiment measurable. Engine B's *recording* is cheap to start now.
- ☐ **E-A1 · case bank scaffold** — a frozen historical case set for A (reuse `data.py` fetch). Define the case schema (input scenario + as-of date + resolvable ground truth).
- ☐ **E-A2 · bias-axis metrics (automate)** — on `ablate.py` output: veto-rate, Buy/Hold/Sell distribution, conviction spread, mean predicted prob, consensus-divergence rate, which gates fire. (Systematize what the in-domain study did by hand.)
- ☐ **E-A3 · blind reasoning judge** — harden `evaluator/SKILL.md`: score reasoning quality only, **outcome-blind** (extend "never reward verbosity" → "never reward matching history"). Distinguish reasoned edge vs reflexive skepticism.
- ☐ **E-B1 · start live recording (parallel, cheap)** — scheduled job: fetch recent events/prices → run all arms → store each judgment **immutably with timestamp + as-of snapshot**. No scoring yet; just start the clock.

## Phase 2 — Composition + the Disney experiment (the key validation)
Tests the deepest finding: can composing worldviews cancel single-book bias?
- ☐ **D-1 · distill an opportunity/contrarian book** — use the current pipeline (don't block on v2). Needed as the counterweight skill.
- ☐ **E-C1 · combinator** — compose 2+ `SKILL.md` into one injected context (or a routing meta-agent).
- ☐ **E-C2 · combination metrics** — bias-cancellation (does veto-rate move toward neutral while reasoning quality holds?) + coherence/degradation check (A+B can be worse than A).
- ☐ **T6 · re-run Disney composed** — discipline book + opportunity book; does the false negative flip to Buy? (`pipeline-v2.md` T6)

## Phase 3 — Distiller v2 (quality upgrades; parallelizable with Phase 1–2)
- ☐ **T2 + T3 (do together) · biggest analytical upgrade** — trace-playbook reads anchored codes + method index (not the whole book again), targeted re-read only at gates; **and** one book → multiple playbooks by narrative segment (cut criterion: executable on a case).
- ☐ **T1 + T5 · merge correctness** — at current scale (250 cards ≈ 87k tokens) do global single-agent merge; cross-book dedup on a global view too. (MapReduce kept in reserve for larger scale.)
- ☐ **T4 · persona metrics** — unique emergent-category coverage / marginal novelty / cross-persona overlap. Unlocks the proven-persona library (V2).

## Phase 4 — Forward truth + calibration (slow, ongoing)
- ☐ **E-B2 · forward-score** resolved cases (Brier / hit-rate / PnL) as horizons close.
- ☐ **E-D1 · calibration loop** — does the A-judge's "good process" predict B's forward outcome? Keeps the judge honest (the keystone).
- ☐ **E-E1 · diagnostic-report format** — turn eval output into actionable signal fed back into the distiller (eval as fitness function).

---

## Backlog / visions (gated or directional)
- ☐ **Distill the remaining usable books** (corpus: 10; 2 corrupt; 3 distilled → ~5 left).
- ☐ **V1 · OCR side-branch** for tables/charts in ingest (opt-in, per-book; tables first).
- ☐ **V2 · proven-persona library** + per-book casting by thesis (needs T4).
- ☐ **V3 · worldview composition as a product form** (one book = one biased lens → composable worldview layer).
- ☐ **Benchmark** — freeze Engine-A protocol + accumulate Engine-B outcomes into a standing skill/skill-combo benchmark (the productized form; connects to the lab benchmark ask).

## Not in this repo (tracked elsewhere)
- `skill-battlefield` (separate repo/entity) — the W/I (workflow/intelligence) skill-grammar theory; its own roadmap.

---
*Suggested critical path:* Phase 1 (E-A1→A2→A3, E-B1 in parallel) → Phase 2 (D-1 + E-C1/C2 → T6) → Phase 3 as capacity allows → Phase 4 accrues over time.
