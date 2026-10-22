# Council v7 prompts: flip the perspective on decision models (run on the laptop)

Claude's Round 1 is in `council_v7_flip_perspective/claude_round1.md`. Codex and Gemini each write their own Round 1 **without reading Claude's** (or each other's). Then all three write Round 2.

## Setup

```bash
git fetch origin claude/decision-model-council
git checkout claude/decision-model-council
git pull
# optional: the most relevant earlier report lives on another branch
git show "origin/claude/future-of-care-research:reports/AI care vectors for Thailand.md" > /tmp/ai_care_vectors.md
```

Run each agent from the repo root, as in v3–v6:

- **Codex:** gpt-6.1-sol, high effort.
- **Gemini:** gemini-4-argon-high via `agy`.

Use the philosopher-council lenses and isolate each agent from its stored memories.

---

## Round 1 prompt (identical for Codex and Gemini)

Replace `<AGENT>` with `codex` or `gemini`.

```text
You are one of three independent advisors (Claude, Codex, Gemini) on a master's capstone council. Apply the philosopher-council lenses: Descartes proposes from first principles, Hume audits every factual claim, Socrates stress-tests the single decisive assumption.

READ FIRST:
- README.md: the student, their constraints, the history of ideas
- council_v7_flip_perspective/brief.md: this round's brief
- /tmp/ai_care_vectors.md if it exists: the most relevant earlier research report

DO NOT open council_v7_flip_perspective/claude_round1.md or any other advisor's file. Your Round 1 must be independent.

THE STUDENT'S QUESTION
How should a DECISION MODEL be used in the Thai healthcare system, with the frame "FLIP THE PERSPECTIVE", rather than building a plain screening or triage system? "Decision model" may mean a clinical decision model or a health-economic decision-analytic model (HTA); consider both.

TASK
Part A: in at most 150 words, say what "flipping the perspective" should mean here. Which hidden assumptions of a plain screening or triage model are worth flipping, and which flips are gimmicks?

Part B: propose exactly 5 flipped decision-model ideas, ranked. For each give:
1. **Name, the flip, and pitch:** which assumption is flipped, normal question → flipped question, 1–2 sentences.
2. **Paradigm and research question:** a falsifiable RQ with the exact comparison or metric.
3. **Thai testbed and impact:** who benefits, how it is measured; mark unverified claims.
4. **POC/MVP:** what a 9-month build on one RTX 4090 Laptop (16 GB) proves, with data, models, compute and API cost. The full vision may be national-scale.
5. **Prior art to beat:** with citations.
6. **Socratic stress-test:** the single decisive assumption, plus a concrete month-1 test with a numeric kill or pivot threshold.

End with "If I were the student I'd pick #N" and one line saying why.

Cite sources (URL or arXiv ID) for factual claims; mark anything unverified as [UNVERIFIED]. Be bold in ambition and honest in evidence.

Write your answer to council_v7_flip_perspective/<AGENT>_round1.md
```

---

## Round 2 prompt (after all three Round 1 files exist)

Replace `<AGENT>` with `codex` or `gemini`. Claude writes `council_v7_flip_perspective/claude_round2.md` in the cloud session.

```text
Council v7 (flip the perspective on decision models), Round 2. Read council_v7_flip_perspective/claude_round1.md, codex_round1.md and gemini_round1.md. Do not read any *_round2.md file.

Write five sections:
1. **Hume audit:** the 5 most load-bearing factual, novelty or feasibility claims made by the OTHER two advisors that are wrong, unverified or overstated. Say why, and what would verify each.
2. **Convergence verdict:** which flips did the advisors converge on? Is that convergence a real signal or the obvious attractor of the brief? Name the best variant in each cluster.
3. **Socrates:** the single most over-rated idea from another advisor, and the assumption it breaks on.
4. **Most under-rated:** the single most under-rated idea from another advisor, and how you would merge or improve it.
5. **Final top 3:** a table with columns # | Project | Flip | Novelty (1–5) | Thai impact (1–5) | POC finish confidence (%) | Gate/dependency | Why. Then name one "moonshot" and one "safe ambitious" pick.

Write your answer to council_v7_flip_perspective/<AGENT>_round2.md
```

---

## Returning the results

Commit and push the new files to the same branch:

```bash
git add council_v7_flip_perspective/
git commit -m "Council v7: <agent> round <n>"
git push
```

Or paste them into the Claude chat. Claude then writes its Round 2 and compiles `full_council_v7_flip_perspective.md`.
