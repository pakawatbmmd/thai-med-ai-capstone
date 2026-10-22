# Council v9: Approvable, feasible capstones. Claude, Round 1

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
