# Council v4 prompts (run on the laptop)

Claude's Round 1 is already in `council_v4/claude_round1.md`. Codex and Gemini each write their own Round 1 **without reading Claude's** (or each other's). Then all three write Round 2.

## Setup

```bash
git fetch origin claude/physical-ai-med-ed-research
git checkout claude/physical-ai-med-ed-research
git pull
```

Run each agent from the repo root, the same way as v3:

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
- reports/Thai physical AI and med education.md: the deep-research report this round is based on
- research_notes/Thai physical AI and med education/*.md: the underlying sourced notes (use them to check claims)

DO NOT open anything else in council_v4/ except this prompt. Your Round 1 must be independent of the other advisors.

STUDENT AND CONSTRAINTS
- Master's in AI and digital health at Chulalongkorn (Medicine + Engineering committee), about 9 months.
- One laptop: RTX 4090 Laptop (16 GB VRAM), i9-13980HX, 32 GB RAM, about 1 TB. No cluster.
- Wants frontier ML as the core contribution, with real, measurable Thai healthcare impact.
- New scope for this round: PHYSICAL AI, ROBOTICS, DRONES, AR/XR, and now MEDICAL EDUCATION.
- Cheap hardware is allowed if justified (for example an SO-101 arm at about US$300, a Quest 3, a GoPro, a handheld ultrasound borrowed from the hospital). Thai drone flights are effectively ruled out by the CAAT rules in force since 17 May 2026.
- Already rejected: "safe" admin/claims ideas, VenomSight, dysarthria. Do not re-propose them.

TASK
Propose exactly 5 capstone ideas, ranked. The report's 7 ranked directions are one input, not a menu: at most 2 of your 5 may be close variants of them, and if you reuse one you must materially sharpen it. For each idea give:
1. **Name and pitch:** 1–2 sentences.
2. **Paradigm and research question:** which frontier paradigm, and a falsifiable RQ with the exact comparison or metric.
3. **Thai testbed and med-ed impact:** who benefits, how impact is measured, which claims are unverified.
4. **Laptop experiment:** models with parameter counts, data (public plus local), VRAM fit, GPU-hour budget, baselines, metrics, hardware cost.
5. **Socratic stress-test:** the single decisive assumption, plus a concrete month-1 test with a numeric kill or pivot threshold.

End with "If I were the student I'd pick #N" and one line saying why.

Cite sources (URL or arXiv ID) for factual claims; mark anything unverified as [UNVERIFIED]. Be concrete and honest. Disagree with the report where you think it is wrong.

Write your answer to council_v4/<AGENT>_round1.md
```

---

## Round 2 prompt (after all three Round 1 files exist)

Replace `<AGENT>` with `codex` or `gemini`. Claude writes `council_v4/claude_round2.md` in the cloud session.

```text
Council v4, Round 2. Read council_v4/claude_round1.md, council_v4/codex_round1.md and council_v4/gemini_round1.md (plus the report and notes as needed). Do not read any *_round2.md file.

Write five sections:
1. **Hume audit:** the 5 most load-bearing factual or feasibility claims made by the OTHER two advisors that are wrong, unverified or overstated. Say why, and what would verify each.
2. **Convergence verdict:** where the three advisors converged, is that convergence a real signal or just the obvious attractor of the constraints? Name the best variant within each cluster and the design choice that makes it publishable.
3. **Socrates:** the single most over-rated idea from another advisor, and the assumption it breaks on.
4. **Most under-rated:** the single most under-rated idea from another advisor, and how you would merge or improve it.
5. **Final top 3:** a table with columns # | Project | Finish confidence (%) | GPU-hours | Frontier-ness | Thai/med-ed impact | Why. Merges across advisors are encouraged.

Write your answer to council_v4/<AGENT>_round2.md
```

---

## Returning the results

Commit and push the new files to the same branch:

```bash
git add council_v4/
git commit -m "Council v4: <agent> round <n>"
git push
```

Or paste them into the Claude chat. Claude then writes its Round 2 and compiles everything into `full_council_v4_physical_med_ed.md`.
