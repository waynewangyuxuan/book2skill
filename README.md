# book2skill

**Distill reusable analysis skills from books — and an honest way to check they're useful.**

A good analysis book isn't a bag of tricks; it's a *playbook* — a procedure for thinking about a problem.

**Terminology (used consistently throughout):**
- **skill** = a **playbook**: a gated, ordered analytical procedure (spine + steps + branches) — a complete capability, shipped as a loadable `SKILL.md`. **This is the deliverable unit.**
- **method** = an atomic building block ("detect a moat from two converging signals", "anchor a forecast on an outside-view base rate"). Methods are the *vocabulary a skill composes* — a retrieval library, **not skills on their own**, and not meant to be dumped into a prompt.

So a book → a **method library** + one or more **skills (playbooks)** built from those methods. The pipeline that produces them (the "distiller") is itself a set of loadable agent-skills, and a **falsifiable** eval rig judges whether a skill actually helps.

## Layout
| Dir | What |
|---|---|
| `skills/` | **The skills** — each a playbook as a loadable `SKILL.md` (`research-and-pick-a-stock/`, `diagnose-and-manage-a-competitive-position-through-barriers-to-entry/`, `diagnose-a-trade-imbalance-and-forecast-its-unwinding/`, `forecast-a-binary-event/`). `skills/_methods/` is the **method library** they compose — building blocks, *not skills* — with `TAXONOMY.md`. |
| `distiller/` | **The skill that distills skills.** The book2skill harness as loadable `SKILL.md`s (`book2skill` orchestrator → ingest → read-perspective → abstract-to-method → synthesize-taxonomy → trace-playbook → promote) + `contracts/` (data schemas) + `roster.md` (reader perspectives). |
| `eval/` | **The eval methodology.** An outcome-grounded ablation rig (resolved prediction-market questions, scored against real outcomes) + an evaluator skill. See `eval/README.md`. |
| `docs/` | **Design & thinking** — see [`docs/DESIGN.md`](docs/DESIGN.md). |

(`runs/` — raw extraction runs — is gitignored: it contains copyrighted book text and is internal provenance. The published artifacts are the *derived, abstracted* methods and playbooks.)

## How it works (the pipeline)
One book in → one immutable **run** + its **playbook(s)** + its **atomic methods**:
1. **ingest** the book into anchored, per-chapter text.
2. **open-code** it through several reader *perspectives* in parallel (trader, quant, historian, skeptic, teacher) — each harvests atoms its own way (grounded-theory open coding).
3. **abstract** codes → atomic method cards, with a **RAG firewall**: if a method can't be stated without the book's specific example, it's dropped (it's knowledge, not a transferable method).
4. **trace the playbook** — the book's latent decision procedure, wired to the atoms. This is the high-value product.
5. **promote** atoms → the registry (cross-book deduped), playbook → a loadable skill.

The three layers — **recipe** (`distiller/`) → **run** (`runs/`) → **output** (`skills/`) — mirror training code → a training run → model weights.

## Results so far
- **3 books distilled** (a competitive-strategy text, an equity-research handbook, a macro/trade-imbalance text) → **4 skills** (playbooks), built on a shared **250-method library** under one 12-category taxonomy. *The headline count is skills (4); the 250 methods are the substrate, not 250 skills.* (3 skills traced from books + 1 forecasting skill composed from the methods.)
- **Eval (v1):** the rig works and is honest. On out-of-domain binary forecasting it found that injecting reasoning methods — whether as a flat checklist or as a playbook — *did not help* a capable base model (it added a skepticism bias); the mechanism is documented. The point: an eval that can falsify "skill helps" is the one worth trusting. The in-domain test (where the base model genuinely lacks the method) is the next build.

## Use
**Run the distiller** (in an agent with these skills loaded): invoke the `book2skill` skill on a book file.
**Use a distilled skill**: load a playbook `SKILL.md` (e.g. `skills/research-and-pick-a-stock/SKILL.md`) — it's a self-contained procedure that cites the methods it applies.
**Run the eval**:
```bash
python -m venv .venv && ./.venv/bin/pip install requests pysocks
cp .env.example .env   # set BOOK2SKILL_LLM_BASE_URL / _MODEL (any OpenAI-compatible endpoint)
./.venv/bin/python eval/data.py -n 40
./.venv/bin/python eval/ablate.py -n 24
```

## Status & limits
Research prototype. 3 of a planned ~7 books distilled. Cross-book dedup is deliberately conservative (near-duplicates can coexist in a retrieval library). The eval's positive case (skills helping where the base model is weak, in-domain) is not yet demonstrated — that's the honest open frontier.

## License
MIT — see [LICENSE](LICENSE).
