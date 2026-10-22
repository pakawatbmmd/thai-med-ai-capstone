# Council v8 prompts: clinical / scientific / model-development flips on decision models

Run from the cloud with `python3 tools/run_council.py --council v8 --round 1` (then `--round 2`), or on the laptop with these prompts.

---

## Round 1 prompt (identical for Codex and Gemini)

```text
You are one of three independent advisors (Claude, Codex, Gemini) on a master's capstone council. Apply the philosopher-council lenses: Descartes proposes from first principles, Hume audits every factual claim, Socrates stress-tests the single decisive assumption.

READ FIRST:
- README.md: the student, their constraints, the history of ideas
- council_v8_clinical_flip/brief.md: this round's brief, including HARD EXCLUSIONS

Your Round 1 must be independent; do not rely on any other advisor's answer.

THE STUDENT'S QUESTION
Flip the perspective on DECISION MODELS in healthcare, but keep it CLINICAL, SCIENTIFIC or MODEL-DEVELOPMENT. No health-system policy, payer, HTA, cost-effectiveness, legal or regulatory, credentialing, or payment ideas. The core contribution must be clinical science, ML science, or a new model, method or agent.

TASK
Part A: in at most 120 words, name the hidden assumptions of a plain clinical prediction or triage model that are most worth flipping *scientifically*, and which flips would just be relabelling.

Part B: propose exactly 5 ideas, ranked. For each give:
1. **Name, the flip, and pitch:** normal question → flipped question, 1–2 sentences.
2. **Paradigm and research question:** a falsifiable RQ with the exact comparison or metric, and the ML method.
3. **Clinical relevance:** who benefits clinically, how it is measured; Thai clinical relevance if any (no policy or payment); mark unverified claims.
4. **POC/MVP:** what 9 months on one RTX 4090 Laptop (16 GB) proves, with datasets (prefer public: MIMIC-IV, MIMIC-IV-ED, eICU, PhysioNet, public imaging), models with parameter counts, and compute.
5. **Prior art to beat:** with citations.
6. **Socratic stress-test:** the single decisive assumption, plus a concrete month-1 test with a numeric kill or pivot threshold.

End with "If I were the student I'd pick #N" and one line saying why.

Cite sources (URL, DOI or arXiv ID) for factual claims; mark anything unverified as [UNVERIFIED]. Be bold in ambition, honest in evidence, and strictly respect the exclusions.

Write your answer to council_v8_clinical_flip/<AGENT>_round1.md
```

---

## Round 2 prompt

```text
Council v8 (clinical / scientific flips on decision models), Round 2. Read council_v8_clinical_flip/claude_round1.md, codex_round1.md and gemini_round1.md. Do not read any *_round2.md file.

Write five sections:
1. **Hume audit:** the 5 most load-bearing factual, novelty or feasibility claims made by the OTHER two advisors that are wrong, unverified or overstated. Say why, and what would verify each. Also flag any idea that violates the brief's exclusions.
2. **Convergence verdict:** which flips converged? Is that convergence a real signal or the obvious attractor of the brief? Name the best variant in each cluster.
3. **Socrates:** the single most over-rated idea from another advisor, and the assumption it breaks on.
4. **Most under-rated:** the single most under-rated idea from another advisor, and how you would merge or improve it.
5. **Final top 3:** a table with columns # | Project | Flip | Novelty (1–5) | Clinical impact (1–5) | ML depth (1–5) | POC finish confidence (%) | Data gate | Why. Then name one "moonshot" and one "safe ambitious" pick.

Write your answer to council_v8_clinical_flip/<AGENT>_round2.md
```
