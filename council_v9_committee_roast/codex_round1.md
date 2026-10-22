# Round 1 — Approval and completion before frontier novelty

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