# In-domain study: does a distilled skill (playbook) actually improve analysis?

The first **in-domain** test of a book2skill skill, used the way it's meant to be used. We took the `research-and-pick-a-stock` playbook and ran a controlled comparison on 4 contested large-caps: an agent **with** the playbook vs the **same agent without it (baseline)**, same model, same prompt. A real human reference (public Street consensus + notable analyst calls) is the yardstick. Calls produced 2026-06-17.

> These are eval artifacts — method demonstrations on public companies from a knowledge-cutoff model. **Not investment advice.**

## Setup
- **Skill under test:** `skills/research-and-pick-a-stock/SKILL.md` (distilled from *Best Practices for Equity Research Analysts*).
- **Arms:** `baseline` (analyst prompt only) vs `playbook` (read + follow the SKILL.md, may consult the cited methods). Neither arm was shown the Street consensus.
- **Cases:** Intel (INTC), Tesla (TSLA), Boeing (BA), Disney (DIS) — diverse analytical shapes; all heavily covered so a public reference exists.
- **Reference:** `reference.md` (public consensus rating / PT / notable calls).
- **Raw outputs:** `cases/<name>-{baseline,playbook}.md`.

## Results

| Name | Street (ref) | Baseline | Playbook |
|---|---|---|---|
| Intel | ~Hold, turnaround debate | HOLD + "small starter defensible" | HOLD — right-but-priced, no fresh trade |
| Tesla | mixed; $25→$600 dispersion | HOLD, bias down, price triggers | HOLD — right-but-priced, no fresh trade |
| Boeing | **Buy** (+23%) | HOLD, buy <$200 | HOLD — right-but-priced; no long, no short |
| Disney | **Buy** (+27%; JPM +50%) | **BUY** (+27%, matches Street) | HOLD — right-but-priced, no trade |

## What the playbook adds (real value)
On Intel / Tesla / Boeing the playbook is **more disciplined and more honest than the baseline**. It forces the four-part edge predicate (material ∧ in-horizon ∧ **forecastable-by-me** ∧ **not-yet-priced**) + an asymmetry hurdle + a catalyst requirement, and correctly lands on "no clean edge → no trade" where the baseline gives a softer "hold with a small starter."
- **Tesla is the sharpest example:** the playbook isolates that "~$370 of the $404 price is autonomy premium — the bull thesis *is* the quoted price, and the one variable that moves the stock (autonomy timing) is the one no analyst can forecast through diligence." The baseline never says this. That is a genuinely better analytical move.
- It's **not process theater**: similar length, and the gates produce different *decision content* (e.g. "no fresh capital" vs baseline's "small starter defensible"), not just S1–S11 headers.

## The systematic bias (the catch)
The playbook concluded **"right-but-priced → no trade" on all four names. It never says Buy.** Its "not-yet-priced?" clause defaults to "priced" for any well-covered stock, so it **vetoes rather than commits.**

**Disney is a false negative.** There is a real Buy case — stock near a 52-wk low at ~13–15× forward vs a ~23× historical multiple, streaming just inflected (Q2: segment OI +88%, first double-digit margin), an $8B buyback, succession resolved. The **Street (+27%), JP Morgan (+50%), and our own baseline arm all said BUY.** The playbook vetoed it ("my edge is the consensus view; it's priced") — it pattern-matched *well-covered → priced* and **missed a genuine opportunity the discipline-light baseline caught.**

## The deep finding
**A distilled skill inherits its source book's *worldview*, not just its methods.** `research-and-pick-a-stock` came from a **discipline / avoid-mistakes** book, so the skill is an excellent **veto-machine** ("don't pay for priced-in stories") but a poor **opportunity-finder** — precisely that book's blind spot, baked in. This explains the skepticism bias seen earlier in the out-of-domain eval (`../README.md`): *the bias is the book's.*

## Takeaways
1. **Skills do add value in use** — measurable analytical discipline the baseline lacks (the edge/forecastability/pricing/asymmetry gates). This is the first grounded evidence beyond "looks good."
2. **But each skill carries its source's bias.** A single book = a single (biased) lens.
3. **The eval has teeth** — it caught a false negative (DIS); "more disciplined" ≠ "more correct."
4. **Design implication:** balanced analysis needs **worldview composition** — compose skills across *multiple* books (a discipline book + an opportunity/contrarian book), or an explicit counterweight to the "not-yet-priced → priced" default. Next experiment: add an opportunity-oriented book's skill and re-run Disney to see if the false negative flips.

## Caveats
- n=4, one playbook, knowledge-cutoff model; judged qualitatively + against public consensus, **not outcome-scored** (we did not check whether the calls actually made/saved money).
- Baselines were strong (not strawmen) — a capable model already does decent analysis, which makes the playbook's marginal discipline (and its bias) the real signal.
