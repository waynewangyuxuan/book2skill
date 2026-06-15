---
name: evaluate-skill-ablation
description: Score whether applying a distilled skill (a playbook) actually improved an LLM's answer to a case, by comparing a baseline answer and a with-skill answer against the case's KNOWN ground-truth outcome. Outputs an objective per-answer score plus a short diagnosis of why the skill helped or hurt. Used by the book2skill eval harness. It grades against provided ground truth; it does NOT free-judge "quality".
---

# evaluate-skill-ablation (the evaluator skill)

Grade one ablation pair against ground truth. **Anchor every judgment to the provided `ground_truth`. Never reward length, structure, or comprehensiveness** — that is exactly the failure mode (Phase-B regression) this eval exists to catch.

## Input (one case)
- `question` — the case the model answered.
- `ground_truth` — the known correct outcome / answer key.
- `baseline_answer` — the model's answer WITHOUT the skill.
- `skill_answer` — the model's answer WITH the skill (playbook) applied.

## Procedure
1. **Extract the decisive call** from each answer — the prediction/verdict the case actually asks for (a direction, a probability, a yes/no, or the key judgment). Discard prose, hedging, length.
2. **Score each answer against `ground_truth`** with an objective rule, stated up front per case type:
   - forecast/binary → correct? plus, if a probability is given, Brier = (p − outcome)².
   - judgment / answer-key → does it match the key on the *decisive* claim (Y/N)? list which sub-claims are right/wrong.
3. **Delta** = skill_score − baseline_score on the objective score.
4. **Diagnose (≤40 words)** *why*: did the skill change the decisive call, and did that move toward or away from ground truth? Name the mechanism (e.g. "added base-rate skepticism → lowered a true-yes").

## Output (JSON only)
```json
{"baseline_score": <num>, "skill_score": <num>, "delta": <num>, "skill_helped": true|false|null, "why": "<=40 words"}
```

## Guardrails
- Grade ONLY against `ground_truth`. If you can't tell which answer is closer to it, return `"skill_helped": null` — don't guess.
- Give **zero credit** for being longer / more structured / "more thorough." Decisiveness toward the truth is the only currency.
- One case at a time, deterministic (temperature 0).
