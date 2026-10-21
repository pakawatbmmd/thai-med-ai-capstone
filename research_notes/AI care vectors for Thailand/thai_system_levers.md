# Thailand's system-level levers for AI (the McKinsey "AI-powered future of care" frame applied to Thai UHC, as of Oct 2026)

Scope note: this is the Thai counterpart to the McKinsey US frame summarised in `00_guidance_mckinsey_summary.md`. The research budget was about 16 tool calls, so several Thai numbers that are widely quoted (UCS headcount, VHV headcount, RDU program results) could **not** be re-verified this session. They are listed under Gaps, not presented as fact. "Verified" here means a source was retrieved this session. Items marked [older] predate 2023.

---

## 1. Thai payer structure: could NHSO be McKinsey's "AI orchestrator"?

### Takeaway
NHSO is already acting as a centralised buyer and deployer of AI, which is something no US payer can do at national scale. It pays for a Thai chest-X-ray AI across hundreds of public hospitals from a ring-fenced innovation budget. It also put an AI pre-audit of outpatient claims onto the national Health Link exchange in April 2026, and it runs the "30-baht treatment anywhere" network of pharmacies, clinics and telemedicine "innovation units." The parts of an orchestrator exist (one payer, a national data spine, a non-physician front door, and a procurement budget for Thai AI). What is missing is the patient-facing "AI clinician" layer that would tie them together.

### Cited Findings
**Payment architecture**
- UCS cost control combines a single public payer, a fixed global budget, capitation for outpatient services, prospective (DRG-type) payment for inpatient admissions, and primary-care gatekeeping to tertiary care [older, source cites pre-2016 literature] — [Kyoto SEAS](https://kyoto-seas.org/pdf/45/2/450204.pdf); [HEFPA policy brief](https://www.eur.nl/sites/corporate/files/2017-10/HEFPA_Thai_PB_4pp.pdf)
- NHSO caps per-capita UCS coverage, so a facility's costs above the capitation are not subsidised [older] — [SpringerPlus 2016](https://springerplus.springeropen.com/track/pdf/10.1186/s40064-016-3665-4)
- *Implication for the McKinsey frame:* under capitation, care diverted to AI is a **saving** for the contracted primary-care unit, not lost fee-for-service revenue. McKinsey's US "provider loses low-acuity volume" problem is largely absent (inference, see below).

**NHSO's AI deployments (verified)**
- **AI chest X-ray reading (Perceptra, Thai startup):** certified by the Royal College of Radiologists of Thailand and the Thai FDA. NHSO funds it as a Thai-innovation benefit. Pilot year (FY2025): 167 public hospitals. **Phase 2, FY2569 (2026): 445 hospitals, THB 135M/yr. Phase 3, FY2570 (2027): 887 hospitals, THB 225M/yr** — [Hfocus, Jul 2025](https://www.hfocus.org/content/2025/07/34642); [PostToday](https://www.posttoday.com/smart-life/726965) (figures relayed via search summary; the Hfocus page returned HTTP 403 on direct fetch)
- **AI pre-audit of outpatient claims:** on **27 Apr 2026** NHSO and the Big Data Institute (BDI, under the Ministry of Digital Economy and Society), with DGA as witness, agreed to upgrade Health Link, integrate it with NHSO's claims database, and add "an AI system for pre-audit verification of outpatient claims." The same upgrade gives patients their history through the **Thang Rath (ทางรัฐ) app** and pilots **e-Referral in Bangkok** — [Jonda Health summary citing Thairath](https://www.jonda.health/articles/thailand-health-link-nhso-ai-claims) (secondary; Thairath original not retrieved)
- **Thai-innovation budget:** NHSO spent >THB 2.9B on its Thai-innovation list (drugs, vaccines, devices, including the chest X-ray AI) in FY2568–69. It targets **THB 5B in FY2570 and THB 10B in FY2571** (announced 12 Mar 2026 by Secretary-General Dr Jadej Thammatacharee). The headline's "5×" claim does not match the body's figures (2.9B to 5B is about 1.7×; 2.9B to 10B is about 3.4×) — [PostToday, Mar 2026](https://www.posttoday.com/smart-life/739294)
- NHSO took part in iMEDEV 2026 (15 Oct 2026), framing domestic medical innovation as a "core mechanism" of the UC system — [The Coverage](https://www.thecoverage.info/news/content/12418)

**30-baht treatment anywhere / non-physician front door**
- Phase 3 (46 provinces) recorded about 14.08M services: **1.21M telemedicine consults, ~94,000 pharmacy pickups, ~574,000 mail-order medicine deliveries**, and 6.15M people using units outside their registered unit. The program now covers **all 77 provinces** — [Money & Banking, 2025](https://en.moneyandbanking.co.th/2025/148364/)
- UC members can use **pharmacies, private clinics and private labs** for minor illnesses and prevention services — [NHSO English news](https://eng.nhso.go.th/view/1/DescriptionNews/Upgrade-UCS-with-neighborhood-healthcare-model-/611/EN-US)
- NHSO "Care Box" telemedicine kiosk in Bangkok treats **42 common illnesses**, with delivery or pharmacy pickup of medicines — [Nation Thailand](https://www.nationthailand.com/health-wellness/40043399)
- From **12 Jan 2026** (2569), gold-card holders can use **"innovation service units" (7 types)** carrying the "30 บาทรักษาทุกที่" logo. Identity must be confirmed by ID verification or QR scan for transparency — [TCIJ](https://www.tcijthai.com/news/2026/1/current/14692); [Hfocus Jan 2026](https://www.hfocus.org/content/2026/01/36630)
- For FY2569, NHSO reports a closed-end budget of about THB 3B for innovation units. It plans to restructure them and to issue monthly coupons through an app — [Matichon](https://www.matichon.co.th/local/quality-life/news_5508254)
- Access to UCS through the **Thang Rath app** without an ID card — [DGA](https://www.dga.or.th/en/document-sharing/en-dga-news/118820/)
- Fiscal stress: experts warned the gold-card scheme is "on the brink" — [Bangkok Post](https://www.bangkokpost.com/thailand/general/3130290/gold-card-health-care-scheme-on-the-brink-experts-warn) (headline only; details not retrieved)

**Referral and tertiary congestion** [older evidence]
- At Siriraj, primary-to-tertiary referral drivers were chronic or complex conditions (cataract, DM, HTN, cancer), an inadequate essential-drug list at the PCU, unsupportable workloads, and missing equipment or physicians [2008–11 data] — [Siriraj Med J](https://he02.tci-thaijo.org/index.php/sirirajmedj/article/download/55265/45885)
- In a Northeast study, workforce and budget shortfalls at every level meant UC primary-care strategies "do not reduce, but rather increase" hospital-level patient numbers, and tertiary hospitals perceive "over-referral" [older] — [Kyoto Univ. repository](https://repository.kulib.kyoto-u.ac.jp/server/api/core/bitstreams/ce16a750-0d46-470c-be50-92ad5f44b93e/content)
- A substantial share of UC beneficiaries use care outside UCS boundaries (2013 data) [older] — [AFHEA](https://afhea.org/pattern-of-outpatient-utilisation-and-cost-for-patients-under-the-universal-coverage/)

**National AI and digital governance context**
- Thailand National AI Strategy & Action Plan 2022–2027 (Cabinet, Jul 2022) — [OECD.AI](https://oecd.ai/en/dashboards/policy-initiatives/thailand-national-ai-strategy-and-action-plan-2022-2027-1728)
- PDPC **draft Guidelines on Personal Data Protection in AI Development and Use (Feb 2026)**: DPIAs for high-risk AI, and data-processing agreements must address model-training prohibitions — [AI Policy Tracker](https://aipolicytracker.org/jurisdictions/thailand) (secondary)

### Inferences
- **Why this is hard in the US and natural in Thailand:** NHSO (one payer for about 70% of the population, through UCS) already (a) holds national OP/IP claims, (b) is wiring claims into the national HIE (Health Link), (c) owns a patient app channel (Thang Rath), (d) contracts a non-physician front door (pharmacies, telemedicine, Care Box kiosks), and (e) has a statutory budget line for buying Thai innovation. McKinsey's "payer moves from financing to orchestrating" is therefore less a prediction for Thailand than an under-exploited configuration. The novel step would be a **payer-level orchestration agent**: one AI layer that triages a gold-card member, routes them to the cheapest safe node (self-care, pharmacy minor-ailment benefit, telemedicine, PCU, or e-Referral), and closes the loop with claims and Health Link data. No US payer can route across all of its members' providers like this.
- AI claims pre-audit plus the chest X-ray AI show NHSO's revealed preference: AI that **saves money or extends scarce specialists**, procured as a per-hospital service. A capstone that frames its MVP as an "NHSO benefit-package item" (with a cost-per-case, a fee-schedule logic and an evaluation by HITAP-style HTA) fits a procurement channel that already exists.
- Capitation changes the economics. AI that keeps patients out of hospital benefits the CUP (contracting unit for primary care) directly, whereas US fee-for-service providers lose revenue. The fiscal stress (the "on the brink" warning) strengthens this case.
- The 30-baht-anywhere data (1.2M telemedicine consults; pharmacy and delivery channels) are the closest Thai analogue to McKinsey's "visits diverted to AI" signal. Today these are *human* tele-encounters, so the diversion path is in place but has no AI in it yet.

### Gaps
- **No official NHSO AI strategy document for 2025–26 was found.** AI appears through individual initiatives (CXR AI, claims pre-audit), not a published plan. Check nhso.go.th annual operating plan FY2569/2570.
- **FDH (Financial Data Hub), e-claim, and the current OP/IP payment parameters** (2026 capitation rate per head, DRG version / base rate, the e-claim to FDH migration) were **not retrieved**. They should be verified from NHSO/MOPH sources before use.
- The **pharmacy common-illness (16-symptom) program** volumes and the **NHSO Line OA** usage numbers were not found.
- **Not verified this session (prior knowledge only):** UCS covers about 47M people, SSO about 12–13M, CSMBS about 5M. The UC capitation is roughly THB 3,800–4,000+ per head (FY2025–26). Treat these as unverified.
- Accuracy and outcome data for the Perceptra CXR AI in NHSO deployment (TB yield, lung-nodule follow-up cascades) were not retrieved.
- No pilot of NHSO deploying a patient-facing conversational AI or "AI clinician" was found.

---

## 2. Care cascades and low-value care in Thailand

### Takeaway
Thai evidence on low-value care is real but old and centred on antibiotics. Antibiotics were prescribed in about 47% of primary-care visits in one northern district, and in about 87–89% of pharyngitis and tonsillitis cases. I found no Thailand-specific Choosing Wisely list or recent Thai incidental-finding cascade data. This is an evidence gap that a capstone could itself fill (e.g., cascades after the CXR AI or after annual check-ups).

### Cited Findings
- Northern Thailand, 32 PCUs (BMJ Open 2018): **46.9% of patients (39,242) received an antibiotic**. Pharyngitis and tonsillitis got antibiotics in about **87–89%** of cases, common cold in about 10.5%. Amoxicillin was the most common [older-ish, 2018] — [BMJ Open](https://bmjopen.bmj.com/content/8/7/e022250)
- Bangkok slum health centres: 91% of URIs were probably viral, yet **60% of viral and 89% of bacterial URI patients got antibiotics** [older, 2005] — [BVS/SEA](https://search.bvsalud.org/gim/resource/en/sea-34734)
- A Bangpakong Hospital (Chachoengsao) study evaluated local guidelines for antibiotics in URI, diarrhoea and simple wounds (Oct 2018–Sep 2020). The results were not retrieved — [Burapha J Med](https://he01.tci-thaijo.org/index.php/BJmed/article/view/268579)
- Choosing Wisely campaigns exist in 35+ countries, including in Asia. No Thai-specific list was found in this search — [Choosing Wisely evidence review, BMJ EBM](https://ebm.bmj.com/content/30/5/355); a Thai journal (JOPOLO) cites Choosing Wisely — [JOPOLO](https://he03.tci-thaijo.org/index.php/JOPOLO/article/view/6104)
- US anchor (from guidance doc): 94.4% of physicians have seen cascades after incidental findings — see `00_guidance_mckinsey_summary.md`

### Inferences
- In a capitated system, **cascades are a cost to the payer and the CUP rather than revenue**. The incentive to break them is aligned in Thailand in a way it is not in US fee-for-service. That makes a "cascade-aware" AI (one that predicts the downstream test chain an incidental finding will trigger and recommends guideline-concordant follow-up) a natural NHSO buy.
- New AI front doors (CXR AI in 445 to 887 hospitals; the pharmacy and telemedicine channels) are **cascade generators**. AI CXR flags of incidental nodules will trigger CT follow-ups at already congested tertiary hospitals. A design that pairs detection with **cascade governance** (Fleischner-style triage, a referral appropriateness check before e-Referral) addresses a risk that NHSO is creating now.
- Antibiotic stewardship at pharmacies and telemedicine (the minor-ailment channels) is the most measurable low-value-care target, with clear Thai baselines.

### Gaps
- No 2023–2026 Thai data were retrieved on antibiotic prescribing, imaging overuse, or check-up cascades (annual check-up packages, private-sector executive check-ups).
- Thailand's **Rational Drug Use (RDU) hospital/country policy** and its KPIs (e.g., antibiotic use in URI/acute diarrhoea below 20%) come from prior knowledge and were **not verified** this session.
- I could not confirm whether a Thai Choosing Wisely list exists (one may exist via the Royal College of Physicians of Thailand). A search in Thai ("Choosing Wisely ประเทศไทย") is recommended.

---

## 3. Deskilling evidence 2023–2026 and countermeasures

### Takeaway
The first real-world clinical evidence of AI-induced deskilling comes from colonoscopy. In the ACCEPT sub-study (Lancet Gastroenterology & Hepatology, 2025), ADR in non-AI colonoscopies fell from 28.4% to 22.4% after AI introduction. Automation-bias experiments show that incorrect AI suggestions pull clinicians of all levels toward error, inexperienced ones most of all. Proposed countermeasures (manual-mode quotas, simulated AI outages, "copilot not autopilot," unaided-first reasoning) are plentiful, but **none has been validated in trials**. A skill-preserving or skill-building AI is therefore an open, publishable design space.

### Cited Findings
**Deskilling**
- **Budzyń et al., Lancet Gastroenterol Hepatol 2025;10:896–903** (online 12 Aug 2025): a retrospective study at 4 Polish centres (ACCEPT trial), 19 experienced endoscopists (>2,000 colonoscopies each). Non-AI colonoscopy ADR went from **28.4% to 22.4% (absolute −6.0%, 95% CI −10.5 to −1.6; p=0.0089)** in the 3 months before vs after AI introduction. AI exposure **OR 0.69 (0.53–0.89)**. Adenomas per positive colonoscopy were unchanged (1.91 vs 1.92). Observational, so association only. The editorialist (Omer Ahmad) called it the first real-world clinical evidence of deskilling — [Warwick WRAP](https://wrap.warwick.ac.uk/id/eprint/191005); [ASCO Post](https://ascopost.com/news/august-2025/routine-ai-assistance-may-lead-to-loss-of-skills-in-endoscopists-study-shows/); [ACG EBGI commentary](https://gi.org/journals-publications/ebgi/zhou_sep2025/)
- In contrast, a 2025 meta-analysis found CADe raises advanced-neoplasia detection modestly (12.7% vs 11.5%; RR 1.16), so AI helps *while on* and may hurt *when off* — relayed in [ASCO Post](https://ascopost.com/news/august-2025/routine-ai-assistance-may-lead-to-loss-of-skills-in-endoscopists-study-shows/) (meta-analysis not retrieved directly)
- A 2025 PRISMA review of 29 studies found automation bias reported in 10 and deskilling in 9. The evidence is mostly observational, simulation or conceptual — via [Dovepress JHL review](https://www.dovepress.com/generative-artificial-intelligence-in-healthcare-automation-bias-deski-peer-reviewed-fulltext-article-JHL)
- A scoping review in ESMO Real World Data & Digital Oncology (2026) on deskilling and loss of expertise argues that assessment should measure *maintained* competencies (diagnostic independence), not only accuracy and speed — [ESMO RWD](https://www.esmorwd.org/article/S2949-8201(26)00012-3/fulltext)
- Annals of Internal Medicine (2026) piece: "The Deskilling Effect: Is AI Eroding Clinical Competence?" — [Annals](https://doi.org/10.7326/ANNALS-26-00613) (content not retrieved)
- Forbes (Feb 2026) summarised the emerging evidence and noted that **no anti-deskilling strategy has been validated in trials** — [Forbes](https://www.forbes.com/sites/jessepines/2026/02/23/will-ai-de-skill-doctors-evidence-is-starting-to-trickle-in/)

**Automation bias**
- **Dratsch et al., Radiology 2023**: 27 radiologists reading 50 mammograms with a purported AI were significantly swayed by incorrect BI-RADS suggestions. Inexperienced readers were most likely to follow incorrect upgrades — [Radiology](https://doi.org/10.1148/radiol.222176)
- In an ACL-MRI crossover study, **45.5% of errors under AI assistance were attributable to automation bias**, across all experience levels — relayed via search summary of [Healio, Oct 2026](https://www.healio.com/news/gastroenterology/20261005/a-slippery-slope-is-ai-eroding-clinical-skills) (primary not retrieved)
- Aneurysm MRA automation-bias study (2025) — [PMC12008054](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12008054/) (results not retrieved)
- A registered RCT protocol, "Mitigating Automation Bias in Physician-LLM Diagnostic Reasoning Using Behavioral Nudges" (NCT07328815), has no results yet — [ClinicalTrials.gov doc](https://cdn.clinicaltrials.gov/large-docs/15/NCT07328815/Prot_SAP_000.pdf)

**Countermeasures proposed (none trial-validated)**
- **Manual-mode protocols** (e.g., 1 in 5 cases done without AI), measuring unaided performance, and tracking override and agreement rates as automation-bias signals. Governance boards with frontline clinicians — [Healio, Oct 2026](https://www.healio.com/news/gastroenterology/20261005/a-slippery-slope-is-ai-eroding-clinical-skills)
- **Aviation-style safeguards** (UCL/Moorfields, npj Digital Medicine): minimum unaided-practice requirements, unannounced simulated AI outages, and "digital copilot not autopilot" — [Ophthalmology Times](https://www.ophthalmologytimes.com/view/using-medical-ai-as-autopilot-risks-deskilling-of-clinicians)
- **"Never-skilling"** in trainees: keep independent reasoning first and reason before consulting AI — [Frontiers in Medicine 2026](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1765692/full); [PMC12909220 "Deskilling dilemma"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909220/)
- Trainee task redistribution: "AI as Teammate: Rethinking Task Distribution in Medical Training" (arXiv 2608.28373) — [arXiv](https://arxiv.org/pdf/2608.28373) (not read)
- McKinsey itself says organisations must "actively design against" deskilling with supervised unassisted practice, but specifies no mechanism — `00_guidance_mckinsey_summary.md`

### Inferences
- **Design opening:** an "unaided-first, AI-second" assistant (the clinician commits a read or diagnosis, then AI reveals its read and the disagreement becomes a teaching moment), with **competence-gated adaptive assistance** (help fades as measured unaided skill rises and returns when drift is detected). This turns each assisted case into a skill-maintenance data point. I found no deployed clinical system that does this, so it is a credible novelty claim (unverified negative).
- **Thailand-specific twist:** the people most exposed to deskilling or never-skilling are rural interns and GPs on mandatory service, and *non-physicians* using AI (pharmacists in the minor-ailment channel, VHVs with screening apps). These groups are also where Thailand most needs to *upskill*. A payer-funded AI that is contractually required to report each user's unaided performance (as part of an NHSO benefit) would be a governance innovation that is hard in the fragmented US market.
- The CXR AI now rolling out to 445–887 public hospitals is a **natural experiment for deskilling in Thailand**: GP CXR reading skill before vs after exposure, mirroring the ACCEPT design. A capstone could propose or prototype the measurement layer.

### Gaps
- I found no trial-tested "skill-preserving AI" in clinical practice. The adaptive-scaffolding and fading-assistance literature (ITS / medical education) was not searched.
- No Thai deskilling or automation-bias study was found.
- The 2026 Annals and Frontiers pieces, and the dermatology deskilling literature, were not read in full.

---

## 4. Progressive disclosure and patient-controlled health data (Thailand)

### Takeaway
Thailand has built a centralised exchange (Health Link, ~20,000 service points, with patient history access via Thang Rath) faster than it has built a legal consent layer. There is no Digital Health Act yet, and the MOPH itself says current laws do not cover health data transfer, AI or telemedicine. PDPA treats health data as sensitive and requires explicit consent, with public-interest exceptions. That gap between a national data spine and an undefined granular-consent mechanism is exactly where a **patient-side disclosure agent** (McKinsey's "progressive disclosure") would be novel and policy-relevant.

### Cited Findings
- Health Link is the national HIE, operated by BDI (Ministry of Digital Economy and Society). It launched in 2023 and rolled out nationally with the Public Health Cloud in 2024. It reaches **~20,000 service points (>10,000 NHSO units, ~8,500 clinics and pharmacies)**. Another report says ">6,600 entities," so the figures measure different things — [Jonda/Thairath](https://www.jonda.health/articles/thailand-health-link-nhso-ai-claims); [OpenGov Asia](https://opengovasia.com/thailand-inter-agency-data-linking-modernises-national-health-system/?c=us)
- **Nov 2025:** the MOPH special committee on the national digital health system approved 4 measures: linking provincial and Bangkok facility data into Health Link, **Mor Prom (หมอพร้อม)** and the Public Health Cloud; linking with the Ministry of Labour (SSO annual check-up and flu-vaccine records); and drafting a **Digital Health Act** framework. The minister called the Act "foundational ... secure, interoperable, innovation-ready" — [Healthcare IT News](https://www.healthcareitnews.com/news/asia/thailand-moves-unify-national-health-data-systems); [Digital Health News](https://www.digitalhealthnews.com/thailand-moves-to-unify-national-health-data-systems)
- MOPH acknowledges there is **no central law on health-data exchange**, and that existing laws do not cover health data transfers or emerging tech such as AI and telemedicine — [Healthcare IT News](https://www.healthcareitnews.com/news/asia/thailand-moves-unify-national-health-data-systems)
- PDPA: health data is sensitive and explicit consent is required, with exceptions (vital interest, public health) — [DLA Piper](https://www.dlapiperdataprotection.com/guide.pdf?c=TH); [Cookie Information 2026 guide](https://cookieinformation.com/blog/what-is-the-thailand-pdpa/)
- Enforcement: a private hospital was fined **THB 1.21M** for >1,000 exposed patient records. PDPC fines exceeded **THB 21.5M** by 2025 — [Jonda citing HSF Kramer](https://www.jonda.health/articles/thailand-health-link-nhso-ai-claims)
- The Apr 2026 Health Link upgrade gives patients medical history access through the **Thang Rath app** — [Jonda/Thairath](https://www.jonda.health/articles/thailand-health-link-nhso-ai-claims)
- PDPC draft AI guidelines (Feb 2026) require DPIAs for high-risk AI and model-training clauses in data-processing agreements — [AI Policy Tracker](https://aipolicytracker.org/jurisdictions/thailand)

### Inferences
- **Novel opportunity:** a "personal health agent" in Thang Rath, Mor Prom or Line that sits between the patient and the AI front door. It would hold a consent policy (consent-as-code: purpose, recipient, duration, data class) and **progressively disclose** Health Link data per encounter, e.g., a pharmacy minor-ailment visit sees medications and allergies only, while the e-Referral recipient sees the full problem list. Because Health Link is a single national spine, this agent is buildable as **one adapter**, unlike the US, where it would need hundreds of EHR and payer integrations. The missing Digital Health Act means a capstone could also prototype the *consent-policy schema* the Act will need.
- McKinsey's insight that "data availability, not model capability, is the limiting factor" is **partially solved by design in Thailand** (one HIE, one payer claims base). The binding constraint shifts to *legitimate, granular consent*, which favours a patient-controlled disclosure design.

### Gaps
- Health Link's actual consent mechanics (opt-in or opt-out, granularity, whether patients can see access logs) were not found.
- Solid pods, patient data wallets, and international "personal health AI agent negotiates disclosure" prototypes were not searched this session.
- Mor Prom and Thang Rath user numbers, and any Line OA health-data features, were not retrieved.

---

## 5. Workforce maldistribution and where AI-first workflows land first

### Takeaway
Doctor density varies roughly 7–12-fold between Bangkok and the rural Northeast (older data). Equity has improved (the GP Gini fell from 0.42 to 0.22, 2015–2024), but specialists remain concentrated. AI-first workflows will plausibly land first where non-physicians already carry the load: VHV community screening (already piloted with AI apps), pharmacies in the minor-ailment benefit, telemedicine innovation units, and CXR reading in community hospitals without radiologists.

### Cited Findings
- **Bangkok about 1 doctor per 800 people vs about 1 per 5,700** in some rural northeastern provinces. Bangkok was the only province consistently meeting the MOPH target of 1 per 1,800 [older] — [Dovepress RMHP](https://www.dovepress.com/equity-of-health-workforce-distribution-in-thailand-an-implication-of--peer-reviewed-fulltext-article-RMHP)
- Physician density in the Central region was **12× the Northeast's** (Noree) [older] — via [HRH 2023, doctor allocation policies](https://human-resources-health.biomedcentral.com/articles/10.1186/s12960-022-00782-5)
- National ratio about **0.92 per 1,000** (one study). Statista (MOPH data) gives about **1 per 1,500 in 2023**. The denominators differ — [HRH 2023](https://human-resources-health.biomedcentral.com/articles/10.1186/s12960-022-00782-5); [Statista](https://www.statista.com/statistics/1191929/thailand-doctor-ratio-to-population/)
- 2015–2024 national workforce database equity analysis: GPs and specialists both expanded. The **GP Gini improved from 0.42 (2015) to 0.22 (2024)**. Specialist distribution also improved, but the abstract gives no regional ratios — [PubMed 41856576](https://pubmed.ncbi.nlm.nih.gov/41856576/)
- Distribution of new graduates to public facilities, 2016–2020 — [PMC9621218](https://pmc.ncbi.nlm.nih.gov/articles/PMC9621218/) (not read in detail)
- **VHVs with AI already:** the RiskOCA AI oral-cancer screening app run by VHVs screened **1,242 adults (≥40 y)** in Phu Kamyao, Phayao. **250 VHVs** completed usability evaluation, with good acceptance — [JMIR mHealth 2026](https://mhealth.jmir.org/2026/1/e83738). T-OHAT oral-health app: 64 VHVs, VHV–dentist inter-examiner reliability **0.81–0.99** — [Special Care in Dentistry 2025](https://onlinelibrary.wiley.com/doi/10.1111/scd.70043)
- VHVs visited **>14M households in Mar–Apr 2020** for COVID-19 surveillance — [Bull WHO / PMC8061662](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8061662/)
- Pharmacy and telemedicine channels already active under UCS (see section 1): 1.21M teleconsults and pharmacy and delivery channels — [Money & Banking](https://en.moneyandbanking.co.th/2025/148364/)

### Inferences
- **Likely landing order for AI-first care in Thailand:** (1) imaging interpretation where radiologists are absent (already funded: CXR AI); (2) pharmacy and telemedicine minor ailments (a payer-funded non-physician channel); (3) VHV-operated screening and chronic-disease follow-up (proven feasibility, about 1M VHVs, unverified count); (4) community-hospital GP decision support. McKinsey's "11 of 19M US workers" task-share analysis would land in Thailand on **non-physician cadres first**, which makes deskilling and never-skilling of *lay and pharmacist* users a distinctively Thai design problem.
- A combined design is plausible and novel. It would be an NHSO-orchestrated, VHV- or pharmacist-facing AI that (a) routes through the 30-baht-anywhere network, (b) discloses Health Link data under patient-held consent, (c) is cascade-aware for referral, and (d) builds the user's skill (competence-gated assistance) rather than replacing it. Each part has Thai infrastructure behind it. The integration is what is new.

### Gaps
- No verified **2024 region-by-region table** of doctors, nurses or pharmacists per population was found (MOPH Health Resource Report / HDC would have it).
- The **VHV headcount (~1.0–1.07M)** and the primary-care-cluster / family-medicine-team coverage (PCC/PCU numbers, the "3 doctors" policy) were **not verified** this session.
- Nurse and pharmacist distribution data, and tertiary-hospital OPD wait-time numbers, were not retrieved.
