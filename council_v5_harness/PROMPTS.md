# Council v5 prompts: medical agent harness (run on the laptop)

Claude's Round 1 is already in `council_v5_harness/claude_round1.md`. Codex and Gemini each write their own Round 1 **without reading Claude's** (or each other's). Then all three write Round 2.

## Setup

```bash
git fetch origin claude/medical-harness-research
git checkout claude/medical-harness-research
git pull
```

Run each agent from the repo root, as in v3/v4:

- **Codex:** gpt-6.1-sol, high effort.
- **Gemini:** gemini-4-argon-high via `agy`.

Use the philosopher-council lenses and isolate each agent from its stored memories.

---

## Round 1 prompt (identical for Codex and Gemini)

Replace `<AGENT>` with `codex` or `gemini`.

```text
You are one of three independent advisors (Claude, Codex, Gemini) on a master's capstone council. Apply the philosopher-council lenses: Descartes proposes from first principles, Hume audits every factual claim, Socrates stress-tests the single decisive assumption.

READ FIRST, in this repo:
- README.md: the student, their constraints, and the history of ideas already rejected or shortlisted
- reports/Medical agent harness.md: the deep-research report this round is based on
- research_notes/Medical agent harness/*.md: the underlying sourced notes (use them to check claims)
- reports/Thai medical LLM landscape.md: background on Thai medical LLMs and the current audit-first plan

DO NOT open anything else in council_v5_harness/ except this prompt. Your Round 1 must be independent of the other advisors.

THE STUDENT'S IDEA, IN THEIR WORDS (paraphrased)
"Most people build models, or build apps on top of models. But the harness also changes how a model performs. Instead of an app, build a harness specific to medical tasks. Claude Code is a big factory that has everything, but it is too big. I want a small infantry section specialised for medicine. Or is this just a mode or a skill? Help me shape it and decide whether it is feasible."

STUDENT AND CONSTRAINTS
- Master's in AI and digital health at Chulalongkorn (Medicine + Engineering committee), about 9 months.
- One laptop: RTX 4090 Laptop (16 GB VRAM), i9-13980HX, 32 GB RAM, about 1 TB. No cluster. API models allowed on synthetic data.
- Wants frontier ML as the core contribution, with real, measurable Thai healthcare impact.
- Already rejected: "safe" admin/claims ideas, VenomSight, dysarthria. Do not re-propose them. Note that coding audit and claims pre-check are close to the rejected admin ideas.
- Key prior art the proposal must survive: MedicalHarness (arXiv 2610.05778), Asclepius (2609.13543), MAI-DxO, MedAgentBench v2, Symbolic Guardrails (2604.15579), Mingbird (2610.02001), Terminal-Bench 2.0.

TASK
Part A: in at most 150 words, answer the student directly. Is a medical harness a real research object, or "just a mode or skill"? Is their factory-vs-infantry analogy right?

Part B: propose exactly 5 capstone framings, ranked. The report's 5 framings are one input, not a menu: at most 2 of yours may be close variants of them, and if you reuse one you must materially sharpen it. For each give:
1. **Name and pitch:** 1–2 sentences.
2. **Paradigm and research question:** a falsifiable RQ, the harness components ablated, and the exact comparison or metric.
3. **Thai testbed and impact:** who benefits and how it is measured; mark unverified claims.
4. **Laptop experiment:** models with parameter counts, tasks and data, design size (models × arms × tasks × epochs), laptop-hours or GPU-hours, API cost if any, statistics.
5. **Socratic stress-test:** the single decisive assumption, plus a concrete month-1 test with a numeric kill or pivot threshold.

End with "If I were the student I'd pick #N" and one line saying why.

Cite sources (URL or arXiv ID) for factual claims; mark anything unverified as [UNVERIFIED]. Be concrete and honest. Disagree with the report where you think it is wrong.

Write your answer to council_v5_harness/<AGENT>_round1.md
```

---

## Round 2 prompt (after all three Round 1 files exist)

Replace `<AGENT>` with `codex` or `gemini`. Claude writes `council_v5_harness/claude_round2.md` in the cloud session.

```text
Council v5 (medical agent harness), Round 2. Read council_v5_harness/claude_round1.md, codex_round1.md and gemini_round1.md (plus the report and notes as needed). Do not read any *_round2.md file.

Write five sections:
1. **Hume audit:** the 5 most load-bearing factual or feasibility claims made by the OTHER two advisors that are wrong, unverified or overstated. Say why, and what would verify each.
2. **Convergence verdict:** where the three advisors converged, is that convergence a real signal or just the obvious attractor of the constraints? Name the best variant within each cluster and the design choice that makes it publishable against MedicalHarness and Symbolic Guardrails.
3. **Socrates:** the single most over-rated idea from another advisor, and the assumption it breaks on.
4. **Most under-rated:** the single most under-rated idea from another advisor, and how you would merge or improve it.
5. **Final top 3:** a table with columns # | Project | Finish confidence (%) | Laptop/GPU-hours | Frontier-ness | Thai impact | Why. Merges across advisors are encouraged.

Write your answer to council_v5_harness/<AGENT>_round2.md
```

---

## Returning the results

Commit and push the new files to the same branch:

```bash
git add council_v5_harness/
git commit -m "Council v5: <agent> round <n>"
git push
```

Or paste them into the Claude chat. Claude then writes its Round 2 and compiles everything into `full_council_v5_harness.md`.
