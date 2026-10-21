# Council v6 prompts: aim high, with McKinsey's "AI-powered future of care" as the frame (run on the laptop)

Claude's Round 1 is already in `council_v6_future_of_care/claude_round1.md`. Codex and Gemini each write their own Round 1 **without reading Claude's** (or each other's). Then all three write Round 2.

## Setup

```bash
git fetch origin claude/future-of-care-research
git checkout claude/future-of-care-research
git pull
```

The McKinsey PDF is **not** in the repo (it is copyrighted and the repo is public). A summary is in `research_notes/AI care vectors for Thailand/00_guidance_mckinsey_summary.md`. If you want the agents to read the original, copy your local PDF into the repo folder as `mckinsey_future_of_care.pdf`, but **do not commit it** (add it to `.git/info/exclude`).

Run each agent from the repo root, as in v3–v5:

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
- research_notes/AI care vectors for Thailand/00_guidance_mckinsey_summary.md: summary of the guiding document, McKinsey "The AI-powered future of care" (Sept 2026). If mckinsey_future_of_care.pdf exists in the repo root, read it too.
- reports/AI care vectors for Thailand.md: the deep-research report this round is based on
- research_notes/AI care vectors for Thailand/*.md: the underlying sourced notes (use them to check claims)
- reports/Thai medical LLM landscape.md: background on Thai medical LLMs

DO NOT open anything else in council_v6_future_of_care/ except this prompt. Your Round 1 must be independent of the other advisors.

THE BRIEF FROM THE STUDENT (paraphrased)
"Use the McKinsey paper as guidance. Aim high: the goal is a groundbreaking, novel solution: a new model, a new agent, or a new way of using AI. Don't constrain the idea to 9 months; if the idea passes the committee, the actual final project can be a POC or MVP."

STUDENT AND CONSTRAINTS
- Master's in AI and digital health at Chulalongkorn (Medicine + Engineering committee). The POC/MVP is built in about 9 months.
- POC hardware: one laptop with an RTX 4090 Laptop (16 GB VRAM), 32 GB RAM, about 1 TB. API models are allowed on synthetic data. The full vision may assume national-scale resources.
- Wants frontier ML as the core contribution, with real Thai healthcare impact.
- Already explored or rejected: "safe" admin/claims ideas, VenomSight, dysarthria. Explored on other branches (may be reused only if made sharper): dual-verifier RSI, a medical safety harness and hooks, and AI skill coaching for medical education.

TASK
Part A: in at most 200 words, critique the McKinsey frame for Thailand. What does it get right? Where is it US-specific or overclaiming? Which of its "signals of scale" does Thailand already have?

Part B: propose exactly 5 ambitious, globally novel capstone ideas, ranked. The report's 6 directions are one input, not a menu: at most 2 of your 5 may be close variants of them, and if you reuse one you must materially sharpen it. For each give:
1. **Name and novel claim:** one sentence that a top venue would accept as new.
2. **McKinsey vector(s) and signal(s) of scale it advances.**
3. **Why Thailand:** what makes it natural in Thailand and hard in the US.
4. **Full vision vs 9-month POC/MVP:** what the full system is, and exactly what the POC proves. Include models with parameter counts, data, laptop-hours or GPU-hours, and API cost.
5. **Prior art to beat:** with citations.
6. **Socratic stress-test:** the single decisive assumption, plus a concrete month-1 test with a numeric kill or pivot threshold.

End with "If I were the student I'd pick #N" and one line saying why.

Cite sources (URL or arXiv ID) for factual claims; mark anything unverified as [UNVERIFIED]. Be bold in ambition and honest in evidence. Disagree with the report and with McKinsey where you think they are wrong.

Write your answer to council_v6_future_of_care/<AGENT>_round1.md
```

---

## Round 2 prompt (after all three Round 1 files exist)

Replace `<AGENT>` with `codex` or `gemini`. Claude writes `council_v6_future_of_care/claude_round2.md` in the cloud session.

```text
Council v6 (aim high, McKinsey frame), Round 2. Read council_v6_future_of_care/claude_round1.md, codex_round1.md and gemini_round1.md (plus the report and notes as needed). Do not read any *_round2.md file.

Write five sections:
1. **Hume audit:** the 5 most load-bearing factual, novelty or feasibility claims made by the OTHER two advisors that are wrong, unverified or overstated. Say why, and what would verify each.
2. **Convergence verdict:** where the three advisors converged, is that convergence a real signal or just the obvious attractor of the report? Name the best variant within each cluster and the design choice that makes it groundbreaking rather than incremental.
3. **Socrates:** the single most over-rated idea from another advisor, and the assumption it breaks on.
4. **Most under-rated:** the single most under-rated idea from another advisor, and how you would merge or improve it.
5. **Final top 3:** a table with columns # | Project | Novelty (1–5) | Thai advantage (1–5) | POC finish confidence (%) | Gate/dependency | Why. Merges across advisors are encouraged. Then name one "moonshot" (highest ceiling regardless of risk) and one "safe ambitious" pick.

Write your answer to council_v6_future_of_care/<AGENT>_round2.md
```

---

## Returning the results

Commit and push the new files to the same branch:

```bash
git add council_v6_future_of_care/
git commit -m "Council v6: <agent> round <n>"
git push
```

Or paste them into the Claude chat. Claude then writes its Round 2 and compiles everything into `full_council_v6_future_of_care.md`.
