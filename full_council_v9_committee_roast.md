# Capstone Council v9: Approvable, feasible capstones plus a committee roast (Claude × Codex × Gemini, 2026-10-22)

**Brief:** `council_v9_committee_roast/brief.md`.
- **Student:** a physician with public data only, no advisor yet, and a proposal exam in November.
- **Private inputs** (programme requirements, last year's anonymised project catalogue) were inlined for the models but are not committed.
- **Models:** Codex = `gpt-6.1-sol` (high effort); Gemini = `gemini-4-argon`.
- **Rounds:** Round 1 = independent proposals; Round 2 = each model acts as the proposal committee.

## Synthesis (Claude, after all six files)

**Unanimous #1 in all three Round 2 committee rankings**

> **A critical-fact-verified Thai medication and discharge instruction editor.** It takes the medication and follow-up instructions a physician wrote (often abbreviated Thai-English), rewrites them into clear plain Thai with a pill timetable, and **highlights any change to drug, dose, unit, frequency, timing or stop-rules** against the source. A professional must approve the result. (Codex #1 + Gemini #2 "DischargeClear", reached independently in Round 1.)

| | Claude R2 | Codex R2 | Gemini R2 |
|---|---|---|---|
| Rank | #1 | #1 | #1 |
| P(approved) / P(finished) | 0.85 / 0.85 | 0.80 / 0.88 | 0.90 / 0.90 |

**The scope everyone can accept** (Codex's limits + Gemini's user + Claude's sourcing):
- **User:** the physician writing discharge and medication instructions; the student's own workflow. Pharmacists are secondary users.
- **In scope:** rewrite instructions *explicitly supplied* by the clinician; a deterministic critical-fact comparison; visible discrepancies; mandatory approval; print/PDF output.
- **Out of scope:** diagnosis inference; any *new* clinical advice; patient-facing delivery or LINE export; prescribing; HIS integration.
  - Red-flag text, if included, comes only from a fixed clinician-approved library the doctor selects. It is never generated, which answers Codex's "who authorised that advice?".
- **Never claim a "guarantee"** (Codex, Claude). Report measured fidelity, planted-error sensitivity and specificity, and abstention, with confidence intervals.
- **Data:** realistic *fictional* source notes written by physician colleagues (some by independent authors for the locked test set), plus planted-error variants. No patient records. MIMIC credentialing stays off the critical path; Gemini warns it can take 3–6 weeks.
- **Comparators:** existing templates/shortcodes vs the same LLM without the checker vs the checked editor.
- **Evaluation:** two blinded raters; ≥12 clinicians in a counterbalanced timed editing study; SUS.
- **Stop condition:** if templates already solve the task, or it is rare, redirect.

**Runners-up:**
- **Photo-ECG triage:**
  - Gemini #2 (it adds an image-quality gatekeeper).
  - Codex dropped it: public data lack adjudicated *acute* STEMI labels.
  - Keep it only if a cardiology advisor appears and the label inventory checks out.
- **Thai red-flag triage review workbench:** in all three top 3s in some form. Acceptable only with a named reviewing owner and no RL.

**Rejected or weak:**
- Needlestick checklist (fails "why AI?").
- AKI or lab-noise alerts (no local problem; "Monte Carlo, not AI").
- ThaiLab-LOINC (TMLT already ships LOINC mappings, so the test set would be circular without a real hospital lab catalogue).
- AMR (duplicates a project from last year).

**Ethics note (all three):** no patient data ≠ no ethics review. Clinician surveys, annotation and user studies need a CU IRB determination. "Clinician-in-the-loop" does not by itself settle medical-device status.

**Next 7 days**, consensus of the three Round 2 plans:
1. Build a 1-screen mock-up with 5–10 fictional notes, showing the note, the fact-diff (red/green) and the Thai patient card. Write a one-page brief.
2. Contact several advisors in parallel: clinical (internal/family medicine, EM, or clinical pharmacy) and engineering (NLP/software). Ask the programme office who supervises LLM/NLP projects. Submit advisor names and 3 exam slots as soon as one pair agrees.
3. Survey 10–30 physician and pharmacist colleagues on discharge-instruction workload and errors. Have 3 colleagues write realistic fictional notes. Book a CU IRB consultation. Freeze scope, comparators and the evaluation matrix, and write portfolio Sections 1–3.

---

# ROUND 1

## CLAUDE: Round 1

## Part A: What this committee rewards and punishes

**Rewards:**
- A **specific local clinical problem** a physician can describe from experience and back with numbers.
- **Named users** and a current workflow with a clear pain point.
- A **working prototype** (an app or tool with a model inside).
- **Honest validation**, even on small sets.
- A user or clinician study, however small (SUS, agreement, time).
- A realistic timeline and clean ethics.

Last year's strongest projects stood out on **validation rigour and real-world fit, not model novelty**: Warfarin pre-post, AMR with a temporal split, newborn screening at scale, and TMT mapping against a pharmacist audit.

**Punishes:**
- Vague "AI for X" with no user.
- Data the student can't get.
- Projects that are research papers rather than tools.
- Duplicates of last year.
- Scope that obviously won't fit nine months.
- Weak answers to "why digital?" and "how will this be used on Monday?".

For a physician **without hospital data**, the winning shape is:

> a public dataset that matches a real Thai workflow + a prototype + a clinician-user evaluation that needs no patient data.

## Part B: Five ideas ranked by P(approved AND finished)

### 1. "Photo-ECG Triage": an AI assistant that reads smartphone photos of paper 12-lead ECGs to flag STEMI and other critical findings for community-hospital doctors
- **Pitch:** In Thai community hospitals, GPs and interns often photograph a printed ECG and send it over LINE to a cardiologist or provincial centre for advice [UNVERIFIED prevalence; gather with a colleague survey]. A web or mobile prototype digitises the photo, flags time-critical patterns (STEMI/equivalents, high-grade AV block, VT), and produces a structured referral message.
- **Local problem and users:**
  - *Primary users:* GPs, interns and ER nurses in community hospitals (รพ.ช.).
  - *Stakeholders:* provincial cardiology and the STEMI fast-track network.
  - *Evidence the student can gather:* published Thai STEMI door-to-reperfusion and referral-delay data; a 15-minute survey of 30–50 physician colleagues (how often they send ECG photos, response time, uncertainty); one workflow map.
- **Data:**
  - PTB-XL: 21,799 12-lead ECGs, 18,869 patients, CC BY 4.0 [verify version].
  - The George B. Moody PhysioNet Challenge 2024 on ECG image digitisation and classification, with ECG-Image-Kit to synthesise realistic paper/photo artefacts [verify licence and data access].
  - A local test set the student creates without patients: print public ECGs on standard Thai hospital ECG paper and photograph them with several phones and lighting conditions. No IRB for this part.
  - IRB only for the clinician reader study (likely exempt or expedited).
- **MVP and evaluation:**
  - **Pipeline:** photo → digitisation (signal extraction) → classifier (fine-tuned 1D CNN or an off-the-shelf PTB-XL model) → flag + explanation + referral template.
  - **Technical metrics:** digitisation fidelity (SNR/correlation vs ground-truth signal); AUROC, sensitivity and specificity for the critical classes on held-out PTB-XL and on the photographed set.
  - **Reader study:** 10–15 GPs or interns read 40 ECG photos with and without the AI; measure accuracy, time and confidence; SUS.
  - **Success criteria:** sensitivity ≥90% for STEMI patterns on the photographed set; SUS ≥70; a reader-accuracy gain or no loss.
- **Committee roast:**
  1. "PMcardio and similar apps already do this. Why build it?" (They are commercial, English-centric, not integrated with Thai referral workflow, and not validated on Thai paper formats; we compare against published performance [UNVERIFIED specifics].)
  2. "PTB-XL is German data. Does it generalise to Thai patients?" (A limitation stated up front; the photographed-paper test addresses the image-domain gap, not the population gap.)
  3. "Is this a medical device?" (A research prototype, not for clinical use; the Thai FDA SaMD pathway goes under future work.)
  4. "How does it fit the workflow?" (It plugs into the existing "photo → LINE" habit; the output is a referral message.)
  5. "What if it misses a STEMI?" (Decision support only; high-sensitivity operating point; the reader study measures over-reliance.)
  - **Most damaging attack:** "You didn't collect any real Thai patient ECGs." *Best answer:* the scope deliberately avoids patient data so it can be finished in nine months; a Thai prospective validation is the clearly defined next step.
- **Fit:** a cardiologist or emergency physician as clinical advisor, plus an engineering co-advisor in signal or image processing. The Digital Image Processing elective is directly relevant.
- **Verdict:** P(approved) ≈ 0.8; P(finished) ≈ 0.8. Main risk: digitisation quality on real photos (month-1 test: does a public digitiser reach usable fidelity on 20 self-made photos?).

### 2. A Thai CPG-grounded clinical question assistant for interns and GPs, with citations and abstention
- **Pitch:** A retrieval-augmented assistant that answers bedside questions *only* from Thai clinical practice guidelines (diabetes, hypertension, CKD, dyslipidaemia, dengue), cites the section, and refuses when the guideline is silent.
- **Local problem and users:** Interns and rural GPs need quick, locally correct answers. Generic chatbots give US/UK-based or hallucinated answers [gather examples]. Evidence: a short colleague survey, plus a pilot showing generic LLM errors on 20 Thai-guideline questions.
- **Data:** public Thai CPG documents (check each society's terms for reuse), and 150–200 clinician-written questions with gold answers. No patient data, so IRB applies only for the user study.
- **MVP and evaluation:**
  - **Build:** an open model (or API) + RAG + citation + an abstention rule, in a web app.
  - **Answer evaluation:** two physicians blind-grade correctness, harmful errors, citation accuracy and appropriate refusal against a generic-chatbot baseline.
  - **User study:** usability with 10 interns.
  - **Success criteria:** ≥90% citation-supported answers and 0 high-harm errors on the test set.
- **Committee roast:**
  - "This is just ChatGPT with PDFs. Where is the contribution?" (A Thai-guideline evaluation set and a measured harm rate.)
  - "Guidelines get updated, so who maintains it?"
  - "Last year had a RAG summariser."
  - "How do you prevent hallucination?"
- **Fit:** a family-medicine or internal-medicine advisor plus an NLP engineer.
- **Verdict:** P(approved) ≈ 0.75; P(finished) ≈ 0.9. Main risk: being seen as low novelty. The rigorous harm evaluation is what lifts it.

### 3. A creatinine-variability-aware AKI alert: fewer false alarms without missing AKI ("Remeasure Before Acting", made practical)
- **Pitch:** Rule-based AKI alerts (KDIGO creatinine rise) fire on changes within analytic and biological noise, which fuels alert fatigue. A prototype alert engine estimates the probability that a rise is real, and suggests "repeat creatinine" instead of "AKI" when it is not.
- **Data:** MIMIC-IV (credentialed PhysioNet access; requires the CITI course, about 1–2 weeks) and possibly eICU.
- **MVP and evaluation:** an alert simulator on MIMIC comparing standard KDIGO e-alerts vs the noise-aware version, measuring alert burden, missed AKI stage ≥2, and time to detection. A clinician review of 50 flagged cases.
- **Committee roast:**
  - "US ICU data; Thai labs differ."
  - "Is AKI alert fatigue a real problem here? Show local evidence."
  - "Clinicians already know to repeat creatinine."
- **Fit:** a nephrology or internal-medicine advisor plus a data-science engineer.
- **Verdict:** P(approved) ≈ 0.6; P(finished) ≈ 0.75. Main risk: weak local evidence and a "so what?".

### 4. A Thai medical chatbot safety audit: an open red-flag benchmark and dashboard (the audit-first plan, re-cut for this programme)
- **Pitch:** Several Thai medical LLMs are public, but no one has independently tested whether they escalate red flags (for example, refer to 1669) in Thai. Build an open benchmark of clinician-written Thai symptom vignettes and an evaluation dashboard, then report each model's under- and over-triage.
- **Data:** public models; 200–300 vignettes written and labelled by the student plus 2 physician colleagues. No patient data.
- **Committee roast:**
  - "Where is the product?" (The benchmark plus dashboard is the product; the users are hospital IT and AI procurement teams.)
  - "This is research, not service improvement."
  - "Inter-rater agreement?"
- **Verdict:** P(approved) ≈ 0.55; P(finished) ≈ 0.85. It fits the student's earlier interest, but this committee may see it as too research-like.

### 5. Empiric antibiotic regimen support for Gram-negative bacteraemia (differentiated from last year's AMR project)
- **Verdict:** P(approved) ≈ 0.4. Last year's #30 already predicts oxacillin resistance with a strong design. MIMIC-only, it needs an infectious-diseases advisor, and the regimen-plus-switch framing is subtle to defend in 30 minutes. Keep it as a backup only.

---

**If I were the student, I'd pick #1, Photo-ECG Triage.**
- It is a physician's own daily problem.
- It uses fully public data, plus a test set the student makes without patients.
- It has a clear user and workflow (the LINE habit), a demonstrable prototype, a reader study that needs only colleagues, and a strong conference story.
- It is not a duplicate of anything in last year's book.

**#2 is the safest fallback** if no cardiology or engineering advisor can be found quickly.

## CODEX (gpt-6.1-sol): Round 1

## Part A — What this committee will reward and punish

This is a **professional innovation capstone, not a methods thesis**. Expect rewards for a named clinical owner, documented Thai workflow problem, bounded MVP, usable prototype, comparison with current practice, and evaluation linked to explicit success criteria. A rigorous simulation study with clinicians is more defensible than an elaborate model awaiting hospital access. Budget for the required conference presentation. [P1]

The catalogue contains public-data, synthetic-data and no-patient-data projects; technical novelty is not the apparent differentiator. Strong examples compare against existing practice, measure time or errors, and disclose disappointing results. However, abstracts are not examination records: they do not prove that weak evaluation guarantees approval. [P2]

Expect punishment for invented “local need,” inaccessible data, no stakeholder commitment, unsupported clinical-benefit claims, duplicate topics, and an LLM demo without an implementation owner. Your immediate bottleneck is **recruiting advisors and a stakeholder—not choosing an architecture**. [P1–P3]

## Decision rules for this ranking

- **Descartes proposes:** build one useful, bounded product.
- **Hume audits:** distinguish available evidence from evidence still to be collected.
- **Socrates asks:** what assumption, if false, makes the project pointless?

**Probability convention:** All probabilities are subjective planning estimates, **[UNVERIFIED]**, not calibrated predictions. “Finished” means the agreed prototype, evaluation, report and conference presentation are completed by the programme deadline. I report \(P(\text{finished}\mid\text{approved})\); multiplying it by approval probability gives the ranking criterion without assuming independence.

**Data convention:** Researcher-authored dataset counts below are **planned collection sizes**, not existing assets. Public accessibility does not automatically grant reproduction rights. External links, current versions and licence conditions have not been live-checked here; dependencies requiring confirmation are marked **[UNVERIFIED]**.

| Rank | Proposal, shortened | P(approved) | P(finished \| approved) | P(both) |
|---|---|---:|---:|---:|
| 1 | Verified Thai medication-instruction editor | 85% | 90% | 77% |
| 2 | Occupational blood-exposure action checklist | 80% | 88% | 70% |
| 3 | Thai red-flag chatbot testing workbench | 76% | 84% | 64% |
| 4 | Observable inhaler-step video reviewer | 74% | 76% | 56% |
| 5 | ECG artifact-recognition training prototype | 68% | 79% | 54% |

### Non-negotiable conditions applying to all five

1. **No hospital data, integration or clinical deployment is on the critical path.** A clinician can be an external collaborator without supplying patients or records.
2. **Human participants still require ethics review.** Clinician interviews, timed user studies and healthy-volunteer recordings are not automatically exempt because they contain no patient data. Obtain the institutional determination before research recruitment or collection.
3. **Before the proposal is emailed:** secure the main advisor, co-advisor, one named stakeholder, and written confirmation that a simulation/feasibility evaluation is an acceptable final scope. The programme requires stakeholder collaboration; last year’s catalogue does not waive it. [P1]
4. **Evidence must remain honest:** local problems below are hypotheses until supported by permitted interviews, surveys or observation. General international guidance cannot establish prevalence in Thai practice.
5. **Conference planning starts immediately:** identify an eligible event occurring before graduation and a backup; dates and acceptance prospects are **[UNVERIFIED]**. Submit once feasibility results exist, rather than waiting for the final report.
6. **No frontier-training dependency:** use a small existing model, rules and ordinary web development first. Fine-tuning is optional only after the evaluation-ready MVP exists.

---

## #1 — Development and Usability Evaluation of a Critical-Fact-Verified Thai Medication Instruction Editor

**Pitch — two sentences.** Build a pharmacist-facing editor that rewrites supplied medication instructions into clearer Thai while checking that dose, unit, frequency, timing and warnings have not changed. Unlike medication reconciliation, drug-envelope OCR or terminology mapping, its contribution is a source-bound editing workflow with measured safety and editing-time performance.

### Local problem and users

- **Primary users:** pharmacists or physicians preparing medication education materials; secondary users are staff maintaining reusable instruction templates.
- **Proposed setting:** a collaborating community-pharmacy educator, pharmacy teaching group or professional training unit—not an assumed hospital partnership.
- **Local problem hypothesis:** staff either repeatedly rewrite similar instructions or use general-purpose AI without a reliable check for altered critical facts. **[UNVERIFIED]**
- **Evidence obtainable without patients:** permitted interviews with 6–8 pharmacists/physicians, a survey of current authoring tools, and timed observation of staff editing researcher-authored examples. Ask for workflow descriptions, not real prescriptions or screenshots.
- WHO identifies medication safety as a major international priority; that establishes importance, not this specific Thai workflow gap. [E1]

**Why digital rather than another leaflet:** the proposed benefit is checking variable instructions against their source. If ordinary templates already solve the problem, the project must acknowledge that rather than manufacture an AI requirement.

### Data

**Planned, wholly non-patient corpus:**

- **120 original source instruction cards:** 60 development, 20 validation, 40 locked test.
- For each card, create three draft rewrites: faithful, critical omission, and critical substitution—**360 drafts**, or **480 source-and-draft artifacts** altogether.
- Split by source card and instruction-pattern family; no paraphrase of a test card enters development.
- Reserve 20 test source cards for an independent pharmacist to author. Other cards are researcher-authored and pharmacist-checked.
- All drug names, doses and instructions are fictional teaching examples or independently authored examples, not copied prescriptions. They are evaluated for fidelity to the supplied source, **not endorsed as treatment regimens**.

**Access/licence:** no purchased dataset required. Release original text and labels under **CC BY 4.0 only after every contributing author agrees**. This is a planned licence, not an existing permission.

**Model:** Qwen3-4B is a possible local component; its model card lists Apache 2.0. Confirm the exact revision and terms before fixing the dependency. **[UNVERIFIED—current access/licence check]** [E2]

**IRB:** obtain a determination for corpus annotation and staff research; the timed user study requires review and informed consent.

### MVP and evaluation

**Build:**

- Source-text pane, proposed rewrite, side-by-side critical-fact comparison, highlighted conflicts and mandatory human approval.
- Small LLM for rewriting; deterministic checks for structured facts.
- Unsupported shorthand or ambiguous instructions cause **abstention**, not inferred clinical advice.
- No OCR, medication reconciliation, dose recommendation, patient account or live dispensing integration.

**Comparators:** ordinary editing with a reusable template; the same LLM without verification; the verified editor.

**Technical evaluation:**

- Two pharmacist raters, blinded to method, with disagreement adjudication.
- Measure critical-fact preservation, unsafe-draft detection sensitivity, specificity, abstention and usable-output rate.
- Proposed targets: **≥98% critical-fact preservation**, **≥95% sensitivity for planted critical errors**, and **≥85% specificity**. These are acceptance targets, not established safety guarantees.
- Report exact numerators and confidence intervals. Eighty planted unsafe drafts in the locked set do not support claims about rare real-world errors.

**User evaluation:**

- **12 pharmacists/physicians**, nine counterbalanced editing tasks each: 108 task observations, analysed as repeated measures rather than 108 independent people.
- Primary criterion: **≥25% lower median completion time** than ordinary editing, without more critical errors.
- Secondary: SUS ≥75, task completion, correction burden and willingness to maintain the templates.
- A negative result remains interpretable if templates outperform AI.

### Committee roast

1. Why is this not simply a ChatGPT prompt?
2. Why would a pharmacist trust instructions generated by AI?
3. Why not use fixed templates?
4. Who decided which errors are clinically important?
5. How do artificial examples establish usefulness in Thai practice?

**Most damaging attack:** “You invented both the problem and the benchmark, so your tool may solve neither.”

**Best honest answer:** “The local-need evidence must precede development. Independent pharmacists author part of the held-out set, staff editing is compared directly with templates, and no patient-safety benefit is claimed. If baseline observation shows negligible editing burden, I will not defend the original product premise.”

### Fit

- **Clinical advisor:** clinical pharmacy, medication safety or family medicine with a medication-education role.
- **Engineering co-advisor:** NLP/software engineering, particularly structured extraction, testing and web interfaces.
- **Why recruitment within two weeks is plausible:** the requested commitment is a bounded education/editing study, several review sessions and access to professional colleagues—not hospital records, IT integration or prospective patient care. Actual willingness and programme eligibility remain **[UNVERIFIED]**.
- **Implementation owner:** the collaborating pharmacy educator; handover includes editable templates, a versioned fact schema and regression tests.

### Verdict

**P(approved): 85%; P(finished | approved): 90%; P(both): 77%. [UNVERIFIED]**

**Main risk:** there may be insufficient benefit beyond templates.

**Socrates’ decisive assumption:** *Variable Thai instruction editing is a real, sufficiently frequent task for the intended owner.* Validate that before spending time on model selection.

---

## #2 — Development and Simulation-Based Evaluation of a Thai Occupational Blood-Exposure First-Response Checklist

**Pitch — two sentences.** Build a clinician-facing tool that converts a fictional needlestick report into a checked list of missing information, immediate actions and referral steps. The language model extracts facts, but a clinician-approved decision table controls the output; medication selection and dosing remain outside scope.

### Local problem and users

- **Primary users:** newly qualified doctors and nurses practising first response to occupational percutaneous blood exposure.
- **Owner:** occupational-health educator, infection-control educator or clinical-skills teaching unit.
- **Local hypothesis:** relevant information is gathered inconsistently, and users spend time locating the correct guidance under pressure. **[UNVERIFIED]**
- **Evidence:** permitted interviews with 6–8 clinicians, a survey using entirely fictional exposure scenarios, and observation of how participants find answers in currently used references.
- CDC publishes occupational HBV and HCV exposure-management resources; a current authoritative occupational-HIV source and its Thai applicability must be pinned with the clinical advisor. [E3–E5]

**Why digital:** interactive missing-information checks may prevent users from applying the wrong branch of a flowchart. A paper checklist is therefore the principal comparator, not an artificially weak “no assistance” condition.

### Data

**Planned original corpus:**

- **80 fictional exposure scenarios:** 40 development, 10 validation, 30 test.
- Three language versions per scenario—formal Thai, colloquial Thai and incomplete/ambiguous reporting—**240 texts**.
- Each scenario has clinician-approved slots, required questions and allowed action-card identifiers.
- No remembered patient cases, real incident forms or identifying occupational histories.

**Knowledge source:**

- A small, independently authored decision table referencing selected official guidance.
- Use source links and independently expressed factual rules, not an assumption that an entire website or translated guideline may be redistributed.
- US government-authored CDC material is generally public domain, but page-specific third-party content and marks require checking. **[UNVERIFIED—selected-page conditions]** [E6]
- A clinician must confirm the current authoritative guidance and acceptable Thai referral wording **before proposal submission**. Local referral contacts are configurable; the tool must not invent them.

**Licence/access:** original cases and labels can be CC BY 4.0 with contributor agreement; guidance documents retain their original terms. No paid database is required.

**IRB:** seek determination for fictional-case annotation and review/approval for clinician simulation research.

### MVP and evaluation

**Build:**

- Thai text entry plus optional structured form.
- Small-model slot extraction, explicit unknown values and a deterministic branch engine.
- Output: missing questions, traceable action checklist and a structured handover draft.
- Exclude non-occupational exposures, children, prescribing, autonomous risk clearance and claims of Thai national-guideline compliance.

**Technical evaluation:**

- Two clinician reviewers plus an adjudicator.
- Measure slot-level F1, critical-information omission, correct branch selection and citation traceability.
- Targets: **≥95% critical-slot recall**, **100% correct rule execution on enumerated branch tests**, and **no invented action on the locked test set**.
- Also test misleading free text, missing timestamps and contradictory statements. Zero observed unsafe actions is not proof of zero risk.

**User evaluation:**

- **12 doctors/nurses**, six matched, counterbalanced simulation tasks each.
- Compare an advisor-approved paper/PDF flowchart with the prototype.
- Targets: **≥25% shorter time to a complete first-response checklist**, ≥90% required-action completion, and no increase in critical omissions.
- Compare structured-form-only entry against language-model entry. If free text adds no value, retain the simpler interface.

### Committee roast

1. Which guideline governs the tool, and is it applicable in Thailand?
2. Why not use a laminated flowchart?
3. What happens when the exposure report omits essential information?
4. Who carries responsibility if advice is wrong or outdated?
5. Without an occupational-health service, where will this actually be used?

**Most damaging attack:** “An unofficial exposure-management tool could delay appropriate care.”

**Best honest answer:** “The evaluated MVP is a simulation and training tool, not an emergency service. It does not prescribe, clear exposures or replace consultation; unknown facts remain unknown. Real-use deployment would require a named service owner, approved local routing, governance and a separate evaluation.”

### Fit

- **Clinical advisor:** occupational medicine, infectious diseases, emergency medicine or infection control.
- **Engineering co-advisor:** decision-support software, rule testing and NLP.
- **Recruitment case:** the collaboration offers a reusable teaching resource and requires no incident records. A clinical-skills educator may be easier to recruit than a service willing to deploy software; availability is **[UNVERIFIED]**.
- **Maintenance owner:** a named educator approves guidance revisions; each action card stores source, version and review date.

### Verdict

**P(approved): 80%; P(finished | approved): 88%; P(both): 70%. [UNVERIFIED]**

**Main risk:** no advisor will accept responsibility for the selected guideline adaptation.

**Socrates’ decisive assumption:** *An identifiable educator wants interactive checklist training beyond the existing flowchart.* Without that owner, this is an attractive but unsupported guideline wrapper.

---

## #3 — Development of a Thai Red-Flag Response Testing Workbench for Symptom Chatbots

**Pitch — two sentences.** Turn the earlier audit-first idea into a usable testing product: a clinician can load chatbot responses, review predefined failure categories and export a traceable safety report. Evaluate the workbench and a bounded Thai challenge set; do not make recursive self-improvement, reinforcement learning or deployment of a new triage chatbot graduation requirements.

### Local problem and users

- **Users:** emergency/family-medicine educators and teams evaluating Thai-language health-chatbot demonstrations.
- **Proposed owner:** a digital-health teaching or evaluation group.
- **Local hypothesis:** reviewers lack a reproducible Thai workflow for checking whether chatbot responses recognise explicit red flags without indiscriminately escalating every case. **[UNVERIFIED]**
- **Evidence:** permitted interviews with 5–8 clinicians/developers, documentation of their existing review procedures, and a timed baseline review exercise.
- The README contains claims about Thai model performance, but those are background leads—not independently verified evidence for the proposal. Do not repeat its numerical claims as established facts. [P3]

**Differentiation:** this is neither synthetic-EMR extraction nor a patient-facing chatbot. The product is an evaluation workflow, with clinician review and reporting.

### Data

**Planned original benchmark:**

- **150 independently specified scenario families**, restricted to adult chest-pain and breathing-difficulty messages.
- Three Thai language variants each: **450 prompts**.
- Split by scenario family: 50 development, 20 validation, 80 locked test.
- Locked test: 40 explicit-red-flag families, 20 clinician-agreed non-emergency examples and 20 insufficient-information families.
- Two emergency/family physicians independently label expected response properties; a third adjudicates. Ambiguous examples may remain explicitly ambiguous rather than being forced into a fabricated ground truth.

**Access/licence:** original prompts, rubrics and agreed labels released under CC BY 4.0 with author agreement. Do not copy proprietary triage scales or commercial benchmark questions.

**Model dependency:** one accessible local model, such as Qwen3-4B, is sufficient for comparing unstructured prompting, structured prompting and a deterministic safe-response baseline. Model revision/licence confirmation is **[UNVERIFIED]**. [E2] Adding multiple commercial APIs is optional, subject to budget and output-use terms.

**IRB:** obtain determination for fictional materials and approval for clinician/user research. No real symptom messages are collected.

### MVP and evaluation

**Build:**

- Import responses, display prompt/output pairs, apply a checklist, allow blinded clinician review and export a versioned report.
- Automatic flags cover explicit escalation, unsupported reassurance, missing-information handling and unsupported claims.
- A model-assisted flag is never treated as ground truth.
- Separate false negatives, unnecessary escalation and abstention; do not collapse everything into one “safety score.”

**Technical evaluation:**

- Clinicians independently review **at least 200 stratified outputs**, including outputs from every tested condition.
- Measure automatic-flag sensitivity/PPV against adjudicated review, inter-rater agreement, review coverage and failure rates by scenario family.
- Target: **≥90% sensitivity and ≥80% PPV for the predefined critical-failure flag**, with confidence intervals.
- Compare automatic methods with simple keyword/rule baselines.
- Analyse uncertainty at scenario-family level; 450 paraphrases are not 450 independent clinical situations.

**User evaluation:**

- **8 clinician/developer reviewers**, counterbalanced manual spreadsheet versus workbench review.
- Targets: **≥30% reduction in review time**, no material loss of adjudicated failure detection, SUS ≥75.
- Record whether a collaborating group actually adopts the report format for teaching or internal model evaluation.

### Committee roast

1. Who needs another benchmark rather than a clinical application?
2. Who says your expected escalation labels are correct?
3. Why does “send everyone to emergency” not win?
4. How do you prevent synthetic-case and verifier bias?
5. What healthcare benefit can you claim without patient outcomes?

**Most damaging attack:** “This is a research benchmark dressed up as a professional capstone.”

**Best honest answer:** “The deliverable is a working review and reporting workflow for a named evaluation owner, with measured task performance. The challenge set supports that workflow. I claim feasibility of structured review—not certification, representative population accuracy or improved patient outcomes.”

### Fit

- **Clinical advisor:** emergency or family medicine with education/digital-health interest.
- **Engineering co-advisor:** NLP evaluation, human-in-the-loop tools or software testing.
- **Recruitment case:** the student can demonstrate a ten-scenario mock-up and ask for a finite rubric-review commitment without requesting hospital access. Whether a group wants to own the tool is **[UNVERIFIED]**.
- **Maintenance:** versioned cases, model settings and reviewer decisions; no continuously available production service required.

### Verdict

**P(approved): 76%; P(finished | approved): 84%; P(both): 64%. [UNVERIFIED]**

**Main risk:** the stakeholder is interested academically but has no recurring review task.

**Socrates’ decisive assumption:** *A local group will use a testing workflow, not merely praise the idea of safer chatbots.* Obtain that commitment before expanding the benchmark.

---

## #4 — Smartphone Video Review of Observable Pressurised Metered-Dose Inhaler–Spacer Steps: A Healthy-Volunteer Feasibility Study

**Pitch — two sentences.** Build a video-review prototype that identifies three externally observable actions in a standardised placebo inhaler-and-spacer demonstration and highlights the corresponding timestamps. It supports educators reviewing demonstrations; it does not infer inhalation flow, lung deposition, symptom control or complete inhaler competence.

### Local problem and users

- **Users:** respiratory nurses, pharmacists and physicians teaching inhaler technique.
- **Owner:** respiratory/pharmacy education group.
- **Local hypothesis:** repeated review of demonstration videos is time-consuming, and observable sequence mistakes could be highlighted automatically. **[UNVERIFIED]**
- **Evidence:** permitted interviews with 5–8 educators and observation of their review of staged demonstrations.
- Device-specific technique and training relevance can be grounded in respiratory guidance, but those sources do not establish local workload or validate computer vision. [E7]

**Differentiation:** last year’s hand-exercise pose project concerned rehabilitation movement classification; this project evaluates a narrow medication-device teaching workflow, with an explicit observability limit. [P2]

### Data

**Planned original, non-patient collection:**

- **30 healthy adult volunteers × 8 scripted clips = 240 clips**.
- Use a **placebo/demo pMDI**, one spacer type and no medication delivery.
- Four correct-sequence variants and four deliberately incorrect demonstrations per participant.
- Actor-disjoint split: 18 training, 6 validation, 6 test participants—144/48/48 clips.
- Two educators independently annotate visible steps and timestamps.

**Access/licence:** there is no assumed public training dataset. Videos are identifiable research data, stored encrypted with access restricted to the approved team; they are **not open-licensed by default**. Any public release needs separate explicit consent. Landmarks are not automatically anonymous.

**Prerequisites:** obtain a demo device, spacer and a clinician-approved filming protocol. Availability/cost is **[UNVERIFIED]** and must be resolved before proposal submission.

**IRB:** prospective healthy-volunteer video research and the educator study require institutional review.

### MVP and evaluation

**Observable scope:** shaking before assembly, attaching the inhaler to the spacer, and bringing the assembled spacer to the mouth in the specified sequence. Do not claim reliable assessment of mouth seal, inhalation, breath-holding or drug delivery.

**Build:**

- Smartphone video upload; visible-action timeline; evidence clips; “cannot assess” option.
- Pretrained hand/pose features plus a small device detector and temporal classifier.
- Compare with simple motion/sequence rules.
- No real-time coaching requirement; offline review is adequate.

**Technical evaluation:**

- Participant-disjoint evaluation, with an additional changed-background/lighting recording condition.
- Metrics: step-level macro-F1, missed incorrect-step rate, falsely accepted sequences, abstention and timestamp error.
- Proposed targets: **macro-F1 ≥0.85**, incorrect-step sensitivity ≥0.90 and falsely accepted sequences ≤5%.
- Confidence intervals must reflect the small number of independent test actors. Passing these targets would not establish clinical safety.

**User evaluation:**

- **10 educators**, 20 counterbalanced clips each, manual video review versus assisted review.
- Targets: **≥25% faster review**, no reduction in error detection, SUS ≥75.
- Report failures caused by occlusion and whether educators actually find the highlighted clips useful.

### Committee roast

1. Can a camera assess an effective inhalation?
2. Are you measuring technique or merely recognising scripted gestures?
3. Will it work with another inhaler or spacer?
4. Why do you need AI for three actions?
5. Why collect healthy-volunteer videos rather than evaluate patients?

**Most damaging attack:** “Your green tick could falsely reassure someone who is using the inhaler ineffectively.”

**Best honest answer:** “There is no overall competence green tick. The interface reports only three observable actions, shows the evidence and labels unobservable components as unassessed. This is an educator-review feasibility study; patient coaching and complete technique validation are explicitly excluded.”

### Fit

- **Clinical advisor:** pulmonology, respiratory nursing or a pharmacist experienced in inhaler education.
- **Engineering co-advisor:** computer vision/video modelling and human-centred interfaces.
- **Recruitment case:** a concrete demo device and eight scripted clips make the ask understandable; no patient recruitment or clinic access is needed. Willingness to supervise a deliberately narrow tool is **[UNVERIFIED]**.
- **Maintenance owner:** the educator maintains the supported device and teaching protocol; other devices remain unsupported.

### Verdict

**P(approved): 74%; P(finished | approved): 76%; P(both): 56%. [UNVERIFIED]**

**Main risk:** the clinically important errors are not sufficiently observable, leaving a technically successful but low-value tool.

**Socrates’ decisive assumption:** *The three visible actions are worth automating for educators.* Have educators inspect staged clips before committing to collection.

---

## #5 — Development of an ECG Artifact-Recognition Training Prototype Using Public Signals and Controlled Noise

**Pitch — two sentences.** Build a waveform viewer that flags possible recording artifact, displays uncertainty and lets learners compare clean and deliberately corrupted ECG segments. Evaluate artifact detection and clinician use of the training interface, without claiming arrhythmia diagnosis, signal restoration or readiness for Thai clinical deployment.

### Local problem and users

- **Users:** junior doctors, nurses and ECG educators.
- **Owner:** an ECG teaching or clinical-skills group.
- **Local hypothesis:** learners would benefit from structured exposure to artifact and from seeing why an automated quality flag can be wrong. **[UNVERIFIED]**
- **Evidence:** permitted interviews with 5–8 educators, an inventory of existing training materials, and a non-patient baseline exercise.
- PhysioNet provides ECG and noise resources specifically suitable for reproducible signal experiments; it does not establish Thai transportability. [E8–E9]

**Why digital:** adjustable noise and paired waveform comparison are difficult to reproduce consistently in static teaching materials. The AI component must still outperform or complement simple signal-quality rules.

### Data

**Public sources:**

1. **MIT-BIH Arrhythmia Database v1.0.0:** 48 approximately half-hour, two-channel recordings from 47 subjects. The PhysioNet release lists **Open Data Commons Attribution License v1.0**. [E8]
2. **MIT-BIH Noise Stress Test Database v1.0.0:** 12 approximately half-hour noise-contaminated ECG records plus three approximately half-hour noise recordings. It also lists **Open Data Commons Attribution License v1.0**. [E9]

Both are publicly downloadable without the credentialing required for some other PhysioNet collections; exact access and release terms must be reconfirmed. **[UNVERIFIED—current access/licence check]**

**Planned derived corpus:**

- Select 100 non-overlapping ten-second windows per arrhythmia recording: **4,800 source windows**.
- Generate two prespecified noise conditions per window: **9,600 derived windows**, or 14,400 windows total.
- Split source subjects before augmentation; all versions of a waveform remain in one partition.
- Partition noise recordings into disjoint time blocks with guard gaps. This prevents direct window reuse, but does **not** create independent noise donors.
- Exclude records 118/119 from training if their Noise Stress Test versions are used as a challenge set; those challenge signals are not an independent external population.

**IRB:** seek determination for public deidentified secondary data; clinician annotation and user testing are separate human-participant activities requiring review.

### MVP and evaluation

**Build:**

- Waveform viewer with adjustable corruption, artifact flags, uncertainty and paired original/corrupted display.
- Compare signal-quality rules, a feature-based classifier and one small 1D CNN.
- No denoising and no “normal ECG” output.

**Technical evaluation:**

- Two clinicians annotate **240 stratified held-out segments** as acceptable for the defined teaching task, artifact requiring review, or uncertain; adjudicate disagreement.
- Separate known injected-noise labels from clinician judgments of interpretability. Signal-to-noise ratio alone is not a clinical-quality label.
- Metrics: sensitivity/specificity for adjudicated artifact, AUROC, abstention, performance by noise type and false flags on genuine rhythm abnormalities.
- Targets: **≥90% artifact sensitivity at ≥80% specificity**, with subject-clustered uncertainty.
- Report how many segments clinicians cannot confidently label. Do not silently discard the difficult cases.

**User evaluation:**

- **10 junior clinicians/ECG educators**, counterbalanced prototype versus a static teaching guide.
- Targets: ≥80% successful completion of predefined comparison tasks, SUS ≥75 and no increase in mistaking genuine abnormal rhythms for artifact.
- Any learning-effect estimate is exploratory; the study is not powered to demonstrate clinical competence.

### Committee roast

1. Why should old US two-lead ECG data apply to Thai 12-lead acquisition?
2. Are you detecting your noise-generation recipe?
3. What happens when an arrhythmia resembles artifact?
4. Why are ordinary signal-quality indices insufficient?
5. Where is the practical implementation without access to an ECG service?

**Most damaging attack:** “Your headline performance could be excellent on injected noise and irrelevant to real recordings.”

**Best honest answer:** “That is why the accepted scope must be a reproducible training prototype, not a clinical acquisition gatekeeper. Clinicians judge a held-out sample, genuine abnormalities are analysed separately, and failure to generalise beyond controlled corruption is a central limitation—not hidden behind AUROC.”

### Fit

- **Clinical advisor:** cardiology, emergency medicine or an ECG educator.
- **Engineering co-advisor:** biomedical signal processing with ordinary ML experience.
- **Recruitment case:** all primary signals are already public and the prototype can be demonstrated without purchasing an ECG device. Finding an advisor willing to accept the educational—not deployment—scope remains **[UNVERIFIED]**.
- **Maintenance owner:** teaching group; handover includes reproducible preprocessing, source attribution and fixed demonstration cases.

### Verdict

**P(approved): 68%; P(finished | approved): 79%; P(both): 54%. [UNVERIFIED]**

**Main risk:** the educational framing may look like a retreat from an inadequately validated clinical classifier.

**Socrates’ decisive assumption:** *An ECG educator wants controlled artifact exploration enough to adopt the prototype.* Without that, it is another public-dataset classification exercise.

---

## Immediate execution plan

| Deadline | Required output | Stop/go question |
|---|---|---|
| Within 48 hours | One-page brief for #1; short recruitment message; mock interface using wholly fictional examples | Can potential advisors understand the owner, task and evaluation immediately? |
| By day 7 | Advisor discussions, stakeholder commitment, ethics-route enquiry, documented comparator and bounded scope | Is there a genuine task worth improving, and can research proceed without a site? |
| By day 10 | Main/co-advisor agreement; feasible dataset protocol; PRD; risk register; conference options | Are recruitment, review effort and governance realistic? |
| Before the one-week email deadline | Full proposal, evaluation table, mock demonstration, timeline and explicit exclusions | Is every promised outcome measurable with accessible resources? |
| Months 1–2 after approval | Ethics clearance as required; needs assessment; dataset and baseline pilot | Does baseline evidence support continuing? |
| Months 3–5 | Frozen test set; evaluation-ready prototype; usability pilot | Is the product ready to test without further architecture expansion? |
| Months 6–7 | Main evaluation; conference submission/presentation as scheduled | Is there enough time for the actual required presentation? |
| Months 8–9 | Analysis, handover, report and final examination | Can the contribution be defended without clinical-benefit overclaims? |

**The decisive council conclusion:** an external clinician collaborator can supply expertise and users, but cannot substitute for a project owner. Do not choose the most exciting model and then search for someone willing to endorse it.

## Sources

### Inlined programme and repository evidence

- **[P1]** `v9_programme_requirements.md`: professional-track requirements, stakeholder collaboration, prototype validation, proposal contents, examination arrangements and conference presentation.
- **[P2]** `capstone_2568_catalogue.md`: supplied abstract catalogue and pattern analysis. It describes projects and reported results, not independently verified approval decisions.
- **[P3]** `README.md` and `council_v9_committee_roast/brief.md`: student history, earlier ideas, hardware and current access/advisor constraints. Landscape claims in the README require independent verification.

### External sources and dependencies

- **[E1]** WHO, **Medication Without Harm** initiative: <https://www.who.int/initiatives/medication-without-harm>
- **[E2]** Qwen, **Qwen3-4B model card**, including listed licence: <https://huggingface.co/Qwen/Qwen3-4B>
- **[E3]** CDC, **Responding to HBV Exposures in Health Care Settings**: <https://www.cdc.gov/hepatitis-b/hcp/infection-control/index.html>
- **[E4]** CDC, **Guidelines for Health Care Personnel Exposed to Hepatitis C Virus**: <https://www.cdc.gov/hepatitis-c/hcp/infection-control/index.html>
- **[E5]** CDC, **HIV Nexus: Clinical Guidance for PEP**: <https://www.cdc.gov/hivnexus/hcp/pep/index.html>. This is a starting resource, **not a substitute for pinning the appropriate current occupational-exposure guideline**; occupational scope and Thai applicability remain **[UNVERIFIED]**.
- **[E6]** CDC, **Use of Agency Materials**: <https://www.cdc.gov/other/agencymaterials.html>. Confirm conditions for each selected item; third-party exceptions matter.
- **[E7]** Global Initiative for Asthma, **strategy and summary reports**: <https://ginasthma.org/reports/>. Current edition, device-specific instructions and permitted reuse must be confirmed; no permission to train on copyrighted videos is assumed.
- **[E8]** PhysioNet, **MIT-BIH Arrhythmia Database v1.0.0**: <https://physionet.org/content/mitdb/1.0.0/>; Moody and Mark, “The impact of the MIT-BIH Arrhythmia Database,” *IEEE Engineering in Medicine and Biology Magazine*, 2001.
- **[E9]** PhysioNet, **MIT-BIH Noise Stress Test Database v1.0.0**: <https://physionet.org/content/nstdb/1.0.0/>; Moody, Muldrow and Mark, “A noise stress test for arrhythmia detectors,” *Computers in Cardiology*, 1984.

If I were the student I'd pick #1  
It offers the clearest route to a useful, clinician-owned prototype and honest workflow evaluation without hospital access, expensive training or unresolved clinical deployment.

## GEMINI (gemini-4-argon): Round 1

## Part A: What This Committee Rewards and Punishes

Judging by the AY 2568 catalogue (`capstone_2568_catalogue.md`) and programme requirements (`v9_programme_requirements.md`), this is a **Plan 2 professional product-and-workflow committee**, not an ML research panel.

**What they reward:**
* **Tangible, workflow-integrated prototypes:** ~60% of passing projects shipped a usable UI (LINE OA, web app, Retool) alongside a model.
* **Thai healthcare contextualisation:** Grounding in local bottlenecks (community hospital load, Thai language/terminology, PDPA, specialist scarcity) (#6, #9, #18, #33).
* **Rigorous, honest validation over big data:** Tiny test sets ($N=4$ to $60$ clinicians or cases) and negative results ($22\%$ accuracy in #17; $\kappa=0.083$ in #15) pass easily if analysed transparently. Measuring time saved, SUS/TAM, or clinician agreement (#4, #6, #11, #33) distinguishes top work.

**What they punish:**
* **Abstract ML theory without a user journey:** Pure algorithmic novelty (e.g., standalone RSI or JEPA) fails the IS I/II mandate for "practical implementation" and a PRD.
* **IRB/data deadlocks:** Proposing retrospective hospital EMR studies in November with no site access guarantees failure to finish by Month 9.

---

## Part B: Five Approvable, Deliverable Capstone Proposals

### 1. ThaiLab-LOINC: Automated Mapping and Confidence-Tiered Verification of Thai Hospital Laboratory Tests to LOINC
* **2-Sentence Pitch:** An embedding- and LLM-powered web workstation that automatically maps messy, non-standardised Thai hospital laboratory test names, specimens, and units to international LOINC codes. It provides confidence-tiered triage and an audit UI so hospital IT and laboratory staff can rapidly standardise data for national health information exchange.
* **Local Problem & Users:** Thai hospitals use bespoke local laboratory codes and free-text names in their LIS, blocking Health Link interoperability, Mor Prom integration, and multi-site OMOP CDM research. Users are hospital lab informaticists and health IT staff. *Non-hospital evidence:* Survey 10–15 doctors/IT staff from the MSc cohort on LIS mapping pain points; cite public Ministry of Public Health (MOPH) and Thai Medical Laboratory Terminology (TMLT) interoperability standards.
* **Data:** 
  * Public LOINC database (Regenstrief Institute, ~100,000 terms, free open licence for research/terminology mapping).
  * Public Thai MOPH / TMLT standard lab dictionaries and National Health Security Office (NHSO/สปสช.) public reimbursement lab schedules (~2,000–5,000 public items).
  * Synthetic/crowd-sourced "noisy" hospital lab catalog: 500 messy lab strings (abbreviations, unit mismatches, typos) generated with input from 5 physician classmates. 
  * *IRB:* Exempt (public reference terminologies and non-patient technical survey).
* **MVP & Evaluation:**
  * *Model:* Hybrid retrieval (multilingual SapBERT / BGE-M3 embeddings over the 6-axis LOINC hierarchy) + local Qwen3-4B / MedGemma-4B cross-encoder reranker with unit-compatibility rule checks (trained/run on the RTX 4090).
  * *Prototype:* Next.js/Streamlit batch-mapping web app with HIGH/MED/LOW confidence tiers (mirroring #9/#33's winning design).
  * *Validation:* Technical Hits@1, Hits@5, and MRR on 500 held-out TMLT-to-LOINC pairs; calibration of confidence tiers; blind audit + timing + SUS/TAM study with $N=5$ pathology/lab staff or physicians comparing manual LOINC search vs. tool-assisted mapping (success criteria: Hits@5 $\ge 85\%$, mapping time reduced $\ge 50\%$, SUS $\ge 70$).
* **Committee Roast:**
  1. *How is this different from last year's TMT-to-RxNorm projects (#9 and #33)?*
  2. *Why not just use TMLT directly instead of LOINC?*
  3. *How does your model avoid mapping a serum glucose test to a urine glucose test or mismatching $\text{mg/dL}$ with $\text{mmol/L}$?*
  4. *Where do you get real messy hospital LIS strings without hospital access?*
  5. *Who maintains this when Regenstrief updates LOINC twice a year?*
  * *Most damaging attack:* "You are just copying last year's TMT drug mapping capstone (#9/#33) and swapping drugs for labs."
  * *Best honest answer:* "Drugs (TMT) match on ingredient and strength, whereas labs fail on 6 compositional axes—analyte, system/specimen, scale, method, time aspect, and quantitative units ($\text{mg/dL}$ vs $\text{mmol/L}$). Furthermore, many rural hospitals lack TMLT mappings entirely. We solve a distinct multi-axial unit-conversion and specimen-disambiguation problem using a local LLM reranker, filling the second major pillar of Chula's OMOP/HealthIT curriculum."
* **Fit:** Clinical Pathology / Lab Medicine faculty (or Biomedical Informatics lecturer teaching the programme's Health IT & Data Standards module) + Computer Engineering NLP co-advisor. Highly plausible to recruit in 2 weeks because the faculty who advised #9/#33 already value terminology mapping and understand the exact thesis template.
* **Verdict:** $P(\text{approved}) = 0.92$, $P(\text{finished}) = 0.90$. *Main risk:* Being viewed as methodologically incremental relative to #9/#33 if the 6-axis lab/unit disambiguation isn't emphasised.

---

### 2. DischargeClear: Hallucination-Guarded Thai Patient After-Visit Summary and Bilingual Care-Plan Generator
* **2-Sentence Pitch:** A clinician-in-the-loop web application that converts English/Thai mixed medical discharge notes ("Tinglish") into structured, plain-Thai patient instructions with automated visual medication schedules and disease-specific red-flag warnings. It uses a deterministic dual-verifier guard to guarantee zero hallucinated drug doses or omitted emergency return precautions before printing/LINE export.
* **Local Problem & Users:** Thai physicians write inpatient discharge summaries and OPD notes in heavily abbreviated English/Thai ("pt dx CHF, f/u 2 wk, Lasix 40mg 1x1 pc"), while patients receive rushed verbal instructions, leading to dosing errors and preventable readmissions. Users are junior doctors/interns, ward nurses, and patients/caregivers. *Non-hospital evidence:* Time-motion self-audit and survey of 15 physician classmates on discharge counselling time; review of public Thai healthcare literacy literature.
* **Data:**
  * Public clinical cases: MIMIC-IV-Note de-identified discharge summaries (PhysioNet credentialed access; or public MedQA / PubMed Central open-access case reports if credentialing takes >2 weeks) + 100 physician-authored synthetic "Tinglish" OPD/discharge notes written by the student and 3–5 physician colleagues (mirroring #1, #17, and #21).
  * Public Thai FDA / MOPH rational drug use (RDU) patient information leaflets for ground-truth RAG.
  * *IRB:* Expedited/Exempt (synthetic notes + clinician usability study on non-patient data).
* **MVP & Evaluation:**
  * *Model:* Local Qwen3-4B / Typhoon-Med fine-tuned/prompted on the RTX 4090 with a **dual-verifier neuro-symbolic guardrail** (entity/dose regex + NLI entailment check against the source note and MOPH RDU database—re-homing the student's v3–v8 verifier work into a concrete product).
  * *Prototype:* Split-screen web app + printable PDF / LINE Flex Message patient card showing diagnosis in plain Thai, visual pill timetable (เช้า/กลางวัน/เย็น/ก่อนนอน), and 1669 red flags.
  * *Validation:* Automated verifier catch-rate on 200 injected dose/contraindication errors; blinded rating by $N=6$ physicians on 50 generated summaries for clinical safety, zero critical dose errors, readability, time saved, and SUS (success criteria: $100\%$ dose fidelity, $<2\text{ min}$ review time, SUS $\ge 75$).
* **Committee Roast:**
  1. *Last year's EMR LLM projects (#1 NIHSS, #17 TOAST) collapsed on real clinical notes ($22\%$ accuracy). Why won't yours?*
  2. *What happens if the LLM hallucinates a drug dose or tells a heart failure patient to drink plenty of water?*
  3. *Why can't the hospital HIS just print standard pre-written disease leaflets?*
  4. *Can elderly Thai patients actually read or use the output?*
  5. *How will you evaluate this without real patients?*
  * *Most damaging attack:* "If your LLM hallucinates a medication dose or misses a critical warning, a patient gets harmed—you have no clinical validation on real patients."
  * *Best honest answer:* "Unlike free-form generation, DischargeClear is a **clinician-in-the-loop drafting tool** with a hard deterministic verifier: medication names, numbers, and frequencies are extracted structurally and locked against the clinician's input; the LLM only translates medical jargon and formats the layout, and the physician signs off on a highlighted diff view before the patient ever sees it."
* **Fit:** Internal Medicine / Family Medicine / Emergency Medicine advisor + NLP/Software Engineering co-advisor. Very easy to recruit in 2 weeks because every clinical faculty member experiences the pain of poor patient discharge comprehension daily.
* **Verdict:** $P(\text{approved}) = 0.88$, $P(\text{finished}) = 0.88$. *Main risk:* Scope creep if trying to cover all medical specialties instead of bounding scope to 5 high-volume NCD/acute conditions (e.g., CHF, DM, HT, COPD, DHF).

---

### 3. TriageGuard-1669: A Neuro-Symbolic Safety Harness and Triage Copilot for Thai Primary-Care Tele-Triage
* **2-Sentence Pitch:** A safety-verified symptom triage copilot for Thai tele-health nurses and primary-care lines that pairs a Thai medical LLM with a deterministic MOPH/ESI red-flag verifier. It benchmarks existing Thai medical LLMs on critical safety failures and delivers an interactive triage dashboard that prevents dangerous under-triage.
* **Local Problem & Users:** Tele-triage nurses (e.g., NHSO 1330, EMS 1669, and hospital LINE OA pre-screeners) face high call volumes and inconsistent escalation of life-threatening red flags, while newly released Thai medical LLMs (`ThaiLLM-27B-Prescreen`, `tma1-medgemma-4b`) have zero independent clinical safety audits (`README.md`). Users are triage nurses, general practitioners, and digital health teams deploying chatbots. *Non-hospital evidence:* Public National Institute for Emergency Medicine (NIEM / สพฉ. 1669) annual reports on under-/over-triage rates; workflow interviews with 5 ER/OPD physicians or nurses.
* **Data:**
  * Public NIEM (1669) Emergency Medical Triage Protocol & CBD (Criteria-Based Dispatch) manuals (publicly downloadable PDFs in Thai).
  * 300 structured synthetic Thai clinical vignettes covering 25 chief complaints (chest pain, dyspnoea, febrile infant, stroke mimics, DHF) co-validated by 3 practising physicians, plus translated public benchmark subsets (e.g., HealthBench / MedQA triage items).
  * *IRB:* Exempt/Expedited (public protocols + clinician vignette evaluation, zero patient data).
* **MVP & Evaluation:**
  * *Model:* Audit of 4 open weights models (`pai1-medgemma-4b`, `EIRAI-8B`, `ThaiLLM-8B-MedApp`, `Qwen3-4B`) on the RTX 4090, followed by a neuro-symbolic guard + GRPO/QLoRA fine-tuned 4B copilot that enforces mandatory red-flag checklists before allowing "Observe at Home" recommendations (preserving the student's existing `README.md` research).
  * *Prototype:* Nurse/GP triage web dashboard showing live symptom checklist extraction, rule-verified ESI/1669 triage tier, and cited MOPH guideline rationale.
  * *Validation:* Under-triage rate (target $<2\%$ on red-flag cases) and over-triage rate across models; randomised crossover vignette study with $N=6$ GPs/ER nurses comparing triage accuracy and decision time with vs. without TriageGuard-1669, plus SUS.
* **Committee Roast:**
  1. *Is this an academic benchmark paper or a healthcare product? This is a Plan 2 professional degree.*
  2. *Who is the actual user—the patient at home or the triage nurse?*
  3. *If you use a deterministic rule checker for red flags, why do you need an LLM at all?*
  4. *Does a patient-facing or triage tool require Thai FDA (อย.) Software as a Medical Device (SaMD) approval?*
  5. *How do you know your 300 synthetic vignettes reflect real Thai callers?*
  * *Most damaging attack:* "You are pitching an AI safety benchmark paper disguised as a product; if deterministic rules catch the red flags, the LLM is redundant, and if the LLM makes the decision, it's an unregulated medical device."
  * *Best honest answer:* "The product is a **Clinician Decision Support System (CDSS) for triage staff**, not an autonomous patient chatbot—exempting it from autonomous SaMD risk while solving a real bottleneck: patients describe symptoms in messy, colloquial Thai dialects that rigid rule-trees cannot parse. The LLM translates colloquial patient complaints into structured clinical findings, while the deterministic NIEM-1669 rule engine makes the final safety-critical triage call."
* **Fit:** Emergency Medicine / Family Medicine advisor + Computer Engineering (LLM/NLP) co-advisor. Plausible in 2 weeks because the student already has the technical background (`README.md`) and ER faculty are keen on 1669/triage standardisation.
* **Verdict:** $P(\text{approved}) = 0.82$, $P(\text{finished}) = 0.85$. *Main risk:* If pitched as "audit-first + RSI self-play" (`README.md`), the committee will reject it as too theoretical; it **must** be pitched as a nurse/GP triage CDSS product where the audit is just the baseline evaluation.

---

### 4. ClaimsReady-TH: Pre-Audit DRG Coding & Summary Discharge Note Completeness Assistant for Public Hospital Interns
* **2-Sentence Pitch:** A web-based clinical documentation integrity (CDI) copilot that scans draft inpatient discharge summaries against Thai Diagnosis Related Group (TDRG v6) and ICD-10-TM criteria to flag missing complication/comorbidity (CC/MCC) justifications before chart sign-off. It reduces medical coder back-and-forth queries and protects public hospitals from NHSO reimbursement clawbacks.
* **Local Problem & Users:** In Thai public hospitals, overworked interns write incomplete discharge summaries (e.g., prescribing IV potassium or antibiotics without documenting "hypokalaemia" or "sepsis" in the final diagnosis list), causing massive delays for medical coders and millions of Baht in lost NHSO/SSO DRG reimbursement or audit clawbacks. Users are junior doctors (interns/residents) and hospital medical coders/auditors. *Non-hospital evidence:* Public NHSO (สปสช.) / Central Office for Healthcare Information (CHI) reports on DRG audit deductions; interviews with 5 hospital physicians/coders on chart-query friction.
* **Data:**
  * Public ICD-10-TM and Thai DRG (TDRG v6.x) manuals and relative weight (RW) tables published by CHI / MOPH.
  * MIMIC-IV-Note discharge summaries paired with ICD codes (PhysioNet) + 100 synthetic Thai/English inpatient summary charts containing deliberate documentation-lab/medication mismatches authored by the student (a practising physician).
  * *IRB:* Exempt (public coding standards + synthetic charts + physician/coder usability study).
* **MVP & Evaluation:**
  * *Model:* Structured clinical entity extractor (medications, abnormal labs, procedures) + RAG over TDRG/ICD-10-TM audit rules using local Qwen3-4B / MedGemma-4B on the RTX 4090 to detect undocumented diagnoses supported by clinical evidence (and flag unsupported diagnoses that risk NHSO audit rejection).
  * *Prototype:* Web IDE where an intern pastes a draft discharge note + lab/med list and receives instant, clickable "Documentation Gap Alerts" (e.g., *"KCl prescribed & K+ 2.8 noted, but E87.6 Hypokalaemia missing from Secondary Dx — est. RW impact +0.4"*).
  * *Validation:* Precision, recall, and F1 of gap detection on 100 synthetic charts with known audit defects; user evaluation with $N=6$ physicians/medical coders measuring ICD completeness, simulated RW recovery, chart review time, and SUS.
* **Committee Roast:**
  1. *Is this tool encouraging illegal "upcoding" to game NHSO reimbursement?*
  2. *How can you build or test a Thai DRG tool without real Chula hospital billing data?*
  3. *Hospital EMRs are closed systems; how would an intern actually use a standalone web app without violating PDPA?*
  4. *Medical coders follow thousands of complex ICD-10-TM rules; how many rules are actually in your MVP?*
  5. *Why not just train interns better on ICD coding?*
  * *Most damaging attack:* "Without real hospital billing records and coder audit logs, your synthetic test cases are just toy examples that you wrote yourself to make your model look good."
  * *Best honest answer:* "To prevent circular evaluation, we scope the MVP to the top 20 high-volume Internal Medicine diagnoses and have **independent hospital medical coders/physicians outside the development process** construct and grade the held-out evaluation cases based on official CHI/NHSO audit rejection criteria, while framing the tool strictly around *audit-defensible documentation completeness* (requiring lab/treatment evidence in the note) rather than upcoding."
* **Fit:** Health Systems / Hospital Management / Medical Informatics clinical advisor (e.g., instructors from the *Data Science for Hospital Operations* or *Health IT & Reimbursement* courses) + Computer Engineering co-advisor. Very fast to recruit because reimbursement and hospital operations are core programme modules.
* **Verdict:** $P(\text{approved}) = 0.80$, $P(\text{finished}) = 0.82$. *Main risk:* The student previously disliked "safe admin/claims ideas" (`README.md`), which could hurt motivation, and examiners may press hard on synthetic billing validation.

---

### 5. ReCheck-CDSS: Uncertainty-Aware Clinical Calculator and Repeat-Testing Advisor for Borderline Lab Decisions
* **2-Sentence Pitch:** A point-of-care clinical decision support web app that models analytical lab measurement error (CV%) and biological within-subject variation across routine blood tests to warn clinicians when a patient's score crosses a treatment threshold purely due to assay noise. It recommends cost-effective "remeasure vs. treat now" actions for Thai NCD clinics.
* **Local Problem & Users:** Physicians in busy Thai NCD and outpatient clinics treat laboratory numbers (e.g., eGFR $<60$ for CKD staging, HbA1c $\ge 6.5\%$, LDL cutoffs, troponin deltas, INR) as exact truths, ignoring analytical coefficient of variation ($\text{CV}_A$) and biological variation ($\text{CV}_I$). Borderline patients are frequently misclassified or started on lifelong medications unnecessarily. Users are GP/NCD clinic physicians and lab directors. *Non-hospital evidence:* EFLM (European Federation of Clinical Chemistry and Laboratory Medicine) biological variation database, Thai Department of Medical Sciences (DMSc) external quality assessment (EQAS) tolerance limits, and a survey of 10 Thai doctors on reference change value (RCV) awareness.
* **Data:**
  * Public NHANES (CDC National Health and Nutrition Examination Survey, >50,000 patients with repeat lab measurements, free public download) + MIMIC-IV lab tables.
  * Public EFLM Biological Variation Database ($\text{CV}_I$, $\text{CV}_G$ for >300 analytes) and Thai Royal College clinical practice guideline cutoffs (DM, CKD, dyslipidaemia, thyroid).
  * *IRB:* Exempt (100% open public NHANES data + clinician vignette usability study).
* **MVP & Evaluation:**
  * *Model:* Monte Carlo / Bayesian measurement-error propagation + Reference Change Value (RCV) decision-fragility engine + cost-utility threshold optimizer (reshaping the student's *Remeasure Before Acting* concept from `brief.md` into a concrete clinical calculator).
  * *Prototype:* Mobile-responsive web CDSS where a clinician inputs standard NCD panel values (Cr, HbA1c, LDL, TSH, K+) and sees (1) the probability of guideline misclassification due to lab noise, (2) the minimum significant change (RCV) between two visits, and (3) an explicit "Treat Now vs. Repeat Lab in $X$ Weeks" recommendation.
  * *Validation:* Retrospective simulation on NHANES/MIMIC repeat-lab cohorts quantifying false-positive treatment initiation rates avoided; prospective clinical vignette study with $N=8$ Thai GPs/internists evaluating decision change on borderline cases and SUS/TAM.
* **Committee Roast:**
  1. *Where is the "AI" in this project? Isn't propagating lab CV% just basic statistics and Monte Carlo simulation?*
  2. *In a crowded Thai public hospital OPD with 80 patients per morning, no doctor will ask a patient to come back for a repeat blood draw just because of a 15% probability of assay noise.*
  3. *NHANES is American data; how does that apply to Thai patients and Thai hospital lab machines?*
  4. *Does repeating tests increase healthcare costs for the hospital under capitation (30-Baht scheme)?*
  5. *How did last year's lab project (#35 paediatric reference intervals) fare, and how is this different?*
  * *Most damaging attack:* "This is a statistical calculator using American NHANES data, not an AI innovation tailored to Thai hospital workflows—and telling busy Thai OPD doctors to order repeat labs is operationally unrealistic."
  * *Best honest answer:* "Over-diagnosing a borderline patient with lifelong CKD or diabetes costs the 30-Baht capitation system years of unnecessary drugs, clinic visits, and patient anxiety compared to a 40-Baht repeat creatinine or glucose test at their next scheduled visit. We calibrate the analytical noise parameters directly to Thai DMSc EQAS lab standards and add a machine-learned individualized baseline predictor so the tool only flags the ~8% of borderline cases where a repeat test actually changes clinical management."
* **Fit:** Clinical Pathology / Laboratory Medicine or Nephrology/Endocrinology advisor + Data Science / Biostatistics co-advisor. Plausible to recruit within 2 weeks via the Department of Laboratory Medicine or Preventive Medicine.
* **Verdict:** $P(\text{approved}) = 0.72$, $P(\text{finished}) = 0.90$. *Main risk:* Committee members expecting "AI/LLM/Deep Learning" may view Monte Carlo measurement-error propagation as insufficient AI depth unless paired with a learned longitudinal trajectory model.

---

## Summary Comparison

| Rank | Short Title | Core Tech (on RTX 4090) | Data Source (No Hospital IRB) | $P(\text{Approved})$ | $P(\text{Finished})$ |
|---|---|---|---|---|---|
| **#1** | **ThaiLab-LOINC** | SapBERT/BGE-M3 + 4B LLM Reranker + Web UI | Public LOINC + Thai TMLT/NHSO lists | **0.92** | **0.90** |
| **#2** | **DischargeClear** | 4B Thai LLM + Dual-Verifier Guard + LINE/PDF UI | Public cases + synthetic Tinglish notes + RDU | **0.88** | **0.88** |
| **#3** | **TriageGuard-1669** | 4B LLM + Symbolic 1669 Verifier + Triage UI | Public NIEM 1669 protocols + 300 vignettes | **0.82** | **0.85** |
| **#4** | **ClaimsReady-TH** | Entity Extractor + TDRG RAG + CDI Web IDE | Public ICD-10-TM / TDRG manuals + MIMIC/synth | **0.80** | **0.82** |
| **#5** | **ReCheck-CDSS** | Bayesian Noise/RCV + Longitudinal ML + Web App | Public NHANES + EFLM + Thai DMSc EQAS | **0.72** | **0.90** |

**If I were the student I'd pick #2 (DischargeClear) [or #1 if maximising pure approval safety, or #3 if determined to salvage existing triage-verifier work]:** I'd pick **#2 (DischargeClear)** because it directly leverages your unfair advantage as a practising Thai physician who knows real "Tinglish" discharge workflows, requires zero hospital patient data, preserves your frontier dual-verifier neuro-symbolic guardrail idea inside a tangible patient-safety product, and gives the committee an immediately relatable demo that both clinicians and engineers will champion.

---

# ROUND 2 (each model as the proposal committee)

## CLAUDE: Round 2

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

## CODEX (gpt-6.1-sol): Round 2

**Invited examiners:** one clinician and one engineer.  
**Decision basis:** the three Round 1 answers, the brief, programme requirements and catalogue supplied here. No Round 2 answers were read; external sources have not been independently checked.

## Committee’s opening judgement

**None of the six rival top-three proposals passes unchanged.** Several could pass after revision, but each currently depends on an unproven clinical premise, an unavailable reference standard, or an overstated safety claim.

The immediate bottleneck is not GPU capacity. It is **a named stakeholder, an eligible advisor pair, and an evaluation that the available data can actually support**.

Two corrections apply throughout:

- **No patient data does not mean no ethics review.** Clinician interviews, annotation and usability studies require an institutional determination; exemption is not the student’s decision.
- **“Clinician-in-the-loop” does not automatically remove medical-device obligations.** Regulatory treatment depends on intended use, functionality and jurisdiction—not the presence of a disclaimer.

---

## 1. Roast of Claude’s top three

### Claude #1 — Photo-ECG Triage

**Clinician’s hardest question:**  
> “Where are the adjudicated acute STEMI and STEMI-equivalent labels that justify your primary endpoint? A historical myocardial-infarction label is not an acute reperfusion decision.”

**Engineer’s hardest question:**  
> “You have chained photo capture, layout recognition, digitisation and classification. Which component fails first, and how will you measure end-to-end diagnostic performance without confusing successful signal reconstruction with a correct clinical diagnosis?”

**Pass as is? — No. Major revision.**

This is the most compelling demonstration and the least secure clinical endpoint. PTB-XL’s standard MI labels do not establish the proposed acute-STEMI reference standard. Photographs of public ECGs can test capture degradation; they cannot establish Thai population transportability or real emergency performance.

The ≥90% STEMI-sensitivity target therefore precedes proof that the required labelled cases exist. Adding VT, high-grade block and equivalents makes the label problem harder.

**Minimum fix to pass:**

1. First identify an accessible dataset with an adequate, clinically defensible reference standard for **one** target finding.
2. Run a small end-to-end feasibility test before committing to diagnostic classification.
3. If the target labels are unavailable, change the project to **ECG-photo capture-quality and referral preparation**, with clinician interpretation retained. That is a different, narrower product—not a validated STEMI detector.

Commercial prior art must also be compared directly on task, input requirements, availability and workflow. “Thai workflow” alone does not establish a gap.

---

### Claude #2 — Thai CPG-grounded clinical question assistant

**Clinician’s hardest question:**  
> “When a guideline is incomplete, outdated or conditional on information the user has not supplied, what precisely counts as a correct answer—and who adjudicates that?”

**Engineer’s hardest question:**  
> “Does your system outperform searchable PDFs and a well-designed index, or only an ungrounded chatbot?”

**Pass as is? — Not yet. Moderate revision.**

Five disease areas are excessive for a student who must also establish document permissions, create gold answers, recruit reviewers and evaluate users. Citation presence is not citation support. A model can cite the right document while making the wrong recommendation.

The proposed zero high-harm errors is an acceptable observed result to seek, but not evidence of zero underlying risk.

**Minimum fix to pass:**

- Restrict to **one guideline and one recurring question workflow**, selected with a named educator or clinical owner.
- Pin the guideline edition and document reuse permissions.
- Compare against **current guideline lookup**, not just generic ChatGPT.
- Use independently authored held-out questions, including unanswerable and missing-information cases. Grade correctness, actual citation support, harmful error and appropriate abstention separately.

This can be approved as a bounded information-retrieval product. It should not be sold as a general bedside clinical authority.

---

### Claude #3 — Creatinine-variability-aware AKI alert

**Clinician’s hardest question:**  
> “How do you know a suppressed KDIGO alert was a false alarm rather than early true AKI?”

**Engineer’s hardest question:**  
> “What is your independent reference standard? If both the original alert and your outcome are derived from creatinine, you may simply be rewarding disagreement with the rule you chose to modify.”

**Pass as is? — No. Major revision.**

“Fewer false alarms without missing AKI” is not established by reducing alert counts while retaining later creatinine-defined stage ≥2 events. That comparison is useful, but it does not identify true renal injury or prove that delayed recognition is harmless.

MIMIC also cannot automatically supply the assay-specific analytical variation relevant to Thai laboratories. Repeat measurements reflect clinical sampling decisions and changing physiology, not merely measurement noise.

**Minimum fix to pass:**

- Reframe as a **retrospective alert-policy simulation**, not a validated false-positive reducer or repeat-testing recommendation.
- Use explicitly sourced variation assumptions with sensitivity analyses.
- Report alert burden and detection delay against prespecified creatinine-defined outcomes, acknowledging their non-independence.
- Prevent future laboratory values from entering simulated decisions.
- Secure a nephrology owner who agrees that this limited simulation answers a useful question.

Technically feasible; currently weaker on local workflow ownership than on modelling.

---

## 2. Roast of Gemini’s top three

### Gemini #1 — ThaiLab-LOINC

**Clinician’s hardest question:**  
> “When the source name omits specimen, property or method, what makes a proposed LOINC code correct rather than merely plausible?”

**Engineer’s hardest question:**  
> “Show us the 500 verified held-out mappings. Are they an existing authorised resource, an expert-annotation commitment, or a number invented for the proposal?”

**Pass as is? — No. Promising, but data-gated.**

The proposal treats public dictionaries, reimbursement schedules, synthetic strings and gold-standard mappings as interchangeable. They are not. A reimbursement item may not identify a unique laboratory observation.

There is also a technical error in the differentiation argument: LOINC’s six principal axes are **component, property, time, system, scale and method**. Units are valuable compatibility evidence, but are not a seventh substitute axis; convertible units do not necessarily imply different LOINC codes.

The strongest contribution would be **recognising when mapping is underdetermined**, not forcing every string to a code.

**Minimum fix to pass:**

- Pin the exact source releases, access conditions and permitted uses.
- Limit the MVP to a small, coherent laboratory domain.
- Obtain a laboratory specialist’s commitment to independent mapping and adjudication, including **“insufficient information/no unique mapping”** labels.
- Distinguish clean terminology matching from robustness to independently created noisy variants; split by underlying concept before augmentation.
- Compare against manual LOINC search and simple lexical retrieval before adding a generative reranker.

This is the strongest rival alternative **if the reference set and laboratory owner materialise**. They are not yet assets.

---

### Gemini #2 — DischargeClear

**Clinician’s hardest question:**  
> “Who authorised the new red-flag advice? Is the tool translating the clinician’s plan, or adding clinical recommendations that were never documented?”

**Engineer’s hardest question:**  
> “How can a regex-plus-NLI verifier guarantee safety when extraction can be wrong and clinically important meaning includes negation, conditions, timing and omissions?”

**Pass as is? — No. The guarantee must go.**

“Guarantee zero hallucinated doses or omitted return precautions” is indefensible. A verifier can share the generator’s blind spots. Even perfect preservation of extracted numbers does not guarantee faithful medication instructions.

This also combines several products: note interpretation, translation, medication scheduling, warning generation, bilingual output and patient communication. Five disease areas are not a narrow scope. MIMIC, MedQA and case reports are not equivalent replacements for Thai discharge instructions.

**Minimum fix to pass:**

Merge it with Codex’s medication editor and retain the smaller task:

> **Rewrite explicitly supplied medication instructions into clearer Thai, highlight critical-fact discrepancies, and require professional approval.**

Exclude diagnosis inference, added warnings, note extraction, prescribing, patient delivery and claims about patient comprehension. Use original non-patient examples with independent pharmacist review. Compare with reusable templates and ordinary editing.

This preserves the useful insight—**source-bound verification**—without pretending it proves clinical safety.

---

### Gemini #3 — TriageGuard-1669

**Clinician’s hardest question:**  
> “Which service and protocol govern the output? Emergency dispatch, ED triage and a primary-care advice line do not have interchangeable decisions or escalation pathways.”

**Engineer’s hardest question:**  
> “If the LLM fails to extract a red flag, what can your deterministic verifier possibly verify?”

**Pass as is? — No. Major rescoping.**

The proposed rules protect only the facts that reach them. An extraction error can make a dangerous case appear rule-compliant.

ESI, criteria-based dispatch and general tele-triage should not be merged into a supposedly universal “ESI/1669 tier.” The proposed 25 complaints, four-model audit, fine-tuning, GRPO and crossover study are multiple projects. The assertion that clinician-facing CDSS is thereby exempt from SaMD risk is also incorrect.

**Minimum fix to pass:**

- Choose **one service context and one authoritative decision framework**.
- Remove GRPO, mandatory fine-tuning and live triage.
- Restrict to adult chest-pain and breathing-difficulty fictional cases.
- Build an **offline response-review and reporting workbench**, with clinician-adjudicated failure categories.
- Include non-emergency and insufficient-information cases so indiscriminate escalation cannot win.
- Measure reviewer time and failure detection—not prevention of patient harm.

That converges with the more defensible audit-first proposals from Claude and Codex.

---

## 3. Hume audit: the three most load-bearing claims

| Claim | Audit finding | Evidence required before approval |
|---|---|---|
| **1. PTB-XL plus synthetic photographs can support the proposed acute-STEMI triage endpoint.** | **Endpoint mismatch.** Standard PTB-XL MI labels do not establish adjudicated acute STEMI/equivalent diagnoses. Successful digitisation does not repair missing clinical labels. | A label inventory, accessible target-case counts, a defensible reference-standard definition and a patient-disjoint evaluation plan. Otherwise remove the acute-triage claim. |
| **2. A legally usable, gold-labelled Thai laboratory-to-LOINC benchmark is readily available from the named public resources.** | **Unverified.** A public terminology is not a verified crosswalk. The proposed 500 gold mappings have not been demonstrated. LOINC is distributed under its own licence; “free” does not establish unrestricted reuse or redistribution. | Exact releases and terms; sample source records; existing crosswalk provenance or a funded/time-bounded expert annotation commitment. Public availability alone is insufficient. |
| **3. A deterministic/NLI dual verifier can guarantee zero clinically important generation errors.** | **False as stated.** Extraction, semantic interpretation and verification can all fail. Rule completeness is not guaranteed, and clinician sign-off does not prove errors will be caught. | Replace the guarantee with measured error detection, fidelity, abstention and human-review performance on independently authored cases. Report numerators, denominators and uncertainty. |

**Our own proposals do not escape this audit.** The medication editor’s workflow need, the exposure checklist’s incremental value and the testing workbench’s recurring users remain unverified. “We can write synthetic examples” establishes data availability, not product demand.

Also, the catalogue documents abstracts—not examination decisions. Weak published metrics are not evidence that a weak proposal will “pass easily.”

---

## 4. Convergence: signal or shared anchoring?

| Convergent theme | Advisors | Committee interpretation |
|---|---|---|
| Source-bound Thai rewriting with critical-fact checks | Codex medication editor; Gemini DischargeClear | **Useful design signal.** A bounded transformation is easier to specify and evaluate than open-ended medical generation. It is not evidence that users need the tool. |
| Thai chatbot safety evaluation | Claude safety audit; Codex workbench; Gemini TriageGuard | **Strongest thematic convergence, but not independent discovery.** The brief already supplied this direction. The defensible common core is a professional review workflow—not a new autonomous triage model. |
| Laboratory uncertainty and repeat testing | Claude AKI; Gemini ReCheck | **Shared conceptual interest, weak validation signal.** Both inherit the earlier shortlist. Neither solves the problem of distinguishing measurement noise from meaningful physiological change. |
| Public/original data, an ordinary prototype and clinician evaluation | All three | **Real feasibility signal.** It follows directly from the student’s lack of hospital access and the programme’s requirements. |

The advisors are not three independent market studies. They read the same brief, constraints and catalogue.

**The genuine convergence is architectural:** narrow the task, retain human authority, expose uncertainty, and evaluate against current practice. There is no comparable convergence proving demand for a particular product.

---

## 5. Final ranking across all advisors

These are subjective planning estimates for the **revised scopes**, not the original pitches. They assume advisor and stakeholder commitments are secured promptly.

**P(finished)** means **P(completing the agreed prototype, evaluation, report and required conference presentation | approved)**. Low patient-data risk does not mean zero recruitment, ethics or governance risk.

| # | Title | P(approved) | P(finished) | Data/IRB risk | Advisor fit | One-line verdict |
|---|---|---:|---:|---|---|---|
| **1** | **Critical-Fact-Verified Thai Medication Instruction Editor** — Codex + narrowed DischargeClear | **80%** | **88%** | Low data-access risk; professional annotation/user-study review required | Medication-safety pharmacist or physician + NLP/software engineer | Best balance of bounded product, accessible evaluation and clinically meaningful failure analysis—provided templates do not already solve the task. |
| **2** | **Occupational Blood-Exposure Checklist Trainer** — revised Codex | **74%** | **85%** | Low data-access risk; guideline adaptation and clinician-study review remain | Occupational health/ID/infection-control educator + decision-support engineer | Clear simulation task and strong paper-flowchart comparator; needs an owner and pinned, locally acceptable guidance. |
| **3** | **Thai Red-Flag Response Review Workbench** — Codex + Claude + stripped-down TriageGuard | **68%** | **83%** | Low patient-data risk; substantial expert-labelling burden and user-study review | Emergency/family medicine evaluator + NLP evaluation engineer | Best continuity with the student’s earlier interests, but only if someone has a recurring review job for it. |

**First alternate: ThaiLab-LOINC.** It could displace #3 once a laboratory owner, authorised source data and credible reference mappings exist. Today those are critical dependencies, not implementation details.

**Why Photo-ECG does not make the final three:** it couples an attractive clinical story to unresolved target labels and several technical failure points. The student cannot afford to discover at month three that the main endpoint is not measurable.

**Why the original broad DischargeClear and TriageGuard do not rank:** the useful parts survive in the merged projects; the safety guarantees, autonomous clinical implications and training ambitions do not.

---

## 6. Recommendation and the next seven days

### Recommend: the source-bound Thai medication instruction editor

Not a discharge copilot, dose checker, medication reconciler or patient-facing chatbot.

Its defensible claim is:

> “For a specified professional authoring task, the editor improves review efficiency while measuring—and visibly exposing—critical changes relative to supplied instructions.”

The first question is whether that authoring task occurs often enough to matter. If fixed templates already solve it, stop or redirect before building.

### Three required actions

1. **Secure the people and the accepted scope — days 1–2.**  
   Obtain a main-advisor commitment, engineering co-advisor commitment and named pharmacy/medication-education owner. Confirm advisor eligibility and that a non-patient, simulation-based evaluation meets programme expectations. Agree on the examination slots and work backwards from the **proposal-email deadline at least seven days before the exam**.

2. **Establish need, comparator and ethics route — days 2–5.**  
   Request the institutional determination before research recruitment or data collection. Obtain any permitted preliminary workflow consultation; otherwise document it as planned research. Identify the actual authoring task, existing templates, baseline editing process and maintenance owner. Put an explicit stop condition in the proposal: **no recurring burden or no advantage beyond templates means no justification for the original tool**.

3. **Produce a bounded feasibility package — by day 7.**  
   Build a source/rewrite/difference mock-up using original fictional text. Prepare approximately 20 varied instruction pairs, with independent professional review under the applicable ethics route. Demonstrate faithful rewrites, deliberate errors and abstention—not just successful examples. Freeze the MVP exclusions and evaluation comparison, then submit a proposal containing the PRD, ethics plan, risk register, realistic remaining-term timeline and a verified conference option with a backup.

**Final committee advice:** choose the smallest useful task a real professional agrees to own. A verifier is a component to evaluate—not a safety certificate, and not a substitute for a validated problem.

## GEMINI (gemini-4-argon): Round 2

**Examiners on the panel:**
* **Examiner 1 (Clinical):** Senior attending physician at King Chulalongkorn Memorial Hospital; cares about bedside workflow, patient safety, Thai hospital reality, and whether any clinician will actually touch this tool on a Monday morning.
* **Examiner 2 (Engineering):** Faculty from the Department of Computer Engineering; cares about technical depth beyond an API wrapper, evaluation leakage, data licensing, and whether the system can be built and validated before the May final exam.

---

## 1. Roast of the Other Two Advisors' Top-3 Ideas

### A. Roasting Claude's Top 3

#### Claude #1: Photo-ECG Triage (Smartphone photo → digitised signal → STEMI classifier + referral template)
* **The Hardest Question:** *"In real Thai community hospitals, ER doctors send ECG photos over LINE using phones with glare, crumpled thermal paper, skew, and faded gridlines. Signal digitisation from arbitrary smartphone photos was an international research grand challenge in 2024 where top teams still failed on real-world artefacts. If your digitiser misreads a 1-mm ST elevation due to paper curvature or shadow, your downstream 1D-CNN fails catastrophically. Why are you chaining two brittle tasks (2D-to-1D signal reconstruction + classification) instead of solving a bounded problem, and how is a self-printed PTB-XL photo test not a toy setup?"*
* **Would it pass as is?** **Conditional Pass / Revise.** The clinical story (rural ER LINE referral habit) is exceptional—every Thai physician examiner knows this exact workflow. However, the engineering examiner will flag the two-stage digitisation-plus-classification pipeline as high technical risk for a 1-person, 6-month build, and the clinical examiner will challenge the lack of real Thai ECG thermal-paper grid variability (3×4 vs 6×2 layouts, 25 mm/s vs 50 mm/s speeds).
* **Minimum Fix to Pass:**
  1. Drop the claim of full 12-lead voltage-time waveform reconstruction as a hard prerequisite; compare **direct 2D image/VLM classification + lead-bounding-box cropping** against **ECG-Image-Kit digitisation + 1D-CNN**, and add an explicit **Image Quality Gatekeeper (reject/retake prompt for glare, tilt, or missing calibration pulse)** as a primary deliverable.
  2. Print PTB-XL signals onto **actual Thai hospital thermal ECG paper (or exact 1:1 red/pink grid templates across the 3 standard machine layouts used in Thailand: Nihon Kohden, Philips, GE)** and photograph them under a pre-registered matrix of degradations (angle, shadow, LINE image compression).

#### Claude #2: Thai CPG-Grounded Clinical Question Assistant with Citations and Abstention
* **The Hardest Question:** *"Thai Royal College CPGs (e.g., Diabetes, Hypertension, Dengue) are dense, 80-page PDFs filled with complex flowcharts, drug dosing tables, and footnotes. Standard chunk-based text RAG mangles clinical tables and cannot read visual algorithms—which is where 80% of bedside management rules actually live. Without structured knowledge extraction, isn't this just a standard NotebookLM / ChatGPT-with-PDFs wrapper that will fail on the exact multi-step flowchart questions interns actually ask?"*
* **Would it pass as is?** **No (Borderline Reject / Major Revision).** As pitched, it reads like a generic weekend RAG demo with low engineering depth and high risk of failing on table/flowchart queries. It also lacks a clear clinical "implementation owner" beyond "interns in general."
* **Minimum Fix to Pass:**
  1. Convert the core engineering contribution from "vanilla text RAG" to **Table- & Flowchart-Aware Structured CPG Grounding** (parsing guideline algorithms into explicit JSON decision trees + hybrid retrieval over text and tables, paired with a deterministic NLI citation/abstention verifier).
  2. Bound the scope to **one specific clinical rotation or setting** (e.g., Pre-internship / Rural GP NCD & Acute Fever Orientation) with a named clinical faculty educator as stakeholder.

#### Claude #3: Creatinine-Variability-Aware AKI Alert ("Remeasure Before Acting" on MIMIC-IV)
* **The Hardest Question:** *"Most Thai public hospitals do not even have automated KDIGO e-alerts firing in their HIS, so 'AKI alert fatigue' is an American Epic/Cerner problem, not a Thai hospital problem. Furthermore, in a patient with suspected sepsis or oliguria, telling a junior doctor to 'wait and remeasure creatinine' instead of checking fluid status and nephrotoxins could delay life-saving care. Who is your local user, and where is your local workflow?"*
* **Would it pass as is?** **Fail.** It solves a non-existent local problem (Thai hospitals don't suffer from automated KDIGO e-alert fatigue) using US ICU data (MIMIC-IV), and lacks a tangible clinician-facing application workflow.
* **Minimum Fix to Pass:**
  1. Abandon inpatient ICU AKI alert suppression. Pivot to **Outpatient NCD Clinic Borderline Lab Re-testing CDSS** (eGFR $<60$ CKD staging, HbA1c, LDL, TSH—like Gemini #5), where Thai doctors genuinely make lifelong treatment decisions on single noisy lab values, **or** drop the topic entirely.

---

### B. Roasting Codex's Top 3

#### Codex #1: Verified Thai Medication-Instruction Editor
* **The Hardest Question:** *"Why would any Thai pharmacist ever type or paste a medication instruction into an LLM editor and wait for a rewrite when every hospital HIS and community pharmacy label printer already uses pre-configured shortcodes (`1x2 pc` → `รับประทานครั้งละ 1 เม็ด วันละ 2 ครั้ง หลังอาหารเช้า-เย็น`)? And if you author both the 120 fictional source cards and the 360 corrupted drafts yourself, aren't you just testing whether your regex catches the exact synthetic errors you planted?"*
* **Would it pass as is?** **Conditional Pass.** The committee will praise the tight scope, clean ethics, and honest statistics, but the **Clinical Examiner** will strongly question the clinical utility: standard dispensing labels in Thailand are generated deterministically by HIS/pharmacy software, not rewritten by hand.
* **Minimum Fix to Pass:**
  1. Broaden the input from "single-drug label rewrites" (which templates already solve) to **Multi-Drug Discharge / After-Visit Care-Plan Synthesis from "Tinglish" Doctor Notes** (merging with Gemini #2 *DischargeClear*), where physicians write unstructured mixed-language instructions (`Lasix 40mg 1x1 pc, hold if BP<90 or dizzy, f/u电解质 1 wk`) that HIS shortcodes *cannot* handle.
  2. Source the raw clinical inputs from **public clinical vignettes / MIMIC discharge medication sections + independent physician colleagues**, rather than writing both the source cards and the verification rules yourself.

#### Codex #2: Thai Occupational Blood-Exposure First-Response Checklist
* **The Hardest Question:** *"Needlestick post-exposure prophylaxis (PEP) follows a rigid 1-page hospital poster with fewer than 15 boolean branches (Source HIV/HBV/HCV status × Exposed staff immunity × Exposure severity). Why on earth would a panicked resident who just stuck themselves with a hollow-bore needle type a free-text narrative story into an LLM instead of tapping 5 checkboxes on a mobile form—and why does a 15-branch decision table qualify as a Master's capstone in AI?"*
* **Would it pass as is?** **No (Reject for insufficient AI justification and artificial UX).** Codex admits in its own evaluation plan that it will compare a structured form against LLM free-text entry. Every examiner on the panel knows the structured form (or a 5-button calculator) will win on speed, safety, and usability—making the AI component pointless.
* **Minimum Fix to Pass:**
  1. Do not pitch this. If forced to salvage it, reframe it as an **Interactive AI Simulated Clinical Incident & Handover Trainer** (where the LLM role-plays the panicked exposed worker/source patient and grades the junior doctor's history-taking and PEP ordering), though that edges close to last year's #22 (simulated patient). Better to drop.

#### Codex #3: Thai Red-Flag Response Testing Workbench for Symptom Chatbots
* **The Hardest Question:** *"In this MSc cohort, how many Thai hospitals or clinical departments actually spend their week auditing symptom chatbots? You are building a developer QA benchmarking tool for AI engineers, not a healthcare service innovation for clinicians or patients. Where is the healthcare service delivery improvement required by Independent Study I & II?"*
* **Would it pass as is?** **Conditional Pass (High risk of 'Too Academic / Tool for Nobody' critique).** The engineering examiner will appreciate the evaluation workbench and rubric rigour, but the clinical examiner will complain that "an LLM benchmark dashboard for developers" has no clinical user in a hospital.
* **Minimum Fix to Pass:**
  1. Merge the **Testing Workbench (Codex #3)** with the **Runtime Nurse/GP Tele-Triage Safety Harness (Gemini #3 *TriageGuard-1669*)**: pitch the product as a **Safety-Verified Tele-Triage Copilot & Red-Flag Gatekeeper for Triage Nurses/GPs**, where the 450-prompt Thai Red-Flag Workbench is the **built-in pre-deployment verification suite and safety audit dashboard** used by the clinical governance team to certify the copilot.

---

## 2. Hume Audit: Top 3 Load-Bearing Factual Claims That Are Wrong or Unverified

1. **Claim (Gemini #1 — *ThaiLab-LOINC*):** *"Public Thai MOPH / TMLT standard lab dictionaries and NHSO public reimbursement lab schedules provide ~2,000–5,000 public items that can be mapped to LOINC as ground truth."*
   * **Hume Audit Verdict — PARTIALLY WRONG / HIGH RISK:** TMLT (Thai Medical Laboratory Terminology, maintained by THIS — Thai Health Information Standards Development Center) **already includes official LOINC mappings** for standard laboratory items inside its release files. If the student downloads TMLT and predicts its LOINC column from its Thai/English description column, examiners who teach the *Health IT & Data Standards* course will immediately recognise that TMLT was engineered *from* LOINC—making a TMLT-to-LOINC test set tautological! **Fix:** The true unmapped pain point is mapping **raw, messy hospital LIS local test names/panels + specimen/unit strings → TMLT/LOINC**, which requires obtaining real (non-patient) hospital lab master catalogs/price lists (e.g., public Comptroller General's Department / กรมบัญชีกลาง medical fee schedules, public hospital lab handbooks from Chula/Siriraj websites, or de-identified LIS dictionary exports from 3–5 physician classmates' hospitals).

2. **Claim (Claude #2 & Gemini #3):** *"Public Thai CPG PDFs (Royal Colleges) and NIEM 1669 emergency triage manuals can be freely ingested, chunked, and redistributed inside an open-access RAG/triage repository without copyright friction."*
   * **Hume Audit Verdict — UNVERIFIED / LEGALLY FALSE FOR REDISTRIBUTION:** Being publicly downloadable as a PDF on a Thai medical society or ministry website does **not** grant a Creative Commons or open-redistribution licence. Under the Thai Copyright Act, redistributing verbatim chunks or full PDFs of Royal College CPGs in a public GitHub dataset is a copyright violation. **Fix:** The student can use public PDFs locally for prototype evaluation and display short fair-use citations with page numbers, while releasing only the **student-authored question/vignette benchmark, structured rule abstractions, and code** under CC BY 4.0.

3. **Claim (Claude #3 & Gemini #2/#4):** *"MIMIC-IV / MIMIC-IV-Note credentialed access via PhysioNet takes 1–2 weeks."*
   * **Hume Audit Verdict — UNVERIFIED & RISKY TIMELINE BOTTLENECK:** PhysioNet credentialing requires completing the CITI "Data or Specimens Only Research" course **and** having a reference/supervisor (often requiring an institutional `.edu` / `.ac.th` verification or signed supervisor endorsement) manually approved by MIT LCP staff. For international students without an already-credentialed advisor, PhysioNet approval frequently takes **3 to 6 weeks** or stalls on institutional verification. **Fix:** Never put MIMIC-IV credentialing on the critical path for the November proposal exam. Use **already-open, uncredentialed datasets** (PTB-XL, MIT-BIH, NHANES, PMC Open Access Case Reports, MedQA) plus physician-authored synthetic Thai/Tinglish cases as the primary data source.

---

## 3. Convergence Analysis: Real Signal or Shared Blind Spot?

Across three independent advisors, strong convergence emerged on **three distinct archetypes**:

1. **Archetype A: Source-Bound Clinical Text Rewriting with a Deterministic Fact/Dose Verifier**
   * *Reached by:* **Codex #1** (Verified Thai Medication-Instruction Editor) + **Gemini #2** (*DischargeClear*: Hallucination-Guarded Thai After-Visit Summary & Care-Plan Generator).
   * *Is it a real signal?* **YES — Strongest Signal.** Both advisors independently deduced that (a) free-form clinical LLMs fail on safety, (b) last year's synthetic EMR extraction projects (#1, #17) failed because they tried to infer clinical diagnoses from noisy notes, whereas **translating/structuring clinician-supplied instructions with a hard neuro-symbolic verifier** is bounded, solvable on a 4B local model, requires zero hospital patient records, and produces an immediately demonstrable side-by-side UI.

2. **Archetype B: Thai Red-Flag Symptom Triage Safety Audit + Deterministic Guardrail**
   * *Reached by:* **Claude #4** (Thai Medical Chatbot Safety Audit) + **Codex #3** (Thai Red-Flag Response Testing Workbench) + **Gemini #3** (*TriageGuard-1669*: Neuro-Symbolic Safety Harness & Triage Copilot).
   * *Is it a real signal?* **YES — With a Crucial Caveat.** All three advisors recognised that this preserves the student's existing `README.md` passion and technical preparation. Crucially, all three also converged on the **exact same committee objection**: *a standalone benchmark paper will fail a Plan 2 product committee unless packaged inside a usable clinician-facing workflow tool (either an evaluation workbench or a nurse triage CDSS).*

3. **Archetype C: Public-Signal ECG Tooling + Clinician Simulation**
   * *Reached by:* **Claude #1** (Photo-ECG Triage on PTB-XL) + **Codex #5** (ECG Artifact-Recognition Training Prototype on MIT-BIH).
   * *Is it a real signal?* **PARTIAL.** It reflects the fact that ECGs are the cleanest uncredentialed public physiological datasets (PTB-XL, MIT-BIH). However, Claude #1 is much stronger clinically (solving the real Thai rural ER LINE photo-referral problem), whereas Codex #5 retreats too far into an artificial teaching toy.

4. **Archetype D: Lab Measurement Variability ("Remeasure Before Acting")**
   * *Reached by:* **Claude #3** (AKI Creatinine Alert) + **Gemini #5** (*ReCheck-CDSS* Outpatient Borderline Lab Advisor).
   * *Is it a real signal?* **WEAK.** Both ranked it low ($P(\text{approved}) = 0.60 - 0.72$) because it struggles to justify "why AI?" and faces clinical resistance in high-volume Thai hospitals.

---

## 4. Final Committee Ranking Across All Advisors

### Master Ranking Table (All Distinct Proposals + Strategic Merges)

| # | Title | P(approved) | P(finished) | Data/IRB risk | Advisor fit | One-line verdict |
|---:|---|---:|---:|---|---|---|
| **1** | **DischargeClear-Rx** *(Merge: Gemini #2 + Codex #1)*: Critical-Fact-Verified Thai Discharge Care-Plan & Medication Editor | **90%** | **90%** | **Very Low** (Physician-authored Tinglish vignettes + public RDU leaflets; IRB exempt/expedited user study) | **Excellent** (Internal/Family Med or Clinical Pharmacy + NLP Engineer) | **Best all-rounder:** Solves a daily Thai physician/pharmacist pain point, turns the student's verifier concept into a safety-critical HITL product, and needs zero patient data. |
| **2** | **Photo-ECG FastTrack** *(Claude #1 + Quality Gate)*: Smartphone Paper-ECG Quality Checker, STEMI Flag & LINE Referral Assistant | **86%** | **82%** | **Very Low** (Public PTB-XL printed on Thai ECG paper + photographed; colleague reader study) | **High** (Cardiology/ER + Image/Signal Processing Engineer) | **Best clinical story:** Hooks clinical examiners instantly via the ubiquitous Thai rural ER "photo-to-LINE" habit; needs a quality gatekeeper to de-risk digitisation. |
| **3** | **TriageGuard-1669 & Workbench** *(Merge: Gemini #3 + Codex #3 + Claude #4)*: Red-Flag Safety Harness & Audit Workbench for Thai Tele-Triage | **82%** | **86%** | **Very Low** (300–450 clinician-authored Thai red-flag vignettes + public NIEM 1669 rules) | **High** (Emergency/Family Med + NLP/Software Testing Engineer) | **Best continuity with prior work:** Salvages the student's Thai LLM safety audit by wrapping the benchmark inside a nurse tele-triage CDSS and governance workbench. |
| **4** | **ThaiLab-LOINC** *(Gemini #1)*: Automated 6-Axis Mapping & Verification of Hospital Lab Catalogs to TMLT/LOINC | **84%** | **85%** | **Low** (Public LOINC/TMLT + public hospital lab fee schedules; no patient data) | **High** (Lab Medicine / Health IT faculty + NLP Engineer) | **Safest institutional template:** Follows last year's winning #9/#33 blueprint, provided the student maps messy hospital lab catalogs rather than already-mapped TMLT. |
| **5** | **Thai CPG Table-Aware Assistant** *(Claude #2)*: Citation-Grounded & Abstaining Thai Guideline Copilot | **75%** | **88%** | **Low** (Local CPG PDFs + 200 clinician Q&A pairs) | **Medium-High** (Internal/Family Med + NLP Engineer) | Feasible and safe, but risks looking like "ChatGPT with PDFs" unless engineered specifically for complex CPG flowcharts and dosing tables. |
| **6** | **ClaimsReady-TH** *(Gemini #4)*: Pre-Audit TDRG & Discharge Summary Completeness Copilot | **76%** | **80%** | **Low-Medium** (Public ICD-10-TM/TDRG + synthetic charts; needs real coder buy-in) | **High** (Hospital Operations / Health IT faculty + NLP Engineer) | Strong hospital ROI story, but vulnerable to attacks on synthetic billing evaluation and low student enthusiasm for admin tools. |
| **7** | **Inhaler-Step Video Reviewer** *(Codex #4)*: Healthy-Volunteer pMDI–Spacer Observable Step Prototype | **72%** | **74%** | **Medium** (Requires filming 30 volunteers = 240 videos; full IRB for identifiable video) | **Medium** (Pulmonology/Pharmacy + CV Engineer) | Honest scope, but filming 30 subjects under IRB in a few months is high operational friction for a tool that cannot assess actual inhalation. |
| **8** | **ReCheck-CDSS** *(Gemini #5 / Claude #3)*: Uncertainty-Aware Lab Repeat-Testing Calculator | **65%** | **85%** | **Low** (Public NHANES + EFLM + Thai DMSc EQAS) | **Medium** (Lab Medicine / Nephrology + Biostat/DS Engineer) | Clever statistical premise, but likely to be attacked by this committee as "Monte Carlo math, not an AI workflow product." |
| **9** | **Occupational Blood-Exposure Checklist** *(Codex #2)*: Needlestick First-Response Slot Extractor | **62%** | **88%** | **Very Low** (80 fictional scenarios + public CDC/Thai rules) | **Medium** (ID / Occupational Health + NLP Engineer) | Fails the "Why AI?" test: a 5-checkbox mobile flowchart beats typing a free-text story after a needlestick injury. |
| **10** | **ECG Artifact Trainer** *(Codex #5)* & **Gram-Neg AMR** *(Claude #5)* | **55%** | **75%** | **Low–Medium** | **Low–Medium** | ECG trainer feels like a toy retreat from clinical ECG analysis; AMR is too close to last year's #30 without local microbiology data. |

---

### Detailed Top 3 Across All Advisors (With Merges)

1. **Top Pick #1 — DischargeClear-Rx (Merged Gemini #2 + Codex #1): *Development and Usability Evaluation of a Critical-Fact-Verified Thai Discharge Care-Plan and Medication Instruction Editor***
   * **Why the merge wins:** Gemini #2 (*DischargeClear*) has the compelling clinical problem (physicians write chaotic "Tinglish" discharge summaries and multi-drug regimens that patients cannot read), while Codex #1 brings the airtight experimental design (source-bound critical-fact verification, planted error sensitivity/specificity, and a counterbalanced timed editing study against standard templates). Together, they neutralise every committee attack: templates cannot handle multi-drug "Tinglish" discharge instructions, and the deterministic fact/dose verifier prevents LLM hallucinations before printing or exporting to LINE.
2. **Top Pick #2 — Photo-ECG FastTrack (Claude #1 enhanced): *A Smartphone Paper-ECG Quality Gatekeeper, Critical-Finding Triage, and Structured Referral Assistant for Thai Community Hospitals***
   * **Why it wins:** If the student wants a clinical diagnostic/triage problem rather than a documentation/communication tool, this is the standout winner. Every Thai clinician knows the "photograph paper ECG → send to LINE group" workflow. Adding a front-end **Image Quality & Grid Calibration Gatekeeper** turns the digitisation risk into a core engineering feature.
3. **Top Pick #3 — TriageGuard-1669 & Safety Workbench (Merged Gemini #3 + Codex #3 + Claude #4): *A Neuro-Symbolic Red-Flag Safety Harness and Evaluation Workbench for Thai Primary-Care Tele-Triage***
   * **Why the merge wins:** If the student wants to keep their existing `README.md` research on Thai medical LLM red-flag safety, merging Gemini #3 (a runtime nurse/GP triage copilot backed by NIEM 1669 rules) with Codex #3 (a reproducible clinician testing workbench and 150-scenario-family Thai red-flag benchmark) gives the committee both a **clinical product** and a **rigorous evaluation tool**.

---

## 5. Final Recommendation to the Student & 7-Day Action Plan

### The One Project We Recommend You Pick Today:
**Pick #1: `DischargeClear-Rx` (Merged Gemini #2 + Codex #1)** — *with **#2 (`Photo-ECG FastTrack`)** or **#3 (`TriageGuard-1669`)** as your 1-page backup depending on which clinical advisor replies first.*

**Why `DischargeClear-Rx` is your highest-EV choice right now:**
1. **Zero external data bottleneck:** As a practising Thai physician, you can author the initial seed corpus of realistic "Tinglish" OPD/discharge notes (`pt dx CHF EF 35%, AKI on CKD, start Lasix 40mg 1x1 pc, hold if dizzy, KCl 1x2 pc...`) tonight, and have 3–5 physician classmates contribute and blind-rate the held-out test set.
2. **Preserves your intellectual core:** Your interest in **neuro-symbolic verification and safety guardrails** becomes the hero of the architecture (a dual-verifier that extracts structured entities—drug, dose, unit, route, timing, stop-rules—and blocks any plain-Thai draft that alters or omits a single critical fact).
3. **Instant advisor recruitment:** Every Internal Medicine, Family Medicine, Emergency Medicine, and Pharmacy lecturer at Chula sees medication miscommunication daily and will immediately grasp a 1-page brief without worrying about hospital IRB delays.

---

### The 3 Things You Must Do in the Next 7 Days

1. **Days 1–2: Build a 1-Screen Clickable Prototype + 1-Page Advisor Pitch Sheet (Two Variants)**
   * Spend 6 hours building a working single-screen Streamlit/Next.js mock-up of **DischargeClear-Rx** running on your RTX 4090 (`Qwen3-4B` or API) using **5 realistic fictional "Tinglish" discharge cases**. Show the 3-pane view: *(Left)* Messy Tinglish Doctor Note → *(Middle)* Deterministic Fact/Dose Diff Verifier (highlighting a caught dose error in red and verified doses in green) → *(Right)* Printable Plain-Thai Patient Care Card + Visual Pill Schedule (เช้า/กลางวัน/เย็น/ก่อนนอน) + 1669 Red Flags.
   * Write a crisp 1-page brief stating: **Problem, Named User, Non-Patient Evaluation Plan ($N=12$ clinicians, 120 source cards / 360 drafts with planted errors), IRB Exemption/Expedited Route, and Timeline to May.** (Keep a second 1-page brief for *Photo-ECG* or *TriageGuard-1669* in your pocket in case an ER/Cardiology advisor prefers triage).

2. **Days 3–5: Run a "Shotgun" Advisor & Stakeholder Recruitment Sprint**
   * Do not wait for sequential email replies. Email **4 potential Clinical Advisors** (Internal Medicine, Family Medicine, Emergency Medicine, or Clinical Pharmacy faculty teaching in the Sandbox programme) and **3 potential Computer Engineering Co-Advisors** (NLP / Software Engineering faculty) simultaneously.
   * Attach your **1-page brief + a 60-second screen-recording GIF/video of your prototype** and ask for a 15-minute Zoom call this week. Emphasise in bold in the first paragraph: ***"This project uses zero hospital patient records, requires only a simulated clinician usability study, and already has a working baseline prototype."***
   * In parallel, ask 10 physician/pharmacist classmates in your MSc cohort to fill out a 5-question baseline workflow survey (how long they spend writing/explaining discharge instructions, common patient dosing mistakes, and current tools) so you have **real local problem numbers** on Slide 2 of your proposal deck.

3. **Days 6–7: Lock Advisor Sign-Off, Submit Exam Slots, and Freeze the Proposal Evaluation Matrix**
   * Lock in the first responsive Clinical Advisor + Engineering Co-Advisor pair and immediately send the programme coordinator your **advisor names and 3 proposed November exam time slots**.
   * Confirm with your advisor the **exact bounded scope** (e.g., 5 high-volume conditions: Heart Failure, Diabetes, Hypertension, COPD/Asthma, Dengue/Acute Febrile Illness; 120 fictional source cases; 2 independent pharmacist/physician raters; 12-clinician counterbalanced usability study) and write out the ** Capstone Portfolio Sections 1–3** so the complete document is ready to email to the committee one full week before your exam.
