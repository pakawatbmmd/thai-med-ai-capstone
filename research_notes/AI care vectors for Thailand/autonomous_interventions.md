# Autonomous interventions in healthcare: deployed closed-loop and decision-without-physician AI, graduated-autonomy frameworks, and a Thailand lens (as of Oct 2026)

Scope: McKinsey's vector 3, "AI plus robotics, devices and software in closed loops that *deliver* care" (see `00_guidance_mckinsey_summary.md`). McKinsey only names this vector. It does not analyse it, and it gives no method for measuring or certifying a "performance floor". This file fills that gap.

Verification legend:
- **[V]**: confirmed this session from a primary source or a reputable secondary source (fetched page or search result).
- **[V-sec]**: secondary or trade-press only.
- **[PK]**: from prior knowledge. The URL is believed correct but was not re-fetched this session, so re-check it before citing in the thesis.
- **[Vendor]**: company-reported and not independently verified.

---

## Q1. What autonomous clinical AI is actually deployed (closed loop, or a decision without a physician), and what are its outcomes and incidents?

### Takeaway
True "decision without a physician" autonomy exists in only a handful of narrow niches:
- binary or near-binary screening (diabetic retinopathy, normal chest X-ray);
- physiologic control loops (insulin);
- a protocolised administrative-clinical act (renewing prescriptions for stable chronic drugs).

Each niche gets its autonomy from a **narrow scope, a conservative operating point, and a hard escalation path to humans**, not from general competence. Surgical autonomy is still preclinical (pigs, ex vivo). EHR "agents" act autonomously mainly in revenue-cycle and administrative work (prior authorization), not in clinical order entry.

### Cited Findings

**Autonomous diagnostic AI: diabetic retinopathy (DR)**
- **2018, older.** IDx-DR (now LumineticsCore, Digital Diagnostics) received the first FDA De Novo authorisation for an autonomous AI diagnostic, which gives a result without a clinician reading the image. In its pivotal trial (900 subjects, 10 US primary-care sites) it reached sensitivity 87.2% and specificity 90.7%, against pre-specified superiority endpoints of 85% and 82.5%. **[PK]** — [Abràmoff et al., npj Digit Med 2018](https://www.nature.com/articles/s41746-018-0040-6)
- **ACCESS RCT (Nature Communications, Jan 2024).** Youth aged 8–21 with diabetes were randomised to point-of-care autonomous AI eye exams versus a referral to an eye-care provider. Exam completion within 6 months was **100% (n=81) vs 22% (n=83)**, p<0.001. Of the 25 abnormal results, **64% completed follow-through** with an eye-care provider, vs 22% in controls. The search did not confirm the device brand used. **[V]** — [Wolf et al., Nat Commun 2024](https://www.nature.com/articles/s41467-023-44676-z)
- A separate cluster-randomised trial tested autonomous AI and specialist-clinic productivity: 105 clinic days (51 with AI and 494 patients; 54 control days and 499 patients). Its headline finding is that the AI increased productivity. **[V]** for design; the effect size was not extracted — [PMC10550906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10550906/)
- A 2025 Ophthalmology Science paper gives health-system adoption lessons for autonomous DR AI. **[V]** that it exists; contents not extracted — [Ophthalmology Science 2025](https://www.ophthalmologyscience.org/article/S2666-9145(25)00233-7/fulltext)
- Implementation detail: the LumineticsCore system includes an **image-quality gating algorithm** that refuses to grade poor images. This is a built-in "know when not to act" mechanism. **[V]** — [PMC10788651](https://pmc.ncbi.nlm.nih.gov/articles/PMC10788651/)

**Autonomous radiology: normal chest X-ray (Oxipit ChestLink)**
- ChestLink holds what is described as the **first CE Class IIb mark for autonomous reporting** of chest X-rays with "no abnormality". Its autonomy covers only **normal** studies; abnormal studies still go to radiologists. **[V-sec]** — [Hardian Health](https://www.hardianhealth.com/insights/autonomous-ai); [Oxipit](https://oxipit.ai/)
- **Independent Finnish retrospective study (9,579 cases):** sensitivity **99.8%**, specificity **36.4%**. The AI correctly identified **1,692** studies as non-significant (about 18% of the workload). **[V-sec]** — [Oxipit research summary of the Radiology paper](https://oxipit.ai/research-paper/chestlink-performance/)
- A UK review notes that tuning autonomous normal-CXR systems to sensitivity above 99% yields specificities of only **28–67%**. Low specificity caps the share of work that can be automated. **[V-sec]** via search snippet; the PMC page was blocked by a bot check — [PMC13353222, "Autonomous reporting of 'normal' chest X-rays by AI in the UK"](https://pmc.ncbi.nlm.nih.gov/articles/PMC13353222/)
- **University Hospitals Birmingham (about 200,000 CXRs, retrospective):** **23.4% of normal scans** would have received an automated report. **[Vendor/V-sec]** — [Oxipit case study](https://oxipit.ai/case-study/the-impact-of-ai-on-radiology-insights-from-the-largest-retrospective-trial-in-uk/)
- Oxipit claims "99.9% sensitivity" and automation of "up to 40%". In one occupational-health setting with a healthy population it claims about 80%. **[Vendor]** — [Oxipit](https://oxipit.ai/); [case study](https://oxipit.ai/case-study/case-study-embracing-ai-for-efficient-chest-x-ray-reporting-and-quality-assurance/)
- 2025 deployments include an evaluation at Vestre Viken (Norway) and Unilabs adopting ChestLink and ChestEye across its European network. **[V-sec]** — [Oxipit knowledge base](https://oxipit.ai/knowledge_base_category/chestlink/)

**Autonomous prescription renewal: Doctronic in Utah (the first US state-sanctioned AI prescribing)**
- **Launch.** Announced 6 Jan 2026 under Utah's Office of AI Policy regulatory sandbox, through a Regulatory Mitigation Agreement (RMA). **[V]** — [Utah Commerce news release](https://commerce.utah.gov/2026/01/06/news-release-utah-and-doctronic-announce-groundbreaking-partnership-for-ai-prescription-medication-renewals/); [Office of AI Policy: Doctronic RMA](https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/doctronic/)
- **Mechanism of granting autonomy (Mello, JAMA Health Forum, 19 Mar 2026; 7(3):e261001):** **[V]** — [JAMA Health Forum](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2846947)
  - Physicians employed by Doctronic **review the AI's output prospectively for the first 250 patients**, then **retrospectively for the next 1,000 patients** once autonomous operation starts. This is an explicit, count-based graduated-autonomy ladder.
  - Scope: **192 drugs** for adult chronic conditions (hypertension, depression, contraception, diabetes, glaucoma, asthma, hyperlipidemia and others). The article does not say whether controlled substances are excluded.
  - Hard escalation triggers send a request to a physician when:
    - a newer Surescripts prescription differs from the patient's;
    - the patient or pharmacist asks for review;
    - the patient reports drug problems or health changes;
    - other clinical criteria are met.
  - Non-AI rule logic declines a renewal when guideline prerequisites (blood pressure checks, labs) are unmet, and renewal counts are capped "based on the accepted standard of care".
  - Utah agreed not to enforce its unprofessional-conduct laws in exchange for a contract with safety and privacy terms. Doctronic must submit performance reports (performance data, complaints, physician observations), indemnify the state, and hold a special malpractice policy. Its terms of service nonetheless **disclaim responsibility for accuracy or harmful outcomes**.
  - Pre-deployment evidence was **simulation on thousands of mock patients (not public)** plus a non-peer-reviewed preprint by equity-holding authors, studied in a different (urgent-care) population.
- **Price and volume.** About 190 drugs, roughly **$4 per renewal**. **[V-sec]** — [Medical Economics](https://www.medicaleconomics.com/view/utah-lets-ai-refill-chronic-prescriptions-in-state-backed-pilot-program); [Deseret News](https://www.deseret.com/business/2026/01/06/utah-artificial-intelligence-prescription-renewal-regulatory-sandbox-innovation-patient-safety/)
- **Company claim.** The AI's plan matched physicians' in **99.2% of 500 urgent-care cases**. **[Vendor]** — [Deseret News, citing Politico](https://www.deseret.com/business/2026/01/06/utah-artificial-intelligence-prescription-renewal-regulatory-sandbox-innovation-patient-safety/)
- **Opposition (Apr 2026).** **11 members of Utah's medical licensing board** asked for a halt. They had learned of the pilot from the news, and they cited blood thinners and interactions among their concerns. **Utah declined**, saying humans still review every refill in phase one. Oversight sits with a **5-member AI board that includes no physicians**. Doctronic said it expected to move to fully automated refills "soon". The FDA told AP it "has authorised no AI chatbots". **[V-sec]** — [The Next Web, 6 Jul 2026](https://thenextweb.com/news/utah-ai-prescription-refills-doctronic)
- **Six-month data.** Forbes (Jesse Pines, 21 Jul 2026) reports "6 months in, data are revealing". The page returned 403, so its figures are **not verified**. — [Forbes](https://www.forbes.com/sites/jessepines/2026/07/21/utah-let-ai-start-renewing-prescriptions-6-months-in-data-are-revealing/)
- **Other states.** Doctronic is reportedly in talks with Arizona, Texas and Wyoming. **[V-sec]** — [search summary of Deseret/Snell & Wilmer coverage](https://www.swlaw.com/publication/when-ai-writes-the-prescription-licensure-liability-and-the-corporate-practice-of-medicine-in-utahs-autonomous-ai-pilot/)
- Federal bill **H.R. 238** is cited alongside Utah as authorising AI to prescribe in an agentic capacity. **[V]** that it is cited — [LaRocco et al., arXiv 2606.25108](https://arxiv.org/abs/2606.25108)

**Closed-loop insulin (artificial pancreas): the most mature autonomous intervention**
- Hybrid closed-loop systems are routine. **Fully** closed loop, with no meal announcement or bolus, is still emerging.
  - **Diabeloop DBLG2** received **FDA 510(k) clearance in Jan 2026**. It is designed to need no meal announcements or manual boluses and is framed for type 1 diabetes. **[V-sec]** — [HCPLive](https://www.hcplive.com/view/diabeloop-s-dblg2-and-a-closed-loop-with-the-twiist-delivery-system-for-t1d)
- **Insulet Omnipod, fully closed loop in type 2 diabetes:**
  - EVOLUTION 2 (n=24, New Zealand) reported mean time in range **68% with no boluses**, a 24% improvement over standard injections. Median time below range was 0.14%, with no severe hypoglycaemia or DKA. **[Vendor]** — [Insulet/BusinessWire, 11 Mar 2026](https://www.businesswire.com/news/home/20260311660681/en/Insulet-Presents-Promising-Study-Results-for-Fully-Closed-Loop-Automated-Insulin-Delivery-System-for-Adults-with-Type-2-Diabetes)
  - FDA granted an investigational device exemption (IDE) in Mar 2026, and the **EVOLVE pivotal study (up to 350 adults)** started enrolling in May 2026. A 510(k) submission is planned for 2027 and launch for 2028. **[V-sec]** — [Drug Delivery Business](https://www.drugdeliverybusiness.com/insulet-initiates-study-fully-closed-loop-t2d/); [MedTech Dive](https://www.medtechdive.com/news/insulet-posts-clinical-data-on-fully-closed-loop-insulin-delivery-system/814516/)
- MiniMed and Tandem are also racing to remove meal announcements. Trade press flags the **"automation comes with trade-offs"** debate: less user control, and the risk of the algorithm mis-handling large meals. **[V-sec]** — [MedTech Dive](https://www.medtechdive.com/news/diabetes-tech-companies-are-racing-toward-fully-closed-loop-devices-but/821954/)
- Precedent RCT (older, 2023): a fully automated closed loop in adults with type 2 diabetes, an open-label crossover trial. **[V]** that it exists — [PMC9873557](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9873557/)

**Autonomous robotic surgery: SRT-H (Science Robotics, July 2025), preclinical**
- **SRT-H** (Surgical Robot Transformer-Hierarchy, Johns Hopkins, Axel Krieger's group) performed the clipping-and-cutting phase of cholecystectomy on **ex vivo pig tissue**. It completed **17 consecutive tasks** at expert-comparable quality, though more slowly.
  - It was trained by imitation learning on surgeon videos with language captions.
  - A high-level language policy calls low-level controllers, and it accepts spoken corrections from a human.
  - It worked on unmarked tissue, without a rigid pre-set plan.
  - Coverage claiming "100% accuracy" is not corroborated.
  - **[V-sec]** — [New Atlas](https://newatlas.com/robotics/worlds-first-robot-surgery/); [OR Manager](https://ormanager.com/briefs/robot-performs-autonomous-gallbladder-surgery-using-video-training-voice-feedback); [Cosmos](https://cosmosmagazine.com/technology/robotics/robot-gallbladder-surgery)

**AI agents acting inside EHRs (orders, referrals, prior authorization)**
- **Epic, HIMSS26 (Mar 2026):** Epic announced **"Agent Factory"**, a no-code builder for health-system agents, along with Cosmos-based models. Epic says more than 85% of its customers use Epic AI. Its revenue-cycle agent "Penny" covers prior authorization, utilization review, coding, denials and appeal letters. **[V-sec]** — [HIT Consultant](https://hitconsultant.net/2026/03/10/epic-ai-himss-2026-agent-factory-curiosity-foundation-models/); [Fierce Healthcare](https://www.fiercehealthcare.com/health-tech/epic-expands-ai-ambitions-agent-platform-cosmos-powered-predictions-and-deeper-workflow)
- **Summit Health:** prior-auth submission time fell **42%**, and **92% of AI-generated responses were accepted without edits**. **[Vendor/V-sec]** — [Capminds blog](https://www.capminds.com/blog/epic-ai-agents-every-health-system-should-consider/). The 92% "accepted without edits" figure is itself a possible automation-bias signal (see Q4).
- **CMS WISeR model:** AI-assisted prior authorization in traditional Medicare in **6 states from 2026**, with **licensed clinicians deciding every denial**. This makes autonomy asymmetric: the AI may approve but may not deny. **[V-sec]** — [RevelEMD HIMSS26 recap](https://www.revelemd.com/blog/why-himss-2026-mattered-for-medical-practices)
- An arXiv proposal, "Before the Tool Call", describes **deterministic pre-action authorization** for autonomous agents: policy checks run before each tool call. **[V]** that it exists — [arXiv 2603.20953](https://arxiv.org/pdf/2603.20953)

### Inferences
- Every deployed autonomous system follows the same safety pattern:
  1. a narrow indication;
  2. an asymmetric operating point (very high sensitivity for "normal" or "safe to act", accepting low specificity);
  3. an input-quality or eligibility gate (image-quality check; Surescripts mismatch; missing labs);
  4. escalation to a human.
- Autonomy is effectively granted to a *(task × population × operating point)* tuple, not to "the AI".
- The **automation yield** (the share of cases handled autonomously) is the economic variable. It ranges from about 18–23% (hospital CXR) to about 80% (healthy occupational cohorts). Yield depends on case mix more than on the model, which makes it a natural target for a method that *expands* the autonomous envelope safely.
- Asymmetric autonomy, where the AI may approve, renew or clear but must escalate denials and abnormal findings, recurs in WISeR, ChestLink and Doctronic. It looks like the de facto regulatory consensus for "safe-direction" autonomy.

### Gaps
- No independent post-market outcome data was found for Doctronic. The Forbes 6-month figures were inaccessible (403). Renewal counts, escalation rate and adverse events are unknown.
- No primary-source incident or recall database search was done (for example FDA MAUDE for LumineticsCore or AID systems). Reported incidents for autonomous AI remain unverified here.
- Real-world, prospective missed-finding rates for ChestLink were not obtained, because the UK review full text was blocked.
- No evidence was found of AI agents placing *clinical* orders autonomously in production. Order write-back is described only as "emerging".

---

## Q2. Which levels-of-autonomy taxonomies exist for medical AI, and how is autonomy granted, credentialed and monitored?

### Takeaway
There is **no consensus standard**. Proposals range from SAE-style 0–5 scales and LLM-agent levels (L0–L3) to a Lancet "clinical certification pathway" modelled on medical training. All are conceptual or preprint-stage and unvalidated.

Regulators control autonomy through *product authorisation plus pre-specified change control*: the FDA's PCCP (final, Dec 2024), the EU CE class, and sandbox contracts such as Utah's. None of these instruments is designed to **expand a deployed system's autonomy boundary incrementally on the basis of accumulating local evidence**.

### Cited Findings

**Taxonomies**
- **Lancet Digital Health comment (2020, older):** argues the assistive-versus-autonomous binary is too coarse and proposes graded autonomy based on risk determinants, using the US DOT/SAE driving levels as the model. **[V]** — [Bitterman, Aerts & Mak, Lancet Digit Health 2020](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(20)30187-4/fulltext)
- **The Lancet, Jan 2025: "A clinical certification pathway for generalist medical AI systems."** Proposes phased certification before greater autonomy is granted, **modelled on clinician training stages** (an "AI residency" analogue). **[V-sec]** via search snippet; full text 403 — [Lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02797-1/abstract)
- **"Evaluating Medical LLMs by Levels of Autonomy" (arXiv 2510.17764, 20 Oct 2025; Ye, …, Riaz, Zhou):**
  - Levels **L0 informational tools; L1 information transformation and aggregation; L2 decision support; L3 supervised agents**.
  - Proposes level-conditioned evaluation that matches metrics to the actions each level permits and the risks those actions carry.
  - Argues that benchmark scores do not show safe workflow performance.
  - **[V]** — [arXiv 2510.17764](https://arxiv.org/abs/2510.17764)
- **"The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy" (arXiv 2607.11175, 2026):** levels run from *assisted autonomy*, where every decision needs clinician confirmation, to *cooperative autonomy* within human-in-the-loop. **[V-sec]** — [arXiv 2607.11175](https://arxiv.org/pdf/2607.11175)
- **Dentistry six-level framework (L0–L5)**, from human-controlled to full operational autonomy within defined clinical contexts. Its authors state it **has not been empirically validated or consensus-developed**. **[V-sec]** — [PubMed 42453389](https://pubmed.ncbi.nlm.nih.gov/42453389/)
- **Non-medical: University of Washington, 2025 (arXiv 2506.12469).** Five agent-autonomy levels defined by the user's role: **operator, collaborator, consultant, approver, observer**. It also proposes **"AI autonomy certificates"**, the closest analogue to credentialing. **[V-sec]** — [arXiv 2506.12469](https://arxiv.org/html/2506.12469v1)
- **Human-training analogue.** ACGME requires residents to progress to **"oversight supervision"**, where care is reviewed after delivery. Surveys show programs struggle to reach it for senior residents. This maps directly onto Doctronic's switch from prospective to retrospective review. **[V]** — [PMC12493152](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12493152/)

**Regulatory mechanisms for granting and changing autonomy**
- **FDA PCCP final guidance (posted 3–4 Dec 2024)** replaced the April 2023 draft and widened scope from machine learning to all AI-enabled device software functions. A PCCP pre-authorises *specified* modifications (Description of Modifications, Modification Protocol, Impact Assessment), so a new submission is not needed for each change. **[V]** — [FDA Roundup 3 Dec 2024](https://www.fda.gov/news-events/press-announcements/fda-roundup-december-3-2024); [King & Spalding](https://www.kslaw.com/insights/articles/fda-publishes-final-predetermined-change-control-plan-guidance-for-ai-enabled-device-software-functions); [Ropes & Gray](https://www.ropesgray.com/en/insights/alerts/2024/12/fda-finalizes-guidance-on-predetermined-change-control-plans-for-ai-enabled-device)
- **State sandbox model (Utah):** autonomy is granted by contract, with a count-based ladder (250 prospective reviews, then 1,000 retrospective reviews), performance reporting, indemnity and insurance. It is overseen by a non-physician AI board. **[V]** — [Mello, JAMA Health Forum 2026](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2846947); [The Next Web](https://thenextweb.com/news/utah-ai-prescription-refills-doctronic)
- **Per-decision gating (proposal):** LaRocco et al. (arXiv 2606.25108, Jun/Aug 2026) argue that aggregate clearance metrics are insufficient. They name three **minimum conditions for autonomous prescribing**:
  1. calibrated per-prediction confidence with action-gated thresholds;
  2. separate signalling of epistemic and aleatoric uncertainty;
  3. inferential transparency at decision time, to allocate liability.

  In their **survey of 136 US prescribing clinicians**, respondents:
  - would not permit autonomous prescribing without confidence-based escalation;
  - preferred abstention for epistemic uncertainty but a competing-options summary for aleatoric uncertainty;
  - would accept liability only when inferential transparency was present.

  **[V]** — [arXiv 2606.25108](https://arxiv.org/abs/2606.25108)

**Technical building blocks: deferral, selective prediction, runtime monitoring**
- **Conformal selective prediction with cost-aware deferral for clinical triage under distribution shift (Sci Rep 2026):**
  - Produces set-valued predictions with **finite-sample coverage guarantees**.
  - Defers to clinicians when doing so lowers expected clinical cost.
  - Reports lower error on retained cases at **80% coverage** that holds up under temporal shift.
  - **[V-sec]** — [Sci Rep 2026](https://www.nature.com/articles/s41598-026-40637-w)
- **WATCH (arXiv 2505.04608, 2025):** adaptive monitoring of deployed AI using **weighted-conformal martingales**, i.e. sequential, anytime-valid tests for detecting when performance has broken. It cites a 2025 NEJM AI review of clinical AI monitoring. **[V-sec]** — [arXiv 2505.04608](https://arxiv.org/pdf/2505.04608)
- **JAMA Network Open: label-agnostic monitoring of a mortality model.** Drift-triggered continual learning and transfer learning mitigated performance degradation. **[V-sec]** — [JAMA Netw Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2834882)
- **Review of degradation detection and correction for medical AI (arXiv 2506.17442, 2025).** **[V-sec]** — [arXiv 2506.17442](https://arxiv.org/pdf/2506.17442)
- **Learning-to-defer bias (arXiv 2608.28050, 2026):** deferral policies can concentrate certain case types on specific humans, which amplifies **human** bias ("Too Much of the Same"). **[V-sec]** — [arXiv 2608.28050](https://arxiv.org/pdf/2608.28050)
- **Causal framework for evaluating deferring systems (arXiv 2405.18902, 2024).** **[V-sec]** — [arXiv 2405.18902](https://arxiv.org/pdf/2405.18902)

### Inferences
- Current frameworks describe *levels*, but almost none specify the **transition rule**: what evidence, gathered how, moves a system from level k to k+1 for a given task and population, and what automatically demotes it.
  - Utah's 250/1,000 ladder is the only operational transition rule found. It is a fixed count with no statistical stopping rule, no stratification by drug class or subgroup, and no demotion trigger.
- The PCCP pre-authorises *model* changes. In my reading it is not built for widening the **operational envelope** (automating a larger share of cases or new subpopulations) on the basis of local evidence. This is an inference and needs checking against the guidance text, which keeps changes within the intended use.
- The pieces of an "autonomy-expansion engine" already exist separately:
  - conformal selective prediction, which gives a coverage–risk guarantee;
  - anytime-valid sequential monitoring (WATCH-style martingales);
  - clinician-preferred uncertainty signalling (LaRocco).

  I found no work that **combines them into a credentialing protocol**: shadow mode, then a promotion test, then autonomous operation with audit sampling, then automatic demotion. This is the clearest opening for a novel contribution.

### Gaps
- The full text of the Lancet 2025 certification-pathway paper was not accessible (403), so its stages and criteria are unverified.
- No NEJM AI or Nature Medicine paper proposing a formal graduated-autonomy credentialing protocol with statistics was found. Absence is not proof; a targeted check of NEJM AI is recommended.
- EU AI Act and MDR provisions on autonomous AI (high-risk obligations from Aug 2026–2027) and the UK MHRA AI Airlock sandbox were not researched in this pass.

---

## Q3. Thailand: diabetic retinopathy AI deployments, Thai FDA SaMD rules, hospital robotics and MOPH policy on AI autonomy

### Takeaway
Thailand hosts one of the world's best-documented real-world DR-AI deployments (Google with Rajavithi and MOPH, 2018 onward). That programme is also the field's canonical cautionary tale: the CHI 2020 study of ungradable images and workflow friction.

Thai regulation treats AI as a medical device under the Medical Device Act B.E. 2551, with SaMD guidance, risk classes and modification guidance. However, **no Thai approval explicitly for *autonomous* clinical AI was found**, and policy and practice remain "AI assists, physician decides".

Chula/KCMH's Physical AI programme (Jan–Feb 2026) concerns service and rehabilitation robotics, not autonomous clinical decisions.

### Cited Findings

**Google ARDA DR AI in Thailand**
- **Prospective interventional study, older (Lancet Digital Health 2022).** 9 Thai MOPH primary-care sites, about **7,651 patients**. The AI's accuracy for vision-threatening DR was about **94.7% vs 93.5% for retina specialists**, with sensitivity and specificity comparable to or better than specialists. **[PK]** — [Ruamviboonsuk et al., Lancet Digit Health 2022](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(22)00017-6/fulltext)
- **Human-centred field evaluation, older (CHI 2020).** 11 Thai clinics. Real-world images were often rejected as ungradable (reported as more than one-fifth in early observation). Internet and upload delays and referral burdens disrupted workflow. **[PK]** — [Beede et al., CHI 2020](https://dl.acm.org/doi/10.1145/3313831.3376718)
- **Scale.** Google's Oct 2024 announcement reported more than **600,000 screenings globally** and a goal of **6 million AI-supported screenings across India and Thailand within 10 years**. Secondary coverage of a **Nature Medicine Comment (23 Sep 2026)** reports **more than 1 million patients** screened across India, Thailand and Australia.
  - Rajavithi Hospital is an anchor site, with Paisan Ruamviboonsuk as co-author.
  - Delivery is licensed through partners Forus Health, AuroLab and **Perceptra (Thai)**.
  - **[V-sec; primary Comment not accessed]** — [AI Weekly](https://aiweekly.co/alerts/google-arda-eye-screening-ai-crosses-one-million-patients); [AI Weekly](https://aiweekly.co/alerts/google-eye-ai-reaches-one-million-patients-in-three-countries)
- **Rajavithi trial NCT05166122:** an integrated AI plus **referral-tracking** system for real-time DR screening, i.e. a closed loop from screen to referral to follow-up. The registry shows it as recruiting, with no results posted. **[V]** — [ClinicalTrials.gov NCT05166122](https://clinicaltrials.gov/study/NCT05166122)
- No Thailand-only screened count for 2025–2026 was found.

**Thai FDA and law on SaMD and AI**
- The Medical Device Act B.E. 2551, Section 4, covers "products, software, or any other items" by intended medical purpose. Thai FDA guidance addresses screening, risk classification, registration and **software modification**. A 2026 article argues the Act has **limits for AI that shapes physicians' clinical decisions**. **[V]** — [Journal article, ThaiJO 2026](https://so02.tci-thaijo.org/index.php/jam/article/view/287392)
- **Class 1 SaMD auto-approval** has applied to listed categories since Jan 2025. Indicative review timelines: up to 200 days for Class 1, 250 days for Classes 2–3, and 300 days for Class 4. **[V-sec, consultancy]** — [meddeviceguide.com](https://meddeviceguide.com/blog/thailand-medical-device-registration-guide); [trustedtracemed](https://trustedtracemed.com/resources/thailand-fda-samd-registration.html)
- **UDI requirement for SaMD in risk classes 2–4** in force from **20 Jun 2026**, with soft enforcement. **[V-sec]** — [Siam Trade Development](https://www.siamdevelopment.com/medical-device-udi-thai-fda-2026/)
- **Malaysia–Thailand medical-device reliance pilot** Feb–Apr 2026, reportedly fully implemented in May 2026. **[V-sec]** — [deemedconsulting](https://www.deemedconsulting.com/thai-fda-medical-device-insights)
- **Human decision-maker principle.** Oct 2025 Thai reporting says the legal, judicial and **public-health** professions are moving toward AI frameworks and standards that keep **human experts as the decision-holders**. The health-side details were not found. **[V-sec]** — [Thansettakij, 16 Oct 2025](https://www.thansettakij.com/technology/ai/641504)

**Thai hospital robotics and automation**
- **KCMH and Chula Faculty of Medicine with True Digital, "Physical AI".** Launched 30 Jan 2026 (Chula release 11 Feb 2026) to build a "Digital Hospital through Digital Intelligence Fabric and Physical AI". The work covers robots for patient services, rehabilitation and treatment support, building on an earlier isolation-ward and rehabilitation robot prototype. **[V]** — [Chula news](https://www.chula.ac.th/en/news/287038/); [Newswise](https://www.newswise.com/articles/king-chulalongkorn-memorial-hospital-launches-physical-ai-powered-medical-robots); [True blog](https://www.true.th/blog/en/chula-2/)
- **Older KCMH "Mr SAM" robots:** outpatient registration and appointment rescheduling. A planned next stage for screening uncomplicated cases was **not confirmed**. **[V-sec]** — [Bangkok Post](https://www.bangkokpost.com/thailand/general/2726860/robots-to-speed-up-service-at-chulalongkorn-hospital); [Thai PBS World](https://www.thaipbsworld.com/world/robots-enter-service-at-chulalongkorn-hospital-to-help-with-the-paper-work)

### Inferences
- Thailand has the ingredients for a credible *graduated-autonomy* pilot in DR screening:
  - a nationally scaled AI (ARDA through Perceptra);
  - a public payer and MOPH network;
  - prior prospective validation;
  - a documented failure mode (ungradable images and referral non-completion);
  - a closed-loop referral-tracking trial already registered.

  The missing layer is the **governance protocol** that would let MOPH move a site from "AI assists, grader confirms" to "AI autonomously clears normals" on the basis of measured local performance.
- Thai FDA already has a **software-modification guideline** and risk classes. A capstone could propose a PCCP-like "autonomy-envelope change protocol" adapted to Thai FDA and MOPH. This is policy-plus-tool novelty, deliverable as a proof of concept.
- KCMH's Physical AI programme gives an institutional home, and a Medicine-plus-Engineering committee fits that.

### Gaps
- **No primary Thai FDA or MOPH document** on autonomous AI decision-making was found. The Thai Medical Council (แพทยสภา) has issued no AI-specific announcement found in this search. The "AI supports; doctor decides" stance is **inferred and reported secondhand**, not verified from an official text. Check tmc.or.th, the Royal Gazette (ราชกิจจานุเบกษา) and Thai FDA's SaMD pages directly.
- No information was found on autonomous-AI device approvals by Thai FDA, pharmacy dispensing robots at KCMH or other Thai hospitals, or a Thailand-only ARDA screening volume.
- The [PK] figures for the Thai 2022 prospective study and the CHI 2020 study should be re-verified before citing.

---

## Q4. Open problems (2025–2026): granting and revoking autonomy, continuous performance floors, liability, drift, automation bias and deskilling, and where a novel contribution fits

### Takeaway
Named open problems cluster around one missing mechanism: **a statistically principled, auditable way to grant, scale and revoke autonomy per task and per population after deployment**, while keeping human overseers both engaged and skilled. Evidence of deskilling exists in endoscopy. Evidence of rubber-stamping is suggestive (92% unedited acceptance in prior auth). Liability is being allocated by contract (Utah) rather than by design.

### Cited Findings
- **Deskilling (Lancet Gastroenterology & Hepatology 2025; Budzyń et al.; 10:896–903).** 19 experienced endoscopists (each with more than 2,000 colonoscopies) at 4 Polish centres. After routine AI introduction, adenoma detection in **non-AI** colonoscopy fell from **28.4% to 22.4%** within about 3 months. Caveats: observational design, mid-study department changes, and the need for randomised crossover trials. **[V-sec]** — [ACG EBGI summary](https://gi.org/journals-publications/ebgi/zhou_sep2025/); [UiO](https://www.med.uio.no/helsam/english/research/groups/clinical-effectiveness/news/2025/ai-colonoscopy.html); [Science Media Centre expert reaction](https://www.sciencemediacentre.org/expert-reaction-to-observational-study-looking-at-detection-rate-of-precancerous-growths-in-colonoscopies-by-health-professionals-who-perform-them-before-and-after-the-routine-introduction-of-ai/)
- **Oversight attention:** an eye-tracking study of gaze responses to **false-positive** CADe prompts during colonoscopy (arXiv 2609.25581, 2026). It is direct evidence that AI prompts capture the overseer's attention. **[V-sec]** — [arXiv 2609.25581](https://arxiv.org/pdf/2609.25581)
- **Liability and accountability in autonomous prescribing:**
  - The vendor disclaims responsibility while the state is indemnified.
  - Patients face barriers to obtaining records, which are reachable only after suit is filed.
  - Prospective oversight covers only the first 250 patients.
  - Renewal visits lose their value as touchpoints for screening and vaccines.
  - A pilot risks "scope creep" from a low-risk start.
  - **[V]** — [Mello, JAMA Health Forum 2026](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2846947)
  - Clinicians accept liability only with inferential transparency. **[V]** — [LaRocco et al., arXiv 2606.25108](https://arxiv.org/abs/2606.25108)
- **Governance legitimacy.** In Utah the medical board was bypassed, and oversight sits with a non-physician AI board. The state refused the board's request to halt. **[V-sec]** — [The Next Web](https://thenextweb.com/news/utah-ai-prescription-refills-doctronic)
- **Performance floor vs. throughput.** Autonomous CXR at sensitivity above 99% gives specificity of 28–67% and automation of about 18–23% in hospital settings. The floor directly caps the automation yield. **[V-sec]** — [PMC13353222](https://pmc.ncbi.nlm.nih.gov/articles/PMC13353222/); [Oxipit/Radiology summary](https://oxipit.ai/research-paper/chestlink-performance/)
- **Drift and monitoring:** label-agnostic shift detection and drift-triggered retraining (JAMA Netw Open), and anytime-valid conformal-martingale monitoring (WATCH). **[V-sec]** — [JAMA Netw Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2834882); [arXiv 2505.04608](https://arxiv.org/pdf/2505.04608)
- **Deferral can amplify human bias** by routing similar cases to the same humans. **[V-sec]** — [arXiv 2608.28050](https://arxiv.org/pdf/2608.28050)
- **Benchmarks ≠ workflow safety**, so evaluation must be conditioned on the level of autonomy. **[V]** — [arXiv 2510.17764](https://arxiv.org/abs/2510.17764)
- McKinsey (Sept 2026) names the "performance floor" and deskilling ("actively design against" it through supervised unassisted practice), but gives no measurement or certification method. **[V: internal summary]** — `00_guidance_mckinsey_summary.md`

### Inferences
Candidate novel contributions, ranked by fit for an MSc proof of concept with a Medicine-plus-Engineering committee:

1. **"Autonomy credentialing engine" (AI residency as code).** A runtime layer around any clinical model that does the following:
   - runs in **shadow mode**, logging AI decisions next to clinician decisions;
   - computes per-stratum conformal risk bounds, with strata such as site, camera, age and comorbidity;
   - **promotes** a stratum to autonomous action only when an anytime-valid sequential test shows the miss rate is below the floor (for example the upper bound of the false-negative rate below 1%);
   - keeps **random audit sampling** after promotion (as in Doctronic's retrospective 1,000);
   - **automatically demotes** a stratum when a martingale monitor detects drift.

   It turns Utah's ad hoc 250/1,000 ladder and the FDA PCCP idea into a statistically principled, auditable protocol. It is generalisable, and the novelty sits in the *mechanism*, not the model.
2. **Thai DR testbed.** Apply (1) to Thai DR screening with ARDA- or open-model outputs, taking the ungradable-image problem from CHI 2020 as a first-class "defer" class. The deliverable is a dashboard showing which sites and strata have "earned" autonomous clearance of normals. It aligns with MOPH scale and Rajavithi's referral-tracking trial.
3. **Anti-rubber-stamp oversight design.** Inject **known-answer probes** (seeded cases) into the overseer's queue to measure clinicians' vigilance and unassisted skill continuously. The probe results feed both the autonomy decision (is the human backstop real?) and a deskilling countermeasure. This answers McKinsey's unspecified countermeasure and the Budzyń finding.
4. **Asymmetric-autonomy policy formalisation.** Formalise "AI may approve or clear; must escalate deny or abnormal" as a cost-sensitive deferral objective, with liability-relevant transparency per LaRocco.

Option (1), carried through (2) and including (3), is the strongest combination.

### Gaps
- No peer-reviewed RCT was found on automation bias in clinicians overseeing *autonomous* (not assistive) AI. The 92% unedited prior-auth acceptance figure is vendor-reported and does not separate appropriate acceptance from rubber-stamping.
- No 2025–2026 legal analysis of Thai liability for autonomous AI errors was found. Who is liable under Thai law (physician, hospital, vendor) is unresolved in these sources.
- No public data shows anyone has *revoked* autonomy for a deployed clinical AI, i.e. a demotion event. Such case studies would be valuable but were not found.
- Research budget was exhausted before covering the EU AI Act, the MHRA AI Airlock, Singapore and Korea frameworks, and FDA MAUDE incidents.
