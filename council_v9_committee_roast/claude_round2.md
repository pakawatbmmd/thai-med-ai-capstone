# Council v9: Claude, Round 2 (acting as the proposal committee: one clinician examiner, one engineer examiner)

**Read:** all three Round 1 answers. No Round 2 file was read.

## 1. Roast of the other advisors' top 3

### Codex #1: Verified Thai medication-instruction editor (pharmacist-facing)
- **Clinician examiner's hardest question:** "Pharmacists print label instructions from the HIS template (ฉลากยา). When do they ever free-text rewrite instructions? You are a physician. Who exactly is the user, and have you seen this task?"
- **Engineer examiner:** "The checker compares structured facts. Where does the structure come from if the source is free text?"
- **Passes as is?** Borderline. The safety design is excellent (source-bound, deterministic fact check, abstention, a template comparator), but the user and owner are far from the student's own practice.
- **Minimum fix:** move the user to *the physician writing discharge and medication counselling instructions*, the student's own workflow, which is Gemini #2's framing. Keep Codex's evaluation design exactly.

### Codex #2: Occupational blood-exposure first-response checklist
- **Hardest question:** "Every Thai hospital already has an infection-control needlestick flow chart, and the national PEP guideline is short. Why build AI for a laminated card?"
- **Engineer:** "This is a rule engine; where is the AI?"
- **Passes?** Probably, but as a low-impact project. Codex's own comparator (a paper flowchart) will be hard to beat meaningfully.
- **Minimum fix:** none worth making. Keep it only as an emergency fallback.

### Codex #3: Thai red-flag chatbot testing workbench
- **Hardest question:** "This is a Plan 2 professional degree. Who uses a workbench on Monday morning?"
- **Passes?** Only with a named owner who reviews chatbots regularly (a hospital digital-health team or a teaching group). Otherwise it reads as a research benchmark.
- **Minimum fix:** merge with Gemini #3's user (a tele-triage nurse or GP), or drop it.

### Gemini #1: ThaiLab-LOINC mapping
- **Clinician:** "Last year had two TMT drug-mapping projects. This is the same idea with labs."
- **Engineer:** "Your 'messy hospital lab strings' are invented by classmates, so the test set is circular."
- **Passes?** At risk on the duplicate attack. It is also furthest from a physician's expertise.
- **Minimum fix:** obtain one real hospital lab test catalogue (a code list is *not* patient data, and a lab director could share it). Without that it is not defensible.

### Gemini #2: DischargeClear, plain-Thai discharge and medication instructions with a dose-locking verifier
- **Clinician:** "Last year's LLM-on-EMR projects collapsed on real notes (22% accuracy). Why won't yours?" and "LINE export of a patient's discharge plan: PDPA?"
- **Engineer:** "If doses are locked deterministically, what does the LLM add, and how do you measure that it helped?"
- **Passes?** Yes, with scope discipline. This is the strongest of the six. The student *is* the user, colleagues are easy to recruit, no patient data is needed, and the safety story is concrete.
- **Minimum fix:**
  - **Scope:** limit it to the medication and red-flag sections, for 5–8 common conditions.
  - **Data:** take source notes written by physician colleagues to realistic style; it needs no real records.
  - **Comparators:** add Codex's comparators (template vs LLM without a checker vs the checked tool) and its locked test set built partly by independent clinicians.
  - **Export:** no LINE export in the MVP; print or PDF only.

### Gemini #3: TriageGuard-1669
- **Hardest question:** "Rules make the safety call, so why the LLM? And GRPO fine-tuning in this timeline?"
- **Passes?** Yes if cut to "the LLM turns colloquial Thai complaints into structured findings, then a rule engine triages". Not with GRPO.
- **Minimum fix:** drop the RL. Make the evaluation clinician vignettes with a with/without-tool comparison.

## 2. Hume audit: three load-bearing claims that are wrong or unverified
1. **Gemini #3: "tele-triage nurses (e.g., NHSO 1330, EMS 1669…)".** NHSO's 1330 hotline is mainly for benefit and rights enquiries, not clinical tele-triage [verify]. Citing it as a triage-nurse setting would be caught by any Thai examiner.
2. **Gemini #5: "NHANES >50,000 patients with repeat lab measurements".** NHANES is largely cross-sectional, with one visit per participant. Repeat-measurement data exist only for limited subsamples [verify], so the proposed "repeat-lab cohort" simulation would not work as described.
3. **Gemini, across ideas: "the student already has the technical background (README)" and "the faculty who advised #9/#33 … highly plausible to recruit".** Neither is established. The README records the student's interests, not their skills, and advisor availability is speculation. Plan as though the student must learn the stack and recruit cold.

Smaller points:
- "LOINC … free open licence": LOINC is free but under Regenstrief's own licence terms with registration, not an open licence [verify].
- On my own Round 1: the PhysioNet Challenge 2024 ECG-image data access and licence must be checked before the photo-ECG idea is promised.

## 3. Convergence
- **A verified medication or discharge-instruction writer (Codex #1 + Gemini #2): an independent convergence, and a real signal.** The two reached it from different directions: Codex from medication-safety editing, Gemini from discharge comprehension. Both put a *deterministic critical-fact lock* around an LLM. It fits every constraint: physician user, no patient data, a practical product, a demonstrable safety mechanism, and a cheap clinician study.
- **Red-flag triage tool (Claude #4 + Codex #3 + Gemini #3):** all three reached it, but all rated it mid-pack. That is more attractor than signal; it comes from the student's history in the README.
- **Lab-noise "repeat vs treat" (Claude #3 + Gemini #5):** both rate it lower. The committee would ask "where is the AI?"
- **ECG (Claude #1 photo-ECG; Codex #5 artifact training):** different products. Photo-ECG has the stronger clinical hook; Codex's version is safer but weaker.

## 4. Final ranking (committee view)

| # | Title | P(approved) | P(finished) | Data/IRB risk | Advisor fit | One-line verdict |
|---|---|---|---|---|---|---|
| 1 | **Verified Thai discharge medication and red-flag instruction generator** (Gemini #2 user + Codex #1 evaluation design) | 0.85 | 0.85 | Low: colleague-written source notes; exempt or expedited clinician study | Internal or family medicine + an NLP/software engineer | The student's own workflow, a concrete safety mechanism, an easy user study |
| 2 | **Photo-ECG triage for community-hospital doctors** (Claude #1) | 0.75 | 0.75 | Low: public ECGs + self-made photos; reader study | Cardiology or EM + signal/image processing | The best demo and conference story; risk is digitisation quality |
| 3 | **Thai colloquial-complaint → structured findings → rule-based red-flag triage CDSS** (Gemini #3 cut, Codex #3 evaluation) | 0.70 | 0.85 | Low: vignettes | EM or family medicine + NLP | Keeps the student's prior interest, but must not look like a benchmark paper |

**Recommendation for this student: #1.**

**The three things to do in the next 7 days:**
1. **Recruit advisors with a one-page brief and a mock screen.**
   - *Who:* a clinical advisor in internal or family medicine (or clinical pharmacy) and an engineering co-advisor in NLP or software.
   - *How:* ask the programme office who supervises LLM/NLP and patient-education projects.
   - *What to bring:* a mock screen showing a note going in and a patient card coming out, with doses highlighted as locked.
2. **Collect local evidence without patients.**
   - Survey 30+ physician colleagues: time spent on discharge counselling, how often medication instructions are misunderstood, current tools.
   - Have 3 colleagues each write 5 realistic, fictional discharge notes in their normal style. This becomes the seed of the test set.
3. **Build a one-day feasibility spike.**
   - A local 4B model (or an API on the fictional notes) rewrites 10 notes into plain Thai.
   - A regex/structured checker verifies dose, frequency and timing against the source.
   - Count critical-fact errors with and without the checker.
   - Book a CU IRB consultation for the clinician user study.
