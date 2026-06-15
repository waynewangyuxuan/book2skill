"""Forecast a single binary market, with or without the skill toolkit injected.
Contamination-aware: the model sees only the question + resolution rules (never
the outcome). The with/without conditions are identical except for the injected
skill block, so any score delta is attributable to the skills.
"""
from __future__ import annotations

import json
import re

from llm_client import chat

SYSTEM_BASE = (
    "You are a careful probabilistic forecaster. Given a prediction-market "
    "question and its resolution rules, estimate the probability the market "
    "resolves YES. Think briefly, then output ONLY a JSON object on the last "
    'line: {"prob_yes": <float 0..1>, "confidence": <float 0..1>, '
    '"reasoning": "<=50 words"}.'
)

SKILL_PREAMBLE = (
    "\n\nBefore answering, apply this analytical toolkit wherever it is relevant "
    "to reason more reliably:\n"
)

_JSON_RE = re.compile(r"\{[^{}]*\"prob_yes\"[^{}]*\}", re.DOTALL)


def _parse(text: str) -> dict | None:
    m = _JSON_RE.search(text)
    if not m:
        return None
    try:
        obj = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    if "prob_yes" not in obj:
        return None
    p = float(obj["prob_yes"])
    return {
        "prob_yes": min(1.0, max(0.0, p)),
        "confidence": float(obj.get("confidence", 0.0)),
        "reasoning": str(obj.get("reasoning", ""))[:300],
    }


def forecast(market: dict, skill_block: str | None = None,
             preamble: str = SKILL_PREAMBLE, **chat_kw) -> dict:
    system = SYSTEM_BASE + (preamble + skill_block if skill_block else "")
    user = (
        f"Question: {market['question']}\n"
        f"Resolution rules: {market.get('rules') or '(none provided)'}\n\n"
        "Return the JSON."
    )
    text, usage = chat(
        [{"role": "system", "content": system},
         {"role": "user", "content": user}],
        **chat_kw,
    )
    parsed = _parse(text)
    return {"parsed": parsed, "raw": text, "usage": usage}


if __name__ == "__main__":
    import pathlib
    from skills import select, build_block

    markets = json.loads((pathlib.Path(__file__).resolve().parent.parent
                          / "data" / "markets.json").read_text())
    mk = markets[0]
    block = build_block(select(categories=("C8",)))
    print(f"MARKET: {mk['question']}  (resolved_yes={mk['resolved_yes']})\n")
    base = forecast(mk)
    print("BASELINE   ->", base["parsed"])
    skl = forecast(mk, skill_block=block)
    print("WITH-SKILL ->", skl["parsed"])
