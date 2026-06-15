# book2skill — design notes

The thinking behind the pipeline, in the order it was figured out.

## 1. Two questions
Distilling skills from books is really two problems: **what do you extract?** and **how do you know it's useful?** They turn out to be linked — the eval criterion defines what's worth extracting.

## 2. A "skill" is two different things
We kept conflating them:
- **Atomic method** — "how to do X" (a transferable procedure / heuristic), short and many. This is *vocabulary*.
- **Skill / playbook** — a *capability*: an assembly of atomic methods into a gated procedure that does a whole task.

The field's evidence backs this split: flat libraries of many small skills, *blanket-injected*, degrade performance (retrieval breaks down, attention dilutes). The fix isn't "fewer, bigger skills" — it's **hierarchy + retrieval + composition**. So:

```
atomic methods  →  playbook (assembly)  →  agent (selects / composes)
   vocabulary          the skill              planning
```

The atomic library is short-and-many *on purpose* — it's a retrieval corpus, not a prompt dump. The playbook is the loadable, eval-able unit.

## 3. The book already contains the assembly
The first mistake was extracting only atoms and discarding the **orchestration logic** — but a book's value is largely *that*: the decision procedure it teaches (its spine, its gates, what depends on what). The table of contents is surface order; the *playbook* is the latent procedure. We extract the latter, as a first-class artifact (`Contracts/playbook.md`), and it doubles as the eval unit.

## 4. Methods, not RAG — the firewall
A distilled method must be statable without the book's specific example. If "you can't explain it without naming the company," it's *knowledge* (belongs in a knowledge base), not a *skill*. The abstraction step enforces this firewall; it's what keeps the library lightweight and transferable.

## 5. Diversity without mirroring the book
Reading a book chapter-by-chapter and "extracting skills" just reproduces the table of contents. To get genuinely diverse, non-TOC atoms we read through several **reader perspectives** (trader, quant, historian, skeptic, teacher) in parallel — grounded-theory *open coding*. Different lenses surface different methods from the same text. (This is also a knob: the perspective roster is itself a versionable, learnable artifact.)

## 6. Eval with teeth
- **Outcome-grounded, not judge-of-quality.** Score against a real, known outcome — never an LLM's opinion of "quality" (that rewards verbosity and, as we saw elsewhere, can make a "sharpened" skill *worse* on real tasks).
- **Falsifiable.** The eval's value is that it can say *no*. Our v1 found that injecting reasoning methods didn't help a strong base model on binary forecasting — and pinned the mechanism (a skepticism bias that helps on "no" outcomes and hurts the surprising "yes" ones). A flat checklist and an assembled playbook both lost; the more structure injected, the stronger the bias.
- **Skills help where the base model is weak.** On a task the base model already does well, a method-injection is at best redundant, at worst a bias. The real test is in-domain tasks where the model genuinely lacks the method.
- **The evaluator is itself a skill** (`eval/evaluator/`) — a prompt that grades against ground truth and is explicitly forbidden from rewarding length.

## 7. Governance at scale
Distilling many books creates two problems the per-book pipeline can't see: **cross-book duplication** and **fragmented taxonomies** (each book's run inventing its own categories). The fix is a **MapReduce reconciliation**: map every method to a coarse unified bucket (so duplicates co-locate even across books), reduce within each bucket (conservative dedup + one taxonomy), then fix references. Runs are immutable; the registry is the curated layer, re-derivable from them.

## Provenance / the three legs
- **recipe** = `distiller/` (the loadable skills that extract) + `distiller/contracts/` (the data schemas). Versioned by `extraction_contract`.
- **run** = `runs/<date>-<book>-<ver>/` — immutable; the raw codes, methods, and book text for one extraction.
- **output** = `skills/_methods/` (atoms) + `skills/` (playbooks).

Like training code → a training run → model weights. Every promoted method carries provenance back to the run and book it came from.
