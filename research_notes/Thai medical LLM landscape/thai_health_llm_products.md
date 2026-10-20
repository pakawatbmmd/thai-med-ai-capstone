# LLM-powered health products in Thailand: deployed vs pilot vs announced (as of 20 Oct 2026)

Status labels used: **DEPLOYED** (source says in live use), **PILOT** (trial/POC/limited rollout), **ANNOUNCED** (plan/strategy only), **RESEARCH** (paper/model, not a product), **NOT-LLM / NO LLM FOUND**. "UNVERIFIED" = company self-report or claim not independently confirmed, or a detail drawn from a search snippet that could not be confirmed in the fetched page.

## Which LLM-powered health products exist in Thailand, and are they deployed, piloting or only announced?

### Takeaway
Clinician documentation (AI scribes) is the only category with clear, multi-hospital live use: Cariva MOR-ASR (465k+ sessions claimed, 30+ hospitals "live or POC") and Looloo Health PresScribe inside BMS-HOSxP (Azure OpenAI; 35-hospital pilot from Nov 2024). Everything else is staff-facing internal tools (Siriraj SiData+ Typhoon chatbot), small pilots (Eidy, AN AN Bot, MUSYA AI, Cariva voice agent, ThaiLLM medical model at Siriraj), or plain AI that isn't an LLM (Siriraj/Rama chest X-ray AI). National platforms (หมอพร้อม, NHSO 1330/LINE @nhso) and big consumer telemedicine apps (MorDee, Doctor Raksa, ooca, Doctor A to Z, BeDee) have no confirmed LLM feature.

### Cited Findings

**DEPLOYED: clinical documentation / AI scribes**
- **Cariva MOR-ASR** (CARIVA (Thailand) Co., Ltd.; BDMS-backed): a Thai-English medical AI scribe offered as a Chrome extension, SDK or "CARIVA Space". It drafts IPD SOAP notes, OPD clinical records and nurse notes. Company claims: up to 50% less documentation work; "465,000+ consultation sessions processed"; "30+ hospitals live or in POC (20+ private, 2 public, 1 medical school)". Logos shown: Siriraj Piyamaharajkarun, Bangkok Hospital, Samitivej, Praram 9 and Bangkok Hospital Chiang Mai. Says "zero data retention" (voice deleted after the service), ISO/IEC 29110, "PDPA compliant", supports JCI. No Thai FDA status, underlying LLM or live-vs-POC split is disclosed. Delivery is cloud/browser-based. — [cariva.co.th](https://cariva.co.th/en) (UNVERIFIED self-report)
- **Looloo Health PresScribe** (Looloo Technology) with **Bangkok Medical Software (BMS)**, a HIS vendor: transcribes doctor–patient conversations and summarises them into the record inside BMS-HOSxP / HOSxP XE. Built on **Microsoft Azure OpenAI Service** (specific GPT model not named). Service officially launched 1 Nov 2024 as a pilot in 35 hospitals nationwide, with expansion planned. "Up to 80%" saving in documentation time is a projection. BMS software overall is said to serve >90% of hospitals at all levels. No hosting or data-handling details and no formal evaluation (testimonials only). — [Microsoft Source Asia (TH), 26 Nov 2024](https://news.microsoft.com/source/asia/2024/11/26/bangkok-medical-software-utilizes-presscribe-ai-by-looloo-health-th/?lang=th); [Microsoft Source Asia (EN), 20 May 2025](https://news.microsoft.com/source/asia/2025/05/20/bangkok-medical-software-utilizes-presscribe-ai-by-looloo-health-to-enhance-healthcare-services-across-35-hospitals-in-thailand-en/)
  - No 2025–2026 update on PresScribe's hospital count was found.

**DEPLOYED: Cariva earlier and adjacent products**
- **PreceptorAI** (Cariva): medical chatbot on LINE, operating since April 2023, positioned as consultant and decision-support assistant for medical personnel. — [Khaosod English, 3 Apr 2024](https://www.khaosodenglish.com/sustain/2024/04/03/bdms-invests-in-cariva-for-ai-driven-personalized-diagnosis/)
  - A search summary attributed a 92–97% accuracy claim to a Cariva co-founder and an LLM-based colour-coded triage function, but neither appeared in the fetched article text (UNVERIFIED).
- **BDMS investment in CARIVA** (Apr 2024): BDMS called CARIVA a "medical AI developer of Medical Large Language Models" and said it had put more than 1,500 MB into Series A-level startup investments the previous year. A "Lab Interpretation" sandbox was trialled at the Health Design Center, Bangkok Hospital HQ (PILOT, 2024). — [Khaosod English](https://www.khaosodenglish.com/sustain/2024/04/03/bdms-invests-in-cariva-for-ai-driven-personalized-diagnosis/)
  - BDMS also listed ASR and a "Symptom Checkers Chatbot" among the BDMS/Cariva solutions. — [Everyday Marketing, 7 Apr 2024](https://everydaymarketing.co/brand/bdms-launches-medical-llms-medical-innovation-from-cariva/)
- **Cariva AI Translator app**: real-time medical speech-to-speech translation between staff and patients; claims PDPA/GDPR compliance. — [Google Play](https://play.google.com/store/apps/details?id=th.co.cariva.aitranslator)
  - A search snippet of a June 2026 Thairath piece said 27+ languages and no conversation data recorded. The page could not be fetched (UNVERIFIED). — [Thairath EN](https://en.thairath.co.th/money/business_marketing/trends/2939372)

**DEPLOYED: staff-facing internal LLM tools**
- **Siriraj SiData+ Admin Chatbot (Typhoon + RAG)**: a non-clinical chatbot for Siriraj staff covering data governance, data management and data-use R&D questions, available 24 hours. Uses the Typhoon LLM with RAG; answers can be traced to their sources. Data is processed and stored in Thailand. Phased rollout at 3/6/12 months. No usage numbers or quantitative metrics. — [OpenTyphoon blog, 23 Apr 2025](https://opentyphoon.ai/blog/th/use-case-siriraj-sidataplus-admin-chatbot)
- **Bumrungrad**: the IT leadership reports "rapid expansion of generative AI applications across both clinical and operational domains" since 2024, with no tools, models or scale named. A lab technician built an HTML app with **Claude Code** to help doctors choose genetic screening packages; its production status is unclear. Earlier, IBM Watson for Oncology (2014) was dropped as too expensive. — [HMA 2026](https://www.hospitalmanagementasia.com/tech-innovation/2026-what-hospital-leaders-across-thailand-are-learning-about-ai/)
- **Phyathai 3 Hospital**: staff use ChatGPT and Claude on their own phones (shadow/personal use, not an institutional deployment); the hospital runs a Friday "AI clinic". — [HMA 2026](https://www.hospitalmanagementasia.com/tech-innovation/2026-what-hospital-leaders-across-thailand-are-learning-about-ai/)

**DEPLOYED, LLM status unclear: patient-facing chatbots and symptom checkers**
- **Siriraj Health Bot ("SaeRé"/เซเร), LINE OA @sirirajhealthbot** (~Nov 2023): free AI chatbot that assesses symptom risk; the first phase covered ophthalmology only. Model not disclosed; no accuracy or validation data. — [Bangkokbiznews](https://www.bangkokbiznews.com/health/well-being/1101456); [Khaosod](https://www.khaosod.co.th/newspaper/newspaper-inside-pages/news_8017827)
- **Agnos Health symptom checker / LINE OA**: in the app for more than 3 years with >200,000 real users, and connected to LINE OA. The company says it was tested more than 100,000 times with specialists across 26 fields. Underlying model not disclosed (LLM not confirmed). — [Thansettakij](https://www.thansettakij.com/health/wellbeing/601151)
  - Agnos also powers Bangkok Hospital's AI self-registration and queue system (LINE, web and app notifications); this is not generative. — [Bangkok Hospital](https://www.bangkokhospital.com/en/content/news-agnos-health-and-bangkok-hospital-introduce-ai-driven-smart-management-system)
- **Bangkok Hospital HQ website "digital health assistant"** (Feb 2026, hospital-authored): AI translation into 8 languages, AI-generated audio for articles, AI specialist matching. Vendor and model not named. — [AustCham Thailand](https://www.austchamthailand.com/resources/news/bangkok-hospital-ai-driven-innovations-healthcare-transformation-bangkok-hospital)
- **icdevelop PAI-1 (Thai Pharmacy Assistant)**: a fine-tune of **Google MedGemma** (27B / 4B, open weights behind a gate, on-prem capable) for OTC requests, contraindication and interaction checks. The vendor says it is "In production at the pharmacy counter" but names no customer (UNVERIFIED). Sister model **TMA-1** (consumer health assistant: history-taking, red-flag referral, no diagnosis) has no production claim. — [icdevelop README](https://icdevelop-readme.static.hf.space/README.md); [HF TMA-1](https://huggingface.co/icdevelop/tma1-medgemma-27b)
- **True Digital "LLM platform"**: analyses initial symptom input to suggest possible diagnoses and treatment pathways. It is described among True's earlier "seven smart healthcare solutions" (with Intel), ahead of the Aug 2026 True–Thammasat–EGG Digital partnership. Hospital, model and status are not stated (UNVERIFIED). — [Hey Thailand News, 8 Aug 2026](https://heythailandnews.com/posts/thailands-ai-healthcare-revolution-how-thammasat-true-corporation-shape-hospital-future)

**PILOT**
- **Eidy** (Trillion Sure, founded early 2024; NIA-supported): "Multilingual Medical LLM" doctor's assistant, specialist Q&A chatbot and teaching aid. More than 400 doctors were trialling it in private hospitals and medical schools. An "AI clinic" with Ramathibodi was planned for 2025. Base model, deployment mode and accuracy metrics not given; no regulatory mention. Article appears to date from ~early 2025; current status unknown. — [Bangkokbiznews](https://www.bangkokbiznews.com/health/well-being/1161010)
- **ThaiLLM medical model at Siriraj** (BDI / MDES / NECTEC): the article says a medical model "is being piloted at Siriraj Hospital to help doctors and nurses screen patients". Models are first tested on NECTEC's blind-test benchmarking platform, then go through a "formal standardisation process" before critical use. The BDI ThaiLLM API has >1,700 users (general, not health). — [Bangkok Post, 3 Aug 2026](https://www.bangkokpost.com/business/general/3295694/launching-a-bid-for-ai-sovereignty)
- **Agnos "AN AN Bot"**: AI patient-question chatbot tested with Vimut Hospital and the Neurological Institute of Thailand; official launch was planned for early 2025. No confirmation that it launched was found. — [WealthyThai](https://www.wealthythai.com/en/updates/news-highlight/31768)
- **MUSYA AI** (ThaiHealth/สสส. + Ubon Ratchathani University), launched 16 Oct 2026: drafts local health-policy proposals for public-health officials (not clinical care).
  - Pilot: Health Region 10 with 110 provincial and district staff.
  - Data: 112,000 road-accident records, >1,000 files, plus 533 documents added after the pilot.
  - Results: usability 97/100, acceptance 4.70/5; its policy proposals scored 95/100 vs 72/100 for "general-purpose AI".
  - Next: may extend to Regions 7–9 for a 1-year trial. LLM not disclosed.
  - — [MGR Online](https://mgronline.com/politics/detail/9690000100264)
- **Cariva multilingual voice agent for hospital phone lines** (OpenAI × MHESI accelerator, launched 28 Aug 2026; Demo Day Nov 2026): handles appointment requests and recognises emergencies. Aims to deploy its first capability in a pilot hospital's live call flow by Demo Day. The accelerator's other health/wellness startups are Wello Food, Dietz, Precisionize and FitSloth. Underlying model not explicitly stated (OpenAI accelerator context). — [OpenAI](https://openai.com/index/supporting-next-generation-ai-startups-thailand/)
- **Ramathibodi CXRReportGen**: pilot multimodal report-drafting tool using Microsoft Foundry models BiomedCLIP and **Phi-3-Mini**. — [Microsoft Source Asia, 17 Apr 2026](https://news.microsoft.com/source/asia/2026/04/17/with-ramaai-thailands-radiologists-get-ai-assistance-to-screen-x-rays/)

**RESEARCH (not products)**
- **Typhoon-Si-Med-Thinking-4B** (Siriraj × SCB 10X, Jan 2026): produces ranked differential diagnoses; "early research stage", needs further testing with clinicians. — [The Story Thailand](https://www.thestorythailand.com/en/scb-10x-siriraj-typhoon-ai/)
- **Eir-8B**: Thai medical LLM; the paper says it is "deployed within the hospital's internal network" (hospital not named) via an on-prem encrypted API. Claims >10% over commercial Thai LLMs and >11% over GPT-4o across 18 Thai clinical tasks. The vendor site markets it for private-cloud hospital use but names no customers, scale or certifications. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523); [thaimedllm.com](https://www.thaimedllm.com/en) (deployment UNVERIFIED)
- **Pathumma (NECTEC)**: positioned for healthcare, but the confirmed deployments are government ones (Parliament, BORA chatbot). — [NSTDA](https://www.nstda.or.th/en/news/news-years-2025/pathumma-llm-ai-technology-tailored-to-thai-context-and-culture.html)

**ANNOUNCED**
- **NHSO (สปสช.)**: strategy to turn the 1330 hotline into an omni-channel "Smart Contact Center" where AI answers general questions and sorts cases for staff. No launch confirmed. — [Thansettakij](https://www.thansettakij.com/health-wellness/668423)
  - LINE @nhso currently does rights checks and service-unit changes, linked to Doctor at Home; no AI chatbot was found. — [Thansettakij](https://www.thansettakij.com/general-news/532128)
- **MOPH–True MOU** for an AI-5G "หมอพร้อม Super App" (2026), including 1 year of zero-rated data for True/dtac users. — [Kaohoon](https://www.kaohoon.com/pr/820211)
- **BeDee (BDMS)**: plans to add "Medical AI" in future. — [Daily News](https://www.dailynews.co.th/news/5311483/)

**NO LLM FEATURE FOUND / NOT LLM**
- **หมอพร้อม (MorProm, MOPH)**: >30 million users; digital referral used >3 million times (MOPH at WHA79, 19 May 2026); no LLM disclosed. — [Hfocus](https://www.hfocus.org/content/2026/05/38121)
  - The original 2022 MorProm chatbot was keyword-based (>1,000 keywords, ~150 questions), per a search summary (UNVERIFIED). — [ThaiPBS Policy Watch](https://policywatch.thaipbs.or.th/article/life-243)
- **MorDee (True Digital)**: telemedicine app with 500+ doctors and >200,000 users; no AI/LLM feature found. — [App Store](https://apps.apple.com/th/app/mordee/id1533061864); [Daily News](https://www.dailynews.co.th/news/4022058/)
- **Doctor Raksa**: 700+ doctors; acquired by Doctor Anywhere in Nov 2021. — [Marketing Oops](https://www.marketingoops.com/news/biz-news/doctor-anywhere)
- **ooca**: mental-health app, 180,000+ users, BDMS Series A. — [Thairath](https://www.thairath.co.th/money/tech_innovation/tech_companies/2620861)
- **Doctor A to Z**: "hospital on cloud", telemedicine and e-claims. — [BOI](https://www.boi.go.th/upload/content/DoctorAtoZ_608194cba35d2.pdf)
- No AI chatbot was found in any of these three apps (Doctor Raksa, ooca, Doctor A to Z).
- **Imaging AI (not LLM)**:
  - Siriraj SiAiR chest X-ray AI expanded to 610 hospitals under an NHSO benefit (Apr 2026). — [Thansettakij](https://www.thansettakij.com/health-wellness/666754)
  - Ramathibodi RAMAAI chest X-ray AI: 8 public hospitals, ~2,000 clinicians, 1,500–2,000 images/day, >500,000 images analysed; 10 more hospitals expected by Jun 2026. — [Microsoft Source Asia](https://news.microsoft.com/source/asia/2026/04/17/with-ramaai-thailands-radiologists-get-ai-assistance-to-screen-x-rays/)
- **Bumrungrad "Smart Personalized HealthMatch"**: checkup-package matching; not LLM-confirmed. — [Bumrungrad](https://www.bumrungrad.com/en/blog-news/smart-personalizd-healthmatch)
- **Samitivej**: AI colonoscopy (27,687 cases 2017–2025) and Smart OPD/IPD; no LLM assistant found. — [Samitivej](https://www.samitivejhospitals.com/page/world-best-hospital-thailand-bangkok)
- **Chulalongkorn Hospital**: True Digital partnership (30 Jan 2026) focused on "Digital Intelligence Fabric" and Physical AI/robots, not LLMs. — [KCMH](https://kcmh.chulalongkornhospital.go.th/digital-intelligence-fabric/)
- **Insurers (AIA Thailand)**: no gen-AI health bot found in searches.

### Inferences
- The only categories with real multi-site scale are ambient scribes. PresScribe's route, built into the dominant public-hospital HIS (HOSxP), is likely the biggest channel for LLM exposure in public hospitals. Cariva's route through BDMS-linked private hospitals is the private-sector equivalent.
- Foreign LLMs (Azure OpenAI in PresScribe; ChatGPT-4o in research; OpenAI in the accelerator; Claude/ChatGPT used informally by staff) dominate the products that are actually used. Thai LLMs (Typhoon, ThaiLLM/Pathumma) appear mostly in internal or staff tools and pilots. MedGemma appears only in one small vendor's open-weight models.
- "AI chatbot" claims from national platforms and older hospital LINE bots (หมอพร้อม 2022, Siriraj Health Bot 2023) are likely rule- or classifier-based, not LLMs. This is an inference from the keyword-based description and the lack of any model disclosure.

### Gaps
- No primary source names the specific LLM behind Cariva MOR-ASR/PreceptorAI, Agnos, Siriraj Health Bot, Eidy, MUSYA AI or the True symptom platform.
- No 2026 figures were found for PresScribe's hospital count, or for Cariva's split between live sites and POCs.
- No confirmation that AN AN Bot or the Eidy × Ramathibodi AI clinic actually launched.
- No evidence found of LLM features in Bangkok Hospital/BDMS patient apps (BeDee), Samitivej, MorDee, ooca, Doctor A to Z or Doctor Raksa, or in insurer health bots (AIA, Muang Thai). Searches were limited, so absence is not proof.
- No named on-prem hospital LLM deployment with patient data was confirmed: Eir does not name its hospital, and Typhoon on-prem cases are not documented.

## What evidence exists on evaluation, regulatory status and post-market performance?

### Takeaway
Almost all product-level evidence is vendor self-reporting: time-savings projections, session counts and internal benchmarks. The only rigorous Thai clinical evaluation found is a single-centre research study of ChatGPT-4o for ED triage, not a product. No LLM product has a disclosed Thai FDA (อย.) SaMD registration. The regulatory frame is the Medical Device Act's purpose test plus the PDPA, with a new non-binding PDPC AI guideline (7 Oct 2026).

### Cited Findings
- **Warin Chamrap Hospital study** (Thai J Emerg Med vol. 7(1), published 17 Jan 2026): voice-enabled ChatGPT-4o for ESI triage in 387 consecutive ED patients, 1 Apr–31 May 2025.
  - Agreement with the physician panel: weighted kappa 0.915 (95% CI 0.844–0.986) vs 0.607 for triage nurses.
  - Mis-triage: 5.9% vs 28.4% (under-triage 3.4% vs 5.2%; over-triage 2.6% vs 23.3%).
  - ESI 1–2 detection: AuROC 97% vs 84%.
  - Research only; single centre; reference standard was a physician panel rather than outcomes.
  - — [TCI ThaiJo](https://he02.tci-thaijo.org/index.php/TJEM/article/view/277102)
- **icdevelop vendor-run evaluation** of TMA-1 27B FP8 (200 or 120 cases per axis): knowledge 58.5% without RAG and 90.0% with RAG; deliberation 48.3%; safety/referral 98.3%. The vendor admits weak drug–drug interaction accuracy; no independent evaluation. — [icdevelop README](https://icdevelop-readme.static.hf.space/README.md)
- **Eir-8B**: benchmarks on MedQA, MedMCQA, PubMedQA and MMLU-medical, plus 18 Thai clinical tasks (>11% over GPT-4o). Preprint, not peer-reviewed in the source. — [arXiv](https://arxiv.org/abs/2409.08523)
- **Typhoon-Si-Med-Thinking-4B**: "preliminary evaluations" claim more accurate ranked diagnoses than larger commercial models; early research stage. — [The Story Thailand](https://www.thestorythailand.com/en/scb-10x-siriraj-typhoon-ai/)
- **MUSYA AI** pilot: usability 97/100, acceptance 4.70/5, proposal quality 95 vs 72 (general AI). Evaluation method not described. — [MGR Online](https://mgronline.com/politics/detail/9690000100264)
- **Scribe claims**: Cariva says up to 50% less documentation and 465k+ sessions ([cariva.co.th](https://cariva.co.th/en)); PresScribe projects up to 80% time saving ([Microsoft](https://news.microsoft.com/source/asia/2024/11/26/bangkok-medical-software-utilizes-presscribe-ai-by-looloo-health-th/?lang=th)). Neither publishes an accuracy or error-rate study.
- **Agnos**: says it was tested >100,000 times with specialists in 26 fields; no published methodology. — [Thansettakij](https://www.thansettakij.com/health/wellbeing/601151)
- **Eidy**: doctors anecdotally reported more accurate diagnoses; no metrics. — [Bangkokbiznews](https://www.bangkokbiznews.com/health/well-being/1161010)
- **Regulatory: Thai FDA (อย.)**
  - Software/AI with a medical purpose under s.4 of the Medical Device Act may be a medical device; diagnostic-support systems must pass FDA screening before manufacture or import. — [TRAINIAC summary of medical.fda.moph.go.th/samd-head](https://www.trainiac.ai/blog/ai-in-healthcare-thailand)
  - A 2026 legal article questions whether the Medical Device Act B.E. 2551 (2008) can govern AI that influences physician decisions. — [Journal of Arts Management](https://so02.tci-thaijo.org/index.php/jam/article/download/287392/189566/1334344)
  - อย. runs a course/pilot to help Thai medical-AI developers assess readiness for registration. — [Matichon](https://www.matichon.co.th/local/quality-life/news_5631491)
  - No LLM-specific อย. guidance was found.
- **Regulatory: PDPC (สคส.) AI guideline v1.0** (7 Oct 2026; non-binding):
  - Entering patient data into gen-AI may count as disclosure to the provider.
  - Use on-prem deployment or no-training agreements for sensitive data.
  - The physician makes the final decision for diagnostic AI.
  - AI contractors are processors under s.40.
  - — [TRAINIAC summary citing pdpc.or.th/28888](https://www.trainiac.ai/blog/ai-in-healthcare-thailand)
- **Regulatory: PDPA s.26** makes health data sensitive (explicit consent or an exemption needed); administrative fines for sensitive data go up to 5 MB.
  - Enforcement example (not AI): Aug 2025, a private hospital was fined 1.21 MB after >1,000 medical records leaked. — [TRAINIAC](https://www.trainiac.ai/blog/ai-in-healthcare-thailand)
- **MOPH (WHA79, May 2026)** set out three AI-governance directions: data protection, risk assessment, auditability and accountability from the start, plus scalable platforms and partnerships. These are not product-specific rules. — [Hfocus](https://www.hfocus.org/content/2026/05/38121)
- **ThaiLLM** says it uses NECTEC blind-test benchmarks and a "formal standardisation process" before hospital use; no published results. — [Bangkok Post](https://www.bangkokpost.com/business/general/3295694/launching-a-bid-for-ai-sovereignty)

### Inferences
- Scribes and staff tools are probably being positioned as non-medical-purpose software (documentation or administration) to fall outside SaMD. This is an inference consistent with the FDA purpose test; no product states it explicitly.
- Vendor privacy claims ("zero data retention", "data stays in Thailand", "PDPA compliant") stand in for independent audits. The new PDPC guideline would push cloud-LLM scribes such as Azure-based PresScribe toward no-training contractual terms.

### Gaps
- No Thai FDA registration or listing for any LLM product was found (the FDA SaMD database was not searched directly).
- No published post-market surveillance, incident reports, patient complaints or hallucination audits for any deployed Thai LLM product.
- The fetched pages did not give the Thai FDA's SaMD risk classes or the date of its AI guidance.

## What is missing: which products have no published evaluation, safety data or regulatory clearance?

### Takeaway
Every deployed or piloted LLM product in this inventory lacks independent peer-reviewed evaluation and a disclosed Thai FDA clearance. Most do not even disclose which LLM they run on.

### Cited Findings
- **No published evaluation, no FDA status, and model undisclosed:**
  - Cariva MOR-ASR, PreceptorAI and AI Translator ([cariva.co.th](https://cariva.co.th/en); [Khaosod English](https://www.khaosodenglish.com/sustain/2024/04/03/bdms-invests-in-cariva-for-ai-driven-personalized-diagnosis/))
  - Agnos symptom checker and AN AN Bot ([Thansettakij](https://www.thansettakij.com/health/wellbeing/601151); [WealthyThai](https://www.wealthythai.com/en/updates/news-highlight/31768))
  - Siriraj Health Bot ([Bangkokbiznews](https://www.bangkokbiznews.com/health/well-being/1101456))
  - Eidy ([Bangkokbiznews](https://www.bangkokbiznews.com/health/well-being/1161010))
  - True LLM symptom platform ([Hey Thailand News](https://heythailandnews.com/posts/thailands-ai-healthcare-revolution-how-thammasat-true-corporation-shape-hospital-future))
  - MUSYA AI: pilot scores only ([MGR Online](https://mgronline.com/politics/detail/9690000100264))
- **Model disclosed, but no evaluation or FDA status:**
  - PresScribe (Azure OpenAI): testimonials only. — [Microsoft](https://news.microsoft.com/source/asia/2024/11/26/bangkok-medical-software-utilizes-presscribe-ai-by-looloo-health-th/?lang=th)
  - Siriraj SiData+ chatbot (Typhoon): no metrics, but non-clinical. — [OpenTyphoon](https://opentyphoon.ai/blog/th/use-case-siriraj-sidataplus-admin-chatbot)
- **Vendor-only evaluation:**
  - icdevelop PAI-1/TMA-1 (MedGemma). — [icdevelop](https://icdevelop-readme.static.hf.space/README.md)
  - Eir. — [arXiv](https://arxiv.org/abs/2409.08523)
- **The only independent clinical evaluation found** (ChatGPT-4o triage, Warin Chamrap) concerns a general-purpose model used in research, not a deployed product. — [TCI ThaiJo](https://he02.tci-thaijo.org/index.php/TJEM/article/view/277102)

### Inferences
- The evidence gap is structural. Products that touch patients (symptom checkers, triage bots) give the least technical disclosure. Products with the most disclosure (Eir, icdevelop, Typhoon) are research or open-weight releases with little or no verified deployment.
- A 2024 Mahidol preprint names compute cost, privacy and Thai being a low-resource language as adoption barriers ([medRxiv](https://medrxiv.org/content/10.1101/2024.06.10.24308731.full.pdf)). These barriers fit the pattern seen here: cloud foreign-LLM scribes in production, Thai LLMs mostly in pilots.

### Gaps
- No information on incidents, complaints or adverse events for any product.
- No user-satisfaction or uptake data beyond vendor counts (Cariva 465k sessions; Agnos 200k users; PresScribe 35 hospitals).
- Could not access some primary pages: Thairath EN on Cariva (fetch failed), Bangkok Post BDMS–Cariva PR (404), and Hfocus pages behind 403 in places.
