"""Round-1 ablation: baseline vs with-skill forecasting on resolved Polymarket
markets, scored against real outcomes (Brier + accuracy).

Usage:
  python eval/run.py -n 24 --categories C8 --workers 6
"""
from __future__ import annotations

import argparse
import json
import pathlib
import time
from concurrent.futures import ThreadPoolExecutor

from forecast import forecast
from skills import select, build_block

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"


def brier(prob_yes: float, resolved_yes: bool) -> float:
    return (prob_yes - (1.0 if resolved_yes else 0.0)) ** 2


def _one(args):
    market, block, chat_kw = args
    return forecast(market, skill_block=block, **chat_kw)


def run(markets, block, workers, max_tokens):
    chat_kw = {"max_tokens": max_tokens}
    tasks = []  # (market_index, condition, payload)
    for i, m in enumerate(markets):
        tasks.append((i, "baseline", (m, None, chat_kw)))
        tasks.append((i, "skill", (m, block, chat_kw)))

    out = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for (i, cond, _), res in zip(tasks, pool.map(_one, [t[2] for t in tasks])):
            out.setdefault(i, {})[cond] = res
    return out


def score(markets, results):
    rows, errors = [], 0
    for i, m in enumerate(markets):
        b = results[i]["baseline"]["parsed"]
        s = results[i]["skill"]["parsed"]
        if not b or not s:
            errors += 1
            continue
        rows.append({
            "q": m["question"],
            "resolved_yes": m["resolved_yes"],
            "base_p": b["prob_yes"], "skill_p": s["prob_yes"],
            "base_brier": brier(b["prob_yes"], m["resolved_yes"]),
            "skill_brier": brier(s["prob_yes"], m["resolved_yes"]),
        })
    n = len(rows)
    agg = {"n_scored": n, "n_errors": errors}
    if n:
        agg.update({
            "base_brier": sum(r["base_brier"] for r in rows) / n,
            "skill_brier": sum(r["skill_brier"] for r in rows) / n,
            "base_acc": sum((r["base_p"] > 0.5) == r["resolved_yes"] for r in rows) / n,
            "skill_acc": sum((r["skill_p"] > 0.5) == r["resolved_yes"] for r in rows) / n,
            "helped": sum(r["skill_brier"] < r["base_brier"] - 1e-9 for r in rows),
            "hurt": sum(r["skill_brier"] > r["base_brier"] + 1e-9 for r in rows),
        })
    return agg, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=24)
    ap.add_argument("--categories", default="C8", help="comma-separated, e.g. C8,C7")
    ap.add_argument("--detail", default="oneliner", choices=["oneliner", "full"])
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--max-tokens", type=int, default=4000)
    args = ap.parse_args()

    markets = json.loads((ROOT / "data" / "markets.json").read_text())[: args.n]
    cats = tuple(c.strip() for c in args.categories.split(","))
    skills = select(categories=cats)
    block = build_block(skills, detail=args.detail)
    print(f"markets={len(markets)}  skills={len(skills)} (cats={cats}, {args.detail})  workers={args.workers}")

    t0 = time.time()
    results = run(markets, block, args.workers, args.max_tokens)
    agg, rows = score(markets, results)
    agg["elapsed_s"] = round(time.time() - t0, 1)

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "round1.json").write_text(json.dumps({"agg": agg, "rows": rows}, indent=2))

    print("\n=== ABLATION (lower Brier = better) ===")
    print(json.dumps(agg, indent=2))
    if rows:
        movers = sorted(rows, key=lambda r: r["skill_brier"] - r["base_brier"])
        print("\nbiggest skill WINS:")
        for r in movers[:3]:
            print(f"  Δ{r['skill_brier']-r['base_brier']:+.3f}  base={r['base_p']:.2f} skill={r['skill_p']:.2f} "
                  f"[{'Y' if r['resolved_yes'] else 'N'}] {r['q'][:70]}")
        print("biggest skill LOSSES:")
        for r in movers[-3:]:
            print(f"  Δ{r['skill_brier']-r['base_brier']:+.3f}  base={r['base_p']:.2f} skill={r['skill_p']:.2f} "
                  f"[{'Y' if r['resolved_yes'] else 'N'}] {r['q'][:70]}")


if __name__ == "__main__":
    main()
