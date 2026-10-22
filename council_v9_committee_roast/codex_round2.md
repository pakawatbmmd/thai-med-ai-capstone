# Proposal Committee — Round 2

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