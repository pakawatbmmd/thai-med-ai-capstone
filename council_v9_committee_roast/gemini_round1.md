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