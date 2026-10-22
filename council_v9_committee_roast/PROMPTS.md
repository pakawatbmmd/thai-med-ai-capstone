# Council v9 prompts: feasible, approvable ideas plus a committee roast

Run with `COUNCIL_PRIVATE_DIR=<scratchpad> python3 tools/run_council.py --council v9 --round 1|2`. The programme requirements and last year's catalogue are private inputs, read from disk and never committed.

---

## Round 1 prompt

```text
You are one of three independent advisors (Claude, Codex, Gemini) helping a student choose a capstone that their committee will APPROVE and that they can FINISH. Apply the philosopher-council lenses: Descartes proposes, Hume audits facts, Socrates finds the decisive assumption.

READ FIRST (all inlined):
- README.md: the student's project history
- council_v9_committee_roast/brief.md: this round's brief and the student's real situation
- v9_programme_requirements.md: the programme's capstone requirements, proposal outline and exam format
- capstone_2568_catalogue.md: last year's ~37 capstones (what passes; what is already taken)

Your Round 1 must be independent of the other advisors.

TASK
Part A (≤150 words): What will THIS committee reward and punish, judging by the requirements and last year's projects? Be concrete.

Part B: propose exactly 5 capstone ideas ranked by P(approved AND finished on time). You may re-use and reshape an idea from the earlier shortlist if it can be made approvable. Avoid last year's topics unless clearly differentiated. For each idea:
1. **Title** (as it would appear on the proposal) and a 2-sentence pitch.
2. **Local problem and users:** who suffers, where, with what evidence a physician without hospital data can gather (public statistics, literature, colleague interviews or surveys, workflow observation).
3. **Data:** exact public datasets or non-patient data, with size and licence/access conditions; IRB needs.
4. **MVP and evaluation:** what is built (model + prototype), and how it is validated (technical metrics, clinician/user study size, success criteria).
5. **Committee roast:** the 5 questions examiners are most likely to ask, the single most damaging attack, and the best honest answer.
6. **Fit:** which advisor profile (clinical specialty + engineering skill) it needs, and why it is plausible to recruit one in 2 weeks.
7. **Verdict:** P(approved), P(finished), and the main risk.

End with "If I were the student I'd pick #N" and one line saying why. Cite sources for factual claims; mark anything unverified as [UNVERIFIED].

Write your answer to council_v9_committee_roast/<AGENT>_round1.md
```

---

## Round 2 prompt

```text
Council v9, Round 2. Read the three Round 1 answers (claude, codex, gemini). Do not read any *_round2.md.

You are now THE PROPOSAL COMMITTEE (two invited examiners: one clinician, one engineer).
1. **Roast the other two advisors' top-3 ideas:** for each, the hardest question, whether the proposal would pass as is, and the minimum fix to make it pass.
2. **Hume audit:** the 3 most load-bearing factual claims (datasets, licences, prior art, feasibility) that are wrong or unverified.
3. **Convergence:** which ideas or themes did several advisors reach independently? Is it a real signal?
4. **Final ranking:** a table with columns # | Title | P(approved) | P(finished) | Data/IRB risk | Advisor fit | One-line verdict. Give your top 3 across all advisors (merges allowed). Then name the one you would recommend to this student and the 3 things they must do in the next 7 days.

Write your answer to council_v9_committee_roast/<AGENT>_round2.md
```
