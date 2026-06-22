---
created: 2026-06-21
type: design-note
role: eval-system-spec
status: proposed
tags: [book2skill, eval, benchmark, skill-evaluation]
---

# eval-system v1 — a system for evaluating skills (and skill combinations)

Promotes deliverable #2 from one-off studies (`README.md` Polymarket null, `in-domain-study/`)
into a **standing system**. The unit under test is a **skill (= playbook)** and, as a first-class
case, a **composition of skills**.

## The central tension (state it, don't dodge it)
The domains where outcomes are clean and fast (prediction markets) **don't exercise** the capability
our skills add; the domain where the skills add capability (equity research) has outcomes that are
**slow (6–24mo) and noisy** (good process loses, bad process wins on any single case). No single
metric escapes this. The system therefore runs **two engines that calibrate each other.**

## What the in-domain study taught us (the reframe)
The most informative signal was **not** "was this call right" — it was the **systematic veto bias**
(4/4 names → never Buy), visible *with no forward data*. Bias/behavior across many cases is the
fast, primary signal; outcome is the slow gold standard. The system centers the fast signal and
uses outcome to keep it honest.

---

## Engine A — backtest engine (history-driven, fast, diagnostic)
Apply a skill's methodology to historical scenarios in bulk. Two outputs:

1. **Behavioral / bias distribution** (Tier-1): across N cases per arm — veto-rate, Buy/Hold/Sell
   distribution, conviction spread, mean predicted probability, agreement-vs-consensus rate, which
   gates fire. This is how worldview bias is measured (the in-domain finding, systematized).
2. **Blind reasoning-quality judgment** (Tier-2): an LLM judge scores the *reasoning*, not the
   outcome — is the divergence a **reasoned, nameable edge** or **reflexive skepticism**? (Tesla's
   "$370 is autonomy premium" = good; Disney's "well-covered→priced" default veto = bad.)

**The hindsight trap (must mitigate).** Backtesting on scenarios whose outcome the model knows
double-cheats: the model may leak the known outcome, and a judge that knows history rewards
"matched history" over "better process."
- **Judge is outcome-blind.** Extends the in-domain rule "never reward verbosity" to "never reward
  matching history." It scores process only.
- Stricter option: **point-in-time data reconstruction** (feed only what was knowable as-of the
  historical date). Rigorous, expensive — phase 2.
- **Honest label:** Engine A measures **process / reasoning quality + behavioral bias**, NOT outcome
  truth. It is contamination-guarded only by blind judging.

**Diagnostic feedback (the real prize).** Engine A's output is not a leaderboard — it is
**actionable signal fed back into the distiller** (eval as the pipeline's fitness function, GEPA
spirit):
- systematic veto bias → source-book worldview → do **worldview composition**
- reasoning cites a method that doesn't fit → bad `uses` linkage in `trace-playbook`
- method too vague to apply → over-aggressive abstraction in `abstract-to-method` (firewall)
- a scenario class has no usable method → tune `read-perspective` persona / add a second book

## Engine B — live rolling case bank (forward-resolving, slow, incorruptible)
A standing, **actively-updated** bank of *recent* cases (events/prices after the model's knowledge
cutoff → contamination-free by construction).
- A scheduled job: fetch recent names/events/prices → run all arms (baseline / skill / combo) →
  **record each judgment immutably with a timestamp + the as-of data snapshot** (no moving the
  goalposts; mirrors book2skill's immutable-run principle).
- As each case's horizon resolves, score it: Brier / hit-rate / PnL.
- Tradeoff (accepted): forward resolution is **slow**. So start the clock **now** — the value is in
  the accumulating ground truth, not in day-one results.

## The keystone — the two engines calibrate each other
> The live bank is the ruler that checks the backtest judge isn't hallucinating.

Periodically test: **does the process-quality the judge rewards actually predict forward outcome?**
If a skill the judge loves keeps losing forward, either the judge or the skill is wrong. This is what
stops the LLM-judge from being mere opinion and keeps the whole system non-circular. Engine A gives
fast iteration + diagnosis; Engine B gives slow truth + judge calibration. Neither alone is trustworthy.

| | driver | speed | measures | role |
|---|---|---|---|---|
| **A · backtest** | historical scenarios | fast | behavioral bias + blind reasoning quality | fast iteration + diagnose distiller |
| **B · live bank** | recent real events, forward-resolved | slow | outcome truth | gold standard + calibrate the judge |

---

## Evaluating skill *combinations* (first-class)
1. **combinator** — compose 2+ `SKILL.md` into one injected context (or a meta-agent that routes).
2. **bias-cancellation metric** — after adding e.g. an opportunity book's skill, does **veto-rate move
   toward neutral while reasoning-quality / outcome holds**? This is the measurable definition of
   "composition cancels single-book bias" — and exactly the Disney re-run experiment (T6 in
   `../distiller/pipeline-v2.md`).
3. **coherence / degradation check** — does the combo still produce a single coherent call, or do two
   worldviews collide into indecision / broken instruction-following (seen on the weak model under
   heavy injection)? A+B can be worse than A alone — the system must detect that.

## Arms (the ablation, unit of truth)
`baseline` (nothing) · `skill-A` · `skill-B` · `skill-A+B` · `blanket` (flat dump of all atoms).
Same model, same prompt, same cases — any delta is attributable to what was injected.

## What exists vs what to build
- **Have:** `ablate.py` (3-arm), `evaluator/SKILL.md` (blind grader seed), `data.py` (recent-market
  fetch), in-domain study's 8 case artifacts.
- **Build:** (a) the case bank (frozen for A, rolling for B) + immutable judgment records;
  (b) automated bias-axis metrics; (c) the combinator + combination metrics;
  (d) the calibration check (A-judge vs B-outcome); (e) the diagnostic-report format fed to the distiller.

## Suggested sequencing
Engine A first (immediately useful + diagnostic + serves combination eval) → start Engine B's
**recording** in parallel (cheap; just start the clock) → forward-score B over time → wire the
calibration loop once B has resolved cases.

## One-line frame
> An ablation harness over a contamination-controlled case bank, measuring primarily what a skill
> *does to the decision distribution* (bias), with blind reasoning-quality judging and forward
> outcomes as the lagged gold standard — natively supporting skill composition, with
> "does the combo cancel single-book bias" as a first-class metric, and every result fed back as a
> fitness signal into the distiller.
