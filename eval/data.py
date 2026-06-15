"""Fetch resolved binary Polymarket markets (Gamma API) as the outcome-grounded
eval set. Each kept market has a known Yes/No resolution we can score against.

We deliberately keep only:
  - binary markets whose outcomes are exactly ["Yes", "No"]
  - markets that are closed AND cleanly resolved (outcomePrices is 1/0)
  - recent markets (endDate >= --since) for contamination headroom + relevance
  - optionally, markets matching a topic keyword set (finance / macro / geopolitics)
"""
from __future__ import annotations

import argparse
import json
import pathlib
import requests

GAMMA = "https://gamma-api.polymarket.com/markets"
DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "data"

# Topic bias toward finance / macro / markets; matched case-insensitively against question+description.
TOPIC_KEYWORDS = [
    "fed", "rate", "inflation", "cpi", "gdp", "recession", "economy", "economic",
    "interest", "treasury", "bond", "yield", "unemployment", "jobs",
    "stock", "s&p", "nasdaq", "market", "price", "earnings", "ipo", "merger",
    "bitcoin", "btc", "ethereum", "eth", "crypto", "etf",
    "oil", "gold", "tariff", "trade", "debt", "default", "currency", "dollar",
    "election", "war", "ceasefire", "sanction", "opec",
]


def _is_clean_binary(m: dict) -> bool:
    try:
        outcomes = json.loads(m.get("outcomes") or "[]")
        prices = json.loads(m.get("outcomePrices") or "[]")
    except json.JSONDecodeError:
        return False
    if outcomes != ["Yes", "No"] or len(prices) != 2:
        return False
    # cleanly resolved => prices are (1,0) or (0,1)
    return {prices[0], prices[1]} == {"0", "1"}


def _resolved_yes(m: dict) -> bool:
    prices = json.loads(m["outcomePrices"])
    return prices[0] == "1"  # outcomes[0] == "Yes"


def _matches_topic(m: dict) -> bool:
    blob = f"{m.get('question','')} {m.get('description','')}".lower()
    return any(kw in blob for kw in TOPIC_KEYWORDS)


def fetch(n: int, since: str = "2026-01-01", topic_filter: bool = True,
          page: int = 500, max_pages: int = 20) -> list[dict]:
    """Return up to n kept markets (recent, resolved, binary, topical)."""
    kept, offset = [], 0
    for _ in range(max_pages):
        params = {
            "closed": "true",
            "order": "volumeNum",
            "ascending": "false",
            "limit": page,
            "offset": offset,
            "end_date_min": f"{since}T00:00:00Z",
        }
        resp = requests.get(GAMMA, params=params, timeout=30)
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        for m in batch:
            if not _is_clean_binary(m):
                continue
            if topic_filter and not _matches_topic(m):
                continue
            kept.append({
                "id": m.get("id"),
                "question": m.get("question"),
                "rules": m.get("description"),
                "end_date": m.get("endDate"),
                "volume": m.get("volumeNum"),
                "resolved_yes": _resolved_yes(m),
            })
            if len(kept) >= n:
                return kept
        offset += page
    return kept


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=40)
    ap.add_argument("--since", default="2026-01-01")
    ap.add_argument("--no-topic", action="store_true", help="disable topic keyword filter")
    ap.add_argument("--out", default=str(DATA_DIR / "markets.json"))
    args = ap.parse_args()

    markets = fetch(args.n, since=args.since, topic_filter=not args.no_topic)
    DATA_DIR.mkdir(exist_ok=True)
    pathlib.Path(args.out).write_text(json.dumps(markets, indent=2))

    yes = sum(m["resolved_yes"] for m in markets)
    print(f"kept {len(markets)} markets  ->  {args.out}")
    print(f"resolution balance: {yes} Yes / {len(markets) - yes} No")
    print("samples:")
    for m in markets[:8]:
        print(f"  [{'Y' if m['resolved_yes'] else 'N'}] {m['question'][:90]}")


if __name__ == "__main__":
    main()
