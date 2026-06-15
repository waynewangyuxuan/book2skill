# eval — does a distilled skill actually help?

A rough but **rigorous** methodology for the hard half of book2skill: proving (or disproving) that a distilled skill makes an LLM better. It is built to be **falsifiable** — it can say "this skill *hurts*," and explain why — which is the only kind of eval worth trusting.

## Design principles
1. **Outcome-grounded, not judge-of-quality.** Every answer is scored against a *real, known outcome* (resolved Polymarket markets), never against an LLM's opinion of "quality." This avoids the failure mode where an eval rewards longer / more "comprehensive" answers (which we'd separately seen cause real-task regressions).
2. **Contamination-aware.** Markets are recent (resolve *after* the model's knowledge cutoff), so the model can't recall the answer; the ablation also controls for any residual memorization (both arms share it).
3. **Ablation = the unit of truth.** Same model, same questions, the *only* difference is what skill is injected → any score delta is attributable to the skill.
4. **Skill-as-unit, three arms.** `baseline` (nothing) vs `blanket` (flat checklist of all relevant atomic methods) vs `playbook` (the assembled, gated procedure). This tests not just "do skills help" but "does *assembling* atoms into a playbook beat dumping them."
5. **The evaluator is itself a skill** — `evaluator/SKILL.md` — a prompt that extracts each answer's decisive call, scores it against ground truth, and diagnoses *why* a skill helped/hurt. It is explicitly forbidden from rewarding verbosity.

## Components
- `llm_client.py` — LLM client (OpenAI-compatible endpoint; strips reasoning traces).
- `data.py` — fetch resolved binary Polymarket markets (Gamma API) as the outcome set.
- `skills.py` — load the method library (`../skills/_methods/`) and the playbooks (`../skills/`).
- `forecast.py` — forecast one market, with/without an injected skill block.
- `ablate.py` — the 3-arm ablation + Brier/accuracy scoring.
- `evaluator/SKILL.md` — the evaluator skill (ground-truth-anchored grader).
- `run.py` — earlier 2-arm version (kept for reference).

## Run
```bash
python -m venv .venv && ./.venv/bin/pip install requests pysocks
cp .env.example .env            # set BOOK2SKILL_LLM_BASE_URL / _MODEL (any OpenAI-compatible endpoint)
./.venv/bin/python eval/data.py -n 40            # fetch resolved markets
./.venv/bin/python eval/ablate.py -n 24
```
(Endpoint config is read from env by `llm_client.py`. PolyBench is a third-party reference, cloned separately.)

## Findings (v1)
Substrate: 24 recent resolved Polymarket markets (macro / markets / geopolitics). Lower Brier = better.

| run | model | baseline | blanket | playbook |
|---|---|---|---|---|
| 2-arm (15 atoms) | Qwen3.6-35B | 0.245 | 0.269 | — |
| 3-arm (44 atoms) | Qwen3.6-35B | **0.229** | 0.260 | 0.270 |
| 3-arm (44 atoms) | Qwen3.5-4B | **0.360** | 0.436 | 0.460 *(15/24 errored — overload)* |

**Consistent, repeatable result: injecting these reasoning skills did *not* help — on a strong model or a weak one.** Mechanism (identical across runs): the skills add a **base-rate / skepticism bias** that lowers predicted probabilities (mean P 0.199 → 0.170 → 0.154 as injection strengthens). That is free on NO outcomes (already near-perfect) but **hurts every YES** (the events that actually happened). On the weak model, heavy injection additionally broke instruction-following.

## What this does and doesn't show
- ✅ **The methodology works** — it falsified "skill helps," pinned the mechanism, and survived a model-size confound check. An eval that can say *no* has teeth.
- ⚠️ **It does not show our distilled skills are useless.** Two mismatches: (1) Polymarket only exercises the *generic epistemic-hygiene* subset — the least likely to add capability (a decent model already weighs base rates); the skills we actually distilled are *equity/competitive-analysis procedures* (capability-adds) with **no** matching questions here. (2) Binary forecasting is something LLMs are already decent at → little headroom.
- 🔭 **Next (deliverable #2, real version):** an **in-domain** outcome substrate — competitive-analysis / financial-reasoning cases where the base model genuinely lacks the method, so a playbook like `diagnose-and-manage-a-competitive-position-through-barriers-to-entry` can show value. The hard part is unpolluted ground truth (post-cutoff or obscure cases).

> The honest negative is the point: a forced positive would have been worth less than an eval you can trust to tell you when a skill *doesn't* work.
