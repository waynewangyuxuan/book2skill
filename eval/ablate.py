"""Three-arm ablation on resolved Polymarket markets, scored against real outcomes:
  baseline   — no injection
  blanket    — flat checklist of the 44 forecasting-relevant atoms (round-1 style; hurt)
  playbook   — the assembled `forecast-a-binary-event` procedure (structured, scoped)

Tests the core thesis: assembling atoms into a playbook beats blanket-injecting them.

Usage: python eval/ablate.py -n 24 --workers 6
"""
from __future__ import annotations

import argparse
import json
import pathlib
import time
from concurrent.futures import ThreadPoolExecutor

from forecast import forecast
from skills import select, build_block, load_playbook

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

PROC_PREAMBLE = "\n\nFollow this forecasting procedure step by step, then give the JSON:\n"


def brier(p: float, y: bool) -> float:
    return (p - (1.0 if y else 0.0)) ** 2


def arms():
    pb = load_playbook("forecast-a-binary-event")
    blanket = build_block(select())  # 44 atoms, one-liner checklist
    return {
        "baseline": {"skill_block": None},
        "blanket":  {"skill_block": blanket},
        "playbook": {"skill_block": pb["body"], "preamble": PROC_PREAMBLE},
    }


def _call(args):
    market, kw = args
    return forecast(market, **kw)


def run(markets, arm_kw, workers, max_tokens, model):
    tasks, index = [], []
    for i, m in enumerate(markets):
        for arm, kw in arm_kw.items():
            tasks.append((m, {**kw, "max_tokens": max_tokens, "model": model}))
            index.append((i, arm))
    out = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for (i, arm), res in zip(index, pool.map(_call, tasks)):
            out.setdefault(i, {})[arm] = res
    return out


def score(markets, results, arm_names):
    rows, errors = [], 0
    for i, m in enumerate(markets):
        got = {a: results[i].get(a, {}).get("parsed") for a in arm_names}
        if any(got[a] is None for a in arm_names):
            errors += 1
            continue
        row = {"q": m["question"], "y": m["resolved_yes"]}
        for a in arm_names:
            row[f"{a}_p"] = got[a]["prob_yes"]
            row[f"{a}_brier"] = brier(got[a]["prob_yes"], m["resolved_yes"])
        rows.append(row)
    agg = {"n_scored": len(rows), "n_errors": errors}
    for a in arm_names:
        if rows:
            agg[a] = {
                "brier": round(sum(r[f"{a}_brier"] for r in rows) / len(rows), 4),
                "acc": round(sum((r[f"{a}_p"] > 0.5) == r["y"] for r in rows) / len(rows), 3),
            }
    return agg, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=24)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--max-tokens", type=int, default=4000)
    ap.add_argument("--model", default=None, help="model id; defaults to BOOK2SKILL_LLM_MODEL env")
    args = ap.parse_args()

    markets = json.loads((ROOT / "data" / "markets.json").read_text())[: args.n]
    arm_kw = arms()
    print(f"model={args.model}  markets={len(markets)}  arms={list(arm_kw)}  workers={args.workers}")

    t0 = time.time()
    results = run(markets, arm_kw, args.workers, args.max_tokens, args.model)
    agg, rows = score(markets, results, list(arm_kw))
    agg["elapsed_s"] = round(time.time() - t0, 1)
    agg["model"] = args.model

    RESULTS.mkdir(exist_ok=True)
    tag = args.model.split("/")[-1]
    (RESULTS / f"ablate3-{tag}.json").write_text(json.dumps({"agg": agg, "rows": rows}, indent=2))

    print("\n=== 3-ARM ABLATION (lower Brier = better) ===")
    for a in arm_kw:
        if a in agg:
            print(f"  {a:9s}  Brier {agg[a]['brier']:.4f}   acc {agg[a]['acc']:.3f}")
    print(f"  (n={agg['n_scored']}, errors={agg['n_errors']}, {agg['elapsed_s']}s)")
    if rows and "baseline" in agg and "playbook" in agg:
        db = agg["playbook"]["brier"] - agg["baseline"]["brier"]
        dk = agg["playbook"]["brier"] - agg["blanket"]["brier"]
        print(f"\n  playbook vs baseline: Δbrier {db:+.4f}  ({'better' if db<0 else 'worse'})")
        print(f"  playbook vs blanket : Δbrier {dk:+.4f}  ({'better' if dk<0 else 'worse'})")


if __name__ == "__main__":
    main()
