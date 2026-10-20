# Thai medical / health LLM benchmarks, datasets, leaderboards and reported scores (as of October 2026)

Status: final v2 (about 25 tool calls, roughly 20 distinct sources). Searches covered: firecrawl web and research search, Hugging Face Hub (datasets, models, papers), arXiv, medRxiv, PMC, IEEE, and model cards. "Self-reported" means the scores come from the model developer. "UNVERIFIED" means I could not confirm the claim from a primary source, or the source itself flags the numbers as unreliable.

## Q1. What Thai medical/health benchmarks exist? (size, format, license, URL)

### Takeaway
As of October 2026 there is no widely adopted, public, natively Thai medical benchmark of the kind KorMedMCQA, KokushiMD-10 or VM14K are for Korean, Japanese and Vietnamese. What exists falls into five groups: (a) one Thai medical-licensing-exam (ThaiNLE Step 1) mock set, which is in ENGLISH and only partly accessible; (b) Thai slices of multilingual medical benchmarks that were machine-translated and expert-reviewed (HealMed, MultiMed-X); (c) health-adjacent subsets of general Thai exam suites (ThaiExam/OpenThaiEval TPAT-1, MMLU-ProX Thai health category); (d) private or developer-internal Thai clinical task suites (Eir's 17-18 Thai clinical tasks, icdevelop's thai_pharma_bench, ThaiLLM-IQ's RAG QA); (e) a general Thai safety benchmark with only a few health-related categories (ThaiSafetyBench).

### Cited Findings
**A. Thai medical licensing exam (ThaiNLE / NL1)**
- ThaiNLE Step 1 mock exam set, built at Ramathibodi Hospital, Mahidol University (Dept. of Clinical Epidemiology & Biostatistics). It has 300 MCQs in the medRxiv preprint and 304 in the journal version. 10.2% have images (n=31). Questions cover 20 topic groups ("general principles" plus organ systems). The source is "Mock NL1 by RA53 (2021)". **The questions are in English, not Thai.** — [medRxiv 2024.12.20.24319441](https://www.medrxiv.org/content/10.1101/2024.12.20.24319441v1.full-text); [JEEHP 2025;22:16](https://www.jeehp.org/journal/view.php?number=562)
- Availability conflicts between versions. The preprint calls it a "private dataset, not publicly available". The JEEHP version says data files are on Harvard Dataverse (https://doi.org/10.7910/DVN/GIVTQY), but still lists "restricted dataset access" as a limitation. The preprint text is CC BY 4.0. — [medRxiv](https://www.medrxiv.org/content/10.1101/2024.12.20.24319441v1.full-text); [JEEHP](https://www.jeehp.org/journal/view.php?number=562)
- I found no public dataset or evaluation for ThaiNLE Step 2 (clinical) or Step 3 (OSCE/Thai-language), and no official Medical Council of Thailand (TMC) question release used for LLM evaluation. See Gaps.

**B. Thai slices of multilingual medical benchmarks**
- HealMed (arXiv 2608.19981, 2026). An expert-reviewed multilingual medical benchmark in 9 languages, including Thai, with 1,000 examples per language (9,000 total). Formats are MCQA (HeadQA, MedQA, MedExpQA, MMLU-Pro), NLI (BioNLI, MedNLI) and open-ended QA (ExpertQA-Bio, ExpertQA-Med, LiveQA), with open QA scored by an LLM judge on a 1-5 scale. The questions come from English and Spanish sources, so the Thai items are translations, not native Thai clinical content. Authors are at U. Tokyo, Yale, UC Berkeley, Stanford, MIT, Harvard and Korean universities; none are Thai. The dataset license was not stated on the page; only the arXiv license was given. — [arXiv HealMed](https://arxiv.org/html/2608.19981)
- MultiMed-X, introduced in the Med-CoReasoner paper (arXiv 2601.08267). 7 languages including Thai, 350 instances per language: 150 BioNLI plus 200 LiveQA long-form QA. Items were machine-translated from English, then each one was reviewed and revised by two native bilingual experts. The paper does not itemise Thai-specific model scores. — [arXiv 2601.08267](https://arxiv.org/html/2601.08267v2)
- MMLU-ProX. A translation of MMLU-Pro into 29 languages, including Thai. MMLU-Pro has a "health" category, so a Thai health slice exists inside MMLU-ProX. I did not retrieve Thai-health-specific scores. — [MMLU-ProX site](https://mmluprox.github.io/); [arXiv 2503.10497](https://arxiv.org/html/2503.10497v1)
- I found no Thai-translated MedQA/MedMCQA dataset on Hugging Face. A targeted search returned nothing, and HF dataset search for "thai medical exam" and "ThaiMedQA" returned no entries. I found no dataset named "ThaiMedQA". — [HF Hub search via MCP]; see Gaps

**C. Health-adjacent subsets of general Thai benchmarks**
- ThaiExam (SCB 10X / Typhoon; used in Stanford HELM Thai). Its TPAT-1 subset (121 MCQs, 5 choices) is the Thai Professional Aptitude Test for medical-school entry. It covers "reasoning and medical ethics", not clinical knowledge. Other subsets: ONET, IC, TGAT, A-Level. License Apache-2.0. — [HF typhoon-ai/thai_exam](https://huggingface.co/datasets/typhoon-ai/thai_exam); [HELM ThaiExam](https://crfm.stanford.edu/helm/thaiexam/v1.0.0/)
- OpenThaiEval (iApp). 1,232 questions in total, of which 515 are Thai national-exam items. It includes TPAT-1 (40 Qs) and O-NET science. It has no dedicated medical subset. 48.7% of rows are translated international benchmarks. The license is mixed: Apache-2.0 for iApp's contribution, while the exam items remain the property of NIETS/CUPT. — [HF iapp/openthaieval](https://huggingface.co/datasets/iapp/openthaieval)
- WangchanThaiInstruct (EMNLP 2025). A human-authored Thai instruction dataset (35,014 pairs per the ACL version; 28,098 per one arXiv snippet, so the count differs between versions). It has a medical domain (9.75%) verified by domain experts and is used for both evaluation and training. License CC BY-SA / NC. — [ACL Anthology 2025.emnlp-main.175](https://aclanthology.org/2025.emnlp-main.175.pdf); [arXiv 2508.15239](https://arxiv.org/pdf/2508.15239)
- SEA-HELM (AI Singapore) supports Thai and runs a public leaderboard. I found no medical/health task in its suite. — [SEA-HELM arXiv 2502.14301](https://arxiv.org/abs/2502.14301); [leaderboard eval details](https://leaderboard.sea-lion.ai/eval-details)

**D. Developer-internal / private Thai clinical suites**
- Eir "Clinically Adapted Thai Medical Tasks". The paper says 18 tasks; the model card lists 17 (NER, temporal extraction, paraphrasing, NLG, keyword extraction, classification, relation extraction, QA, summarization, abbreviation expansion, concept normalization, open-ended, MCQ, yes/no, translation, Thai extraction, ICD prediction). The scale looks like 0-10, but the scoring method was not described on the card, so treat it as UNVERIFIED. The suite is not released. — [HF EIRTHAIMED/Llama-3.1-EIRAI-8B](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B); [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- icdevelop thai_pharma_bench_v2 (200 lookup cases), thai_pharma_bench_v2_rag (200 cases) and deliberation_bench_v1 (120 cases). These are Thai community-pharmacy evaluations reported on the pai1-medgemma-27b model card. They are not public, and the repo is gated. — [HF icdevelop/pai1-medgemma-27b](https://huggingface.co/icdevelop/pai1-medgemma-27b)
- ThaiLLM-IQ "Medical Information Query" setting. Thai citation-grounded RAG QA, scored by BLEU for the response and Jaccard for citations. The test set is not described or released. — [HF ThaiLLM/ThaiLLM-30B-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ)

**E. Thai health datasets on HF that are training corpora, not benchmarks**
- ZombitX64/Medical-o1-Reasoning-SFT-Thai (Thai translation of HuatuoGPT-o1 SFT data, CC-BY-SA-4.0, 10K-100K) and ZombitX64/Medical-o1-verifiable-problem-Thai. — [HF](https://hf.co/datasets/ZombitX64/Medical-o1-Reasoning-SFT-Thai); [HF](https://hf.co/datasets/ZombitX64/Medical-o1-verifiable-problem-Thai)
- icdevelop/thai-medical-kb (gated). The training corpus for the TMA-1 Thai Medical Assistant models (tma1-medgemma-4b/27b). — [HF](https://hf.co/datasets/icdevelop/thai-medical-kb)
- AIoTx-Tech/thai_medicalCare_dataset (Apache-2.0, no card). — [HF](https://hf.co/datasets/AIoTx-Tech/thai_medicalCare_dataset)
- scb10x/med-datasets: Typhoon-Si medical training data, all English. — [Typhoon blog](https://opentyphoon.ai/blog/en/typhoon-si-med-thinking)

### Inferences
- The "Thai" NL1 evaluation measures medical knowledge on Thai-curriculum English items. It does not test Thai-language clinical comprehension. Even in its published form, it is not a reusable open benchmark.
- The only reproducible, cross-model Thai medical MCQ scores come from translated Western items (HealMed Thai). These miss Thai epidemiology (melioidosis, liver fluke/cholangiocarcinoma, dengue, snakebite, thalassemia), Thai drug brands, and Thai clinical guidelines.

### Gaps
- I could not confirm whether any public Thai-native medical MCQ set exists (for example, from Chula, Siriraj, Thai nursing or pharmacy council exams). None surfaced on HF or the web.
- I did not find whether NECTEC (Pathumma) or ThaiLLM (national LLM program) publish a medical eval suite. ThaiLLM-IQ only reports a RAG metric.
- I did not retrieve whether the WangchanThaiInstruct medical-domain test split has per-model medical scores.

## Q2. Reported scores, by model (self-reported vs independent)

### Takeaway
Independent Thai medical scores exist for frontier models only: GPT/Claude/Gemini on the English-language ThaiNLE mock, and GPT/Claude/Gemini/MedGemma/Qwen/Llama on HealMed-Thai. Every score for Thai-specialised medical models (Eir/EIRAI-8B, pai1-medgemma, ThaiLLM-IQ, Typhoon-Si-Med) is self-reported, mostly on non-public or English benchmarks. I found no head-to-head independent evaluation of Thai medical models against frontier models on a shared Thai benchmark.

### Cited Findings: cross-model score table

**Table 1. ThaiNLE Step 1 mock (English items, 304 MCQ; micro-accuracy, mean of 5 API runs; INDEPENDENT academic study, run Mar/Jun 2024)** — [JEEHP 2025](https://www.jeehp.org/journal/view.php?number=562)
| Model | Micro-acc | Macro-acc |
|---|---|---|
| GPT-4o | 88.9% | 89.1% |
| GPT-4 | 83.3% | 82.8% |
| Claude 3.5 Sonnet | 80.1% | 81.7% |
| Claude 3 Opus | 77.8% | 77.1% |
| Gemini 1.5 Pro | 72.8% | 75.5% |
| Gemini 1.0 Pro | 61.4% | 63.1% |
| Human pass mark (mean 2019-2024) | 52.3% (range 51.0-53.0%) | |
- All models passed. The top performers scored more than 2 SD above the national examinee average. Text-only accuracy was slightly higher than image-question accuracy. — [medRxiv](https://www.medrxiv.org/content/10.1101/2024.12.20.24319441v1.full-text)

**Table 2. HealMed, Thai-language slice (translated items; zero-shot accuracy %; INDEPENDENT, non-Thai authors, 2026)** — [arXiv 2608.19981](https://arxiv.org/html/2608.19981)
| Model | HeadQA-TH | MedQA-TH | MedExpQA-TH | MMLU-Pro-TH | BioNLI-TH | MedNLI-TH |
|---|---|---|---|---|---|---|
| o4-mini | 94.67 | 98.67 | 92.00 | 70.67 | 70.00 | 84.00 |
| GPT-5.4 | 86.67 | 97.33 | 92.00 | 73.33 | 68.00 | 84.00 |
| Gemini-3-Flash | 90.67 | 93.33 | 93.33 | 78.67 | 74.67 | 86.67 |
| Claude-Sonnet-5 | 93.33 | 90.67 | 89.33 | 69.33 | 68.67 | 88.00 |
| Claude-Opus-4.8 | 89.33 | 89.33 | 86.67 | 72.00 | 74.00 | 89.33 |
| Qwen3-32B (thinking) | 88.00 | 93.33 | 84.00 | 66.67 | 67.33 | 80.67 |
| HuatuoGPT-o1-72B | 86.67 | 86.67 | 84.00 | 68.00 | 63.33 | 78.67 |
| DeepSeek-V3 | 72.00 | 72.00 | 84.00 | 74.67 | 62.67 | 76.67 |
| LLaMA3.3-70B-Instruct | 73.33 | 81.33 | 77.33 | 64.00 | 61.33 | 70.67 |
| Qwen2.5-72B-Instruct | 76.00 | 69.33 | 80.00 | 60.00 | 57.33 | 80.00 |
| MedGemma-27B | 72.00 | 70.67 | 81.33 | 56.00 | 53.33 | 76.00 |
| Gemma-3-27B-it | 74.67 | 57.33 | 70.67 | 52.00 | 60.00 | 78.00 |
| Qwen3-32B | 58.67 | 69.33 | 64.00 | 46.67 | 58.00 | 67.33 |
| MediPhi | 37.33 | 45.33 | 34.67 | 29.33 | 57.33 | 38.00 |
- HealMed-Thai open-ended QA, LLM-judge score on a 1-5 scale (ExpertQA-Bio / ExpertQA-Med / LiveQA): GPT-5.4 4.52 / 4.46 / 4.56; Gemini-3-Flash 4.01 / 4.07 / 3.91; MedGemma-27B 3.68 / 3.72 / 3.77; MediPhi 2.31 / 2.14 / 2.08. — [arXiv 2608.19981](https://arxiv.org/html/2608.19981)
- Caveat: the per-task Thai accuracies are multiples of 1.33, which suggests about 75 items per task per language. Small n means wide confidence intervals. This is my inference, not stated in the source. No Thai-specialised model (Typhoon, OpenThaiGPT, Pathumma, Eir, ThaiLLM) appears in HealMed. — [arXiv 2608.19981](https://arxiv.org/html/2608.19981)

**Table 3. Thai-specialised medical models: SELF-REPORTED**
| Model (developer) | Benchmark | Reported score | Source |
|---|---|---|---|
| Llama-3.1-EIRAI-8B (EIR Thaimed) | MMLU-med subsets / MedQA / PubMedQA / MedMCQA (English) | Avg 71.9 (MedQA 64.5, PubMedQA 79.0, MedMCQA 58.6); "+Prob" variant avg 80.2 (MedQA 69.6, MedMCQA 67.1) | [HF card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B) |
| EIRAI-8B vs GPT-4o / Typhoon-v1.5x-8B / GPT-3.5 | 17-task Thai clinical suite (scale ~0-10, method unstated, UNVERIFIED) | Eir wins 13 of 17 tasks (e.g., QA 6.82 vs GPT-4o 6.11; MCQ 6.40 vs 5.40). GPT-4o is better on translation (7.79 vs 7.65), Thai extraction (8.62 vs 8.16) and ICD prediction (8.12 vs 6.41); summarization is tied (7.51). Typhoon-v1.5x-8B scores 3.16-7.16. | [HF card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B) |
| Eir-8B (paper) | Same | Claims ">10%" over commercial Thai LLMs and ">11%" over GPT-4o across 18 Thai clinical tasks. Human evaluation is mentioned, with no details in the abstract. | [arXiv 2409.08523](https://arxiv.org/abs/2409.08523) |
| pai1-medgemma-27b v26-DPO (I C Develop Co.; from MedGemma-27B-it) | thai_pharma_bench_v2 lookup, no RAG (n=200) | 50.5% (v20 46.5%, v24 43.0%) | [HF card](https://huggingface.co/icdevelop/pai1-medgemma-27b) |
| same | lookup + RAG (n=200) | 64.5% (v24 65.3%) | same |
| same | deliberation_bench_v1 (n=120) | 38.3% (v20 29.2%, v24 37.7%) | same |
| ThaiLLM-30B-IQ (Medical) (ThaiLLM) | Thai medical info-query RAG | Fine-tuned: BLEU 0.4331, citation Jaccard 0.5458. Base ThaiLLM-30B: 0.406 / 0.1786. The table row is labelled "ThaiLLM-8B-SFT-IQ", which is inconsistent with the model name. | [HF card](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ) |
| Typhoon-Si-Med-Thinking-4B (SCB 10X + SiData+ Siriraj; from Qwen3-4B) | ENGLISH MedQA, MedMCQA, MedXpertQA, MMLU-Pro Health; ranked-list eval | List eval 94.73 acc / 90.68 MRR vs Gemini 2.5 Pro 68.46 / 58.85. "Never trained on Thai medical data… not yet intended for Thai-language use." | [Typhoon blog, Jan 2026](https://opentyphoon.ai/blog/en/typhoon-si-med-thinking); [arXiv 2509.20866](https://arxiv.org/abs/2509.20866) |
- General Thai models have no medical scores. OpenThai 2.0 (iApp) reports OpenThaiEval Thai national exams at 0.842 vs Typhoon 2.5 at 0.742 and Pathumma think 3.0 (NECTEC) at 0.660. These are general exams, not medical, and self-reported. — [HF iapp/openthai2.0](https://huggingface.co/iapp/openthai2.0-qwen3.8-27b); [openthai.ai](https://openthai.ai/en/openthai2p0)
- The OpenThaiEval dataset card has a "baseline" table (GPT-4 85.2%, Claude-3 83.7%, OpenThaiGPT-70B 72.3%…). The card itself labels these "example baseline results". UNVERIFIED; do not cite them as real scores. — [HF iapp/openthaieval](https://huggingface.co/datasets/iapp/openthaieval)

### Inferences
- Eir's "beats GPT-4o" claim rests on an unreleased task suite with an undisclosed (probably LLM-judge) scoring method, against GPT-4o from 2024. It cannot be independently reproduced.
- Frontier models now score about 87-99% on translated Thai MedQA/HeadQA (HealMed). So Thai MCQ medical-knowledge tests are near saturation for frontier models, and they do not discriminate on safety or clinical-workflow quality.
- No scores were found for OpenThaiGPT, Pathumma, Typhoon 2/2.5 general models, or MedGemma on any Thai-native medical benchmark. MedGemma-27B base appears only in HealMed-Thai.

### Gaps
- Eir's exact scoring rubric, judge model and test-set size are not available. Its human-evaluation details are also missing (I fetched only the abstract).
- I could not access the pai1-medgemma public baselines comparing against GPT/Claude/MedGemma base, because the repo is gated; the card extract showed only version-to-version comparisons.
- I could not determine HealMed Thai translation QA details (translator, reviewer count for Thai) or the dataset license.

## Q3. Thai-specific safety, hallucination, triage, red-flag escalation, medication-instruction and patient-facing chatbot evaluations; clinician evaluation studies

### Takeaway
I found no Thai-language medical safety, triage or red-flag-escalation benchmark. ThaiSafetyBench (general Thai safety) touches health only through a few categories. Clinician-rated Thai evaluations exist only as small, single-application studies: a 5-pharmacist pilot, the Glumii GDM chatbot rated by 10 professionals, and Eir's unspecified human evaluation.

### Cited Findings
- ThaiSafetyBench (SCB 10X / Typhoon; ICLR 2026). 1,954 malicious Thai prompts across 6 risk areas and 17 harm types, about half grounded in Thai culture. The health-relevant categories are "Mental Health / Overreliance Crisis", "Causing Material Harm by Dissemination" (misinformation, including health risks) and "COVID-19" (Thai socio-cultural harm). It has no explicit medication, dosing, triage or self-harm category. License CC BY 4.0. ASR results appear in figures only; I extracted no numbers. — [arXiv 2603.04992](https://arxiv.org/html/2603.04992v2); [HF typhoon-ai/ThaiSafetyBench](https://huggingface.co/datasets/typhoon-ai/ThaiSafetyBench); [Typhoon blog](https://opentyphoon.ai/blog/en/thaisafetybench)
- Community pharmacists pilot (Prince of Songkla University; Digital Health 2024). 5 Thai community pharmacists rated ChatGPT-3.5 Thai-language answers to 3 special-population medication questions on a 1-5 Likert scale for accuracy, relevance, completeness and citation/limitations. The questions were chlorpheniramine for a 2-year-old, ibuprofen at 8 months' pregnancy, and fish oil with warfarin. At least 60% of accuracy ratings were 4-5, and 20-40% were neutral or disagree. This is the closest thing found to a Thai medication-instruction evaluation, and it is tiny. — [PMC11418248](https://pmc.ncbi.nlm.nih.gov/articles/PMC11418248/)
- Glumii (Chiang Mai University with Khon Kaen Hospital; IEEE Access, 4 Sep 2026). A Thai-language patient-facing RAG multi-agent chatbot for gestational diabetes, built on Gemini 2.5 Flash. 10 professionals (3 obstetricians, 4 nurse-midwives, 3 nutritionists) rated 75 questions × 3 trimesters (225 responses). Question-level accuracy was 84% (GDM 88-96%, nutrition 88%, general antenatal care 68-72%). Carbohydrate-estimation accuracy (Acc@0.5) was 92.8% on 125 foods. Reviewers noted "medical hallucinations" with vague terminology and confusion between screening criteria and control targets. The system includes a safe-fallback abstention. There was no real-patient testing; an RCT is proposed. — [IEEE Access 11679108](https://ieeexplore.ieee.org/abstract/document/11679108/)
- Eir-8B reports a "human evaluation… to ensure adherence to care standards and unbiased answers" and deployment inside a hospital network. I found no protocol, rater count or results. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- Developer disclaimers state that no safety evaluation was done. Typhoon-Si-Med-Thinking-4B "has not been evaluated for safety, guardrails, hallucination risks, or deployment reliability". The pai1-medgemma knowledge base is "not yet pharmacist-reviewed" with "534 entries flagged", and every output must be reviewed by a pharmacist. ThaiLLM-30B-IQ is "not suitable for patient-facing clinical advice / emergency use". — [Typhoon blog](https://opentyphoon.ai/blog/en/typhoon-si-med-thinking); [HF pai1-medgemma-27b](https://huggingface.co/icdevelop/pai1-medgemma-27b); [HF ThaiLLM-30B-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ)
- The ThaiLLM-IQ citation-grounded RAG metric (citation Jaccard) is the only Thai medical groundedness / hallucination-adjacent metric found. It is self-reported. — [HF ThaiLLM-30B-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ)

### Inferences
- Thai clinician evaluations so far are application validations with n ≤ 10 raters and n ≤ 225 responses. They are not reusable benchmarks, and none compares several LLMs under the same protocol in Thai.
- Medication instructions are a known Thai risk: OTC antibiotics and pharmacy self-care are common, which matches the focus of the pharmacist and pai1 work. Yet the only Thai pharmacy benchmark (thai_pharma_bench) is private and self-reported.

### Gaps
- I found no Thai triage, emergency or red-flag escalation dataset, no Thai symptom-checker evaluation, and no Thai multi-turn patient-simulation benchmark of the HealthBench or CRAFT-MD kind. The searches were general web and research queries; Thai-language queries were not tried, so Thai-language journals (for example, TCI ThaiJo) may hold small studies I missed.
- I found no Thai medical hallucination benchmark beyond ThaiLLM-IQ's citation metric.

## Q4. What evaluation gaps remain (what no benchmark yet measures)

### Takeaway
The Thai evaluation ecosystem measures exam-style medical knowledge, mostly via English or translated items, and generic safety. It does not yet measure Thai-native clinical reasoning, patient-facing safety, or real-workflow performance.

### Cited Findings (evidence for each gap)
- **No public Thai-language licensing-exam benchmark.** The only ThaiNLE set is English and only partly accessible, and Steps 2/3 are absent. — [JEEHP](https://www.jeehp.org/journal/view.php?number=562)
- **No Thai-native clinical content.** Cross-model Thai scores (HealMed, MultiMed-X) are translations of US, Spanish and English sources. — [HealMed](https://arxiv.org/html/2608.19981); [MultiMed-X](https://arxiv.org/html/2601.08267v2)
- **No independent evaluation of Thai medical models.** Eir, pai1, ThaiLLM-IQ and Typhoon-Si scores are all self-reported on private or English sets. — [Eir card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B); [pai1 card](https://huggingface.co/icdevelop/pai1-medgemma-27b); [ThaiLLM-IQ card](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ); [Typhoon-Si blog](https://opentyphoon.ai/blog/en/typhoon-si-med-thinking)
- **No Thai medical safety, triage or red-flag benchmark.** ThaiSafetyBench covers only generic health-misinformation and mental-health categories. — [ThaiSafetyBench](https://arxiv.org/html/2603.04992v2)
- **No major leaderboard has a Thai medical track.** SEA-HELM, HELM ThaiExam and OpenThaiEval have no medical track. TPAT-1 tests medical-school aptitude and ethics, not clinical knowledge. — [SEA-HELM](https://arxiv.org/abs/2502.14301); [ThaiExam](https://huggingface.co/datasets/typhoon-ai/thai_exam); [OpenThaiEval](https://huggingface.co/datasets/iapp/openthaieval)
- **Clinician evaluations are tiny and single-system.** — [PMC11418248](https://pmc.ncbi.nlm.nih.gov/articles/PMC11418248/); [Glumii](https://ieeexplore.ieee.org/abstract/document/11679108/)

### Inferences: what no benchmark measures yet (as far as these searches found)
1. Thai-language clinical vignettes reflecting Thai disease burden (melioidosis, opisthorchiasis/cholangiocarcinoma, dengue, leptospirosis, scrub typhus, thalassemia, snakebite) and Thai CPGs (Thai MOPH / RCPT guidelines).
2. Triage and red-flag escalation in Thai: whether a model tells users to go to the ED or call 1669, the Thai emergency number.
3. Thai medication instructions: Thai brand names, NLEM (national essential drug list) coverage, OTC antibiotic misuse, herbal/traditional Thai medicine and supplement interactions, and pregnancy/paediatric dosing. Only a 3-question pilot and a private pharmacy bench exist.
4. Patient-facing multi-turn dialogue quality in Thai: empathy, register/politeness (ครับ/ค่ะ), health literacy and readability, and dialects (Isan, Northern, Southern).
5. Hallucination and groundedness on Thai medical sources, with no released test set; ThaiLLM-IQ's internal metric is the only one.
6. Clinical documentation in Thai-English code-switched notes (EHR summarisation, ICD-10-TM coding). Eir claims ICD prediction internally, but nothing is public.
7. Multimodal Thai medical items: the ThaiNLE set has only 31 image items, and those are English.
8. Fairness, bias and privacy (PDPA) behaviour specific to Thai healthcare contexts.
9. Real-world or prospective outcome studies: no RCT or deployment outcome data found; Glumii only proposes an RCT.

### Gaps
- Coverage note: Thai-language search queries and Thai journal portals (ThaiJo) were not searched, so small Thai-language studies may exist. NECTEC, Chula, Siriraj and ThaiLLM program pages were not directly crawled beyond what search surfaced. The SEA-HELM leaderboard task list was not fully fetched; the "no medical task" finding comes from search results and the paper description and should be treated as likely but not exhaustively verified.
