# Thai Clinical IT and Data Environment for a Thai-Medical LLM Agent Harness (as of Oct 2026)

Scope note: researched 21 Oct 2026. About 30 searches and fetches, using Firecrawl, web search, and direct page scrapes. "Verified" means read on the primary or first-hand page. "Snippet only" means it came from a search summary and the page was not opened. Items dated before 2023 are marked [OLDER].

---

## 1. Hospital information systems (HOSxP, JHCIS, 43 files, HDC, FDH, university hospital EHRs) and data access

### Takeaway
Thai public-hospital data mostly sits in vendor HIS databases. The main one is BMS HOSxP / HOSxP XE, which runs on an SQL back end. Primary-care units (รพ.สต.) mostly run JHCIS or HOSxP-PCU. These systems feed two standard flat-file exports: the MOPH "43 แฟ้ม" set for HDC reporting, and the 16/13-file Financial Data Set sent to FDH for claims. BMS has an "API Gateway" and a new marketplace, but I found no public, documented clinical API. A realistic harness should therefore expect to read a 43-file-shaped extract or a de-identified SQL or FHIR snapshot. Live HIS APIs are not a realistic starting point.

### Cited Findings
- HOSxP is made by Bangkok Medical Software (BMS). A pharmacist started it in 1999. Wikipedia says it serves "over 300 hospitals". The page lists claimed SQL back ends (MySQL, MS SQL Server, PostgreSQL, Firebird), but that list is uncited. HOSxP-PCU is free, while HOSxP and HOSxP XE (v4, announced 2015) need a yearly subscription. The architecture is client/server with DCOM/DataSnap and Pascal scripting. **The article says nothing about an API.** — [Wikipedia: HOSxP](https://en.wikipedia.org/wiki/HOSxP); [SourceForge: HOSxP "300+ hospitals"](https://sourceforge.net/projects/hosxp/)
- A "BMS API Gateway" landing page exists at cloud4.hosxp.net, but it is only a login/welcome page with no public documentation. BMS has been promoting a "Build on BMS-HOSxP Marketplace" for third-party developers on Facebook in 2026. I did not see terms or docs. — [BMS API Gateway](https://cloud4.hosxp.net/); [BMS Facebook post on HOSxP Marketplace](https://www.facebook.com/BangkokMedicalSoftware/posts/-build-on-bms-hosxp-marketplace-%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%84%E0%B8%95%E0%B9%8C%E0%B8%AA%E0%B8%B2%E0%B8%A2-tech-%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%84%E0%B8%A7%E0%B8%A3%E0%B8%9E%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%A7%E0%B9%88%E0%B8%B2%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%88%E0%B8%B0%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B8%99%E0%B8%B1%E0%B8%81/1597179925745772/) (snippet only)
- Thai academic work has built record-search tools that connect directly to the HOSxP database. This suggests that in practice integrators work through DB-level access, not a vendor API. — [TBPS ThaiJO paper: EMR search program connected to HOSxP](https://li01.tci-thaijo.org/index.php/TBPS/article/download/179712/127604) (snippet only; date not checked)
- **JHCIS** is the primary-care system that MOPH's ICT centre developed around 2004–05 for รพ.สต./PCU. It covers OPD and health promotion/prevention. JHCIS and HOSxP-PCU use different databases and different entity names for the same data, so merging data needs careful mapping. — [R8 MOPH "JHCIS the past-now-future" (2019)](https://r8way.moph.go.th/r8wayNewadmin/page/upload_file/20190820113100_JHCIS%20the%20past-now-future.pdf) [OLDER]; [ThaiJO DCJ article](https://he01.tci-thaijo.org/index.php/DCJ/article/download/149499/109742/400823) (snippet only)
- **43-file standard and HDC.** An MOPH HDC presentation (2023) says HDC began on Pentaho about ten years earlier and moved to cloud. The file set grew from 12 to 21 to 43 files. The latest version reference I found is "โครงสร้างมาตรฐานข้อมูลด้านสุขภาพ v2.2" (Sept 2016). Under it, รพ.สต. store OP/PP data, higher-level hospitals also store IP data, and everything goes to the provincial data warehouse. The deck lists known data-quality problems: records that don't match the standard structure, and duplicates across units. — [MOPH BDH breakout slides, 22 Aug 2023](https://bdh.moph.go.th/site/wp-content/uploads/2023/10/ห้องย่อย-3-22Aug2023-2.pdf); [HDC 2016 slides, PLG](https://pyh.moph.go.th/media/kunena/attachments/156/HealthDataCenter_2016_PLG.pdf) [OLDER] (snippets only)
- Several ThaiJO studies look at 43-file data-quality management in primary-care networks, such as Ban Kruat in Buriram. — [ThaiJO NKP journal](https://he01.tci-thaijo.org/index.php/nkpjournal_9/article/view/257651)
- **FHIR version of the 43 files.** SIL-TH and MOPH built the "MoPH-PC-1" FHIR IG, which converts the 43-file dataset to FHIR for primary-care exchange. — [SIL-TH IG index](https://www.fhir-ig.sil-th.org/) (verified)
- **FDH (Financial Data Hub).** From 1 Apr 2024, MOPH hospitals claiming UC (บัตรทอง) reimbursement from NHSO must send service data through MOPH's FDH as the only channel. FDH uses a "Financial Data Set 16/13 แฟ้ม". MOPH training material from Apr 2025 covers pre-check of rejected items, appeals, and handling items flagged "ติด C". A Sakon Nakhon study (May 2025 to May 2026, 18 hospitals) looked at FDH data-quality monitoring. — [PPTV: NHSO links FDH](https://www.pptvhd36.com/health/news/5144); [MOPH BDH FDH slides 2023](https://bdh.moph.go.th/site/wp-content/uploads/2023/08/2-3.3-finance-data-hub.pdf); [R8 FDH 2025 slides](https://r8way.moph.go.th/r8wayNewadmin/page/upload_file/20250421091353.pdf); [ThaiJO ECH Sakon Nakhon FDH study](https://he03.tci-thaijo.org/index.php/ech/article/view/5832) (snippets only)
- **University hospitals.** Siriraj contracted iSOFT for the SiHMIS front office (IPD Mar 2012, OPD Apr 2012) and Sysmex for SiLIS across 60 labs. IBA Health separately won a contract at Siriraj, date unclear. KCMH (Chula) has an in-house IT department page but names no current HIS vendor. — [Siriraj annual report 2011](https://www.si.mahidol.ac.th/th/annual-report2011/files/210.pdf) [OLDER]; [iTWire: IBA contract](https://itwire.com/it-industry-news/deals/iba-wins-$66m-hospital-contract-in-thailand) [OLDER, undated]; [KCMH IT dept](https://chulalongkornhospital.go.th/kcmh/en/dept/__trashed-13)
- SIL-TH's "Claimcon" IG, built with Clinixir Co., converts the five public claim datasets that all hospitals generate daily into FHIR. These are shared among 8 medical schools. — [SIL-TH IG index](https://www.fhir-ig.sil-th.org/) (verified)

### Inferences
- The most portable data contract for a Thai harness is a **43-file-shaped schema**. Its tables (PERSON, SERVICE, DIAGNOSIS_OPD, DRUG_OPD, LABFU, and so on) exist at every MOPH facility regardless of vendor. MoPH-PC-1 also provides a FHIR mapping. I did not re-verify the individual table names in this pass. They are commonly known but should be checked against the official spec.
- A laptop study should use **synthetic or de-identified 43-file / FHIR (MoPH-PC-1) records**. Live HOSxP integration is blocked by vendor access and PDPA.
- The university hospitals (Siriraj, Chula, Rama) run heterogeneous, partly in-house systems with no public interfaces. Treat them as research partners, not integration targets.

### Gaps
- No public HOSxP / HOSxP XE API documentation was found. The API Gateway's scope, authentication, and terms are unknown and are **hard to access**. You would need to contact BMS or a partner hospital.
- I did not find the current official 43-file spec version (post-2016) or a public HDC API. Facility-level HDC reports are public dashboards, but I did not verify any API.
- The FDH 16-file field list was not confirmed from an official manual.
- Current HIS vendors for Siriraj, Chula (KCMH), and Ramathibodi in 2024–26 were not found.

---

## 2. Standards and terminologies (FHIR, Health Link, PHR, TMT, TMLT, ICD-10-TM, CPGs, DDI resources, NHSO e-claim)

### Takeaway
Thailand's FHIR use is moderate and voluntary. Work is on R4 and there is no mandate. SIL-TH's MoPH-PC-1 is the base IG, with a draft TH Core from DMS/MOPH. There is no national FHIR terminology server. The national code systems a harness would need are TMT (drugs), TMLT (labs), ICD-10-TM (diagnoses), Thai DRG (grouping and payment), and NHSO/FDH claim files. TMT is actively maintained, with a release dated 19 Oct 2026 and roughly biweekly releases. It needs a free login to download, and it has a public TMT Browser. Health Link (national HIE) and Mor Prom (PHR) are live and growing, and a Digital Health Act is being drafted.

### Cited Findings
- **FHIR adoption (State of FHIR survey 2025).** Use is moderate and focused on R4. "No specific regulation mandates the use of standards in electronic health data exchange, including FHIR." There are no deadlines or fines, and government funds are available. There is **no national FHIR terminology server and none is planned**. Active use cases are prescriptions/pharmacy, referrals, terminology, diagnostic orders/reports, and International Patient Summary. Listed barriers are cost, unclear regulation, and limited FHIR skills. The base IG is fhir-ig.sil-th.org/th/mophpc1. — [Simplifier.net Thailand jurisdiction page](https://simplifier.net/jurisdictions/th) (verified)
- **SIL-TH IGs.** These include MoPH-PC-1 (43 files to FHIR), Claimcon (claims to FHIR, 8 medical schools), a terminology repo (terms.sil-th.org), and an extensions repo. Drafts include TH Core (DMS-sponsored, open for comment), TH Cancer (based on mCODE), TH Palliative, TH Dental, TRT (renal) Registry, and KT Registry. — [SIL-TH](https://www.fhir-ig.sil-th.org/) (verified); [packages.fhir.org TH](https://packages.fhir.org/jurisdictions/TH)
- **Health Link / national HIE (Nov 2025).** MOPH's special committee on the national digital health system approved four measures: (1) integrate public-health information systems nationwide; (2) link MOPH provincial facility data with Bangkok Metropolitan Administration facilities, which already feed **Health Link (national HIE), Mor Prom (หมอพร้อม), and the Public Health Cloud**; (3) link MOPH and Ministry of Labour data (checkups, flu vaccination); (4) set a framework for a **new Digital Health Act**, because "Thailand still lacks a central law governing health data exchange". MOPH also planned a government directive requiring integration with Health Link, and a PDPA MOU across 13+ agencies. Health Link and the Public Health Cloud went live in 2024. Mor Prom is being consolidated into a **"Mor Prom+" super app** that merges 50+ apps and adds an AI chatbot and chest-X-ray AI. — [Healthcare IT News, 10 Nov 2025](https://www.healthcareitnews.com/news/asia/thailand-moves-unify-national-health-data-systems) (verified)
- **Health Link scale (conflicting).** A government PR page says more than 400 public and private facilities participate. A 2023 MOPH deck cites 1,165 hospitals, including those still connecting. — [thailand.go.th event page](https://thailand.go.th/event-detail/-----------health-link--moph-cloud---400-); [MOPH digital transformation deck, Aug 2023](https://bdh.moph.go.th/site/wp-content/uploads/2023/08/1.2-Digital-transformation-in-Healthcare-sector-MOPH-digital-health-170823-TC.pdf) (snippets only)
- **TMT (Thai Medicines Terminology).** THIS (สมสท., Thai Health Information Standards Development Center) publishes it. The latest release file is **TMTRF20261019 (19 Oct 2026)**, which requires login to download. The published schedule shows releases on 2 Nov, 16 Nov, 8 Dec, and 21 Dec 2569 (2026), so roughly biweekly. Tools include the **TMT Browser** (tmt.this.or.th) and **TMT Connect**, used for new-item requests by companies and hospitals. There is also a separate TTMT (Thai traditional medicines) release for the NHSO Drug Catalogue. — [THIS TMT page](https://this.or.th/service/tmt/) (verified); [THIS home](https://this.or.th/)
- TMT is also listed on the national open-data catalogues as an ETDA Recommendation standard. — [ETDA Data Catalog](https://opendata.etda.or.th/dataset/e654bc68-abc4-40b3-a668-9b799ede6700); [gdcatalog.go.th](https://gdcatalog.go.th/dataset/gdpublish-dataset-16-021/resource/34f0f3f8-8ceb-4e6c-bbbe-eca43511772d)
- Hospitals map their local drug lists to TMT in a "Drug Catalogue" for NHSO claims. This mapping is a known operational burden. — [UC@KKPHO TMT drug catalogue guide, 2023](https://www.uckkpho.com/wp-content/uploads/2023/03/660221-Drug-cat-Program-edit.pdf) (snippet only)
- **TMLT (Thai Medical Laboratory Terminology).** THIS also publishes this national lab code set (listed on the THIS home page). A 2024 AeHIN presentation by Dr. Boonchai Kijsanayotin says TMLT is tied to reimbursement and data standardisation. It also flags outdated lab test lists and codes and the need to align with LOINC. **I found no published TMLT-to-LOINC crosswalk.** — [THIS home](https://this.or.th/); [AeHIN post](https://asiaehealthinformationnetwork.org/?p=2656) (snippet only)
- **ICD-10-TM / Thai DRG.** Thai DRG v6.2 (ศรท. with สวรส., Oct 2017) includes CC/DCL tables and CC-exclusion lists, and DRG is the basis of inpatient reimbursement. Public hospitals have used ICD-10 since 1994. Since 2015 they submit individual coded records to MOPH monthly. There is research on an ICD-10-TM ontology for infectious-disease coding support. — [TDRG v6.2 vol.1](https://medinfo.psu.ac.th/medrec/mediplus-lite/uploads/TDRGVersion6.2V1.pdf) [OLDER]; [JTMI ThaiJO](https://he03.tci-thaijo.org/index.php/jtmi/article/view/118); [Mahidol ICD-10-TM ontology](https://repository.li.mahidol.ac.th/items/af2ed339-f165-4059-8dd5-802d8e21bdf7/full) (snippets only)
- **NHSO and AI claim review.** As early as 2021, NHSO considered AI-assisted "pre-audit" claim review after fraudulent private-facility claims in 2020, and held a JICA workshop on Japan's AI claim review. — [JICA, Oct 2021](https://www.jica.go.jp/project/english/thailand/033/news/general/211020.html) [OLDER]
- **Drug-interaction resources usable in Thai.** A Thai study comparing DDI databases (Drugs.com, Liverpool, Micromedex) on HIV antiretrovirals against the National List of Essential Medicines 2021 found **low agreement**. Drugs.com flagged 302 pairs, Liverpool 222, and Micromedex 160. Prince of Songkla University built an in-house DDI-checking database earlier (MS Access era) and validated it at PSU and Narathiwat hospitals. A national "AI Drug Interaction Center" linked to the PHR has been proposed in Thai media, but the date and status were not verified. — [HSRI KB: PSU DDI system](https://kb.hsri.or.th/dspace/handle/11228/1694) [OLDER]; [SJST/PSU DDI comparison](https://sjst.psu.ac.th/index.php/article/168/PaperPDF/download); [Thansettakij](https://www.thansettakij.com/health-wellness/health/627474) (snippets only)

### Inferences
- **Harness tool belt (terminology layer):**
  - `tmt_lookup` and `tmt_normalize` over the TMT release file, offline and refreshed biweekly. It would map Thai/English trade and generic names to TMT GP/GPU/TP/TPU levels.
  - `tmlt_lookup` for labs.
  - `icd10tm_search` and `icd10tm_validate` for diagnoses.
  - `tdrg_group` or a CC/DCL checker for inpatient coding.
  - `fhir_validate` against MoPH-PC-1 / TH Core profiles.
  
  All of these can run fully offline on a laptop.
- No national terminology server exists, so the harness must **bundle its own local terminology service**. That is an argument for harness-level engineering over model capability.
- TMT has no built-in interaction or contraindication knowledge. A DDI tool must come from an external source, licensed (Micromedex/Lexicomp) or open (for example DrugBank-derived or RxNav-style). TMT therefore needs to be cross-mapped to RxNorm/ATC, and the low agreement between DDI databases argues for showing provenance in outputs.

### Gaps
- TMT licence terms for research or redistribution were not checked. Downloading requires an account.
- No TMLT-to-LOINC or TMT-to-RxNorm/ATC crosswalk was found publicly.
- The official ICD-10-TM version and licensing (MOPH SPS/สนย.) were not confirmed. It is believed to be a paid publication, but this is unverified.
- I found no Thai-language, open, maintained DDI database.
- I did not search for a curated index of Thai clinical practice guidelines (Royal Colleges, DMS, NHSO CPGs). This is an open gap.
- Current NHSO e-claim / FDH audit rules engine (the "ติด C" deny codes) is not publicly documented beyond training slides.
- I found no public Health Link developer API spec.

---

## 3. Thai LLMs' agentic and tool-use ability (Typhoon, OpenThaiGPT, Pathumma/ThaiLLM, Eir, benchmarks, tokenization)

### Takeaway
Several open Thai models in the 4–8B range claim function calling. The best documented are Typhoon 2 (BFCL-v3 EN plus machine-translated TH), Typhoon 2.5 (Qwen3 4B and 30B-A3B, Apache-2.0, function calling), OpenThaiGPT 1.5, Pathumma-llm-text-4.0.0 (4.5B, claims "structured tool use"), and OpenJAI-v1.0. Thai tool-calling evaluation is thin. All Thai function-calling benchmarks I found are **machine-translated BFCL**, and none is clinical. Thai medical models (Eir-8B, Typhoon-Si-Med-Thinking-4B) are QA/reasoning models without tool-use evaluation. This gap is exactly where a harness study adds value.

### Cited Findings
- **Typhoon 2 (arXiv 2412.13702, Dec 2024).** Function calling was evaluated on BFCL v3 in English and in a Thai version made by in-house MT. Overall Thai BFCL scores:

  | Model | Thai BFCL overall |
  |---|---|
  | Typhoon2-Qwen2.5-7B | 75.12 |
  | Typhoon2-Llama-8B | 74.24 |
  | Typhoon2-Llama-3B | 71.36 |
  | Typhoon2-Llama-70B | 70.89 |
  | OpenThaiGPT1.5-7B | 65.53 |

  English: Typhoon2-Qwen-7B 79.08 vs Qwen2.5-7B 74.81. The 70B model scored lower on English multi-turn (33.62) than the small models. Function-calling training data was partly translated from APIGen/ToolACE. — [Typhoon 2 paper](https://arxiv.org/html/2412.13702v1) (table excerpt verified via search snippet)
- **Typhoon API** supports OpenAI-style `tools` (example uses `typhoon-v2.1-12b-instruct`) and LangChain `bind_tools`. — [Typhoon docs: Tool Calling](https://docs.opentyphoon.ai/en/tool/) (verified)
- **Typhoon 2.5.** typhoon2.5-qwen3-4b is a 4B instruct model with 256k context, function calling, and an Apache-2.0 licence. A 30B-A3B MoE variant exists, and the collection was updated Oct 2025 with GGUF builds. I did not find Typhoon 2.5 tool-use benchmark numbers. — [HF: scb10x/typhoon2.5-qwen3-4b](https://huggingface.co/scb10x/typhoon2.5-qwen3-4b); [HF collection typhoon-25](https://huggingface.co/collections/typhoon-ai/typhoon-25)
- **Typhoon-S (arXiv 2601.18129, 2026).** This is a "minimal open post-training" recipe for sovereign LLMs. Tool use is reported on **BFCL v4 English only**. Thai evaluation covers chat and math. — [Typhoon-S arXiv](https://arxiv.org/pdf/2601.18129); [SCBX PDF](https://www.scbx.com/wp-content/uploads/2026/06/Typhoon-S.pdf) (snippets only)
- **OpenJAI-v1.0 (arXiv 2510.06847).** Its authors built **BFCL-v3-TH** by machine-translating BFCL-v3. — [OpenJAI arXiv](https://arxiv.org/pdf/2510.06847) (snippet only)
- **Pathumma (NECTEC/NSTDA).** Listings on third-party hosts include:
  - Pathumma Gemma-3-27B Thai (Apr 2025; 8B Thai tokens of continued pre-training plus 3M Thai QA pairs)
  - Pathumma-ThaiLLM-qwen3-8b-it-2.0.0 (Dec 2025, Apache-2.0)
  - Pathumma-ThaiLLM-8B-Think-3.0.0 (Jan 2026, "built upon the ThaiLLM foundation model")
  - **Pathumma-llm-text-4.0.0** (4.5B reasoning model, listed Aug 2026), which claims "structured tool use in both Thai and English", 262k context

  The Thai Parliament reportedly uses Pathumma for summarisation and drafting. NSTDA and Siam AI signed an MoU for a native Thai LLM (300M THB, June 2025). — [NSTDA news 2025](https://www.nstda.or.th/en/news/news-years-2025/pathumma-llm-ai-technology-tailored-to-thai-context-and-culture.html); [HF nectec org](https://huggingface.co/nectec); [Featherless: Pathumma-llm-text-4.0.0](https://featherless.ai/models/nectec/Pathumma-llm-text-4.0.0) (dates come from third-party hosts and are **unverified** against an official changelog)
- **Eir-8B (arXiv 2409.08523, Sept 2024).** This is a Thai medical LLM (8B). It was evaluated on MedQA, MedMCQA, PubMedQA, and MMLU-medical, and the authors claim more than 10% better than commercial Thai LLMs. It has a custom 18-task Thai clinical eval where it claims to beat GPT-4o by more than 11%. It is **"deployed within the hospital's internal network"** for security. No tool-use evaluation was reported. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523) (abstract verified)
- **Typhoon-Si-Med-Thinking-4B (Jan 2026).** Typhoon (SCB10X) built this with **SiData+ (Siriraj)**. It is Qwen3-4B-Instruct-2507 with RFT for ranked-list differential answers, reporting 94.73 accuracy / 90.68 MRR on list evaluation vs Gemini 2.5 Pro's 68.46 / 58.85. It is explicitly a research preview, **"never trained on Thai medical data and is not yet intended for Thai-language use"**, and was not evaluated for safety or hallucination. — [Typhoon blog](https://opentyphoon.ai/blog/en/typhoon-si-med-thinking) (verified); [arXiv 2509.20866](https://arxiv.org/abs/2509.20866)
- **Thai LLM leaderboards.** These are the OpenThaiGPT Thai LLM Leaderboard (HF Space) and Stanford HELM ThaiExam. They cover knowledge and exams, not tool use. — [Thai LLM Leaderboard](https://huggingface.co/spaces/openthaigpt/thai-llm-leaderboard); [HELM ThaiExam, Sept 2024](https://crfm.stanford.edu/2024/09/04/thaiexam.html)
- An unofficial "SakThai Bench v3" Thai tool-calling scaffold exists on HF (200-row target, only 8 real tasks). It is not a usable benchmark yet. — [HF Nanthasit/sakthai-bench-v3](https://huggingface.co/Nanthasit/sakthai-bench-v3) (snippet only)
- **Tokenization.** The original Typhoon paper reports its extended tokenizer (Mistral plus 5k Thai subwords) is **2.62x more efficient on Thai than GPT-4's**. It also notes GPT-2's 50k vocabulary needs **3.8x more tokens** for Thai than a 5k Thai-trained vocabulary. SeaLLMs reports Thai compression improving from 4.29 to 1.57 after vocabulary extension. — [Typhoon arXiv 2312.13951](https://arxiv.org/pdf/2312.13951) [OLDER, Dec 2023]; [SeaLLMs arXiv 2312.00738](https://arxiv.org/pdf/2312.00738)

### Inferences
- **What fits a 16 GB RTX 4090 Laptop** (this is an inference; quantisation memory was not measured here). Typhoon2.5-Qwen3-4B, Pathumma-llm-text-4.0.0 (4.5B), Typhoon2-Qwen2.5-7B / Llama-8B, Pathumma-ThaiLLM-8B, OpenThaiGPT1.5-7B, and Eir-8B all fit at 4- to 8-bit with room for the KV cache. Typhoon2.5-30B-A3B at Q4 is about 17–19 GB of weights, so it needs partial CPU offload. It is the "ceiling" model for that laptop.
- Thai BFCL scores (about 65–75%) mean roughly 1 in 4 calls fails even on generic tools. Harness features likely to dominate model choice are:
  - schema-constrained decoding (JSON grammar via llama.cpp / vLLM / Outlines)
  - argument validation against TMT/ICD code lists
  - retry and repair loops
  - "irrelevance" gating
- **Tokenization risk for structured output.** Thai has no spaces and uses combining vowels and tone marks. Byte-level fallback on non-Thai-extended tokenizers can split a Thai character mid-codepoint. Under constrained decoding this can cause invalid UTF-8 or truncated strings inside JSON. Two mitigations follow: tool arguments should be **code-keyed** (TMT ID, ICD code), not free Thai text, and Thai display names should be resolved by the tool, not generated by the model. This is a reasoned hypothesis. I found **no published study** of Thai tokenization in JSON tool calls.
- The fact that no Thai medical model has tool-use evaluation is itself a research opportunity. "Harness vs model" ablations on Thai clinical tool tasks appear to be unexplored ground, as far as these searches show.

### Gaps
- No native-Thai (non-translated) function-calling benchmark was found, and no clinical Thai tool-use benchmark either.
- No Typhoon 2.5 / Pathumma 4.0 / OpenThaiGPT 2.x tool-calling scores were found. OpenThaiGPT's latest release was not checked.
- Eir model weights, licence, and an HF repo were not verified ("EIRAI" naming unclear).
- I found no quantitative study of Thai text in JSON / grammar-constrained decoding failures.

---

## 4. Rules and guardrails (PDPA, Thai FDA SaMD, MOPH AI governance, Medical Council, data residency)

### Takeaway
Health data is "sensitive data" under PDPA s.26. Clinical care can use statutory exemptions, but secondary uses need explicit consent or another basis, and DPIAs are expected for AI tools. Cross-border/cloud transfer is the PDPC's stated focus in its 2026 draft healthcare guideline. Thai FDA regulates software, including AI, as a medical device by intended purpose. It has SaMD guidance from June 2024 (revised Oct 2024), and new UDI labelling rules for SaMD take effect 20 Jun 2026. MOPH has had a medical-AI development committee since Feb 2025 that stresses cybersecurity and PDPA. As of Oct 2025 the MOPH minister and the Medical Council were jointly drafting AI-use guidelines, with "the doctor remains the main decision-maker; AI is only a support tool". Thailand has no central health-data-exchange law yet, and a Digital Health Act is being drafted. Together these point to local, on-prem, human-in-the-loop, auditable harnesses.

### Cited Findings
- **PDPA s.26 (health data).** Health, genetic, and biometric data are sensitive categories, so explicit consent is needed unless an exception applies. Clinical activities may rely on statutory exemptions. Marketing, personalised recommendations, and before/after photos likely need explicit consent. — [Private AI blog](https://www.private-ai.com/en/blog/thailand-pdpa) (secondary)
- **PDPC draft healthcare guideline (consultation, reported 9 Jul 2026).** It asks for:
  - a separate legal basis for each processing activity
  - PDPA consent kept **separate from clinical informed consent** and withdrawable on its own
  - cross-border transfers as a key focus (overseas cloud, regional EMRs, global patient platforms)
  - **DPIAs for AI-enabled healthcare applications**
  - DPAs and due diligence for cloud and EMR vendors, labs, and telemedicine

  The article does not cover de-identification. — [HLC (law firm), Jul 2026](https://hlc.com/en/publications/thailand-pdpc-consults-on-first-healthcarespecific-data-protection-guideline) (verified; draft status)
- **MOPH medical AI committee.** The first meeting was on 18 Feb 2025, chaired by Dr. Viroj Eamsamran. It oversees AI projects across MOPH units and must ensure budget efficiency and compliance with **cybersecurity law and PDPA**. Projects discussed were AI chatbots, imaging AI, and **systems for verifying medical-data accuracy**. — [Hfocus, Feb 2025](https://www.hfocus.org/content/2025/02/33170) (verified summary)
- **MOPH and Medical Council (แพทยสภา), 9 Oct 2025.** Minister Pattana Promphat, acting as honorary president of the Medical Council, pledged to set AI-use guidelines with the Council that are "ปลอดภัย โปร่งใส และเป็นประโยชน์ต่อผู้ป่วย" (safe, transparent, beneficial to patients). The Council's position is **"แพทย์ยังคงเป็นผู้ตัดสินใจหลักในการรักษา ส่วน AI เป็นเพียงเครื่องมือช่วยสนับสนุน"** (doctors remain the main decision-makers; AI is only a support tool). The policy slogan is "หมอไม่ล้า ประชาชนไม่รอ" (doctors not exhausted, citizens not waiting). Target uses named: screening and preliminary diagnosis, radiology reading, **lab-result analysis**, treatment planning, AI-assisted telemedicine triage, and a 24-hour AI in a super app. The Medical Profession Act is also to be revised to accommodate technology. — [Hfocus, 9 Oct 2025](https://www.hfocus.org/content/2025/10/35551) (verified)
- **Digital Health Act.** In Nov 2025 MOPH said existing laws don't fully cover health-data transfer, AI, or telemedicine. The committee endorsed a drafting framework, and the minister said the two national systems will connect with "two-layer access control". — [Healthcare IT News, Nov 2025](https://www.healthcareitnews.com/news/asia/thailand-moves-unify-national-health-data-systems) (verified)
- **Thai FDA and SaMD.** The Medical Device Act B.E. 2551 (amended 2019) defines devices to include "products, software, or any other items" by intended medical purpose. Thai FDA SaMD guidance was issued June 2024 and revised Oct 2024. It covers screening, risk classification, registration, and software modification. A 2026 Thai law-journal analysis argues it is **insufficient when AI strongly shapes clinical judgment**, citing human oversight, transparency, bias, post-market monitoring, and model updates. — [Bangkok Univ. law journal (ThaiJO JAM), 2026](https://so02.tci-thaijo.org/index.php/jam/article/view/287392) (snippet only)
- **UDI labelling for SaMD.** The MOPH notification was published in the Government Gazette on 22 Dec 2025 and **takes effect 20 Jun 2026**. It brings in UDI requirements for SaMD for the first time. — [Tilleke & Gibbins](https://www.tilleke.com/insights/thailand-introduces-udi-labeling-requirements-for-software-as-a-medical-device/8/) (snippet only)
- Thai device classification is a four-class, risk-based scheme aligned with ASEAN (since 2021). Thai FDA software assessment references IEC 62304, ISO 14971, and ISO 13485. — [Pure Global](https://www.pureglobal.com/markets/thailand/thailand-medical-device-and-ivd-classification); [QuASoQ 2023 paper](https://ceur-ws.org/Vol-3612/QuASoQ_2023_Paper_03.pdf) (snippets only)
- ETDA's AI Governance Center published "Medical AI 101 for Health Professionals" in Thai. — [ETDA PDF](https://www.etda.or.th/getattachment/Our-Service/AIGC/Research-and-Recommendation/01-MedicalAI101forHealthProfessionalsEssential_TH-Piyaritt.pdf.aspx?lang=th-TH) (not opened)
- **The on-prem precedent is already established.** Eir-8B was deployed "within the hospital's internal network" for security and speed. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)

### Inferences
- **Guardrails a harness should implement:**
  - human sign-off before any write-back. This reflects the Medical Council's "AI as support" position.
  - full audit log of tool calls, inputs, and outputs, for DPIA and the FDA's post-market expectations
  - PII minimisation and de-identification before any model call
  - no outbound network calls by default, which avoids the PDPA cross-border issue
  - versioned terminology snapshots, so outputs are reproducible
  - an explicit "intended purpose" statement scoping the tool as documentation or administrative support, not diagnosis
- A research harness that only drafts documents or flags coding issues for human review sits more plausibly outside SaMD registration than one that triages or diagnoses. **This is not a legal conclusion.** The intended-purpose test decides it, and the official Thai FDA text was not reviewed.
- A local 16 GB laptop harness is directly motivated by four things: PDPA cross-border concern, DPIA requirements, MOPH's cybersecurity focus, and the lack of an exchange law.

### Gaps
- The official Thai FDA SaMD guidance text (2024 and its revision) and any AI-specific registration rules were not retrieved. The Thai FDA site was not accessed.
- No final Medical Council AI guideline or ประกาศ text was found, and its status as of Oct 2026 is unknown.
- No final PDPC healthcare guideline was found (draft as of Jul 2026). No MOPH-specific "AI guideline" document was found beyond the committee news.
- The PDPA section citations above come from secondary commentary. The statute text was not re-read.

---

## 5. Candidate Thai clinical tasks for a laptop harness study, and existing Thai AI products

### Takeaway
The best harness-study candidates are tasks where correctness depends on **looking up and validating against Thai code systems**, not on model knowledge:
- (1) medication reconciliation and normalisation to TMT, with a DDI check
- (2) ICD-10-TM / Thai DRG coding audit and FDH/e-claim pre-check
- (3) structured discharge summary or referral letter generation into a 43-file / FHIR (MoPH-PC-1) shape
- (4) lab interpretation keyed by TMLT

Guideline-based 1669 triage is higher-risk and lacks public Thai data. Existing Thai products focus on ambient scribing (PresScribe on HOSxP) and imaging. I found no product doing TMT reconciliation or ICD-10-TM audit with LLMs.

### Cited Findings
- **PresScribe (Looloo Health and BMS).** This AI ambient scribe records doctor-patient conversations and summarises them. It is integrated with **HOSxP / HOSxP XE** and built on Azure OpenAI with a medical-term speech-to-text model. It went live on 1 Nov 2024 as a pilot in 35 hospitals, and a later Thai report says more than 40 hospitals and over 30,000 cases. The vendor projects up to 80% less documentation time (not independently verified). — [Microsoft Source Asia, May 2025](https://news.microsoft.com/source/asia/features/bangkok-medical-software-utilizes-presscribeai-by-looloo-health-to-enhance-healthcare-services-across-35-hospitals-in-thailand/); [Dailynews](https://www.dailynews.co.th/news/5162723/) (snippets only)
- Mor Prom+ is planned with an AI chatbot and chest X-ray AI. — [Healthcare IT News](https://www.healthcareitnews.com/news/asia/thailand-moves-unify-national-health-data-systems)
- The MOPH AI committee's project list includes "systems for verifying medical data accuracy". This is a natural fit for 43-file / FDH data-quality checks. — [Hfocus, Feb 2025](https://www.hfocus.org/content/2025/02/33170)
- FDH data quality and claim rejection ("ติด C") are active operational pain points. There is training on pre-checking rejected items and appeals, and an 18-hospital study ran 2025–26. — [R8 FDH slides 2025](https://r8way.moph.go.th/r8wayNewadmin/page/upload_file/20250421091353.pdf); [ThaiJO ECH](https://he03.tci-thaijo.org/index.php/ech/article/view/5832)
- **1669 / Criteria Based Dispatch (CBD).** A KMUTT decision-tree DSS for 26 CBD symptom groups reports 82% accuracy vs 70% for human triage. A 2020 BMC MIDM triage app covers 25 CBD chief complaints and notes that wrong Initial Dispatch Codes waste or under-allocate resources. I found no สพฉ. (NIEMS) LLM deployment. — [KMUTT publication](https://kirim.kmutt.ac.th/converis/portal/detail/Publication/1504627774?lang=en_GB); [BMC MIDM 2020 via DOAJ](https://doaj.org/article/e9a5ae12827740c6bebbe66afd5704fa) [OLDER]
- There are automated ICD-10 coding studies in Thailand (KMITL classification, Mahidol ICD-10-TM ontology), but they are not LLM- or agent-based. — [KMITL](https://dspace.kmitl.ac.th/handle/123456789/15845); [Mahidol](https://repository.li.mahidol.ac.th/items/af2ed339-f165-4059-8dd5-802d8e21bdf7/full)
- Low agreement between DDI databases (302 / 222 / 160 flagged pairs) shows that DDI tool outputs need provenance and human review. — [SJST/PSU](https://sjst.psu.ac.th/index.php/article/168/PaperPDF/download)
- Typhoon-Si (Siriraj) shows Thai hospital and LLM-lab partnerships exist for clinical reasoning, though in English only so far. — [Typhoon blog](https://opentyphoon.ai/blog/en/typhoon-si-med-thinking)

### Inferences
These are ranked candidate tasks for a laptop harness study (judgement, based on the findings above).

1. **Medication reconciliation and TMT normalisation.** Free-text or HOSxP drug lists, in Thai, English, or brand names, are mapped to TMT, then checked for duplicates and dose/route. An optional DDI check is attached with a cited source.
   - Tools: `tmt_search`, `tmt_resolve`, `ddi_check`, `dose_range_check`.
   - The ground truth is a deterministic TMT release, so scoring is exact-match on TMT IDs.
   - It is easy to synthesise data, and the harness clearly matters through constrained ID output and lookup-then-verify.
2. **ICD-10-TM coding audit / FDH pre-claim check.** Given a synthetic discharge record, the harness proposes or validates principal diagnosis, comorbidities, and procedures, checks CC exclusions and DRG, and flags likely deny reasons.
   - Tools: `icd_search`, `icd_validate`, `tdrg_group`, `claim_rules_check`.
   - The financial pain is high, an "accuracy-verification" use case is endorsed by MOPH, and it is non-diagnostic, so regulatory risk is lower.
3. **Referral letter or discharge summary into a structured 43-file / FHIR (MoPH-PC-1) record.** Thai narrative text becomes coded fields, validated against the FHIR profile.
   - Tools: `fhir_validate`, the terminology tools, and a section-completeness checker.
   - This complements PresScribe-style scribing and aligns with Health Link exchange.
4. **Lab interpretation keyed by TMLT and reference ranges.** Abnormal-result explanation and follow-up suggestions.
   - Tools: `tmlt_lookup`, `ref_range`, `trend`.
   - This matches the Medical Council and MOPH's named "lab-result analysis" use case. However, I found no public TMLT-to-LOINC mapping, so data construction is harder.
5. **1669 CBD triage support.** This is a guideline-tool lookup over CBD protocol cards. It is clinically meaningful, but it is safety-critical, lacks public Thai call data, and is closer to SaMD. It is better suited as a small safety-focused ablation than as the main task.

Common evaluation design: run the same local model (for example Typhoon2.5-Qwen3-4B or Pathumma-4.5B) with and without the harness's tools, verification, and guardrails. Measure code exact-match, invalid-JSON rate, hallucinated-code rate, and unsafe-action rate. This directly tests "harness > model" on a 16 GB GPU.

### Gaps
- I found no public Thai clinical datasets with TMT / ICD-10-TM labels suitable for benchmarking. Synthetic data generation would be required.
- I found no LLM-based Thai product for TMT reconciliation, ICD-10-TM audit, or Thai discharge summaries beyond PresScribe. The hospital-internal tools at Siriraj, Chula, and Rama are unknown.
- The 1669 / NIEMS CBD protocol text and its licensing for reuse were not retrieved.
- Independent evaluations of PresScribe (accuracy, privacy) were not found.
