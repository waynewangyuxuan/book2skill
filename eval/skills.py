"""Load promoted skills from the book2skill registry and build the "with-skill"
injection block for the ablation.

For a forecasting eval only the domain-general *reasoning* skills can apply
(epistemic hygiene, causal attribution, analytic method) — the equity-specific
decision skills (moat/valuation/game-theory) have nothing to bite on in a
prediction market, so they are excluded by default via category selection.
"""
from __future__ import annotations

import pathlib
import re

REGISTRY = pathlib.Path(__file__).resolve().parent.parent / "skills" / "_methods"
PLAYBOOKS = pathlib.Path(__file__).resolve().parent.parent / "skills"

# Forecasting-relevant categories (prefix match on the `category:` field).
DEFAULT_CATEGORIES = ("C8", "C7", "C9", "C2")

_FM = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def _field(frontmatter: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", frontmatter, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _section(body: str, name: str) -> str:
    m = re.search(rf"##\s*{re.escape(name)}\s*\n(.*?)(?=\n##\s|\Z)", body, re.DOTALL)
    return m.group(1).strip() if m else ""


def load_all() -> list[dict]:
    skills = []
    for path in sorted(REGISTRY.glob("*.md")):
        if path.name.startswith("_") or path.name == "Methods.md":
            continue
        m = _FM.match(path.read_text())
        if not m:
            continue
        fm, body = m.groups()
        skills.append({
            "name": _field(fm, "name"),
            "kind": _field(fm, "kind"),
            "category": _field(fm, "category"),
            "one_liner": _field(fm, "one_liner"),
            "method": _section(body, "Method"),
        })
    return skills


def select(categories=DEFAULT_CATEGORIES, max_n=None) -> list[dict]:
    chosen = [s for s in load_all() if s["category"].split(" ")[0] in categories]
    return chosen[:max_n] if max_n else chosen


def build_block(skills: list[dict], detail: str = "oneliner") -> str:
    """Render the injection block. `oneliner` = lightweight checklist (default,
    avoids the Phase-B overload failure); `full` = include the Method steps."""
    lines = []
    for i, s in enumerate(skills, 1):
        lines.append(f"{i}. **{s['name']}** — {s['one_liner']}")
        if detail == "full" and s["method"]:
            method = re.sub(r"\n+", " ", s["method"]).strip()
            lines.append(f"   method: {method}")
    return "\n".join(lines)


def load_playbook(slug: str) -> dict:
    """Load a playbook SKILL.md (the assembled skill = the eval unit).
    Returns name, description, body (and raw text)."""
    text = (PLAYBOOKS / slug / "SKILL.md").read_text()
    m = _FM.match(text)
    fm, body = m.groups() if m else ("", text)
    return {
        "name": _field(fm, "name"),
        "description": _field(fm, "description"),
        "body": body.strip(),
        "text": text,
    }


if __name__ == "__main__":
    sk = select()
    print(f"registry total: {len(load_all())}  |  selected (forecasting): {len(sk)}")
    from collections import Counter
    for cat, c in Counter(s["category"] for s in sk).most_common():
        print(f"  {c:2d}  {cat}")
    print("\n--- sample block (oneliner) ---")
    print(build_block(sk[:5]))
