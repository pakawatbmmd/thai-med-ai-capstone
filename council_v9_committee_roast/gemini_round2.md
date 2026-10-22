# Council v9, Round 2 — The Proposal Committee Roast & Final Verdict

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