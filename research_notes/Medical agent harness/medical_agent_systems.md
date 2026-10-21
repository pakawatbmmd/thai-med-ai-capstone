# Medical / Clinical LLM Agent Systems, Harnesses and Benchmarks: How Much Comes From the Harness? (as of Oct 2026)

Verification tags used throughout:
- **[V]** = primary source fetched/read this session (paper text or abstract).
- **[S]** = search-result snippet or secondary report only (not read in full).
- **[T]** = from researcher's prior knowledge (pre-2026 literature); URL given but NOT re-fetched this session. Treat numbers as "verify before citing".
- Items dated before 2025 are marked **(pre-2025)**.

---

## Q1. Systems: what medical agent harnesses/orchestrators exist, and what do they add per model?

### Takeaway
Medical agent orchestrators are a crowded, well-funded area (Microsoft MAI-DxO, Google AMIE, Stanford MedAgentBench v2 agent, Harvard Asclepius, MDAgents, Agent Hospital, AgentMD, etc.). The best model-held-fixed evidence (MAI-DxO, Asclepius, MedAgentBench v2, Kather-lab OpenManus study) shows harness gains ranging from ~0 or negative (generic agent frameworks) to +4 to +8 points average (MAI-DxO across models) to +20 points or more on specific tool-sensitive tasks. Gains are biggest for weaker models and for tasks where tools fix a specific failure mode (arithmetic, API formatting, cost discipline).

### Cited Findings

**Microsoft MAI-DxO / SDBench (2025)** [V]
- MAI-DxO is described as "a model-agnostic orchestrator that simulates a panel of physicians, proposes likely differential diagnoses and strategically selects high-value, cost-effective tests". The Nov 8 2025 version extends SDBench to 304 NEJM-CPC cases plus 325 MIMIC-IV-ED admissions. — [Nori et al., Sequential Diagnosis with Language Models, Nov 2025 version (PDF)](https://erichorvitz.com/sequential_diagnosis_LM.pdf)
- Orchestrator roles: Dr. Hypothesis (Bayesian-updated top-3 differential), Dr. Test-Chooser (up to 3 discriminating tests per round), Dr. Challenger (devil's advocate against anchoring), Dr. Stewardship (vetoes low-yield expensive tests), Dr. Checklist (validates test names and internal consistency). It has 4 budget modes (Instant Answer, Question Only, Budgeted, No Budget) plus an Ensemble mode. — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1)
- SDBench mechanics: an o4-mini "Gatekeeper" holds the full case and reveals findings only when explicitly queried. Costs are $300 per physician visit plus CPT-mapped test prices from a 2023 US health-system price table. 56 most recent cases are a hidden test set. — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1)
- Model-held-fixed deltas, June 2025 version: o3 off-the-shelf scored 78.6% at $7,850 per case. With MAI-DxO, o3 scored 81.9% at $4,735, or 79.9% at $2,396 (budgeted), or 85.5% at $7,184 (ensemble). Generalist physicians scored 19.9%. — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1)
- Model-held-fixed deltas, Nov 2025 version: GPT-5 off-the-shelf scored 78.9% at $8,409. With MAI-DxO, GPT-5 scored 83.2% at $5,430, or 84.5% at $8,945 (ensemble). — [Nori et al. Nov 2025 PDF](https://erichorvitz.com/sequential_diagnosis_LM.pdf)
- "MAI-DxO boosted the accuracy of off-the-shelf models from a variety of providers by an average of 7.9 percentage points." It raised Gemini 2.5 Flash by 24.4%. Gains were significant (p<0.05) for Claude 4.5 Sonnet, Gemini 2.5 Flash, GPT-5, GPT-OSS 120B, Llama 4 Maverick and DeepSeek R1, but not for every model. The orchestrator was "primarily developed using GPT-4.1". — [Nori et al. Nov 2025 PDF](https://erichorvitz.com/sequential_diagnosis_LM.pdf)
- On MIMIC-IV-ED, the orchestrator was unchanged "aside from minor changes including a bug fix". There, "MAI-DxO improves base-model accuracy by an average of 4.4% (all tested models improve except Gemini 2.5 Pro)". GPT-5 + MAI-DxO scored 80.3% vs physicians' 46.8%. — [Nori et al. Nov 2025 PDF](https://erichorvitz.com/sequential_diagnosis_LM.pdf)
- The physician baseline changed between versions:
  - June 2025: 21 physicians, closed-book, 19.9%. — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1)
  - Nov 2025: 22.3% closed-book and 36.1% open-book (search allowed). — [Nori et al. Nov 2025 PDF](https://erichorvitz.com/sequential_diagnosis_LM.pdf)
  - The widely quoted "4x physicians" claim rests on the closed-book number.
- Authors' own interpretation: the harness gives "scaffolding" to weaker models, and "useful discipline" (anti-anchoring, cost-consciousness) to stronger ones. — [Nori et al. Nov 2025 PDF](https://erichorvitz.com/sequential_diagnosis_LM.pdf)
- Status: Microsoft says MAI-DxO is "not yet approved for clinical use", and neither SDBench nor MAI-DxO is publicly available. — [Microsoft AI blog](https://microsoft.ai/news/the-path-to-medical-superintelligence/)
- Stated limitations: no benign or healthy cases, so false-positive rates are unmeasured; the cost model is a first-order US approximation; physicians were generalists without usual resources. — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1)

**Google AMIE (2024–2026)**
- 2026 prospective feasibility study: AMIE talked with 100 real patients before urgent-care visits, embedded in an ambulatory workflow. It used Gemini 2.5 with Thinking Mode and a "refined state-aware chain-of-reasoning strategy" for pre-visit history taking. — [arXiv 2603.08448v2](https://arxiv.org/html/2603.08448v2) [S]
  - A secondary summary claims the differential diagnosis contained the final diagnosis in 90% of cases (75% top-3). Unverified against the preprint. — [Flipped newsletter](https://flipped-newsletter.beehiiv.com/p/from-data-to-diagnosis-26f2) [S]
- Multimodal AMIE uses a state-aware dialogue controller. Conversation flow is "dynamically controlled by intermediate model outputs reflecting patient states and evolving diagnoses", with follow-ups directed by uncertainty. Built on Gemini 2.0 Flash. — [Google Research blog](https://research.google/blog/amie-gains-vision-a-research-ai-agent-for-multi-modal-diagnostic-dialogue/) [S]
- Original AMIE (pre-2025 preprint, Nature 2025): a self-play simulated-dialogue training loop plus an inference-time chain-of-reasoning. — [Google Research blog](https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/) [S]
- g-AMIE / "physician-centred oversight" (2025): a guardrail that stops AMIE from giving individualized advice and routes it through an asynchronous clinician review ("clinician cockpit"). This is a harness-level safety and HITL design. — [arXiv 2507.15743](https://arxiv.org/abs/2507.15743) [T]

**Stanford MedAgentBench v2 agent (PSB 2026)** [V]
- Harness changes:
  - new system prompt (plan before tool calls, CoT, few-shot good/bad examples);
  - structured FHIR tools replacing raw HTTP construction;
  - sandboxed calculator tool;
  - dedicated "finish" tool for output formatting;
  - mem0-style memory of past failures.
- Results with GPT-4.1: 91.0% without memory and 98.0% with memory. The original paper's best was 69.67% (Claude 3.5 Sonnet v2). — [Chen et al., PSB 2026](https://psb.stanford.edu/psb-online/proceedings/psb26/chen_eric.pdf); [PubMed 41758153](https://pubmed.ncbi.nlm.nih.gov/41758153/)
- Caveat (verified in text): the 91% is compared "to the best-reported SRs from Table 4 of the original MedAgentBench paper", not to GPT-4.1 under the original harness. So it is not a strictly model-fixed comparison, though the authors attribute the gain to "better tooling and prompt engineering".
- Specific gains: task 6 (averaging vitals) improved via the calculator, and task 10 (conditional ordering) via prompt logic.
- The memory train/test split is on the same task templates, so the 98% is optimistic. The authors also add 300 new physician-designed tasks. — [Chen et al., PSB 2026](https://psb.stanford.edu/psb-online/proceedings/psb26/chen_eric.pdf)

**Asclepius: adaptive harness for long-horizon clinical agents (Harvard DBMI / Rajpurkar lab, 11 Sep 2026)** [V]
- Explicitly frames "harness" as "the non-parametric scaffolding around an LLM, including prompts, tools, control flow, and inter-agent coordination". — [arXiv 2609.13543](https://arxiv.org/html/2609.13543)
- Three components:
  1. a self-evolving operating manual, rewritten between "shifts" by a proposer agent;
  2. an externalized clinical skills library;
  3. three isolated subagents (triage, diagnosis, treatment).
- Backbone: Claude Code with Claude Opus 4.6, evaluated in an ED-like Clinical Environment Simulator.
- Model-fixed results, all batches (n=120): overall +0.30 (p<0.01); critical actions +0.73 (+25%, p<0.001); timeliness +0.45 (+13%); diagnosis −0.02 (n.s.).
- Held-out batches (n=48): only critical actions significant (+0.625, +22%, p=0.024). Overall was +0.193 (n.s.).
- Ablation: the self-evolving harness alone gave the largest pooled gain (+0.18 overall). Skills alone gave +0.12; subagents alone gave +0.04. — [arXiv 2609.13543](https://arxiv.org/html/2609.13543)
- Key point: the harness improved process and safety behaviors (critical actions, timeliness) but not diagnostic accuracy.

**Older academic multi-agent frameworks (mostly pre-2025)** [T]
- **MDAgents** (Kim et al., NeurIPS 2024 oral, MIT): adaptive routing by case complexity (solo / multidisciplinary team / integrated care team). It reports best results on 7 of 10 medical benchmarks, with up to +4.2% over prior methods, and about +11.8% average from moderator review plus external knowledge (recalled numbers). — [arXiv 2404.15155](https://arxiv.org/abs/2404.15155)
- **MedAgents** (Tang et al., ACL Findings 2024): training-free multi-disciplinary role-play discussion for MedQA-style QA. — [arXiv 2311.10537](https://arxiv.org/abs/2311.10537)
- **Agent Hospital / MedAgent-Zero** (Tsinghua AIR, 2024): a simulated hospital where doctor agents self-evolve on simulated patients. It reports about 93% on a MedQA respiratory subset (recalled). — [arXiv 2405.02957](https://arxiv.org/abs/2405.02957)
- **AgentMD** (Jin et al., NIH/NCBI, 2024): an agent that curates and applies 2,164 clinical calculators (RiskCalcs). It reports about 87.7% vs 40.9% for GPT-4 chain-of-thought on RiskQA (recalled), a large same-model tool-use delta. — [arXiv 2402.13225](https://arxiv.org/abs/2402.13225)
- **EHRAgent** (Shi et al., EMNLP 2024): a code-generating agent over EHR tables with interactive debugging. It reports up to +29.6% success over the strongest baseline (recalled). — [arXiv 2401.07128](https://arxiv.org/abs/2401.07128)
- **ClinicalAgent** (Yue et al., 2024): a multi-agent system for clinical trial outcome prediction. — [arXiv 2404.14777](https://arxiv.org/abs/2404.14777)
- **TxAgent** (Gao et al., Harvard, 2025): a therapeutic reasoning agent over a 211-tool ToolUniverse (drug data, FDA labels, interactions). This is one of the clearest "medical tool harness" designs. — [arXiv 2503.10970](https://arxiv.org/abs/2503.10970)
- **Med-Gemini** (Google, 2024): uncertainty-guided web search at inference, an agentic retrieval loop on top of the model. — [arXiv 2404.18416](https://arxiv.org/abs/2404.18416)

**Commercial healthcare agent products**
- **Claude for Healthcare** (launched 11 Jan 2026 at JPM; "HIPAA-ready"):
  - connectors to the CMS Coverage Database, ICD-10, the NPI Registry and PubMed;
  - Agent Skills for FHIR integration and prior-authorization review;
  - consumer health-record features for Pro/Max US users.
  - These are harness-level features (connectors, skills), not a new model. — [The Register](https://www.theregister.com/2026/01/12/claude_anthropic_healthcare/); [MobiHealthNews](https://www.mobihealthnews.com/news/anthropic-launches-claude-healthcare) [S]
- **ChatGPT Health** (consumer, launched about a week earlier, Jan 2026) and **ChatGPT for Healthcare** (enterprise; early sites include Boston Children's and Cedars-Sinai). — [Cloudwards](https://www.cloudwards.net/?p=142066); [The Register](https://www.theregister.com/2026/01/12/claude_anthropic_healthcare/) [S]
- **Epic, Microsoft/Nuance, Abridge** (not re-verified this session) [T]:
  - Epic announced agentic assistants (Art for clinicians, Emmie for patients, Penny for revenue cycle) at UGM, Aug 2025.
  - Microsoft launched Dragon Copilot (ambient plus dictation) in March 2025.
  - Abridge does ambient documentation integrated into Epic.
  - None of these publish model-fixed harness ablations.

### Inferences
- The strongest industrial medical agents (MAI-DxO, AMIE, Claude for Healthcare skills/connectors) are themselves harnesses around general models. "Medical harness" is in effect the product strategy of Microsoft, Google and Anthropic, even when the word "harness" isn't used.
- Reported harness deltas cluster into three groups:
  - **Small but consistent accuracy gains** for diagnosis orchestration: MAI-DxO averages +4.4 to +7.9 pp across models.
  - **Large gains** where a tool fixes a mechanical failure: the MedAgentBench v2 calculator and FHIR tools; AgentMD's calculators.
  - **Process and safety gains without accuracy gains**: Asclepius critical actions +25% with diagnosis flat; MAI-DxO cost reductions of about 35–40% at similar or higher accuracy.
- Harness gains shrink as base models get stronger. MAI-DxO's gain on frontier o3/GPT-5 is about 3–5 pp, versus +24.4% for Gemini 2.5 Flash.

### Gaps
- No per-model numeric table for MAI-DxO was extractable (Figure 9 is a chart). Only the average (+7.9 pp NEJM, +4.4% MIMIC) and selected examples are verified.
- AMIE's 2026 real-world numbers are unverified from the primary source.
- No public, model-fixed ablation exists for any commercial product (Claude for Healthcare, ChatGPT Health, Epic agents, Dragon Copilot).
- MDAgents, AgentMD, EHRAgent and Agent Hospital numbers are from memory and should be checked.

---

## Q2. Benchmarks: which exist, and which allow swapping the harness while holding the model fixed?

### Takeaway
There are now many medical agent benchmarks. Most are built to rank models under one fixed reference harness (MedAgentBench, AgentClinic, CRAFT-MD, HealthBench, MedHELM). In 2026, several explicitly cross harness × model:
- **MedicalHarnessBench**: 5 models × 6 harnesses, with variance decomposition.
- **HealthAgentBench** (Microsoft): Codex vs Claude Code.
- **χ-Bench/CHI-Bench**: 30 harness-model configurations.
- **HealthAdminBench**: standardized vs native computer-use harness.

### Cited Findings

**Benchmarks with harness × model crossing (2026)**
- **MedicalHarness / MedicalHarnessBench** (Northwestern; Wang, Zhao, Ding; 5 Oct 2026) [V]. This is the closest direct prior art to "medical harness as research variable". — [arXiv 2610.05778](https://arxiv.org/html/2610.05778v1)
  - 107 executable tasks in 4 domains, each testing one harness capability:
    - MedTool (32): clinical calculation and tool selection.
    - MedMemory (23): long-context retrieval across 70–100 sessions.
    - MedPlanning (28): trial eligibility and tumor localization workflows.
    - MedWeb (24): EMR, payer and fax portals.
  - Harnesses: OpenClaw, Hermes, ZeroClaw, Codex, Claude Code, MH-Lab (custom).
  - Models: Gemma4-26B-A4B, Qwen3.6-35B-A3B, GPT-OSS-120B, Nemotron-3.5-30B-A3B, GLM-4.7-Flash.
  - **Variance decomposition:** model 58%, harness 12%, harness×model interaction 12%, seed noise 18%. Harness plus interaction is about 24%, or "about a quarter".
  - By environment:
    - MedMemory: harness main effect 25% (40% with interaction). The HV/MV ratio is 0.64 for all models and 1.45 for the three main models, the only case where harness > model.
    - MedTool: HV/MV is 0.18.
    - MedPlanning: seed noise (40%) is comparable to the model effect (36%).
  - "No single harness is best across all models and tasks". Harnesses differ mainly in whether an episode ends with an answer at all.
  - Ablations in MH-Lab:
    - Removing summarization overflows context in 67 of 72 MedWeb episodes (Qwen), and outcome falls 0.39 (Qwen) / 0.17 (GPT-OSS).
    - Removing the plan tool drops GPT-OSS MedWeb outcome by 0.18.
    - Hiding tools behind search causes misnamed tool calls in 95 of 96 MedTool episodes and 3× tokens (Qwen); for GPT-OSS, MedWeb drops 0.15.
  - Note: all models are small open-weight ones served locally; no frontier closed models.
- **HealthAgentBench** (Microsoft; Liu, Poon, Naumann et al.; 30 Jun 2026). — [arXiv 2606.31179](https://arxiv.org/abs/2606.31179) [V abstract]; [GitHub microsoft/HealthAgentBench via search](https://huggingface.co/papers/2606.31179) [S]
  - 54 executable tasks in 7 categories, covering text, EHR, 2D, 3D and WSI modalities.
  - Evaluates agent harnesses such as Codex and Claude Code. The best is Codex GPT-5.5 at about 42% task success.
  - Imaging is "especially hard, particularly for Claude Code models".
  - The abstract does not separate harness and model effects.
- **χ-Bench / CHI-Bench** (May 2026). — [Emergent Mind summary of arXiv 2605.16679](https://www.emergentmind.com/papers/2605.16679); [benchmarklist](https://benchmarklist.com/benchmarks/bench_chi_bench/) [S]
  - Domains: prior authorization, utilization management, care management.
  - 20 simulated apps via 87 MCP tools, plus a handbook of about 1,290 documents built with Johns Hopkins clinicians.
  - Across 30 harness+model configurations the best solved 28.0%. None exceeded 20% on pass^3, and running all tasks in one session dropped to 3.8%.
- **HealthAdminBench** (Apr 2026): computer-use agents on healthcare admin tasks. It compares a standardized harness vs native computer-use harnesses and reports "a substantial gap", with Claude Opus 4.6 native computer use highest. — [arXiv 2604.09937](https://arxiv.org/pdf/2604.09937) [S]
- **BioMedArena** (May 2026): an open-source toolkit for comparing biomedical deep-research agents and "harness modes" under fixed scoring. — [arXiv 2605.06177](https://arxiv.org/pdf/2605.06177) [S]
- **PatientAgentBench** (Jul 2026): patient-facing health agents. — [arXiv 2607.25485](https://arxiv.org/pdf/2607.25485) [S]

**Model-ranking benchmarks with a fixed reference harness**
- **MedAgentBench** (Stanford, NEJM AI 2025). — [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144); [arXiv 2501.14654](https://arxiv.org/html/2501.14654v2); [GitHub](https://github.com/stanfordmlgroup/medagentbench) [V]
  - FHIR environment (Docker): 100 patients, 785k records, 300 tasks.
  - 12 models under one harness; best was Claude 3.5 Sonnet v2 at 69.67% (Query 85.33%, Action 54.00%). Others: GPT-4o 64.0%, DeepSeek-V3 62.67%, Gemini 2.0 Pro 18.0%, Mistral 7B 4.0%.
  - The harness is swappable in practice, as v2 showed. The 69.67% → 91% (GPT-4.1, new harness) jump is the most-cited "harness matters" medical datapoint, with the model-not-fixed caveat above.
- **SDBench** (Microsoft): the harness is the object of study (MAI-DxO vs off-the-shelf), but the benchmark is not public. — [Microsoft AI](https://microsoft.ai/news/the-path-to-medical-superintelligence/) [V]
- **AgentClinic** (Schmidgall et al., 2024, pre-2025): multimodal simulated clinical dialogue with patient, measurement and moderator agents, plus cognitive-bias injection. It reports large drops vs static MedQA and big tool gains (recalled: notebook and experiential tools gave Llama-3 up to about 92% relative improvement). — [arXiv 2405.07960](https://arxiv.org/abs/2405.07960) [T]
- **CRAFT-MD** (Johri et al., Nature Medicine, Jan 2025): conversational evaluation; LLM accuracy drops sharply from vignettes to multi-turn history-taking. — [Nature Medicine](https://www.nature.com/articles/s41591-024-03328-5) [T]
- **MedAgentGym** (Xu et al., 2025): about 72k code-centric biomedical reasoning instances; used to train Med-Copilot via SFT/RL. It is a training environment as much as a benchmark. — [arXiv 2506.04405](https://arxiv.org/abs/2506.04405) [T]
- **HealthBench** (OpenAI, May 2025): 5,000 multi-turn conversations with 48,562 physician-written rubric criteria from 262 physicians. It evaluates model responses, not tool-using agents; no harness variable. — [OpenAI](https://openai.com/index/healthbench/) [T]
- **MedHELM** (Stanford CRFM, 2025): a holistic clinician-validated task taxonomy (about 121 tasks, 35 benchmarks). It is a model eval, not agentic. — [arXiv 2505.23802](https://arxiv.org/abs/2505.23802) [T]
- **MedAgentsBench** (Tang et al., 2025): hard-subset medical QA comparing thinking models vs agent frameworks, with cost accounting. — [arXiv 2503.07459](https://arxiv.org/abs/2503.07459) [T]
- **MedAgentBoard** (NeurIPS 2025 Datasets & Benchmarks): multi-agent vs single-LLM vs conventional methods across 4 task types. — [arXiv 2505.12371](https://arxiv.org/pdf/2505.12371); [project site](https://medagentboard.netlify.app/) [S]

### Inferences
- By mid-to-late 2026, "harness × model" crossing has moved into medical benchmarking: HealthAgentBench (Microsoft), χ-Bench, HealthAdminBench, BioMedArena, and especially MedicalHarnessBench, which does a formal variance decomposition.
- A student benchmark claiming "first to compare harnesses on medical tasks" would be incorrect as of Oct 2026.
- Best quantitative anchor for "how much is harness?": about 12% main effect, about 24% including interaction, model about 58% (MedicalHarness). It is larger for memory/long-context tasks and smaller for calculator/tool tasks.
- Directly reusable open environments for harness experiments:
  - MedAgentBench (FHIR Docker);
  - MedicalHarnessBench (if code is released; not verified);
  - HealthAgentBench (GitHub);
  - χ-Bench (GitHub actava-ai/chi-bench; Harbor dataset);
  - AgentClinic.

### Gaps
- Could not verify whether MedicalHarnessBench code and data are released.
- HealthAgentBench per-harness numbers with a fixed model were not available from the abstract.
- MedHELM, HealthBench, MedAgentGym, CRAFT-MD and AgentClinic details are from memory and were not re-fetched.

---

## Q3. Medical-specific harness components in the literature (tools, safety hooks, audit, permissions, cost, HITL, regulation)

### Takeaway
Nearly every proposed component already exists in at least one system, though usually bundled rather than ablated:
- clinical calculators, FHIR tools, drug databases and guideline retrieval;
- cost-aware test ordering;
- devil's-advocate and checklist roles;
- guardrails with clinician oversight;
- memory and self-evolving manuals;
- prior-auth skills and connectors.

Less studied as isolated, measured harness variables:
- permission gates for orders;
- red-flag escalation;
- audit trails and provenance;
- abstention.

### Cited Findings
- **Clinical calculators and arithmetic tools**:
  - The MedAgentBench v2 sandboxed calculator drove the task-6 improvement. — [Chen et al., PSB 2026](https://psb.stanford.edu/psb-online/proceedings/psb26/chen_eric.pdf) [V]
  - AgentMD has 2,164 calculators. — [arXiv 2402.13225](https://arxiv.org/abs/2402.13225) [T]
  - The MedicalHarness MedTool domain targets calculator selection. — [arXiv 2610.05778](https://arxiv.org/html/2610.05778v1) [V]
- **FHIR / EHR tools**: structured FHIR tools replaced error-prone raw HTTP construction. — [Chen et al., PSB 2026](https://psb.stanford.edu/psb-online/proceedings/psb26/chen_eric.pdf) [V]. Claude for Healthcare ships a FHIR Agent Skill. — [MobiHealthNews](https://www.mobihealthnews.com/news/anthropic-launches-claude-healthcare) [S]
- **Drug and therapeutic databases**: the TxAgent / ToolUniverse 211-tool harness. — [arXiv 2503.10970](https://arxiv.org/abs/2503.10970) [T]
- **Coverage and administrative connectors** (CMS Coverage DB, ICD-10, NPI, PubMed) and prior-auth skills. — [The Register](https://www.theregister.com/2026/01/12/claude_anthropic_healthcare/) [S]. χ-Bench's 87 MCP tools and policy handbook. — [Emergent Mind](https://www.emergentmind.com/papers/2605.16679) [S]
- **Cost-aware test ordering**: the MAI-DxO Dr. Stewardship role, budget tracker and CPT-based cost model. — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1) [V]
- **Anti-bias / verification roles**: Dr. Challenger (anchoring) and Dr. Checklist (validity). — [arXiv 2506.22405v1](https://arxiv.org/html/2506.22405v1) [V]
- **Safety filters**: the Kather-lab study reports that safeguards filtered 89.9% of hallucinations, but hallucinations persisted. — [npj Digit Med 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13031301/) [V]
- **Guardrails plus HITL**: g-AMIE withholds individualized advice until a clinician approves it asynchronously. — [arXiv 2507.15743](https://arxiv.org/abs/2507.15743) [T]
- **Critical-action / timeliness** gains come from harness engineering, not diagnosis gains. — [Asclepius arXiv 2609.13543](https://arxiv.org/html/2609.13543) [V]
- **Memory / self-evolving harness**:
  - MedAgentBench v2 memory took success from 91% to 98%. — [PSB 2026](https://psb.stanford.edu/psb-online/proceedings/psb26/chen_eric.pdf) [V]
  - Asclepius evolved manual: +0.18 overall, the largest single component. — [arXiv 2609.13543](https://arxiv.org/html/2609.13543) [V]
  - A review on self-evolving healthcare agent harnesses: "the model determines what an agent can reason about; the harness determines whether that reasoning persists". — [Preprints.org 202605.1547](https://www.preprints.org/manuscript/202605.1547) [S]
- **Context management, planning and tool exposure** are measured as harness mechanisms on medical tasks. — [MedicalHarness](https://arxiv.org/html/2610.05778v1) [V]
- **Regulation (US)**:
  - FDA revised its Clinical Decision Support Software guidance on 6 Jan 2026 (some sources cite a 29 Jan reissue). Enforcement discretion now extends to CDS giving a single recommendation when only one is clinically appropriate.
  - Image-analysis functions remain regulated.
  - The guidance "does not expressly change FDA's current approach to AI", and nothing is specific to agents.
  - — [Covington](https://www.cov.com/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance); [ACR](https://www.acr.org/News-and-Publications/2026/fda-updates-guidance-on-clinical-decision-support); [Innolitics](https://innolitics.com/articles/fda-guidance-clinical-decision-support-software-2026/) [S]
- **Regulation (EU)**: AI that is (part of) a medical device under MDR/IVDR is classified high-risk under the EU AI Act (Annex I route), with obligations phasing in through Aug 2027. — [EU AI Act, Art. 6 / Annex I](https://artificialintelligenceact.eu/article/6/) [T]

### Inferences
- A defensible design space for a "medical harness" (for example, for Thai deployment) can be mapped onto these components. The novelty is unlikely to be any single component. More likely sources of novelty:
  - controlled ablation of safety-oriented components on safety outcomes;
  - a specific locale's tool stack and regulatory regime: Thai drug formulary, Thai guidelines, NHSO/UC coverage rules, Thai FDA SaMD rules.
- Safety-oriented components currently lack controlled, model-fixed ablations measuring unsafe-action rates: order permission gates, contraindication checks, red-flag escalation, abstention, audit logs. Asclepius ("critical actions") and g-AMIE come closest.

### Gaps
- No paper found that ablates order-permission gates, contraindication checkers or audit/provenance logging as harness variables with safety metrics.
- Thai FDA SaMD / AI regulatory guidance was not researched here (out of scope; likely covered by other notes).
- EU AI Act details were not re-fetched.

---

## Q4. Explicit gaps: has anyone framed "harness for medicine" as the research variable? Critiques of multi-agent medical frameworks?

### Takeaway
**The student's claim that "no one talks about medical harnesses" is false as of Oct 2026.** At least two 2026 papers use the word "harness" in the title for medical agents and treat it as the research variable:
- MedicalHarness (Oct 2026): a harness × model variance decomposition plus component ablations.
- Asclepius (Sep 2026): a self-evolving clinical harness with component ablations.

Others are adjacent: MedClaw (a harness for surgical video), HealthAgentBench and χ-Bench (harness-model configurations), and the MedAgentBench v2 harness redesign. There is also a substantial critique literature showing that generic or multi-agent scaffolds often add little over a strong single model.

### Cited Findings

**Prior art framing the harness as the variable**
- MedicalHarness: "A Controlled Evaluation of LLMs and Agent Harnesses on Medical Tasks". Harness and interaction explain about 24% of variance; no single harness is best; harnesses mostly differ in answer production. — [arXiv 2610.05778](https://arxiv.org/html/2610.05778v1) [V]
- Asclepius: "An Adaptive Harness for Long-Horizon Clinical Agents". Gains appear in critical actions and timeliness, not diagnosis. — [arXiv 2609.13543](https://arxiv.org/html/2609.13543) [V]
- MedClaw: "Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning", with ablations on a 259-question neurosurgery split. — [arXiv 2608.14015](https://arxiv.org/html/2608.14015v1) [S]
- Related work cited by Asclepius includes EvoClinician (He et al., 2026), HORIZON (Wang et al., 2026) and Meta-Harness (Lee et al., 2026), indicating more self-evolving clinical harness work. — [arXiv 2609.13543](https://arxiv.org/html/2609.13543) [V, citation list only]
- General (non-medical) harness-science literature that MedicalHarness builds on: Harness-Bench, scaffold-effects-on-GAIA, natural-language agent harnesses, and "grow the harness, not the context". — [arXiv 2610.05778](https://arxiv.org/html/2610.05778v1); [arXiv 2603.25723](https://arxiv.org/html/2603.25723v2); [arXiv 2609.26760](https://arxiv.org/pdf/2609.26760) [S]
- MAI-DxO is itself framed as a model-agnostic orchestrator tested across 6 or more model families. That is a harness-as-variable experiment in substance. — [Nori et al. Nov 2025](https://erichorvitz.com/sequential_diagnosis_LM.pdf) [V]

**Critiques: agents and multi-agent setups vs a strong single model**
- Liu, ..., Kather (npj Digital Medicine, 18 Feb 2026), all on the Llama-4 backbone: "Agent systems yield marginal improvement over baseline LLMs". — [PMC13031301](https://pmc.ncbi.nlm.nih.gov/articles/PMC13031301/) [V]
  - Vanilla OpenManus vs Llama-4:
    - AgentClinic-MedQA: −3.3 pp (51.4% → 48.1%).
    - NEJM image-by-request: −12.5 pp.
    - HLE multimodal: −5.1 pp.
    - MedAgentsBench: +7.1 pp.
  - Medical prompt plus tools (OpenManus_MedAssist_Tool): +8.9 pp on AgentClinic-MedQA.
  - Overhead: >10× (up to about 100×) tokens and ≥2× latency.
  - So a generic harness can hurt, and medical customization recovers modest gains.
- MedAgentBoard (NeurIPS 2025): multi-agent collaboration "does not consistently" beat strong single LLMs (e.g., textual medical QA). Conventional specialised methods beat multi-agent on VQA and EHR prediction. Multi-agent helps on workflow-automation completeness. — [arXiv 2505.12371](https://arxiv.org/pdf/2505.12371) [S]
- AgentRx (May 2026): "single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated" on multimodal clinical prediction. — [arXiv 2605.10286](https://arxiv.org/html/2605.10286v1) [S]
- MedAgentsBench (2025): thinking models (e.g., DeepSeek-R1, o3-mini) are competitive with or better than multi-agent frameworks at lower cost. — [arXiv 2503.07459](https://arxiv.org/abs/2503.07459) [T]
- MedicalHarness: no harness dominates. Mechanisms only help "when they fire and when their interface fits the model". Hiding tools behind search can reduce accuracy. — [arXiv 2610.05778](https://arxiv.org/html/2610.05778v1) [V]
- MAI-DxO: gains on the strongest models are small (o3 +3.3 pp; GPT-5 +4.3 pp), and on MIMIC-IV-ED Gemini 2.5 Pro did not improve. — [Nori et al. Nov 2025](https://erichorvitz.com/sequential_diagnosis_LM.pdf) [V]

### Inferences
- The broad novelty claim ("first medical harness", "first to study harness effects in medicine") is undercut, most directly by MedicalHarness (Oct 2026) and Asclepius (Sep 2026).
- Plausible remaining gaps a master's thesis could own:
  1. **Language and locale**: every harness study found is English and US-centric (US price tables, CMS, NEJM, MIMIC). No harness-ablation study was found in Thai or any SE Asian language, or with locale-specific tools (Thai formulary, Thai CPGs, NHSO rules).
  2. **Safety-component ablation with safety outcomes**: MedicalHarness ablates context, planning and tool exposure (capability mechanisms). Asclepius reports critical actions. Neither isolates guardrail, permission-gate, contraindication-check, escalation or abstention components against unsafe-action metrics.
  3. **Frontier-closed vs small-open interaction**: MedicalHarness used only small open models. Whether harness share shrinks with frontier models is suggested by MAI-DxO but not formally decomposed.
  4. **Cost and latency as first-class harness outcomes** in a low-resource health system (e.g., Thai public hospitals), building on the Kather overhead findings and SDBench cost modelling.
  5. **Run-to-run variance**: MedicalHarness found 18% seed variance (40% on MedPlanning), so any thesis must use multiple seeds and paired tests.

### Gaps
- Not verified whether EvoClinician, HORIZON or Meta-Harness are medical-specific or general.
- Did not find a systematic review specifically of "medical agent harnesses". A general medical-MAS review exists — [Preprints.org 202606.0640](https://www.preprints.org/manuscript/202606.0640) [S] — and a curated list — [Landmark-of-medical-agent](https://nus-project.github.io/Landmark-of-medical-agent/) [S] — neither was read.

---

## Q5. Evidence from Asian / low-resource-language settings

### Takeaway
Asian medical LLM work is mostly knowledge-QA benchmarks and fine-tuned models: Thai Eir, Vietnamese VM14K. China has large-scale deployments with weak evaluation (DeepSeek in hospitals, Agent Hospital/Zijing). No agentic, tool-using, harness-level clinical benchmark or harness ablation was found for Thai or other SE Asian languages. This is the clearest open gap.

### Cited Findings
- **Eir** (2024, pre-2025): an 8B Thai medical LLM evaluated on 18 Thai clinical tasks, reported to exceed GPT-4o by more than 11%. A model paper, not an agent harness. — [arXiv 2409.08523](https://www.arxiv.org/pdf/2409.08523v1) [S]
- **VM14K** (2025): about 14k Vietnamese medical MCQs across 34 specialties; knowledge QA, not agentic. — [arXiv 2506.01305](https://arxiv.org/pdf/2506.01305) [S]
- **Agent Hospital / Zijing AI Doctor** (Tsinghua):
  - Simulation research from 2024, then press reports of 42 AI doctors and public use. — [Med-Tech World](https://med-tech.world/news/worlds-first-ai-hospital-china/) [S]
  - No independent outcome evaluation found. Original paper: [arXiv 2405.02957](https://arxiv.org/abs/2405.02957) [T]
- **DeepSeek in Chinese hospitals**:
  - A survey of 261 hospitals found national local-deployment rate is low (0.7%). — [medRxiv 2025.05.15.25326843](https://www.medrxiv.org/content/10.1101/2025.05.15.25326843v1.full.pdf) [S]
  - A scoping review of the top 100 hospitals found 58 deployments across 48 hospitals. Only 36.2% reported pre-deployment assessment, and 22.4% reported results. — [JMIR preprint 80770](https://preprints.jmir.org/preprint/80770) [S]
  - A JAMA perspective co-authored by Tsinghua Medicine's Wong Tien Yin warns of "substantial clinical risk". — [SCMP](https://www.scmp.com/tech/tech-trends/article/3310178/deepseeks-ai-hospitals-too-fast-too-soon-chinese-medical-researchers-warn) [S]
- **Language mismatch in the Kather-lab benchmark**: authors were in Germany and China, but all benchmarks were English. — [PMC13031301](https://pmc.ncbi.nlm.nih.gov/articles/PMC13031301/) [V]

### Inferences
- A Thai-language, Thai-health-system medical harness with controlled ablations has no direct prior art in what was found:
  - Thai tools: formulary/DDI, Thai CPG retrieval, NHSO/UCS coverage rules, ICD-10-TM.
  - Thai safety hooks.
  - Evaluation on a Thai-adapted MedAgentBench/FHIR or SDBench-style task set.
- To be credible it must cite and position against MedicalHarness, Asclepius, MAI-DxO and MedAgentBench v2. It must not claim the general idea is new.
- China's deployment-without-evaluation pattern supports a framing around harness-level auditability and evaluation for non-English health systems.

### Gaps
- Did not search Japanese, Korean, Indonesian or Indian agentic clinical benchmarks specifically, such as KorMedMCQA-based agents or Indic health agents. A targeted follow-up search is needed.
- Did not confirm whether any Thai hospital (e.g., Siriraj, Ramathibodi, Chulalongkorn) has published an agentic or tool-using LLM evaluation. The parallel "Thai medical LLM landscape" notes may cover this.
