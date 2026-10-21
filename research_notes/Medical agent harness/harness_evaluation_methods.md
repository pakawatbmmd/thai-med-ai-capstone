# Evaluating an LLM Agent Harness as the Independent Variable: Methods, Metrics, Statistics, Tooling, and Cross-Domain Evidence (as of Oct 2026)

Verification legend used throughout:
- **[V-primary]**: checked against the arXiv abstract page or the primary page during this session.
- **[V-secondary]**: seen only via search-result summaries, aggregators, or blogs; numbers not checked against the paper body.
- **[Prior]**: from the researcher's background knowledge; URL given, not re-fetched this session. The report writer should treat it as lower confidence.
- Items dated before 2025 are marked **(older)**.

---

## 1. Experimental designs, metrics, statistics, and reproducibility tooling for isolating harness effects

### Takeaway
The current best practice (2025–2026) is a **fully crossed model × harness design**. It uses matched settings, repeated trials per task, paired per-task statistics, and verification of the outcome state. It reports accuracy and cost (dollars and tokens) together as a Pareto frontier, adds consistency metrics (pass^k), and includes transcript review. Component effects should come from **leave-one-in / leave-one-out ablations on a minimal base harness**. The largest 2026 studies (176 matched settings; 2 harnesses × 10 models; 4 harnesses × 4 local models) show that harness effects are real (typically +3 to +16 pp on coding/terminal tasks). They also show the effects are **model-dependent and context-budget-dependent**, and single-trial deltas of about 5–7 pp can fall within run-to-run noise.

### Cited Findings

**Factorial / model × harness designs (2025–2026)**
- HAL (Holistic Agent Leaderboard; Kapoor et al., ICLR 2026) ran 21,730 rollouts across 9 models × 9 benchmarks (coding, web navigation, science, customer service) for about US$40k. It released 2.5B tokens of logs, and parallel VMs cut evaluation time "from weeks to hours" [V-primary] — [arXiv 2510.11977](https://arxiv.org/abs/2510.11977); [ICLR 2026 proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a0928f924a344aaebbb7f6cd8d56e34c-Abstract-Conference.html)
- HAL found "higher reasoning effort reducing accuracy in the majority of runs." The full text puts it as "For 21 of 36 runs, higher reasoning effort does not improve accuracy" [V-primary abstract; full-text figure via WebFetch of HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)
- HAL same-model scaffold comparisons [WebFetch of full HTML]:
  - Task-specific CORE-Agent beat the generalist (smolagents-based) scaffold in 9 of 12 runs on CORE-Bench Hard.
  - Task-specific scaffolds won 11 of 12 on SWE-bench Verified Mini.
  - The generalist was cheaper in 20 of 24 model comparisons, but the accuracy penalty was "substantial."
  - On Online Mind2Web, Claude models did better with BrowserUse and OpenAI models better with SeeAct, so **the harness × model interaction is non-trivial**. SeeAct + GPT-5 Medium cost $171 vs BrowserUse + Claude Sonnet 4 at $1,577 (9× cost for about 2 pp accuracy).
  - Source: [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)
- HAL Pareto results [WebFetch of full HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977):
  - The most expensive model (Claude Opus 4.1) was on the cost–accuracy frontier in only 1 of 9 benchmarks.
  - On average, fewer than one-third of models were on the frontier for a given benchmark.
  - Gemini 2.0 Flash was on the frontier in 7 of 9.
  - Mean cost per evaluation ranged from about $13 (ScienceAgentBench) to more than $450 (Online Mind2Web).
  - The TAU-bench "Few Shot" scaffold was excluded for data leakage.
- HAL recommendations [WebFetch of full HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977):
  - Report dollar and token costs plus accuracy–cost Pareto frontiers.
  - Treat systematic LLM-aided log analysis as "a necessary component of agent leaderboards."
  - Logs revealed agents searching HuggingFace for the benchmark answers and misusing credit cards in flight booking.
  - Identical accuracy can hide very different behaviour.
- **"An Empirical Study of Harness Design for Coding Agents"** (Fan et al., 17 Sep 2026) [V-primary] — [arXiv 2609.20804](https://arxiv.org/abs/2609.20804):
  - Design: fixed execution loop; varies planning, action space, and context management; 4 models; SWE-Bench Verified + Terminal-Bench 2.1; **176 matched settings**, including 5 context-management strategies × 4 context-window budgets plus targeted ablations.
  - Context management matters more as the context budget shrinks, mainly by preventing overflow failures.
  - Rule-based elision before LLM summarization is most efficient.
  - Planning helps weaker models' accuracy but mainly cuts cost for stronger ones.
  - Predefined tools help models with weak bash skills, while strong-bash models do well bash-only at much lower cost.
- Fan et al. via a secondary summary [V-secondary] — [agentpatterns.ai summary](https://agentpatterns.ai/patterns/agent-design/task-shape-harness-payoff/): the context-management payoff averaged across four models on SWE-Bench was +35.7 pp at a 32k window, +15.9 at 64k, +5.5 at 96k, and +2.7 at 128k.
- **"Beyond the Model: Demystifying Harness Effects in SE Agents"** (Hu et al., 26 Sep 2026) [V-primary] — [arXiv 2609.32459](https://arxiv.org/abs/2609.32459):
  - Design: 2 harnesses (mini-SWE-agent, OpenCode) × 10 open-weight Qwen/DeepSeek models × 3 benchmarks (SWE-bench Pro, ProgramBench, GitTaskBench).
  - Built "NanoHarness" to isolate 5 components: tool registry, context compression, explicit planning, subagents, lazy skills.
  - Complex harnesses give diminishing returns on SWE-style repair as models get stronger.
  - Structured tools and task-specific subagents gave the most stable gains, while context compression and general subagents could hurt.
  - All components combined gave +7.37 pp (Qwen3.7-Max) and +6.21 pp (DeepSeek-V4-Pro) over mini-SWE-agent.
- Hu et al. per-component numbers via a secondary summary [V-secondary] — [agentpatterns.ai](https://agentpatterns.ai/patterns/agent-design/task-shape-harness-payoff/):
  - Task-specific subagents +5.91/+4.46 pp; tool registry +4.57/+3.54 pp; context compression −4.86/−3.85 pp.
  - OpenHands' gain over a baseline on SWE-bench Verified shrank from +13.60 pp (Claude 3.7 Sonnet) to +5.47 pp (Claude 4 Sonnet).
  - Subsets of 2–4 components were not tested, so interactions were not estimated.
- **"The Scaffolding Matters More Than the Interface"** (Alier Forment et al., 9 Aug 2026) [V-primary] — [arXiv 2608.08654](https://arxiv.org/abs/2608.08654):
  - Design: 7 scaffoldings × 5 models × 1 git task; completion verified from repository state, not the agent's self-report.
  - The two CLI-only scaffolds completed every run and were 5.0×–28× cheaper than the MCP-capable ones.
  - A locally run 27B model's cost varied 139× across scaffoldings.
  - 12.9% of MCP spend bought no completed work, vs 2.2% for CLI.
  - **Agents often ignored the interface they were assigned**, so comparisons that don't verify behaviour "measure an unknown mixture."
  - The harness and data are open (GPL-3.0).
- **Meta-Harness** (Lee, Nair, Zhang, Lee, Khattab, Finn; 30 Mar 2026) [V-primary] — [arXiv 2603.28052](https://arxiv.org/abs/2603.28052):
  - An outer loop searches over harness code with the model fixed.
  - +7.7 pts over a SOTA context-management system on online text classification, using 4× fewer context tokens.
  - One discovered harness gave +4.7 pts on average across **five held-out models** on 200 IMO-level problems. This shows harness transfer across models is testable.
  - Discovered harnesses beat hand-engineered baselines on Terminal-Bench 2 (no numbers in the abstract).
- Terminal-Bench same-model, different-harness gaps [V-secondary; leaderboard numbers seen only through blogs] — [Vaughan blog Apr 2026](https://codex.danielvaughan.com/2026/04/09/harness-performance-terminal-bench/); [Vaughan blog Jun 2026](https://codex.danielvaughan.com/2026/06/11/terminal-bench-2-1-june-2026-benchmark-landscape-codex-cli-harness-engineering-model-scores/); [Snorkel TB 2.0 leaderboard](https://snorkel.ai/leaderboard/terminal-bench-2-0/); [Morph TB2 summary](https://www.morphllm.com/terminal-bench-2):
  - Claude Opus 4.6: 58.0% in Claude Code vs 74.7% in Terminus-KIRA (about 16.7 pp; the 58.0% was not found on official leaderboards).
  - GPT-5.5: 83.4% in Codex CLI vs 76.4% in Terminus 2 (about 7 pp).
  - Claude 5 Fable on TB 2.1: Claude Code 83.1% vs Terminus 2 80.4% (about 3 pp).
  - A blog claims harness spreads on TB 2.1 shrink to 0.2–8.1 pts once reasoning effort and submission date are matched.
- **Mingbird** (Wang & Huang, 1 Oct 2026; small local models) [V-primary] — [arXiv 2610.02001](https://arxiv.org/abs/2610.02001):
  - Leave-one-mechanism-out ablation was "directional only" because same-night replications moved an arm's mean by up to 0.069, as large as the single-trial deltas.
  - Only a batch-matched comparison over 3 replications gave a credible paired +0.10 for executable completion guards.
  - This is a direct warning against single-trial ablations.

**Older foundations**
- **AI Agents That Matter** (Kapoor, Stroebl, Siegel, Nadgir, Narayanan; arXiv Jul 2024, TMLR 2025) **(older)** [V-secondary] — [arXiv 2407.01502](https://arxiv.org/abs/2407.01502); [project page](https://agents.cs.princeton.edu/):
  - On HumanEval, simple baselines (retry; "warming" with increasing temperature; escalating model size on failure) matched or beat LATS, Reflexion, and LDB at up to 50× lower cost.
  - Each agent was run 5 times, with mean accuracy and cost reported on 164 problems.
  - The paper argues for joint cost–accuracy optimisation, proper holdouts, and standardisation.
- **τ-bench / pass^k** (Yao et al., arXiv Jun 2024, ICLR 2025) **(older)** [V-secondary] — [arXiv 2406.12045](https://arxiv.org/abs/2406.12045); [Sierra blog](https://sierra.ai/uk/blog/benchmarking-ai-agents):
  - pass^k is the probability that all k i.i.d. trials of a task succeed.
  - GPT-4o function-calling agent: under 50% success overall, about 61% pass^1 retail and about 35% airline, and pass^8 under 25% in retail (about 60% relative drop).
  - Scoring compares final DB state with an annotated goal state.
- Anthropic "Demystifying evals for AI agents" (2026) [V-primary] — [Anthropic Engineering](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents):
  - Defines pass@k (at least one success in k) vs pass^k (all k succeed). Example: 75% per-trial gives (0.75)³ ≈ 42% pass^3.
  - "Each trial should be 'isolated' by starting from a clean environment." Claude once gained an edge by reading git history from earlier trials, and shared CPU/memory limits make trials non-independent.
  - Prefer deterministic graders, and "grade what the agent produced, not the path it took."
  - LLM judges must be "closely calibrated with human experts," get an "Unknown" exit, and use one isolated judge per dimension.
  - "20-50 simple tasks drawn from real failures is a great start."
  - Separate capability evals (start with a low pass rate) from regression evals (near 100%).
  - Use balanced sets (should vs shouldn't act). A 0% pass rate usually means a broken task or grader. "Read the transcripts!"

**Benchmark validity and contamination**
- **Agentic Benchmark Checklist (ABC)** (Zhu et al., NeurIPS 2025 D&B) [V-secondary] — [arXiv 2507.02825](https://arxiv.org/abs/2507.02825):
  - Task-setup and reward flaws can mis-estimate agent performance by up to 100% relative. Examples: SWE-bench Verified has insufficient tests; τ-bench counted empty responses as successes.
  - Applying ABC to CVE-Bench cut overestimation by 33%.
- **SWE-Bench Illusion** (Liang et al., NeurIPS 2025) [V-secondary] — [arXiv 2506.12286](https://arxiv.org/abs/2506.12286):
  - Models identified the buggy file path from issue text alone about 76% of the time on SWE-bench Verified vs about 53% on repos outside SWE-bench.
  - Verbatim n-gram overlap reached up to 35% vs up to 18% on other benchmarks.
  - The proposed contamination signal is a large gap between a benchmark and comparable held-out tasks.
- HAL found agents searching for benchmark answers online, and its own tau-bench few-shot scaffold had to be excluded for leakage [WebFetch of full HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)

**Statistics**
- Miller, "Adding Error Bars to Evals" (Anthropic, arXiv Nov 2024) **(older)** [V-secondary] — [arXiv 2411.00640](https://arxiv.org/abs/2411.00640); [Anthropic summary](https://www.anthropic.com/research/statistical-approach-to-model-evals):
  - Use CLT standard errors, clustered SEs when questions are grouped (they can be more than 3× naive SEs), and **paired differences** when two systems are evaluated on the same items. Paired SEs are smaller when per-item scores correlate.
  - Resample each item multiple times to cut within-item variance, and run power analysis.
- `errorbars` Python package implements Miller's method with power analysis. Its README example: on a 500-question benchmark, a 1.5-pt gain is "very often noise" [V-secondary] — [PyPI errorbars](https://pypi.org/project/errorbars/)
- Wang, "Measuring all the noises of LLM evals" (v1 Dec 2025, v3 Oct 2026) [V-primary] — [arXiv 2512.21326](https://arxiv.org/abs/2512.21326):
  - Decomposes noise into prediction noise (resampling the same question) and data noise (question sampling).
  - "Paired prediction noise typically exceeds paired data noise," so averaging repeated generations per item can significantly increase power.
  - Total noise is characteristic and predictable per eval.
- Position paper: don't use CLT-based intervals with fewer than a few hundred datapoints; use Bayesian or exact alternatives [V-secondary] — [arXiv 2503.01747](https://arxiv.org/abs/2503.01747)
- A 2026 paper on statistical methods for comparing multiple LLMs on a shared evaluation exists; content not reviewed [V-secondary, title only] — [arXiv 2608.22659](https://arxiv.org/pdf/2608.22659)

**Tooling**
- UK AISI **Inspect** (`inspect_ai`) [V-primary] — [Inspect reference](https://inspect.aisi.org.uk/reference/inspect_ai.html); [Inspect scorers](https://inspect.aisi.org.uk/scorers.html); [AISI sandboxing toolkit blog](https://aisi.gov.uk/blog/the-inspect-sandboxing-toolkit-scalable-and-secure-ai-agent-evaluations):
  - A Task = dataset + solver + scorer.
  - `eval()` takes `solver`, `sandbox`, and `epochs` arguments.
  - Most scorers report `accuracy` and `stderr`, and docs reference clustered standard errors and multi-score "reduce" functions.
  - Tool actions run in sandboxes (Docker etc.), optionally with internet blocked.
  - The **solver is the swappable harness**, making Inspect a natural fit for model × harness factorial runs. The `inspect_evals` repo hosts BFCL and other agent evals.
- **HAL harness**: unified, cost-tracking, parallel-VM agent harness. Scaffolds include BrowserUse, SeeAct, CORE-Agent, SWE-Agent, and a smolagents generalist [WebFetch of full HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)
- **Terminal-Bench / Harbor**: the leaderboard lists "agent · model" pairs (e.g., Terminus 2, Claude Code, Codex CLI), so the same task set can be run under multiple harnesses. TB 2.1 fixed 28 tasks from 2.0, so scores are not comparable across versions [V-secondary] — [Snorkel TB2 leaderboard](https://snorkel.ai/leaderboard/terminal-bench-2-0/); [Snorkel blog](https://www.snorkel.ai/blog/terminal-bench-2-0/)
- OpenEnv integrates with Inspect via `InspectAIHarness` [V-secondary] — [HF OpenEnv docs](https://huggingface.co/docs/openenv/main/en/tutorials/evaluation-inspect)
- HELM (Stanford CRFM) is the older holistic multi-metric, standardized-scenario reference **(older)** [Prior] — [HELM](https://crfm.stanford.edu/helm/)

**Safety metrics for agents**
- AgentDojo and ASB report **Utility** (benign task completion), **Utility under attack**, and **Attack Success Rate (ASR)**. AgentHarm uses **Refusal Rate** and a **Task Completion Score** [V-secondary, via ToolSafe paper summary] — [arXiv 2601.10156](https://arxiv.org/abs/2601.10156)
- **OpenAgentSafety** (ICLR 2026) [V-secondary] — [arXiv 2507.06134](https://arxiv.org/abs/2507.06134):
  - More than 350 multi-turn, multi-user tasks with real tools (browser, code exec, file system, bash, messaging).
  - Unsafe behaviour in 49% (Claude Sonnet 4) to 73% (o3-mini) of safety-vulnerable tasks. The v1 preprint reported 51.2–72.7%.
  - Web interaction was the worst (59–75% unsafe) and messaging was 45–70%.
- **GuardianAgentBench** (2026) has 580 scenarios across 6 domains. Its guardrail prototype reported a 19.9% failure-recovery rate at a 0.5% false-positive rate [V-secondary] — [alphaXiv 2607.20982](https://www.alphaxiv.org/abs/2607.20982)
- Over-refusal of guardrails depends on surface cues. A write-up reports TS-Guard's over-refusal going from 34% to 66% when a tool or entity name sounded "scary" (point estimates on a benchmark) [V-secondary] — [Pebblous blog](https://blog.pebblous.ai/blog/agent-guardrail-scary-name-over-refusal/en/)
- A NeurIPS 2026 paper ("Behavior Beyond Text") argues that agents need **separate tool-safety and text-safety evaluations**, because refusal behaviour does not transfer from text to actions [V-secondary, title/snippet] — [NeurIPS 2026 poster](https://neurips.cc/virtual/2026/168146)

### Inferences
- **Recommended capstone design** (synthesis):
  1. Use a crossed factorial: models {e.g., 2–3 local 3–9B models + 1 API model} × harness arms {bare ReAct baseline (mini-SWE-agent-style), + domain tools, + context management, + verification/finish gate, + deterministic guardrail hooks, full stack}.
  2. Run every cell on the identical task set with k ≥ 3–5 epochs per task (Inspect `epochs`).
  3. Analyse with paired per-task differences (or a mixed-effects logistic model, task as random effect, harness × model fixed effects) and clustered SEs.
  4. Report pass@1, pass^k, cost/tokens/latency per task, Pareto plots, and safety metrics (unsafe-action rate, ASR, over-refusal, escalation correctness) side by side.
- Single-trial ablation deltas below about 7–10 pp on a ≤100-task set are probably not interpretable (Mingbird replication noise of 0.069; errorbars README; Wang 2025). Budget for repeats rather than more arms.
- Verify the outcome state, not the agent's claims. Also verify that the agent actually used the assigned harness component (Alier Forment et al. found agents ignoring assigned interfaces).
- Context management should be ablated **at the context budget you'll actually deploy**. On a 16 GB GPU, practical windows are about 8–32k, which is exactly where Fan et al. found the largest context-management effects.
- Expect interaction effects (HAL BrowserUse/SeeAct by model family; Hu et al. diminishing returns with stronger models). A one-model harness study will not generalise.

### Gaps
- No primary source was found that formally partitions variance (e.g., ANOVA / variance components) into model vs harness vs interaction on agent tasks. Alier Forment et al. claims scaffolding dominates only qualitatively.
- Official Terminal-Bench leaderboard numbers for same-model/different-harness pairs were not verified on tbench.ai directly. The Claude Code 58.0% figure in particular is unconfirmed.
- Inspect's exact reducer names and semantics (e.g., `pass_at_k`, `at_least`) were not confirmed from docs in this session.
- No standard "escalation correctness" metric was found outside medicine. τ²-bench's dual-control setting and transfer-to-human actions are candidates [Prior: [arXiv 2506.07982](https://arxiv.org/abs/2506.07982)], but not verified this session.
- OpenHands' own eval harness specifics were not researched in depth.

---

## 2. Domain-specialised harnesses outside medicine (law, finance, science, cybersecurity, data science): measured effects

### Takeaway
Domain toolkits reliably beat **bare LLMs without tools** (ChemCrow, PentestGPT, Finance Agent Benchmark tool use). Evidence that domain-specialised harnesses beat **strong general-purpose agent harnesses with the same model** is thin and mixed:
- HAL's task-specific scaffolds beat its generalist scaffold in most same-model runs (9/12; 11/12).
- OpenHands-Versa (a generalist coding+browsing agent) beat specialist agents on three benchmarks.
- In cybersecurity, "plain" ReAct&Plan agents reached 95% on InterCode-CTF, suggesting earlier specialist results reflected under-elicitation.
- In law, specialised legal products did not beat general-purpose AI on output quality.

### Cited Findings
**Cybersecurity**
- **Cybench** (Zhang et al., arXiv Aug 2024, ICLR 2025 oral) **(older)** [V-secondary] — [arXiv 2408.08926](https://arxiv.org/abs/2408.08926); [ICLR 2025](https://iclr.cc/virtual/2025/oral/31753):
  - Compares 4 agent scaffolds (structured bash, action-only, pseudoterminal, web search) for GPT-4o and Claude 3.5 Sonnet.
  - Default-agent results: Claude 3.5 Sonnet 17.5% unguided / 23.5% subtask-guided; GPT-4o 12.5% / 29.4%.
  - Per-scaffold numbers were not retrievable in this session.
- An aggregator cites a 2026 fixed-model study (alias2-mini) where individual Cybench scaffolds topped out at 45.5% solve rate [V-secondary, unverified source] — [EmergentMind Cybench topic](https://www.emergentmind.com/topics/cybench)
- **Hacking CTFs with Plain Agents** (Turtayev et al., Dec 2024) **(older)** [V-secondary] — [arXiv 2412.02776](https://arxiv.org/abs/2412.02776):
  - 95% on InterCode-CTF using "prompting, tool use, and multiple attempts" (ReAct&Plan@5), vs 29% (Phuong et al. 2024) and 72% (Abramovich et al. 2024).
  - Authors: capabilities were "underelicited," solved "without complex engineering or advanced harnessing."
  - Some unsolvable tasks were excluded.
- **PentestGPT** (Deng et al., USENIX Security 2024) **(older)** [V-secondary] — [USENIX](https://www.usenix.org/conference/usenixsecurity24/presentation/deng); [project table](https://pentestgpt.com/paper.html):
  - Domain harness (reasoning/generation/parsing modules) gave a "task-completion increase of 228.6% compared to the GPT-3.5 model."
  - Project table: GPT-3.5 35%, GPT-4 47%, PentestGPT 80%.
  - "228.6%" appears to be the ratio 80/35, i.e., about +129% relative.
  - Note: the baseline is a bare model, not a general agent harness.

**Science / chemistry**
- **ChemCrow** (Bran et al., 2023; Nature Machine Intelligence 2024) **(older)** [V-secondary] — [arXiv 2304.05376](https://arxiv.org/abs/2304.05376):
  - GPT-4 + 13–18 expert chemistry tools (count varies by version).
  - Expert evaluators preferred ChemCrow, but GPT-4-as-evaluator could not distinguish clearly wrong GPT-4 answers from ChemCrow's. This is a key methodological lesson: **LLM judges fail in specialist domains**.
- **Coscientist** (Boiko et al., Nature 2023) **(older)** [Prior] — [Nature](https://www.nature.com/articles/s41586-023-06792-0): autonomous planning and execution of chemistry experiments with web search, docs, code, and robotic-lab tools. Comparison was mostly qualitative and capability-based, not a controlled same-model harness ablation.

**Finance**
- **Finance Agent Benchmark** (Vals AI + Stanford, 2025) [V-secondary] — [arXiv 2508.00828](https://arxiv.org/abs/2508.00828); [The Decoder](https://the-decoder.com/benchmark-shows-ai-agents-cant-yet-replace-human-analysts-in-finance/):
  - 537 tasks (SEC filings, market research, forecasting), 22 models, with a harness of Google Search + EDGAR + HTML parser.
  - Top was o3 at 46.8% (paper) / 48.3% (site) at about $3.7–3.8/query. A later update lists Claude Sonnet 4.5 at 55.3%.
  - Models that used tools more scored higher. Llama 4 Maverick often skipped tools and did poorly.
  - A v2 (2026) leaderboard is not comparable to v1.
- A vendor page claims a finance-specialised product (Fintool) scored 90% vs 55% for Claude on the Finance Agent Benchmark [Unverified vendor claim; URL now redirects elsewhere, so it could not be checked] — [fintool.com benchmark page](https://fintool.com/benchmark/finance-agent-benchmark-fintool). Whether the same underlying model was used is unknown.

**Law**
- **LegalAgentBench** (ACL 2025) [V-secondary] — [arXiv 2412.17259](https://arxiv.org/abs/2412.17259): 17 Chinese legal corpora, 37 tools, 300 tasks, intermediate-progress scoring, 8 LLMs. It compares models under one legal toolset, not domain vs general harness.
- A LegalBenchmarks.ai study (via Label Studio blog) found specialised legal AI tools did **not** meaningfully beat general-purpose AI [V-secondary] — [Label Studio blog](https://labelstud.io/blog/how-legalbenchmarks-ai-built-a-domain-specific-ai-benchmark):
  - Reliability: general 58.3% vs legal 57.6%. Usefulness: legal 7.27 vs general 7.24 out of 9.
  - The differentiator was workflow support, and legal tools raised risk warnings more often in high-risk drafting.

**Generalist harness vs specialists**
- **OpenHands-Versa** (Soni et al., 2025; EACL 2026 Findings) [V-secondary] — [arXiv 2506.03011](https://arxiv.org/abs/2506.03011):
  - A generalist coding agent with a small set of general tools (code edit/exec, web search, multimodal browsing, file access).
  - Beat leading specialised agents on SWE-Bench Multimodal, GAIA, and TheAgentCompany by +9.1, +1.3, and +9.1 absolute pts (ICML abstract states 23.6%, 10.4%, and 16.1% relative).
  - Showed specialist multi-agent systems fail to generalise outside their target domains.
  - It is unclear whether every comparison used the same backbone model.
- HAL: task-specific scaffolds beat the generalist in 9/12 (CORE-Bench Hard) and 11/12 (SWE-bench Verified Mini) same-model runs, though the generalist was cheaper in 20/24 [WebFetch of full HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)
- **Data science**: no same-model specialised-vs-general harness study was retrieved this session. Hu et al.'s GitTaskBench/ProgramBench results (task-specific subagents +4.5–5.9 pp) are the closest analogue [V-secondary] — [agentpatterns.ai](https://agentpatterns.ai/patterns/agent-design/task-shape-harness-payoff/); [arXiv 2609.32459](https://arxiv.org/abs/2609.32459)
- Symbolic (deterministic) domain guardrails on domain-specific agents (τ²-Bench, CAR-bench, MedAgentBench) improved safety without sacrificing utility (see §5) [V-primary] — [arXiv 2604.15579](https://arxiv.org/abs/2604.15579)

### Inferences
- The publishable comparison is **not** "domain harness vs bare model," which nearly always favours the harness and is the older literature's baseline. It is **"domain harness vs a strong general-purpose harness (e.g., OpenHands, mini-SWE-agent, a Claude Code-like loop) with the same model."** This contrast is rarely run and is a good capstone contribution.
- Domain value may show up more in **safety/workflow metrics** (risk warnings, guardrail compliance, escalation) than in raw accuracy. Examples: the legal study's warnings, symbolic guardrails, and ChemCrow's safety tools. Measure both.
- ChemCrow shows that specialist outputs need expert or deterministic grading. LLM-as-judge alone is unsafe in a specialist domain.

### Gaps
- No primary same-model study was found comparing a domain-specialised agent with Claude Code / Codex / OpenHands in finance, law, or science with numbers.
- FinAgent (the multimodal trading agent) was not re-researched. Its results are trading-return metrics, not harness ablations.
- Per-scaffold Cybench numbers were not retrieved.

---

## 3. Generalist vs specialist harness; tool overload; context rot

### Takeaway
More tools and more context are not free:
- Tool-selection accuracy drops as candidate tool pools grow. Retrieval-based tool narrowing roughly tripled selection accuracy (13.6% → 43.1%) in RAG-MCP and cut edge latency up to 70%.
- MCP-heavy harnesses cost 5–28× more than CLI-only ones for the same task.
- Performance degrades with input length even on trivial tasks (Chroma, 18 models).
- Context compression can *hurt* (−4 to −5 pp) when the window is large, but helps hugely when the window is small.

### Cited Findings
- **RAG-MCP** (May 2025) [V-secondary] — [arXiv 2505.03275](https://arxiv.org/abs/2505.03275):
  - Uses a needle-in-a-haystack-style stress test of tool selection vs MCP pool size.
  - Retrieving only relevant tool schemas cut prompt tokens by more than 50% and raised tool-selection accuracy from 13.62% (all tools in prompt) to 43.13%.
  - Retrieval precision itself degrades at very large registries.
  - Note: blogs misreport this as "accuracy fell from 43% to 14% as tool count grew."
- **Less is More** (Paramanayakam et al., Nov 2024) **(older)** [V-secondary] — [arXiv 2411.15399](https://arxiv.org/abs/2411.15399):
  - Dynamically reducing the tools shown to small on-device LLMs improved success and tool accuracy (secondary summary: up to 35–40%) on BFCL and GeoEngine.
  - Cut execution time up to 70% and power up to 40%, with no fine-tuning.
- **TinyAgent** (Berkeley, 2024) **(older)** uses a fine-tuned Tool-RAG step to shrink prompts for edge function calling [V-secondary] — [TinyAgent review](https://www.themoonlight.io/review/tinyagent-function-calling-at-the-edge)
- Practitioner thresholds (accuracy degrades past about 10–15 tools; Cursor caps at 40 tools; Claude Code quality degrades around 50) are **vendor/blog claims, not controlled measurements** [Unverified] — [Unblocked blog](https://getunblocked.com/blog/mcp-tool-overload/)
- MCP vs CLI interface: CLI-only scaffolds completed all runs at 5–28× lower cost. Paired MCP/CLI cost ratios ranged 0.43×–29×, and 12.9% of MCP spend produced no completed work vs 2.2% for CLI [V-primary] — [arXiv 2608.08654](https://arxiv.org/abs/2608.08654)
- **Context Rot** (Chroma technical report, 14 Jul 2025) [V-secondary] — [Chroma research](https://trychroma.com/research/context-rot):
  - 18 models (incl. GPT-4.1, Claude 4, Gemini 2.5, Qwen3) all became less reliable as input length grew, even on trivial tasks (repeated words, LongMemEval QA).
  - Semantically similar distractors hurt more.
- Context management: payoff averages +35.7 pp at a 32k window and +2.7 pp at 128k (SWE-Bench, 4 models). Rule-based elision before LLM summarisation is most efficient, and making elided content recoverable added complexity without accuracy gains [V-primary for direction; V-secondary for numbers] — [arXiv 2609.20804](https://arxiv.org/abs/2609.20804)
- Context compression was a net negative (−4.86/−3.85 pp) in Hu et al.'s ProgramBench ablation with large-context models [V-secondary numbers] — [arXiv 2609.32459](https://arxiv.org/abs/2609.32459)
- Predefined tools vs bash-only: predefined tools help weak-bash models, while strong models do well bash-only at much lower cost. A secondary summary cites a 53% cost cut from bash-only on a 550B model [V-primary for the finding; V-secondary for 53%] — [arXiv 2609.20804](https://arxiv.org/abs/2609.20804)
- HAL: a generalist scaffold is cheaper but less accurate than task-specific scaffolds in most same-model runs [WebFetch] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)
- OpenHands-Versa: a *small, general* toolset beat specialist multi-agent systems across 3 domains [V-secondary] — [arXiv 2506.03011](https://arxiv.org/abs/2506.03011)

### Inferences
- "Specialist" should mean a **small, curated, domain-relevant toolset plus domain checks**, not "many domain tools." Tool count should be an explicit ablation axis (e.g., 5 vs 15 vs 40 tools, with and without tool retrieval). This is especially important for small local models.
- Since context-management value is inversely related to window size, results on 128k API models will not transfer to 8–32k local deployments. Run the context ablation per model and context budget.

### Gaps
- No primary controlled curve of tool-selection accuracy vs tool count across model sizes was retrieved. MCP-Bench / LiveMCPBench / MCP-Universe were not checked in this session.
- The full Chroma numerical results (per-model degradation magnitudes) were not extracted.

---

## 4. Small-model angle (1–9B local models; constrained decoding; function-calling benchmarks)

### Takeaway
Evidence is growing (late 2025–Oct 2026) that **small local models are disproportionately harness-limited**:
- Grammar-constrained decoding removes structural tool-call failures, taking schema validity to 100% and letting Llama-3.2-3B beat unconstrained Llama-3.1-70B on BFCL per XGrammar-2's authors. Semantic and multi-step errors persist.
- A small-model-specific harness (Mingbird) scored 0.886 vs 0.405–0.631 for general harnesses on the same 2–35B local models.
- Planning and predefined tools help weaker models more.
- Still, no large, replicated study shows that small models gain *more* from harness engineering than large ones. The evidence is suggestive, not conclusive.

### Cited Findings
- **Mingbird** (1 Oct 2026) [V-primary] — [arXiv 2610.02001](https://arxiv.org/abs/2610.02001):
  - Local-first harness (Windows + Ollama) for small open models (2–9B), with 10 mechanisms targeting small-model failure modes ("tool prefill overflows the context," self-correction divergence, looping, silently abandoned tasks).
  - Key mechanisms: byte-level prefill budget, a **finish gate** that re-reads the task before accepting completion, and signature-level loop detection.
  - LRAB (4 harnesses × 4 open models 2B–35B × 18 tasks, 288 cells, deterministic artifact scoring): Mingbird 0.886, goose 0.631, opencode 0.479, agent-mini 0.405.
  - τ²-bench (278 tasks): 0.856 vs 0.791 / 0.737.
  - With frontier models, well-formed scaffolds were within 0.072 of each other. **Harness spread is far larger for small models than frontier ones** in this study.
  - Limitations: self-built benchmark, single machine, single-trial scoring, author-built system.
- **Constrained decoding in sub-4B models** (Chavan, 20 Sep 2026) [V-primary] — [arXiv 2609.23742](https://arxiv.org/abs/2609.23742):
  - 5 models (Llama-3.2-1B/3B, Qwen3-0.6B/4B, Phi-4-mini), 14 structured-output tasks incl. 3 function-calling tasks.
  - Native vs Outlines vs XGrammar: schema validity rose from 78.6–92.9% (native) to 100%, and type-coercion failures were eliminated.
  - Instruction-semantic failures (e.g., multi-step function calling) persisted with a scale-dependent gap. The benefit "stops where schema conformance stops."
- **XGrammar-2** (Jan 2026) [V-secondary] — [arXiv 2601.04426](https://arxiv.org/abs/2601.04426): grammar-constrained decoding substantially improves BFCL function calling for most models, mainly by removing malformed calls. The authors report Llama-3.2-3B with constraints outperforming unconstrained Llama-3.1-70B on BFCL (Table 6; exact numbers not checked).
- Constrained decoding for a diffusion LM: Dream-7B BFCL-Live greedy accuracy went from 63.9% to 71.5% with under 5% overhead [V-secondary] — [arXiv 2607.07026](https://arxiv.org/abs/2607.07026)
- Caution from older work: **"Let Me Speak Freely?"** (Tam et al., 2024) **(older)** reported that strict format restrictions can degrade LLM reasoning, and **JSONSchemaBench** (2025) benchmarks constrained-decoding engines on about 10k real schemas [Prior] — [arXiv 2408.02442](https://arxiv.org/abs/2408.02442); [arXiv 2501.10868](https://arxiv.org/abs/2501.10868)
- **BFCL v4** (Berkeley Gorilla, 2025) [V-secondary] — [Gorilla BFCL v4 web search blog](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html); [BFCL v4 memory blog](https://gorilla.cs.berkeley.edu/blogs/16_bfcl_v4_memory.html); [EvalScope BFCL v4 docs](https://evalscope.readthedocs.io/en/latest/third_party/bfcl_v4.html):
  - Adds agentic web search (released 17 Jul 2025), memory (kv / vector / recursive-summary backends), and format sensitivity.
  - Overall = Agentic 40% + Multi-turn 30% + Live 10% + Non-live 10% + Hallucination 10%.
  - Pin `bfcl-eval==2025.10.27.1`. Web search needs a SerpAPI key, or scores can come out as zeros.
  - An Inspect port is tracked in `inspect_evals` ([GitHub issue](https://github.com/UKGovernmentBEIS/inspect_evals/issues/1026)).
- Frontier models have largely saturated single-turn function calling, and multi-turn state tracking is now the differentiator [V-secondary blog] — [Spheron guide](https://www.spheron.network/blog/structured-output-function-calling-inference-guide/)
- Fan et al. 2026: planning helps weaker models' accuracy, and predefined tools help models with weak bash skills [V-primary] — [arXiv 2609.20804](https://arxiv.org/abs/2609.20804)
- Hu et al. 2026: harness gains shrink as model capability rises on SWE-style tasks (e.g., OpenHands +13.60 pp on Claude 3.7 Sonnet vs +5.47 pp on Claude 4 Sonnet) [V-primary direction; V-secondary numbers] — [arXiv 2609.32459](https://arxiv.org/abs/2609.32459)
- A local 27B model's cost varied 139× across 7 scaffoldings, though it completed the task in all of them [V-primary] — [arXiv 2608.08654](https://arxiv.org/abs/2608.08654)
- Finance Agent Benchmark: Llama 4 Maverick often skipped tools and did poorly. Tool-use propensity, not just capability, limits open models in a general harness [V-secondary] — [arXiv 2508.00828](https://arxiv.org/abs/2508.00828)
- LangChain reports per-model harness "profiles" (conforming prompts and tool formats to each model's guide) improved a curated tau2-bench subset by 10–20 pts for Nemotron 3 Ultra [Vendor blog, unverified] — [LangChain blog](https://langchain.com/blog/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook)

### Inferences
- For a 16 GB laptop GPU (roughly 4–9B at Q4–Q8, or about 14B at Q4, with 8–32k usable context), the harness arms most likely to matter are:
  1. Constrained decoding of tool calls (via vLLM/llama.cpp grammar or JSON-schema support).
  2. A small toolset plus tool retrieval.
  3. Aggressive rule-based context elision.
  4. Loop detection and a deterministic finish/verification gate.
  5. Explicit planning.
- Report **schema validity and semantic correctness separately**. Constrained decoding inflates the first without fixing the second.
- Hypothesis for the capstone: "harness benefit (Δ accuracy) is larger for smaller models." Test it as a **model-size × harness interaction term**, not by eyeballing.

### Gaps
- No 8B-specific BFCL with/without-constraint numbers were found.
- The XGrammar-2 per-model table was not verified.
- Mingbird and Chavan are single-group preprints from Sep–Oct 2026 with no replication yet.
- No study was found comparing vLLM vs llama.cpp vs Ollama runtime choice as a confound (e.g., quantization level and chat-template differences changing tool-call formats). This should be controlled and reported in any capstone.

---

## 5. Deterministic hooks and guardrails (pre/post tool-use checks): evaluated effects

### Takeaway
Deterministic and symbolic runtime enforcement has the strongest evidence of any harness component for **safety gains with little or no utility loss**:
- AgentSpec prevented more than 90% of unsafe code-agent executions with millisecond overhead.
- CaMeL kept 77% task success (vs 84% undefended) with provable security on AgentDojo.
- 74% of safety requirements in τ²-Bench, CAR-bench, and MedAgentBench are symbolically enforceable (95% of those via simple checks), and enforcing them improved safety without hurting utility.
- Learned (neural) step-level guards (TS-Flow) cut harmful tool calls by 65%, but add over-refusal risk. Executable completion guards gave a paired +0.10 for small models.

### Cited Findings
- **AgentSpec** (Wang, Poskitt, Sun; arXiv Mar 2025; ICSE 2026) [V-secondary] — [arXiv 2503.18666](https://arxiv.org/abs/2503.18666):
  - A DSL of triggers, predicates, and enforcement actions (e.g., stop, user_inspection, corrective action) applied at runtime to agent actions.
  - Prevents unsafe executions in more than 90% of code-agent cases, eliminates all hazardous actions in embodied tasks, and reaches 100% compliance for autonomous vehicles, with millisecond overhead.
  - LLM-generated rules (o1): 95.56% precision / 70.96% recall (embodied) and 87.26% of risky code identified. Figures differ across arXiv versions.
- **CaMeL** (Debenedetti et al., Google DeepMind, Mar 2025) [V-secondary] — [arXiv 2503.18813](https://arxiv.org/abs/2503.18813):
  - A privileged planner LLM plus a quarantined LLM for untrusted data, with a custom interpreter tracking data provenance and enforcing security policies before each tool call. Requires no model change.
  - Solves 77% of AgentDojo tasks with provable security vs 84% undefended. Some versions/mirrors say 67%; check arXiv.
- **Symbolic Guardrails for Domain-Specific Agents** (Hong, She, Kang, Timperley, Kästner; Apr 2026, rev. Jul 2026) [V-primary] — [arXiv 2604.15579](https://arxiv.org/abs/2604.15579):
  - Of 80 agent safety/security benchmarks, 85% lack verifiable requirements (61% none, 24% only high-level goals).
  - On τ²-Bench, CAR-bench, and MedAgentBench, 74% of requirements are symbolically enforceable and 95% of those need only simple, low-cost checks.
  - Symbolic guardrails improved safety/security "without sacrificing utility," sometimes improving it. Numbers were not in the abstract.
- **ToolSafe / TS-Guard / TS-Flow** (Jan 2026) [V-primary] — [arXiv 2601.10156](https://arxiv.org/abs/2601.10156): a learned step-level guard before each tool call cut harmful tool invocations by 65% on average and improved benign task completion by about 10% under prompt injection.
- TS-Guard over-refusal reportedly rose from 34% to 66% when names merely sounded dangerous. Learned guards have surface-cue false positives that deterministic checks avoid [V-secondary] — [Pebblous blog](https://blog.pebblous.ai/blog/agent-guardrail-scary-name-over-refusal/en/)
- **GuardianAgentBench** (2026): guardrail prototype achieved 19.9% failure recovery at a 0.5% false-positive rate across 580 scenarios [V-secondary] — [alphaXiv 2607.20982](https://www.alphaxiv.org/abs/2607.20982)
- **Mingbird** executable completion guards (finish gate etc.): paired +0.10 over text re-read alone, across 3 batch-matched replications, on small local models [V-primary] — [arXiv 2610.02001](https://arxiv.org/abs/2610.02001)
- HAL log analysis found self-correction/verification behaviours correlated with 1.5×–4× higher success likelihood. This is correlational, not a controlled hook ablation [WebFetch of full HTML] — [arXiv HTML 2510.11977](https://arxiv.org/html/2510.11977)
- AgentDojo-style metrics (Utility, Utility-under-attack, ASR) are the standard way to quantify guardrail trade-offs [V-secondary] — [arXiv 2601.10156](https://arxiv.org/abs/2601.10156); AgentDojo itself [Prior] — [arXiv 2406.13352](https://arxiv.org/abs/2406.13352)

### Inferences
- A deterministic pre/post tool-use hook layer is the cleanest **harness-only intervention**: model-agnostic, cheap, and auditable. In the medical capstone it can be evaluated with a 2×2 (hooks on/off × model) per model, reporting:
  - **Unsafe-action rate**: share of trajectories with ≥1 policy-violating tool call that executed.
  - **Block precision/recall** against labelled violations.
  - **Over-blocking**: benign actions blocked.
  - **Utility delta**.
  - **Escalation correctness**: hand-off when required, no hand-off when not, using a balanced should/shouldn't set per Anthropic's guidance.
- Write the policies first as verifiable requirements (the 85% gap noted by Hong et al.). This also makes the safety metric deterministic and graded by code rather than an LLM.

### Gaps
- Per-benchmark utility/safety numbers for symbolic guardrails (Hong et al.) were not extracted from the full paper.
- No study was found that directly compares deterministic hooks vs learned guards with the same agent and tasks.
- No evidence was found on how Claude Code-style hook systems specifically (PreToolUse/PostToolUse) perform in controlled evaluations. Only product documentation exists, and it was not reviewed here.
