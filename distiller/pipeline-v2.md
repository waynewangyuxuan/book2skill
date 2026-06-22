---
created: 2026-06-21
type: design-note
role: pipeline-roadmap
skill_set: book2skill-harness
supersedes-target: extraction_contract v1
status: proposed
tags: [book2skill, skill-distillation, harness, v2]
---

# book2skill pipeline v2 — design note

Roadmap for the next `extraction_contract` bump. Grounded in the first in-domain eval
(see `../eval/in-domain-study/FINDINGS.md`) and a design review of the v1 stages.
Three buckets: **TODOs** (do now), **visions** (directional), **principles** (how we think now).

---

## TODOs — actionable now (evidence/scale sufficient)

### T1 · merge → global single-agent (drop bucket-local dedup at this scale)
- **Current:** taxonomy-based / MapReduce bucketed merge.
- **Measured:** whole registry 250 cards ≈ **87k tokens**; one book ≈ **35k tokens** — fits one context.
- **Change:** at this scale, do **global all-vs-all merge in one agent**. Bucketing risks "two duplicates land in different buckets → never compared → missed merge."
- **Keep MapReduce in reserve** for when the library outgrows a context (many books → thousands of methods); it was for parallelism + 529-resilience, not necessity.

### T2 · trace-playbook reads codes, not the whole book again
- **Current:** trace re-reads full `book-text/` (a second whole-book pass).
- **Change:** input = **codes (already anchored, e.g. `ch03¶12`) + method index (name + one line, ~3k tokens)**.
  1. Build spine + locate gate/transition points *on the codes* (codes = the book's compressed map).
  2. **Targeted re-read only the passages that define a gate/transition**, by anchor (retrieval-over-anchors).
  3. Reference atoms by canonical name from the index; don't restate.
- **Why:** big context win; `uses` references stay accurate.

### T3 · one book → multiple playbooks (segment by narrative)
- **Current:** one book → one (dominant-spine) playbook.
- **Change:** trace first **segments the book into separable argument arcs**, then traces one spine per arc.
- **Guard against over-segmentation:** a playbook must be **executable end-to-end on a real case → outcome** (it is the eval unit). Fragments that can't run a case get merged back.
- Composes with T2: each playbook traces only on its own segment's codes → context naturally bounded.

### T4 · make persona value measurable (prereq for the persona library, V2 below)
- **Add metrics per persona per run:** unique emergent-category coverage, marginal novelty, cross-persona overlap.
  (v1 run-log already observed trader↔quant overlap 13/16 → fold; skeptic/historian each own a category → keep — formalize these into computed metrics.)
- Without an automatic score there is no data-driven roster selection.

### T5 · cross-book dedup uses a global view too
- **Current:** promote-to-registry incrementally merges a run onto existing canonicals (per-run, no global view → same "miss" risk as T1).
- **Change:** do cross-book merge against a **global registry view**, not incremental per-run. (T1 and T5 are the two ends of the same fix.)

### T6 · next experiment — add an opportunity book's skill, re-run Disney
- In-domain eval found the playbook is a **veto-machine** (never says Buy; Disney false negative).
- **Test worldview composition:** distill an opportunity/contrarian book, compose, re-run Disney, see if the false negative flips to Buy.

---

## Visions — directional (gated on a prereq or uncertain payoff)

### V1 · OCR side-branch for tables/charts (ingest)
- Figures-as-images are currently lost. Add an **opt-in, per-book** ingest stage.
- **Tables** (numeric) = high value, `FireRed-OCR` recovers them faithfully.
- **Charts** = harder: need multimodal caption (`qwen36-35b-a3b-mm`) to read semantics, and a firewall against fabricated numbers.
- Only worth it for **chart-heavy books** (valuation / technical). Not default-on.

### V2 · proven-persona library + per-book casting
- After enough books, keep a library of personas/prompts with **measured yield** (uses T4's metrics).
- Per book, **pick a subset by thesis/domain** instead of a fixed roster of 5. This is the terminal state of the roster's second-order loop.

### V3 · worldview composition as a product form
- One book = one biased lens. Compose skills across books (a discipline book + an opportunity book) to cancel single-book bias.
- Output form evolves from "one book → one skill" into a **composable worldview layer**.

---

## Principles — how we think now (will shape future design)

1. **"Merge, not dedup."** Same method captured by multiple lenses/books → collapse into one canonical + **union the provenance**, don't delete. Semantics = combine + preserve origin.
2. **Scale dictates architecture.** When methods fit in a context, **global merge beats bucketing** (more accurate). Taxonomy at current scale is **navigation/grouping**, not a required dedup backbone — sharding becomes necessary only when the library outgrows a context. Don't pre-pay complexity for a scale you haven't reached.
3. **A playbook's unit is "a separately executable narrative," not "a book."** A book contains several playbooks; the cut criterion is **executability on a case**, because **playbook = eval unit**.
4. **Anchored codes are the book's compressed map; downstream consumes the map, not the raw text.** Once ingest structures the book into anchored codes, every later stage (especially trace) works on the codes + targeted anchor-retrieval — not by re-stuffing full text into context. (Core context-management principle.)
5. **Persona/prompt is a learnable hyperparameter, not hand-fixed.** The roster should evolve data-driven (measure → select), not by manual v1→v2 guesses.
6. **A distilled skill inherits its source book's worldview, not just its methods.** This reframes the question from "is the skill useful?" to "whose bias does the skill carry?" — the heaviest principle, from the in-domain eval.

---

## Suggested order
T2 + T3 together (context + multi-playbook, biggest analytical upgrade) → T1 + T5 (merge correctness) → T6 (worldview experiment, needs a second book distilled) → T4 (unlocks V2) → V1/V2/V3 as capacity allows.
