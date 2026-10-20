# Thai Medical / Health LLMs: Model Inventory (as of 20 Oct 2026)

Scope note: this file covers models only, not deployed commercial products. Release dates are Hugging Face (HF) "last updated" timestamps unless a paper or announcement gives a date; treat them as approximate. HF model cards were read directly (raw README via the HF API) or, for gated I C Develop repos, through the public HF web page.

## Q1. Which Thai medical / health LLMs exist, and what are their base model, size, license, release date, modality and intended use?

### Takeaway
I verified four families of Thai-built medical LLMs, all open-weight or gated-open: (1) Eir / Llama-3.1-EIRAI-8B (Sep 2024); (2) the national ThaiLLM consortium's medical suite (8B-SFT-IQ, 30B-IQ, 27B-Prescreen(-Preview), 8B-ToolUse, 8B-IQ, 8B-MedApp v1 and v2, Jan–Aug 2026); (3) I C Develop's MedGemma derivatives (PAI-1 pharmacy and TMA-1 consumer health, 4B and 27B, Jul 2026); and (4) Typhoon-Si-Med-Thinking-4B from SCB 10X and Siriraj (Sep/Oct 2025). Typhoon-Si-Med is English-language, not Thai. I found no official medical variant of NECTEC Pathumma, OpenThaiGPT, iApp or KBTG, and no medical model from Chula or Ramathibodi.

### Cited Findings

**A. Eir AI: Llama-3.1-EIRAI-8B (and -8B-Prob, -8B-bnb-4bit)**
- Developer: the "Eir Team" (Yutthakorn Thiprak, Rungtam Ngodngamthaweewesuk, Songtam Ngodngamthaweewesuk MD). The paper "EIR: Thai Medical Large Language Models" is dated 17 Sep 2024. — [arXiv 2409.08523 / HF paper](https://arxiv.org/abs/2409.08523)
- Base: meta-llama/Llama-3.1-8B (the card says architecture "Meta-Llama-3.1-8B-Instruct"). 8.03B parameters. License: llama3.1. Languages: th, en. HF repo last updated 16 Sep 2024. Hosted by the inference provider featherless-ai. — [HF EIRTHAIMED/Llama-3.1-EIRAI-8B](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B)
- There are two variants. Eir-8B is "specifically trained for reading Electronic Health Records (EHR) data"; Eir-8B-prob "focuses on question-answering tasks". Repos: EIRTHAIMED/Llama-3.1-EIRAI-8B-Prob and a bnb-4bit quantization. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523); [HF EIRTHAIMED org](https://huggingface.co/EIRTHAIMED)
- Intended use: Thai clinical and EHR tasks (NER, ICD-10 prediction, summarization, translation, RAG) for professionals and patients. The paper says the model "is deployed within the hospital's internal network" but does not name the hospital. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- Training data includes the Open PMC-Patients / Open-Patients datasets, translated from English to Thai with GPT-4o. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- The card's own disclaimer says it is "not yet optimized for safe, practical use", should not be used for clinical decision-making "without further validation, including randomized controlled trials", and "real-world deployment is not recommended". — [HF model card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B)
- Modality: text only. — [HF model card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B)
- Evaluation code is on GitHub. — [github.com/EIRAI-Thaimedical/EIRAI](https://github.com/EIRAI-Thaimedical/EIRAI)

**B. ThaiLLM national consortium medical models (HF org "ThaiLLM"; training code at vistec-AI)**
- The GitHub repo vistec-AI/thaillm-medical-post-training holds prime-rl configs for ThaiLLM-8B-Prescreen, ThaiLLM-8B-ToolUse, ThaiLLM-8B-IQ and ThaiLLM-8B-MedApp. IQ uses SFT. Prescreen and ToolUse use RL. MedApp is SFT on the IQ config, then RL on the ToolUse config. The repo shows no license and no scores. — [GitHub vistec-AI/thaillm-medical-post-training](https://github.com/vistec-AI/thaillm-medical-post-training)
- Public medical datasets in the ThaiLLM org: med-facts, med-qas-golden, med-qas-golden-articles, med-articles, med-iq, med-prescreen, prescreen-profiles, med-app-instruct, med-tool-use (updated Jul 2025 – May 2026). — [HF ThaiLLM datasets](https://huggingface.co/ThaiLLM)
- **ThaiLLM-8B-SFT-IQ (Medical)**
  - Base: ThaiLLM-8B-SFT (qwen3 architecture, 8.19B), fine-tuned with LoRA (r=32, Unsloth, 3 epochs).
  - Thai only. Context length 4096.
  - Purpose: citation-grounded medical RAG/QA that outputs strict JSON `{"answer","citations"}` and answers "unknown" when the context lacks the answer.
  - "Not suitable for" diagnosis or treatment decisions, patient-facing clinical advice, or emergency use.
  - License: not stated. HF updated 19 Jan 2026.
  - — [HF ThaiLLM/ThaiLLM-8B-SFT-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-8B-SFT-IQ); also hosted on [Featherless](https://featherless.ai/models/ThaiLLM/ThaiLLM-8B-SFT-IQ)
- **ThaiLLM-30B-IQ (Medical)**
  - Base: ThaiLLM-30B (qwen3_moe, 30.5B total), LoRA SFT (r=16, LLaMA-Factory, 4-bit).
  - Same RAG/citation purpose and same exclusions as the 8B model.
  - License: not stated. HF updated 29 Jan 2026.
  - — [HF ThaiLLM/ThaiLLM-30B-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ)
- **ThaiLLM-27B-Prescreen-Preview**
  - Base: ThaiLLM/ThaiLLM-27B, QLoRA SFT (axolotl) on 989 synthetic doctor–patient conversations.
  - Purpose: predict disease, department and severity (Emergency / Visit Hospital / Observe at Home).
  - License: apache-2.0. HF updated 19 Jan 2026. HF lists the task as image-text-to-text.
  - — [HF ThaiLLM/ThaiLLM-27B-Prescreen-Preview](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen-Preview)
- **ThaiLLM-27B-Prescreen**
  - An RL fine-tune (prime-rl, LoRA r=64, 500 steps) of **google/medgemma-27b-text-it**, not of ThaiLLM-27B. It is distributed as a LoRA adapter served on top of MedGemma.
  - Trained on ThaiLLM/med-prescreen with rewards for disease, department, severity and format (weights 2.0 / 1.0 / 1.0 / 0.3).
  - Disease and department lists come from vistec-AI/thaillm-prescreen-rulesets.
  - License: not stated in the card. Inference: MedGemma's HAI-DEF terms likely apply.
  - HF updated 22 Apr 2026.
  - — [HF ThaiLLM/ThaiLLM-27B-Prescreen](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen)
- **ThaiLLM-8B-ToolUse**
  - An RL fine-tune of typhoon-ai/typhoon-s-thaillm-8b-instruct-research-preview.
  - Purpose: route requests to 8 medical-app tools: create/list appointment, create/list reminder, get_health_emergency_contact, prescreen, search_medical_facts, no_tool.
  - HF updated 25 Apr 2026.
  - — [HF ThaiLLM/ThaiLLM-8B-ToolUse](https://huggingface.co/ThaiLLM/ThaiLLM-8B-ToolUse)
- **ThaiLLM-8B-IQ**: listed on HF (updated 3 May 2026). I did not read its card. — [HF ThaiLLM org listing](https://huggingface.co/ThaiLLM/ThaiLLM-8B-IQ)
- **ThaiLLM-8B-MedApp v2.0.0** (current `main`, HF updated 12 Aug 2026)
  - Thai-English medical assistant with structured tool calling. qwen3 architecture, 8.19B.
  - It is a linear weight merge: 0.70 × MedApp v1 + 0.30 × ToolUse (MergeKit 0.1.4, no post-merge fine-tuning). v1 is preserved at tag `v1.0.0`.
  - Intended for "research and carefully monitored applications".
  - License: the card says the parent repos "do not currently expose explicit license metadata" and tells users to confirm terms with ThaiLLM.
  - A community GGUF exists (mradermacher/ThaiLLM-8B-MedApp-GGUF).
  - — [HF ThaiLLM/ThaiLLM-8B-MedApp](https://huggingface.co/ThaiLLM/ThaiLLM-8B-MedApp); engineering report at [github.com/c4n/thaillm-medical-merging-experiments](https://github.com/c4n/thaillm-medical-merging-experiments)
- **National context for these models**
  - A Thairath English article (Dec 2025) on BDI's launch of ThaiLLM said a specialized medical model for symptom screening was planned for early 2026. It would be built with Siriraj Faculty of Medicine and public hospitals, for preliminary assessment and self-care advice rather than diagnosis, with a prototype chatbot for public trial in April–May 2026. — [Thairath English](https://en.thairath.co.th/news/governmentpolicy/2901246). UNVERIFIED: the page returned a 500 error on fetch, so these details come from the search-engine snippet only.
  - VISTEC listed a workshop, "ThaiLLM – Diagnose the Future Built for Thai Patients", in April 2026. The listing gives inconsistent dates (21–22 vs 22–23 April). — [VISTEC events](https://vistec.ac.th/news-events/events/144)
  - Thansettakij cites medical-trial use of ThaiLLM at VISTEC. I saw the snippet only. — [Thansettakij](https://www.thansettakij.com/technology/ai/657014)

**C. I C Develop Co., Ltd. (HF "icdevelop"): MedGemma derivatives, all gated**
- **PAI-1 "Thai Pharmacy Assistant", pai1-medgemma-4b** (v25-DPO, "standard tier")
  - Base: google/medgemma-4b-it, 4.3B. LoRA r=64 SFT on thai_pharma_v24 (33,760 examples), then DPO (2,872 OTC-accuracy pairs + 3,776 deliberation pairs).
  - License: Health AI Developer Foundations (HAI-DEF) terms. Gated (auto).
  - Modality: image-text-to-text. Image input is only for medicine boxes, labels and prescriptions.
  - Intended use: Thai community-pharmacy OTC assistance. Must be paired with RAG over icdevelop/thai-pharma-kb.
  - Knowledge base contents: the TMT drug registry (~31,000 products) plus 1,918 AI-generated ingredient entries, of which 534 are flagged and not pharmacist-reviewed.
  - "Not a medical device." Clinical use without a licensed pharmacist is prohibited.
  - HF updated 26 Jul 2026. A demo Space exists.
  - — [HF icdevelop/pai1-medgemma-4b](https://huggingface.co/icdevelop/pai1-medgemma-4b)
- **pai1-medgemma-27b** (v26-DPO, "premium tier"; an FP8 build also exists)
  - Base: google/medgemma-27b-it, 27.4B. LoRA r=32 SFT on ~33k dialogues, then DPO on 6,648 pairs.
  - License: HAI-DEF. Marked "DRAFT pending pharmacist and legal review".
  - HF updated 28 Jul 2026.
  - — [HF icdevelop/pai1-medgemma-27b](https://huggingface.co/icdevelop/pai1-medgemma-27b)
- **TMA-1 "Thai Medical Assistant", tma1-medgemma-4b v2 (SFT)**
  - Base: google/medgemma-4b-it. LoRA SFT on ~11.8k Thai behavior dialogues. Two DPO experiments were reported as negative.
  - Consumer-facing: "educate, triage, refer". Covers health education, OTC selection, supplements, home devices, and red-flag/crisis referral (1669 for EMS, 1323 for mental health).
  - Out of scope: diagnosis, prescription-drug dosing, interpreting labs or images.
  - Gated (manual). Described as an "unreviewed draft for internal evaluation".
  - HF updated 29 Jul 2026.
  - — [HF icdevelop/tma1-medgemma-4b](https://huggingface.co/icdevelop/tma1-medgemma-4b)
- **tma1-medgemma-27b v1 (SFT)** (an FP8 build also exists)
  - Base: google/medgemma-27b-it. Same scope and terms as the 4B model.
  - HF updated 29 Jul 2026.
  - — [HF icdevelop/tma1-medgemma-27b](https://huggingface.co/icdevelop/tma1-medgemma-27b)
- **Other I C Develop repos**
  - icdevelop/tai1-qwen35-9b (+fp8), updated 4 Aug 2026, image-text-to-text. Its purpose and whether it is medical are UNVERIFIED; I did not read the card. — [HF icdevelop](https://huggingface.co/icdevelop)
  - Dataset icdevelop/thai-medical-kb (gated). — [HF icdevelop](https://huggingface.co/icdevelop)

**D. SCB 10X (Typhoon) × Siriraj: Typhoon-Si-Med-Thinking-4B (research preview)**
- Developers: Typhoon (SCB 10X) and the Siriraj Informatics and Data Innovation Center (SiData+), Faculty of Medicine Siriraj Hospital, Mahidol University. — [HF typhoon-ai/typhoon-si-med-thinking-4b-research-preview](https://huggingface.co/typhoon-ai/typhoon-si-med-thinking-4b-research-preview)
- Base and license: Qwen/Qwen3-4B-Instruct-2507, 4.41B. RL-trained to output ranked lists of candidate answers. Apache-2.0. **Primary language: English.** HF updated 7 Oct 2025. — [HF model card](https://huggingface.co/typhoon-ai/typhoon-si-med-thinking-4b-research-preview)
- Paper: arXiv 2509.20866. The title on the HF card is "Single Answer is Not Enough: On Generating Ranked Lists with Medical Reasoning Models". v2 (5 Jan 2026) is retitled "On the Robustness of Answer Formats in Medical Reasoning Models". Training data is the English AlphaMed set. — [arXiv 2509.20866](https://arxiv.org/abs/2509.20866)
- Card disclaimer: "not intended for medical use". — [HF model card](https://huggingface.co/typhoon-ai/typhoon-si-med-thinking-4b-research-preview)
- The partnership was publicized around January 2026. Coverage describes the model as a clinician-assisting differential-diagnosis tool. — [Brand Inside](https://brandinside.asia/?p=248011); [Marketeer](https://marketeeronline.co/archives/339799); [Brandbuffet tag](https://www.brandbuffet.in.th/tag/medical-thinking-ai/)

**E. Searched for but not found as an official medical model**
- **NECTEC Pathumma:** the nectec HF org has general models only (Pathumma-llm-text 1.0.0/4.0.0, Pathumma-ThaiLLM-qwen3-8b it/think 2.0.0, pathumma-thaillm-8b-think-3.0.0, vision/audio/STT/TTS, pathumma-crossborder-guardrail). None is medical. — [HF search: pathumma](https://huggingface.co/models?search=pathumma)
- **SCB 10X / Typhoon:** no "Typhoon-Med" or "typhoon2-*-medical" exists under scb10x or typhoon-ai. Repos named "typhoon-med" are individual fine-tunes (batprem, Ponrudee, NoteEB, Preeda, kongp007, Sakan1314; 2024–2026). — [HF search: typhoon med](https://huggingface.co/models?search=typhoon-med)
- **OpenThaiGPT:** no official medical model. There is a third-party Aekanun/openthaigpt-MedChatModel (Feb 2024). — [HF search: openthaigpt](https://huggingface.co/models?search=openthaigpt)
- **Other community "thai-med" fine-tunes:** amornpan/qwen2.5-32b-med-thai(-optimized, V1/V3) (Feb–Mar 2025); jettaponbb/thai-med-qwen; Aekanun/thai-med-qwen-12-2025. Contents and evaluations are UNVERIFIED. — [HF search: thai med](https://huggingface.co/models?search=thai%20med)
- **iApp, KBTG, Chula, Ramathibodi:** no HF medical LLM repos found (the kbtg HF namespace search returned nothing). Ramathibodi/Mahidol work found was an evaluation of general LLMs on the Thai licensing exam, not a model. — [Mahidol repository](https://repository.li.mahidol.ac.th/items/a56b5885-c0f4-4e61-87bd-28fc95007449/full)
- **General Thai LLMs that are not medical:** JAI-1 (75B) and OpenJAI-v1.0 (Qwen3-14B). — [arXiv 2510.08620](https://arxiv.org/pdf/2510.08620); [arXiv 2510.06847](https://arxiv.org/pdf/2510.06847)

### Inferences
- The ThaiLLM-27B-Prescreen line and MedApp's `prescreen` tool are very likely the realization of the "symptom screening model with Siriraj and public hospitals" announced for early 2026. I found no source that explicitly links them.
- The field converged in 2026 on small (4–30B) open-weight models fine-tuned from Qwen3 / ThaiLLM or from Google MedGemma. They are designed for RAG with external knowledge bases, not standalone recall.
- The Typhoon-Si-Med model should be classed as "Thai-developed medical model, English language", not as a Thai-language medical LLM.
- MedGemma-derived models (I C Develop, ThaiLLM-27B-Prescreen) inherit HAI-DEF terms, which restrict redistribution and use. Several ThaiLLM repos have no license metadata at all, which is a deployment risk.

### Gaps
- Exact public release and announcement dates for most ThaiLLM and I C Develop models; only HF update timestamps were available.
- The ThaiLLM-8B-IQ and icdevelop/tai1-qwen35-9b cards were not read.
- The underlying ThaiLLM-8B / 30B / 27B base models (developer list, base architecture) are outside this scope. The Thairath article with consortium details failed to load.
- Whether any of these models powers a named product. Only demo Spaces (icdevelop) and the Featherless hosting (EIRAI-8B, ThaiLLM-8B-SFT-IQ) were confirmed. Eir's paper claims an in-hospital deployment at an unnamed hospital.
- No closed or proprietary Thai medical LLM with a model-level disclosure was found.

## Q2. What benchmarks were they evaluated on, and what were the exact scores? (methodology; self-reported?)

### Takeaway
Every score found is self-reported by the developers. None is on the Thai national medical licensing exam (ThaiNLE), a public ThaiMedQA, or a Thai-translated MedQA/PubMedQA. Eir reports English medical MCQ benchmarks plus a GPT-4o-judged Thai clinical-task set. ThaiLLM and I C Develop report small in-house test sets (96–5,122 cases) scored by LLM judges, BLEU/Jaccard, or F1. Typhoon-Si-Med reports English benchmarks only.

### Cited Findings

**Eir-8B / Eir-8B-Prob** (self-reported; lm-evaluation-harness; English benchmarks) — [HF card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B); [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- Medical MCQ benchmarks (MMLU medical subsets, MedQA, PubMedQA, MedMCQA):

| Model | Clinical KG | Med Genetics | Anatomy | Pro Med | College Bio | College Med | MedQA | PubMedQA | MedMCQA | Avg |
|---|---|---|---|---|---|---|---|---|---|---|
| Eir-8B | 75.1 | 80.0 | 69.6 | 76.8 | 77.1 | 66.5 | 64.5 | 79.0 | 58.6 | 71.9 |
| Eir-8B-Prob | 83.8 | 89.0 | 83.0 | 84.9 | 89.6 | 75.7 | 69.6 | 78.8 | 67.1 | 80.2 |
| GPT-3.5 Turbo 1106 | 74.7 | 60.2 | 65.9 | 72.0 | 64.73 | 64.73 | 57.71 | 72.66 | 66.0 | 66.6 |
| Typhoon-v1.5x-8B | 75.9 | 79.0 | 63.7 | 70.6 | 77.1 | 63.6 | 59.7 | 74.4 | 58.0 | 69.1 |
| OpenThaiGPT-beta-7B | 37.4 | 38.0 | 4.5 | 32.7 | 36.1 | 32.4 | 32.4 | 62.0 | 31.8 | 34.1 |

- The paper describes using zero-shot, few-shot, CoT, and ensemble/self-consistency strategies. It does not say whether these benchmarks were translated to Thai. Inference: they appear to be the standard English versions. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- Thai general-language evaluation (SEACrowd), Eir-8B scores:
  - ThaiExam 0.418, M3Exam 0.458, XNLI 0.332, XCOPA 0.734.
  - Comparisons: Llama 3.1-8B-Instruct 0.441 / 0.446 / 0.335 / 0.732; Typhoon-v1.5x-8B 0.421 / 0.441 / 0.334 / 0.822; GPT-4-0613 0.602 / 0.560 / 0.623 / 0.920.
  - — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- Medical translation (custom set):
  - BLEU: Eir-8B 61.10; Eir-8B-Prob 47.91; Llama 3.1-8B-Instruct 35.74; Typhoon-v1.5x-8B 34.42.
  - — [HF card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B)
- "Clinically Adapted Model Enhanced" Thai test (18 tasks, GPT-4o as judge on a 0–10 scale):
  - Averages: Eir-8B 7.11, GPT-4o 6.38, Typhoon-v1.5x-8B 5.33, GPT-3.5 3.05.
  - Eir-8B scored highest in 15 of 18 categories.
  - GPT-4o scored higher on Medical Translation (7.79 vs 7.65), Medical Thai Extraction (8.62 vs 8.16) and ICD Prediction (8.12 vs 6.41), and tied on Summarization (7.51).
  - — [HF card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B); [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- The abstract states "human evaluation was conducted to ensure that the model adheres to care standards and provides unbiased answers". In the portion I read (the first ~45 KB of the paper text), I found no protocol or scores for this. — [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)

**ThaiLLM-8B-SFT-IQ** (self-reported; "Medical Information Query" setting) — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-8B-SFT-IQ)
- Response BLEU / citation Jaccard:
  - Qwen3-8B-Base: 0.267 / 0.075
  - ThaiLLM-8B-SFT: 0.406 / 0.133
  - ThaiLLM-8B-SFT-IQ: **0.4363 / 0.5485**

**ThaiLLM-30B-IQ** (self-reported) — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ)
- Response BLEU / citation Jaccard: ThaiLLM-30B 0.406 / 0.1786; a row labeled "ThaiLLM-8B-SFT-IQ (Medical)" 0.4331 / 0.5458.
- The second row label is probably a copy-paste error for the 30B-IQ result. Its numbers also differ slightly from the 8B card's own 0.4363 / 0.5485. Treat the 30B result as UNVERIFIED.

**ThaiLLM-27B-Prescreen-Preview** (self-reported, SFT) — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen-Preview)
- Department F1 / severity F1:
  - ThaiLLM-27B zero-shot: 0.2320 / 0.2215
  - Prescreen-Preview: 0.3919 / 0.2186
  - MedGemma-27B-it zero-shot: 0.3853 / 0.3031

**ThaiLLM-27B-Prescreen** (self-reported, RL on MedGemma-27B-text-it; test size per class-support table = 288 cases; GitHub says the Prescreen eval uses 96 samples) — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen); [GitHub](https://github.com/vistec-AI/thaillm-medical-post-training)
- Overall F1 (disease / department / severity):

| Model | Disease | Department | Severity |
|---|---|---|---|
| ThaiLLM-27B-Prescreen | 0.735 | 0.541 | 0.571 |
| MedGemma-27b-text-it | 0.287 | 0.493 | 0.601 |
| Qwen3-30B-A3B-Thinking-2507 | 0.515 | 0.464 | 0.659 |
| Qwen3-8B | 0.157 | 0.449 | 0.574 |
| MedGemma1.5-4b-it | 0.095 | 0.424 | 0.525 |

- Accuracy for Prescreen: disease 0.729, department 0.677 (base 0.436), severity 0.799 (the highest of all models tested).
- Per-class severity:
  - Emergency: P 0.878, R 0.857, F1 0.867 (n=84)
  - Visit Hospital/Clinic: P 0.767, R 0.940, F1 0.845 (n=168)
  - **Observe at Home: F1 0.000 (n=36).** The card says the model "never predicts Observe at Home".

**ThaiLLM-8B-ToolUse** (self-reported) — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-8B-ToolUse)
- Accuracy / Trigger F1 / Macro F1:
  - typhoon-s-thaillm-8b-instruct base: 0.675 / 0.475 / 0.394
  - Qwen3-30B-A3B-Thinking-2507: 0.990 / 0.992 / 0.978
  - ToolUse: **0.999 / 1.000 / 0.993**
- Per-tool F1 for ToolUse: 0.981 to 1.000 (prescreen 0.981, list_appointment 0.981).

**ThaiLLM-8B-MedApp v2.0.0 vs v1** (self-reported; protocol-aligned reproduction of the vistec-AI pipeline at commit 7377263) — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-8B-MedApp)
- med-IQ (200 examples × 3 rollouts; correctness judged by deepseek/deepseek-v4-flash):
  - v2: format 100.00%, citations 67.82%, response 75.83%, combined 1.5366
  - v1: 95.67%, 62.29%, 63.17%, 1.3502
- ToolUse (5,122 examples × 3 rollouts):
  - v2: pass@1 99.92%, trigger F1 100.00%, macro F1 99.39%, pass@3 99.94%
  - v1: 90.36%, 87.54%, 78.30%, 94.79%
- Multi-turn stability (10 Thai scenarios × 8 turns): flag rate v1 46.88% (published-style) / 33.12% (stabilized); v2 3.12% / **0.00%**.
- The card notes that the v1 control "did not reproduce every score on the previous public model card".

**I C Develop PAI-1** (self-reported; vLLM seed 0; LLM judge pass/fail; for 27B, a case passes only if the judge passes it AND there is no `must_not` safety violation; decontaminated)
- pai1-medgemma-4b v25-DPO — [HF](https://huggingface.co/icdevelop/pai1-medgemma-4b)
  - thai_pharma_bench_v2 (lookup, no RAG, 200 cases): 37.5%
  - thai_pharma_bench_v2_rag (200 cases): 64.0% (v24-DPO 62.5%, v24-SFT 53.0%, v20 55.0%)
  - deliberation_bench_v1 (120 cases): 48.3% (v24-DPO 40.0%, v24-SFT 44.2%, v20 37.5%)
  - The card's prose conflicts with its own table ("55% → 62.5%"; deliberation stated as 40.0%).
- pai1-medgemma-27b v26-DPO — [HF](https://huggingface.co/icdevelop/pai1-medgemma-27b)

| Benchmark | Cases | v20 | v24 | v26-DPO |
|---|---|---|---|---|
| Lookup, no RAG | 200 | 46.5% | 43.0% | 50.5% |
| Lookup + RAG | 200 | 64.5% | 65.3% | 64.5% |
| Deliberation | 120 | 29.2% | 37.7% | 38.3% |

  - The 27B is not better than the 4B on RAG lookup (64.5% vs 64.0%) and is worse on deliberation (38.3% vs 48.3%).

**I C Develop TMA-1** (self-reported; LLM judge plus deterministic hard checks; decontaminated at token overlap ≥0.55)

| Axis | Cases | Base 4B | TMA-1 4B v2 | Base 27B | TMA-1 27B v1 |
|---|---|---|---|---|---|
| Knowledge, no RAG | 200 | 38.5% | 45.0% | 38.5% | 61.5% |
| Knowledge + RAG | 200 | 83.5% | 83.5% | 83.5% | 89.5% |
| Deliberation | 120 | 2.5% | 39.2% | 2.5% | 45.0% |
| Safety / referral | 120 | 75.8% | 96.7% | 75.8% | 98.3% |

- Drug–drug interaction accuracy is reported as ≤27%.
- The 27B card lists base-27B numbers identical to base-4B and repeats a "~45%" no-RAG note that matches the 4B. This may be a copy error and is UNVERIFIED.
- — [HF tma1-4b](https://huggingface.co/icdevelop/tma1-medgemma-4b); [HF tma1-27b](https://huggingface.co/icdevelop/tma1-medgemma-27b)

**Typhoon-Si-Med-Thinking-4B** (self-reported; English)
- Benchmarks: MedQA (1,273 MCQ / 1,233 QA), MedMCQA (6,150 / 2,180), MedXpertQA text (2,450 / 2,086), MMLU-Pro Health (818 / 736), in MCQ, QA and ranked-list formats. — [arXiv 2509.20866](https://arxiv.org/abs/2509.20866)
- The card claims it surpasses "Gemini 2.5 Pro on list-based and short-answer tasks". The scores are shown only as an image. — [HF card](https://huggingface.co/typhoon-ai/typhoon-si-med-thinking-4b-research-preview)
- Across 15 models, format robustness ranged from 35% to 100%. — [arXiv 2509.20866](https://arxiv.org/abs/2509.20866)

**Thai medical benchmarks that exist but were not used by any of these models**
- ThaiNLE Step 1 mock exam (304 questions, ~10% image-based): evaluated only on general frontier LLMs (GPT-4, Claude, Gemini).
  - The search summary reported GPT-4 at 88.9% and all models above passing. UNVERIFIED in detail: the snippet contradicts itself on which models were tested.
  - — [medRxiv 2024.12.20.24319441](https://www.medrxiv.org/content/10.1101/2024.12.20.24319441.full.pdf); [Mahidol repository](https://repository.li.mahidol.ac.th/items/a56b5885-c0f4-4e61-87bd-28fc95007449/full)

### Inferences
- No independent or third-party evaluation of any Thai medical LLM was found. Every number is self-reported, often on the developer's own in-house test set, and frequently judged by another LLM (GPT-4o, DeepSeek-v4-flash, or an unnamed judge).
- The scores are not comparable across families. Eir uses English MCQ accuracy, ThaiLLM uses BLEU/Jaccard/F1, I C Develop uses LLM-judge pass rates, and Typhoon-Si-Med uses English list-format accuracy.
- RAG dependence is explicit and large. TMA-1 4B knowledge goes from 45.0% without RAG to 83.5% with it; PAI-1 4B lookup goes from 37.5% to 64.0%.
- Eir's "outperforms GPT-4o by 11%" rests on GPT-4o judging its own outputs against Eir's on a custom set. That is a weak basis for the claim.

### Gaps
- No model reports scores on ThaiNLE (NL1/NL2), a Thai-translated MedQA/PubMedQA, or Thai MMLU medical subsets.
- Exact Typhoon-Si-Med numbers are in a figure I could not read.
- Test-set sizes and composition for ThaiLLM IQ were not described on the cards. The med-iq dataset exists but I did not inspect it.
- Eir's human-evaluation methodology was not found in the portion of the paper I read.

## Q3. What has NOT been evaluated for each model?

### Takeaway
None of the models report real clinical-outcome studies, prospective or RCT validation, systematic hallucination rates, bias or fairness audits, or independent red-teaming. Only I C Develop's TMA-1 reports a safety/referral metric, and only ThaiLLM-27B-Prescreen reports triage per class. That triage result shows a serious failure mode: it never predicts "Observe at Home".

### Cited Findings
- **Eir-8B**
  - Has: English MCQ, Thai general-language, translation, and GPT-4o-judged Thai clinical tasks.
  - Missing: no reported safety, hallucination, triage, medication-instruction or bias metrics. The card says it needs "further validation, including randomized controlled trials" before clinical use.
  - The claimed human evaluation and in-hospital deployment have no published outcomes.
  - — [HF card](https://huggingface.co/EIRTHAIMED/Llama-3.1-EIRAI-8B); [arXiv 2409.08523](https://arxiv.org/abs/2409.08523)
- **ThaiLLM-8B/30B-IQ**
  - Has: BLEU and citation-Jaccard only.
  - Missing: no faithfulness or hallucination rate beyond citation overlap, no evaluation of the "unknown" (abstention) behavior, no safety eval.
  - — [HF 8B-SFT-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-8B-SFT-IQ); [HF 30B-IQ](https://huggingface.co/ThaiLLM/ThaiLLM-30B-IQ)
- **ThaiLLM-27B-Prescreen**
  - Triage is evaluated, with 0% recall on Observe at Home (over-triage).
  - Missing: no undertriage analysis beyond the class table, no clinician comparison, no real-patient data. Training and evaluation data are synthetic profiles and conversations.
  - — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen); [HF Preview](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen-Preview)
- **ThaiLLM-8B-MedApp v2**
  - The card itself says "Medical safety, refusal behavior, privacy handling, and production workload monitoring require additional evaluation".
  - It says the stability diagnostics "are not medical-correctness or safety judgments", that merging "can introduce behavior absent from either parent", and that tool calls can have real-world consequences.
  - — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-8B-MedApp)
- **ThaiLLM-8B-ToolUse:** routing accuracy only. No evaluation of conversational medical content or safety. — [HF](https://huggingface.co/ThaiLLM/ThaiLLM-8B-ToolUse)
- **PAI-1 (pharmacy)**
  - Has: a deliberation benchmark (ruling out a contraindicated drug) and `must_not` safety checks in scoring.
  - Missing: no stand-alone safety benchmark, no pharmacist review of the model or of the knowledge base (534 flagged AI-generated entries), no evaluation of image input.
  - Marked DRAFT pending pharmacist and legal review.
  - — [HF 4B](https://huggingface.co/icdevelop/pai1-medgemma-4b); [HF 27B](https://huggingface.co/icdevelop/pai1-medgemma-27b)
- **TMA-1 (consumer health)**
  - Has: safety/referral evaluated (96.7% for 4B, 98.3% for 27B).
  - Missing: image inputs "not evaluated"; drug–drug interaction is weak (≤27%); no physician or pharmacist review ("unreviewed draft"); no bias or real-user evaluation.
  - — [HF 4B](https://huggingface.co/icdevelop/tma1-medgemma-4b); [HF 27B](https://huggingface.co/icdevelop/tma1-medgemma-27b)
- **Typhoon-Si-Med-Thinking-4B**
  - No Thai-language evaluation at all. No safety or bias evaluation reported.
  - The card warns it may produce "inaccurate, biased, or otherwise objectionable" answers.
  - — [HF card](https://huggingface.co/typhoon-ai/typhoon-si-med-thinking-4b-research-preview)

### Inferences
- Across the field, medication-instruction correctness (dose, interactions) is evaluated only by I C Develop, and the results are weak: DDI ≤27%, deliberation 38–48%.
- Bias, Thai dialect and regional-language robustness (e.g., Isan), privacy/PDPA handling, and prompt-injection resistance in RAG or tool-use are unevaluated for every model.
- No model has published real-world clinical outcomes, a prospective study, or regulatory clearance as a medical device. Several cards explicitly state they are not medical devices.

### Gaps
- I found no external red-team, academic replication, or leaderboard (for example a Thai medical leaderboard) covering these models.
- Thai FDA (อย.) or Ministry of Public Health regulatory status for any of these models was not found.
