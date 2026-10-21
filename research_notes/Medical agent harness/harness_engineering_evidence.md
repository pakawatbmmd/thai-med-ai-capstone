# Harness Engineering as a Research Object: Evidence That the Agent Harness, Not Just the Model, Changes Task Performance (as of Oct 2026)

Verification legend used below:
- **[V-primary]** means I read the primary source (paper text, first-party blog or docs) this session.
- **[V-secondary]** means the claim comes from a secondary summary, a search snippet or an aggregator. I did not read the primary source.
- **[Pre-2025]** marks older work, kept because it is foundational.

---

## Q1. Definitions: what is an agent harness, and how does it differ from a model, app, prompt, skill, mode, plugin or multi-agent framework?

### Takeaway
The definition has converged: **agent = model + harness**. The harness is everything outside the weights that runs a task: the loop, the tools and their interface, context and memory management, state, sandbox, verification and guardrails. Prompts, CLAUDE.md files, skills, hooks, subagents, MCP servers and output styles ("modes") are **components or configuration of a harness**. They are not alternatives to it. Plugins are a **packaging layer** for those components. An "app" such as Claude Code is a productised harness plus a UI. A multi-agent framework (LangGraph, smolagents, OpenHands) is a **toolkit for building harnesses**.

### Cited Findings
- Wikipedia (2026) defines an agent harness, or agent scaffolding, as "the software infrastructure surrounding a large language model (LLM) that enables it to operate as an AI agent". It covers tool use, memory, state persistence, execution environments and feedback loops, as opposed to the model's internal reasoning. It gives the formula "agent = model + harness". Listed components: tool dispatch, memory/state persistence, isolated sandbox/workspace, context management, and guardrails (scoped permissions, approval tiers, monitoring). [V-primary, but a tertiary source] — [Wikipedia: Agent harness](https://en.wikipedia.org/wiki/Agent_harness)
- The same entry places prompt engineering (optimising a single interaction) and context engineering (what the model sees at a given moment) as **narrower layers contained within** harness engineering. It traces "model + scaffold" language to a UK AI Security Institute (then the AI Safety Institute) discussion paper from Oct 2023. — [Wikipedia: Agent harness](https://en.wikipedia.org/wiki/Agent_harness)
- Birgitta Böckeler (Thoughtworks, martinfowler.com, reportedly 2 Apr 2026) proposes three distinctions, as summarised by Wikipedia:
  - **inner harness** (shipped by the model builder) vs **outer harness** (assembled by the user: instruction files, MCP servers, custom skills);
  - **guides** (steer the agent before it acts) vs **sensors** (observe results and enable self-correction);
  - **computational** checks (linters, tests) vs **inferential** checks (LLM-as-judge).
  [V-secondary] — [Böckeler, "Harness engineering for coding agent users"](https://martinfowler.com/articles/harness-engineering.html) via [Wikipedia](https://en.wikipedia.org/wiki/Agent_harness)
- Anthropic (26 Nov 2025) calls the **Claude Agent SDK** "a powerful, general-purpose agent harness adept at coding", with tool use and context management such as compaction. Its long-running-agent design runs the *same harness* with two different initial prompts (an "initializer agent" and a "coding agent"), keeping system prompt, toolset and harness otherwise identical. This is effectively a within-harness manipulation of one component, the prompt. [V-primary] — [Anthropic, Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Anthropic (29 Sep 2025) defines **context engineering** as "the set of strategies for curating and maintaining the optimal set of tokens" during inference. It calls this "the natural progression of prompt engineering": prompt engineering covers writing instructions, while context engineering covers the whole state the model sees (tools, external data, message history) and is iterative on every turn. [V-primary] — [Anthropic, Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Claude Code documentation describes the product as "a model that reasons about your code with built-in tools", and describes an "extension layer" that "plug[s] into different parts of the agentic loop". The extensions, with the documentation's descriptions: [V-primary] — [Claude Code docs: Extend Claude Code](https://code.claude.com/docs/en/features-overview)
  - **CLAUDE.md** is persistent context loaded every session.
  - **Output styles** set "role, tone, and response format" for a session (the closest thing to a "mode").
  - **Skills** are a "markdown file containing knowledge, workflows, or instructions". Only their descriptions load at start; full content loads on demand or via `/name`.
  - **Subagents** "run their own loops in isolated context, returning summaries".
  - **Hooks** run a script, HTTP request, MCP tool call, prompt or subagent at lifecycle events. They are deterministic ("Fires on its event without Claude deciding").
  - **MCP** "connects Claude to external services and tools". Only tool names load at start; schemas are deferred via tool search.
  - **Plugins** "are the packaging layer. A plugin bundles skills, hooks, subagents, and MCP servers into a single installable unit."
- On enforcement, the Claude Code docs state: "An instruction like 'never edit .env' in CLAUDE.md or a skill is a request, not a guarantee. A PreToolUse hook that blocks the edit is enforcement." This separates **probabilistic harness components** (prompts, skills) from **deterministic ones** (hooks, permission gates). [V-primary] — [Claude Code docs](https://code.claude.com/docs/en/features-overview)
- LangChain (Vivek Trivedy, 17 Feb 2026): "The goal of a harness is to mold the inherently spiky intelligence of a model for tasks we care about". Harness engineering means optimising the system prompt, tools and execution flow (middleware) for task performance, token efficiency and latency. [V-primary] — [LangChain, Improving Deep Agents with harness engineering](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)
- Academic definition (Pan et al., arXiv 2603.25723, Mar 2026, rev. May 2026): a harness is "the external execution system around a model that organizes a task run". The authors argue harness logic is usually "buried in tightly coupled controller code", which makes it hard to inspect, compare, transfer and ablate. They propose expressing harnesses as editable natural-language documents (NLAHs) executed by a shared runtime, so harnesses can be treated "as scientific representation objects rather than incidental glue code". [V-primary, abstract only] — [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723)
- Terminal-Bench 2.0 (ICLR 2026) separates two harnesses:
  - **evaluation harness**: Harbor, which runs tasks in containers and orchestrates agents;
  - **agent scaffolds**: Claude Code, Codex CLI, Gemini CLI, OpenHands, Mini-SWE-Agent and Terminus 2.

  The paper notes "agent and model performance are hard to decouple. Many agent scaffolds have been engineered to accommodate the tendencies of certain models, especially when the model and agent are developed by the same organization." [V-primary] — [Terminal-Bench 2.0, arXiv 2601.11868](https://arxiv.org/html/2601.11868v1)
- The HAL paper (ICLR 2026) frames agent evaluation as three-dimensional: **models × scaffolds × benchmarks**. Its "standardized evaluation harness" is distinct from the agent scaffolds under test. [V-secondary, abstract/snippet] — [HAL, arXiv 2510.11977](https://arxiv.org/abs/2510.11977v1)

### Inferences
- A defensible operational definition for a capstone: the **harness** is the set of all non-weight, run-time choices that determine what the model sees and what its outputs can do. It has six parts:
  1. control loop/orchestration;
  2. tool set and tool interface (ACI);
  3. context/memory policy;
  4. state/persistence;
  5. verification, guardrails and permissions;
  6. instructions (system prompt, skills).

  Each part can be swapped while the weights are held fixed. That is what makes the harness a manipulable independent variable.
- Map the student's vocabulary as follows:
  - **Prompt, skill, output style ("mode"), CLAUDE.md:** instruction components of the harness. They are probabilistic and load into context.
  - **Hooks, permission gates:** deterministic control components.
  - **MCP servers:** a tool-provision protocol. They feed the tool component.
  - **Subagents:** an orchestration/context-isolation component.
  - **Plugin:** a distribution bundle, not a component.
  - **App** (Claude Code, Codex CLI): one specific harness plus a UI.
  - **Multi-agent framework** (LangGraph, smolagents): a library for building harnesses.
  - **Evaluation harness** (Harbor, HAL harness, Inspect): measures agents. It is not part of the agent.
- The model/harness boundary is blurred by post-training: vendors train models on their own harness, as the Terminal-Bench authors note. A committee may raise this. The answer is to report a model × harness interaction term rather than claim full independence.

### Gaps
- OpenAI's "Harness engineering" post (openai.com/index/harness-engineering) returned HTTP 403, so I could not verify its definition, date or quantitative claims. Wikipedia describes it only as "a widely cited OpenAI engineering report on a large codebase built largely by coding agents", undated. My recollection that it is a Feb 2026 post about Codex is unverified.
- I did not read OpenAI Agents SDK or Codex CLI documentation for a formal definition of "harness".
- I did not directly read the Böckeler article or Anthropic's Agent SDK launch post.

---

## Q2. Quantitative evidence that changing the harness while holding the model fixed changes results

### Takeaway
Same-model harness swaps routinely move scores by **3–17 percentage points (pp)** on mainstream agent benchmarks:
- Terminal-Bench 2.0: up to 16.9 pp across off-the-shelf agents.
- Engineered harness improvements: +13.7 pp (LangChain).
- Edit-interface changes alone: about +15 pp average across 16 models, and up to about +60 pp for one weak model.
- Single ACI ablations (SWE-agent): 2–8 pp.
- Cost-efficiency at equal accuracy can differ by up to about 100×.

However, **swapping the model usually moves scores more than swapping the harness**. On Terminal-Bench 2.0, models span about 3–58% under one fixed harness. The defensible claim is that the harness is a *significant, measurable second factor with strong model × harness interactions*, not that it dominates the model.

### Cited Findings

**A. Terminal-Bench 2.0: off-the-shelf harness swaps (ICLR 2026) [V-primary, Table 2 read directly]** — [arXiv 2601.11868](https://arxiv.org/html/2601.11868v1)
- Setup: 6 agents × 16 models, at least 5 runs per combination, 32,155 trials, 89 tasks. Resolution rates are reported with 95% CIs (about ±2–3 pp).
- **Terminus 2** is a deliberately neutral scaffold: "a single tool, a headless terminal, and completes tasks using only Bash commands."
- Same-model spreads across harnesses (resolution rate, highest to lowest):

| Model | Results by harness | Spread |
|---|---|---|
| Gemini 2.5 Pro | Terminus 2 32.6%; Mini-SWE-Agent 26.1%; Gemini CLI 19.6%; OpenHands 15.7% | **16.9 pp** |
| Claude Haiku 4.5 | Mini-SWE-Agent 29.8%; Terminus 2 28.3%; Claude Code 27.5%; OpenHands 13.3% | **16.5 pp** |
| GPT-5 | Codex CLI 49.6%; OpenHands 41.5%; Terminus 2 35.2%; Mini-SWE-Agent 33.9% | **15.7 pp** |
| Grok Code Fast 1 | Mini-SWE-Agent 24.5%; Terminus 2 14.5% | **10.0 pp** |
| GPT-5-Mini | Codex CLI 31.9%; OpenHands 27.7%; Terminus 2 24.0%; Mini-SWE-Agent 22.2% | **9.7 pp** |
| Grok 4 | Mini-SWE-Agent 29.0%; Terminus 2 23.4%; OpenHands 19.6% | **9.4 pp** |
| GPT-5.2 | Codex CLI 62.9%; Terminus 2 54.0% | **8.9 pp** |
| Claude Opus 4.5 | Terminus 2 57.8%; Claude Code 52.1%; OpenHands 51.9% | **5.9 pp** |
| GPT-5-Nano | Codex CLI 11.5%; OpenHands 9.5%; Terminus 2 7.9%; Mini-SWE-Agent 7.0% | 4.5 pp |
| GPT-OSS-120B | Terminus 2 18.7%; Mini-SWE-Agent 14.2% | 4.5 pp |
| Claude Opus 4.1 | Terminus 2 38.0%; Mini-SWE-Agent 35.1%; OpenHands 34.9%; Claude Code 34.8% | 3.2 pp |
| Claude Sonnet 4.5 | Terminus 2 42.8%; Mini-SWE-Agent 42.5%; OpenHands 40.3%; Claude Code 40.1% | 2.7 pp (within CI) |
| Kimi K2 Instruct | Terminus 2 27.8%; OpenHands 25.6% | 2.2 pp |
| Gemini 2.5 Flash | 15.4–17.1% across 4 harnesses | 1.7 pp |
| Qwen3 Coder 480B | OpenHands 24.3%; Terminus 2 23.9% | 0.4 pp |

- **The first-party harness was not always best.**
  - Gemini 2.5 Pro scored 13 pp *lower* in Gemini CLI than in the 1-tool Terminus 2.
  - Claude Opus 4.5 scored 5.7 pp lower in Claude Code than in Terminus 2.
  - Codex CLI was best for every GPT model tested.
- **Token cost varies by orders of magnitude for the same model.**
  - Opus 4.5: Claude Code used 256.9M input tokens vs 3.9M for Terminus 2.
  - Haiku 4.5: OpenHands used 663.1M input tokens vs 3.9M for Terminus 2.
  - Caveat: the table caption says token counts are "for running all 74 tasks", which is inconsistent with 89 tasks elsewhere. I did not resolve this.
- **The paper's own conclusion** favours the model: "Codex CLI resolution rate increases by 52% when using GPT-5.2 instead of GPT-5-Nano, while Gemini-2.5-Pro sees a 17% increase in resolution rate when paired with Terminus 2 instead of OpenHands, implying that model selection is usually more important than agent scaffold." Under the fixed Terminus 2 harness, models range from 3.1% (GPT-OSS-20B) to 57.8% (Opus 4.5).

**B. Engineered harness improvement, model fixed [V-primary]** — [LangChain, 17 Feb 2026](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)
- Setup: deepagents-cli with **GPT-5.2-Codex held fixed** on Terminal-Bench 2.0. Score went from **52.8% to 66.5% (+13.7 pp)**, roughly "Top 30 to Top 5". Only the system prompt, tools and middleware changed.
- No per-component ablation is reported. Changes made:
  - plan → build → verify → fix prompting;
  - `PreCompletionChecklistMiddleware`, which forces a verification pass before exit;
  - `LocalContextMiddleware`, which maps the directory and discovers tools at start;
  - time-budget warnings;
  - `LoopDetectionMiddleware`, which nudges the agent after N edits to the same file;
  - a "reasoning sandwich" schedule.
- One within-harness sub-result, on reasoning-effort scheduling:
  - xhigh-only: **53.9%** (timeouts);
  - high-only: **63.6%**;
  - xhigh-plan / high-build / xhigh-verify: **66.5%**.
- The most common failure the team observed was the agent "re-reading its own code, confirming it looked fine, and stopping" without running tests.
- Caveats: single benchmark, single model, no held-out set. Claude Opus 4.6 scored 59.6% on an earlier harness version.

**C. Automated harness search, model fixed [V-secondary, from search snippets of the paper]** — [Meta-Harness, Lee et al., arXiv 2603.28052, Mar 2026](https://arxiv.org/abs/2603.28052)
- Starting from Terminus 2 and Terminus-KIRA, an agentic proposer reads earlier harness code, scores and traces, then writes new harness code.
- On **Claude Opus 4.6**, the discovered harness scored **76.4%** vs the hand-engineered **Terminus-KIRA at 74.7%** on Terminal-Bench 2.0.
- Caveat: search and evaluation used the same 89 tasks with no held-out split. The authors say they audited for leakage.
- Other results:
  - +7.7 pts over a state-of-the-art context-management system on online text classification, using 4× fewer context tokens;
  - +4.7 pts average on 200 IMO-level problems across five held-out models, from a single discovered retrieval harness. This shows a harness transferring across models.

**D. Same model on public leaderboards [V-secondary]**
- A third-party leaderboard blog reports Claude Opus 4.6 at **58.0% in Claude Code vs 74.7% in Terminus-KIRA** on Terminal-Bench 2.0, a gap of about 16.7 pp. Unverified against tbench.ai. — [codex.danielvaughan.com, Apr 2026](https://codex.danielvaughan.com/2026/04/09/harness-performance-terminal-bench/)

**E. Edit-interface (ACI) change only, model fixed [V-primary, but a vendor/author benchmark, not peer reviewed]** — [Can Bölük, Stencil, 12 Feb 2026](https://stencil.so/blog/the-harness-problem)
- Setup: 16 models, 180 mutated-React-file bug-fix tasks × 3 runs. The only variable was the edit tool: `apply_patch`, str_replace, or "hashline" (lines tagged with content hashes).
- Results:
  - Hashline beat patch for **14 of 16 models**, averaging **+15 pts over patch**.
  - Grok Code Fast 1 went from **6.7% to 68.3%**. The per-row table lists +64.6, an internal inconsistency in the post.
  - Claude Sonnet 4.5 gained +14.4 over patch; Haiku 4.5 +13.0 over patch and +11.3 over str_replace.
  - GPT-5.2 Codex gained only +4.6.
  - DeepSeek V3.2 got worse: −5.
  - Output tokens fell 17–61% for most models.
- Caveat: the author built the hashline tool, and the task distribution is narrow.

**F. SWE-agent ACI ablations (NeurIPS 2024) [Pre-2025] [V-primary, Table 1 and Table 3 read]** — [Yang et al., SWE-agent, arXiv 2405.15793](https://arxiv.org/abs/2405.15793)
- Model held fixed at GPT-4 Turbo, on SWE-bench Lite (300 tasks):

| Configuration | Resolved | Change vs full SWE-agent |
|---|---|---|
| Full SWE-agent | 18.0% | — |
| **Shell-only** agent (no custom ACI) | 11.0% | −7.0 pp (SWE-agent is a "64% relative increase compared to Shell-only") |
| Shell-only without demonstration | 7.33% | −10.7 pp |
| No edit command | 10.3% | **−7.7 pp** |
| Edit without linting guardrail | 15.0% | −3.0 pp |
| Iterative search | 12.0% | −6.0 pp |
| No search tool | 15.7% | −2.3 pp |
| File viewer: 30 lines | 14.3% | −3.7 pp |
| File viewer: full file | 12.7% | −5.3 pp (100 lines was optimal) |
| Full history instead of last-5 observations | 15.0% | −3.0 pp |
| No demonstration | 16.3% | −1.7 pp |

- Full SWE-bench (2,294 tasks): SWE-agent 12.47% vs the previous best non-interactive RAG baseline at 3.8%. On Lite, SWE-agent cost 8–13× more than RAG and gave a 6.7-fold higher resolve rate.
- Note the iterative-search result: adding a tool can hurt. Iterative search scored below having no search tool, because agents "look through every match exhaustively".

**G. Pipeline vs agent [Pre-2025] [V-primary, abstract]** — [Xia et al., Agentless, arXiv 2407.01489](https://arxiv.org/abs/2407.01489)
- Agentless uses a fixed three-phase pipeline (localise → repair → validate) with no agent loop.
- It reached **32.00% (96/300) on SWE-bench Lite at $0.70**, "the highest performance… compared with all existing open-source software agents" at the time.
- This shows a *less agentic* harness can beat more agentic ones.

**H. Cross-benchmark scaffold analysis on HAL data [V-secondary: blog post read, underlying analysis not peer reviewed]** — [Gundlach, Brown, Lynch & Thompson (MIT FutureTech), "Just a Wrapper? How Much Do Scaffolds Matter?", 26 Jun 2026](https://www.lesswrong.com/posts/jXLi3dhSpSMd7B6z8/just-a-wrapper-how-much-do-scaffolds-matter-1)
- Data: 18 models, 8 HAL benchmarks, accuracy on a logit scale vs API cost.
- Findings:
  - Inference efficiency "can vary by up to **100x** between scaffolds". In the best cases, specialist scaffolds give about 100× cheaper performance at equal accuracy, which the authors equate to roughly two years of model progress.
  - In a regression controlling for log price and benchmark, **"scaffolds explain more variance in performance than models do"** (baseline adjusted R² = 0.519; per-factor increment not reported).
  - Scaffolds re-order model rankings. On GAIA, Kendall τ = 0.17, about a 58% chance two models keep their order. On CORE-Bench Hard the rank correlation is negative. On SciCode rankings are largely preserved.
  - Scaffold effects are heterogeneous by model. HF Open Deep Research helps some models and hurts others on GAIA. Self-Debug consistently improves both accuracy and cost on ScienceAgentBench. The SWE-agent harness reduces performance for some models.
- The authors call it a "first pass". It cannot isolate individual components, and specialist scaffolds may overfit.
- It cites Davidson et al. (2023) estimating the LATS scaffold at about a **10× compute-equivalent** gain [Pre-2025].

**I. HAL leaderboard: CORE-Bench Hard [V-primary, leaderboard page]** — [HAL, Princeton](https://hal.cs.princeton.edu/)
- Claude Opus 4.5 in a **Claude Code** scaffold scored **77.8% (95.5% with manual grading)** at $87.16.
- The earlier CORE-Agent scaffold with Claude Opus 4.1 scored 51.1% at $412.42.
- HAL states: "Running Opus 4.5 with an updated scaffold that uses Claude Code drastically outperforms the CORE-Agent scaffold we used." It then declared CORE-Bench "solved".
- Caveat: this is *not* a clean same-model comparison on the page (Opus 4.1 vs 4.5), and grading was also fixed.
- Claude Sonnet 4.5 with Claude Code scored 62.2%.
- HAL totals 26,597 rollouts on the site; the paper reports 21,730 rollouts, 9 models, 9 benchmarks and about $40k. The paper's headline finding that "higher reasoning effort reduced accuracy in the majority of runs" is from a snippet only. — [HAL paper arXiv 2510.11977](https://arxiv.org/abs/2510.11977v1); [ICLR 2026 listing](https://iclr.cc/virtual/2026/poster/10006806)

**J. Context-management policy, model and scaffold fixed [V-secondary, abstract/snippets]** — [Lindenbauer et al., "The Complexity Trap", arXiv 2508.21433, NeurIPS 2025](https://arxiv.org/abs/2508.21433)
- In SWE-agent on SWE-bench Verified, simple **observation masking** (hiding old tool outputs) **halved cost** relative to the raw agent and matched or slightly beat LLM summarization on solve rate.
- With Qwen3-Coder 480B: raw agent 53.8%, masking 54.8%.
- A hybrid policy cut cost a further 7% vs masking and 11% vs summarization.
- There is initial evidence the results generalise to OpenHands.

**K. Epoch AI [V-secondary, search snippet of Epoch page]** — [Epoch AI, SWE-bench Verified](https://epoch.ai/benchmarks/swe-bench-verified)
- Epoch runs its own simple one-action-per-turn scaffold, upgraded "significantly" in Feb 2026, on 484 of 500 Verified samples.
- It also reports Claude Code and Codex scaffolds via Inspect-SWE.
- It explicitly treats scaffold as a reporting dimension.

**L. Unverified secondary claims, to be treated with caution**
- Claude Sonnet 4.5 is said to score 43.2% in SWE-agent v1 vs 59.8% in Cline on SWE-bench Verified. The primary source was not found. — [morphllm.com](https://www.morphllm.com/swe-benchmark) (search snippet)

### Inferences
- Across these sources, the realistic magnitude for a capstone to cite is:
  - **about 5–17 pp** from swapping mature off-the-shelf harnesses on a fixed model (Terminal-Bench 2.0, peer-reviewed, with CIs);
  - **about 10–15 pp** from deliberate harness engineering on one model (LangChain; Meta-Harness vs Terminus 2 baseline);
  - **2–8 pp** per individual ACI component (SWE-agent).
- Larger effects (tens of pp) appear when a harness component is the binding bottleneck for a weak model, as with edit format for Grok Code Fast 1.
- The strongest committee-proof evidence is the **Terminal-Bench 2.0 Table 2**: peer-reviewed (ICLR 2026), at least 5 runs per cell, 95% CIs, and many models crossed with many harnesses. It gives *both* sides: harness effects are real and often exceed CI width, but model effects are larger.
- Two consistent cautions:
  1. A vendor's own harness is not automatically optimal for its own model.
  2. Harness choice changes **cost** far more than accuracy: 10–100× token differences at similar accuracy.

  For a medical harness, cost and latency should therefore be co-primary outcomes.
- Many results above (LangChain, Meta-Harness, hashline) tune and test on the same benchmark. A capstone should use a held-out split to avoid the same critique.

### Gaps
- I found no peer-reviewed, factorial ablation that isolates each harness component's contribution across several models at 2025–2026 frontier level. The Terminal-Bench table swaps whole harnesses, and HAL-based analysis "cannot isolate individual scaffold components".
- METR: I did not retrieve a METR report quantifying scaffold effects this session. I am aware METR uses its own scaffolds (e.g., in time-horizon work), but I have no verified number.
- I did not verify current SWE-bench Verified leaderboard same-model deltas (e.g., mini-SWE-agent "bash-only" vs vendor scaffolds).
- I did not verify Anthropic's 2024 claim, from "Building effective agents" and its SWE-bench Verified post, that they spent more time optimising tools than prompts. It is plausible but not re-read this session.
- I did not read the HAL paper's scaffold tables directly (PDF not parsed).

---

## Q3. Which harness components matter most? (taxonomy plus evidence per component)

### Takeaway
The best-evidenced high-leverage components are:
1. **the tool/action interface**, especially file editing and viewing (SWE-agent −7.7 pp without the edit tool; hashline about +15 pp average);
2. **verification loops and guardrails** (SWE-agent linting −3 pp when removed; LangChain's forced pre-exit verification identified as the main fix);
3. **context management** (last-5-observations −3 pp vs full history; masking halves cost);
4. **environment and context bootstrapping, plus persistent state**, for long tasks.

Orchestration choices (multi-agent, planning) have less clean evidence. Adding tools or complexity can *hurt*.

### Cited Findings
- **Tool interface / ACI (observation formatting and action granularity).**
  - In SWE-agent, removing the edit command cost −7.7 pp. File-viewer window size is non-monotonic: 30 lines −3.7 pp, full file −5.3 pp. An iterative search tool scored −6.0 pp, worse than no search tool. [Pre-2025, V-primary] — [SWE-agent](https://arxiv.org/abs/2405.15793)
  - The hashline edit format averaged +15 pts over patch across 16 models. The author's thesis is that many failures come from the model's inability to *express* edits, not to understand the task. [V-primary] — [Stencil](https://stencil.so/blog/the-harness-problem)
- **Tool-set size and clarity.**
  - Anthropic: "Bloated tool sets with ambiguous choices are a common failure mode". Tools should be "self-contained, token-efficient", with minimal overlap. "If a human engineer can't definitively say which tool should be used… an AI agent can't be expected to do better." This is guidance, with no numbers given. [V-primary] — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  - LongFuncEval (IBM) reports a **7% to 85%** performance drop as the number of tools grows, plus drops from longer tool responses and conversations. [V-secondary, snippet] — [arXiv 2505.10570](https://arxiv.org/abs/2505.10570)
- **Verification / self-check loops and guardrails.**
  - SWE-agent's lint-gated edit (rejecting syntactically broken edits) is worth 3.0 pp. [Pre-2025, V-primary] — [SWE-agent](https://arxiv.org/abs/2405.15793)
  - LangChain's biggest failure class was premature success claims without testing. A pre-completion checklist middleware plus build-verify-fix prompting were core to the +13.7 pp. [V-primary] — [LangChain](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)
  - In Anthropic's long-running harness, agents "mark features complete without verifying them end-to-end". Adding browser-automation testing "dramatically improved" bug detection. This is qualitative, with no numbers. [V-primary] — [Anthropic long-running harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  - On HAL ScienceAgentBench, the Self-Debug scaffold "consistently makes models both more accurate and cheaper". [V-secondary] — [Just a Wrapper](https://www.lesswrong.com/posts/jXLi3dhSpSMd7B6z8/just-a-wrapper-how-much-do-scaffolds-matter-1)
- **Context / memory management (compaction, masking, notes, sub-agents).**
  - SWE-agent: last-5-observations vs full history is worth 3.0 pp. [Pre-2025] — [SWE-agent](https://arxiv.org/abs/2405.15793)
  - Observation masking halves cost at equal or better solve rate vs LLM summarization. [V-secondary] — [Complexity Trap](https://arxiv.org/abs/2508.21433)
  - Anthropic names compaction, tool-result clearing, structured note-taking (NOTES.md, to-do lists), sub-agents returning condensed summaries ("often 1,000–2,000 tokens" from "tens of thousands") and just-in-time retrieval. It grounds them in "context rot": recall falls as context grows, so context is a finite "attention budget". [V-primary] — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  - Meta-Harness found a harness beating a state-of-the-art context-management system by 7.7 pts with 4× fewer tokens. [V-secondary] — [Meta-Harness](https://arxiv.org/abs/2603.28052)
- **State / checkpointing / persistence.** Anthropic's components for multi-session work:
  - an initializer agent producing `init.sh`;
  - a progress file;
  - a JSON feature list. JSON was chosen because models are "less likely to overwrite it inappropriately than Markdown", and agents may only flip the `passes` field;
  - git commits as rollback points;
  - a fixed start-of-session routine.

  [V-primary, qualitative] — [Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **Environment/context bootstrapping.** LangChain's `LocalContextMiddleware` maps directories and finds tools up front, because agents wasted effort discovering their environment. [V-primary] — [LangChain](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)
- **Error recovery / loop detection.** LangChain saw "10+ small variations of the same broken approach" in traces. Its `LoopDetectionMiddleware` nudges the agent after N edits to one file, though the model may persist anyway. In Bölük's benchmark, Grok 4 Fast's output tokens fell 61% "because it stopped looping on retries" once the edit format changed. [V-primary] — [LangChain](https://langchain.com/blog/improving-deep-agents-with-harness-engineering); [Stencil](https://stencil.so/blog/the-harness-problem)
- **Reasoning-budget scheduling** (a harness-controlled inference parameter). Uniform xhigh scored 53.9%, uniform high 63.6%, and phase-scheduled 66.5%. [V-primary] — [LangChain](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)
- **Permission / approval gates and hooks (deterministic control).** Claude Code docs: hooks fire "without Claude deciding", and "If a rule must hold every time, make it a hook rather than a prompt instruction." This is a design principle, not a performance study. [V-primary] — [Claude Code docs](https://code.claude.com/docs/en/features-overview)
  - The SafeHarness paper (arXiv 2604.13630) argues that prior harness engineering focuses on performance and "largely overlook[s] security", and proposes lifecycle-integrated defenses. [V-secondary, title/snippet only] — [SafeHarness](https://arxiv.org/pdf/2604.13630)
- **Orchestration: pipeline vs agent loop.** Agentless's fixed pipeline beat contemporary open-source agents on SWE-bench Lite. [Pre-2025] — [Agentless](https://arxiv.org/abs/2407.01489)
- **Evaluation harness vs execution harness.**
  - Harbor (Terminal-Bench) and the HAL harness are evaluation infrastructure. HAL's harness "orchestrates parallel evaluations across hundreds of VMs, reducing evaluation time from weeks to hours". [V-secondary] — [HAL](https://arxiv.org/abs/2510.11977v1); [Terminal-Bench 2.0](https://arxiv.org/html/2601.11868v1)
  - Grading fixes in the evaluation harness changed CORE-Bench results: Opus 4.5 went from 77.8% to 95.5% with manual grading. Evaluation-harness validity is therefore a separate confound. [V-primary] — [HAL](https://hal.cs.princeton.edu/)

### Inferences
- A practical taxonomy for the capstone, with evidence strength:
  1. **Tool set and ACI** (action granularity, edit format, observation formatting and truncation). Strong evidence.
  2. **Context/memory policy** (masking, compaction, notes, retrieval). Moderate to strong; strongest on cost.
  3. **Verification and guardrails** (lint gates, test-before-exit, LLM/rule checkers, hooks). Moderate.
  4. **State/persistence and checkpointing.** Qualitative.
  5. **Orchestration and planning** (pipeline vs loop, subagents, reasoning schedule). Mixed.
  6. **Permissions and approval gates.** Safety-relevant; no performance data.
  7. **Instructions** (system prompt, skills, examples). SWE-agent "w/o demo" −1.7 pp.
  8. **Error recovery** (loop detection, retries). Anecdotal.

  The evaluation harness is a separate measurement layer.
- The recurring lesson ("more tools/more context is not better") supports an ablation-first design. Start from a minimal harness, the analogue of Terminus 2 or mini-SWE-agent, and add one component at a time.

### Gaps
- No source gives a ranked, cross-benchmark importance estimate per component for 2025–2026 frontier models. The ordering above is my synthesis.
- I found no quantitative evidence on permission/approval gates' effect on task success or on multi-agent vs single-agent with the model fixed. Anthropic's context-engineering post mentions a "substantial improvement" from multi-agent research systems but gives no figures there.

---

## Q4. Does the harness help small/local models more or less than frontier models? (harness × model interaction)

### Takeaway
The evidence points to a **strong interaction rather than a simple "small models benefit more" rule**.
- Weak or small models are **more fragile** to harness choice: large swings and large failures. Long tool schemas, many tools and unfamiliar tool names hurt them disproportionately, and tailoring the interface can recover large gains.
- Very weak models (GPT-OSS-20B, GPT-5-Nano) gain little from any harness: there is a floor effect.
- Frontier models show smaller, but still non-trivial, spreads.

### Cited Findings
- Terminal-Bench 2.0 same-model spreads. [V-primary] — [arXiv 2601.11868](https://arxiv.org/html/2601.11868v1)
  - Mid/small models often show the *largest* spreads: Claude Haiku 4.5 16.5 pp (OpenHands collapses to 13.3%), GPT-5-Mini 9.7 pp, Grok Code Fast 1 10.0 pp.
  - Some frontier models show small spreads: Claude Sonnet 4.5 2.7 pp, Opus 4.1 3.2 pp.
  - Floor effects: GPT-OSS-20B scored 3.1–3.4% and GPT-5-Nano 7.0–11.5% across all harnesses.
  - Exception: some frontier models still show large spreads (GPT-5 15.7 pp, Gemini 2.5 Pro 16.9 pp).
- Edit-interface study. [V-primary] — [Stencil](https://stencil.so/blog/the-harness-problem)
  - The largest hashline gains were for cheaper/weaker models: Grok Code Fast 1 from 6.7% to 68.3%; MiniMax M2.1 +41.7; Devstral Medium +40.5; GLM-4.5 Air +27.0.
  - Frontier coding models gained less: GPT-5.2 Codex +4.6; Claude Sonnet 4.5 +14.4.
  - DeepSeek V3.2 regressed (−5).
- Small models and tool schemas: "Don't Adapt Small Language Models for Tools; Adapt Tool Schemas to the Models" (Lee et al., ACL 2026 Main, arXiv 2510.07248). [V-primary, abstract] — [arXiv 2510.07248](https://arxiv.org/abs/2510.07248)
  - Small LMs struggle with tool selection and parameters because of **schema misalignment**: they hallucinate plausible tool names from pretraining conventions.
  - A training-free renaming of tool components (PA-Tool) gives "up to 17%" improvement on MetaTool and RoTBench. It is unclear whether this is pp or relative. Schema-misalignment errors fell 80%.
  - A snippet says models below about 10B parameters show "severe performance degradation" on tool selection [V-secondary].
- Long tool catalogs: LongFuncEval reports a 7–85% drop as tool count grows (across long-context models generally, not only small ones). [V-secondary] — [arXiv 2505.10570](https://arxiv.org/abs/2505.10570)
- Context budget for local models: a 2026 single-author preprint tested 14 models (1.5B–32B) with 28 tool definitions. At an 8K budget, JSON-schema definitions overflow context (exact match 2.6% average). Compressing schemas by 44–50% restored performance. Weak source: independent and not peer reviewed. [V-secondary] — reported in search results for [ToolMATH / related](https://arxiv.org/pdf/2602.21265) (exact URL of the Sakizli preprint not retrieved)
- HAL-based analysis does **not** establish whether scaffolds help weaker or stronger models more. It only shows heterogeneous effects and ranking reversals. [V-secondary] — [Just a Wrapper](https://www.lesswrong.com/posts/jXLi3dhSpSMd7B6z8/just-a-wrapper-how-much-do-scaffolds-matter-1)
- Meta-Harness evaluated both Claude Opus 4.6 and Claude Haiku 4.5 on Terminal-Bench 2.0. Haiku numbers were not retrieved. Its retrieval harness for math transferred to five held-out models (+4.7 pts average). [V-secondary] — [Meta-Harness](https://arxiv.org/abs/2603.28052)

### Inferences
- For a medical harness likely to run on smaller or local (possibly Thai-capable open-weight) models, the evidence suggests:
  - keep tool catalogs small and schemas short;
  - name tools in conventional, pretraining-familiar ways;
  - prefer structured, forgiving action formats;
  - budget context for tool definitions explicitly.
- Expect a bigger *variance* from harness choices with small models. That argues for testing at least two model tiers to estimate the harness × model interaction.
- Floor effects mean a harness cannot rescue a model lacking the base capability. This sets a lower bound on model choice.

### Gaps
- I found no controlled 2025–2026 study that varies model *size within one family* across *the same set of harness components* to directly test "harness helps small models more".
- Constrained decoding / structured outputs as a harness component: I did not retrieve a quantitative study this session. Known prior work (e.g., grammar-constrained decoding for function calling) was not verified.
- The RAG-MCP tool-retrieval paper and the "Less is More" edge function-calling paper were not found in searches. Their numbers are unverified and omitted.

---

## Q5. Is "harness engineering" a named field/term in 2025–2026? Who uses it?

### Takeaway
Yes. "Harness engineering" emerged as a named practice in **early 2026**: OpenAI, Mitchell Hashimoto and LangChain in February; Martin Fowler/Thoughtworks in April; O'Reilly in May. Anthropic used "agent harness" from late 2025. It rapidly became an **academic research object**, with at least eight 2026 arXiv papers carrying "harness" in the title, including automated harness search and harness-as-specification work. Attribution of the phrase is contested.

### Cited Findings
- **Timeline per Wikipedia** [V-primary, tertiary source] — [Wikipedia: Agent harness](https://en.wikipedia.org/wiki/Agent_harness)
  - Pre-term foundations: ReAct (2023) and Toolformer (2023).
  - Oct 2023: the UK AI Security Institute (then the AI Safety Institute) described an agent as model plus scaffold.
  - Feb 2026: Mitchell Hashimoto blogged about engineering permanent fixes into the agent's environment after each mistake. "Several accounts credit him with the phrase."
  - Early 2026: Vivek Trivedy (LangChain), "Anatomy of an Agent Harness".
  - Undated: an OpenAI engineering report "helped spread the term".
  - 2 Apr 2026: Böckeler, "Harness engineering for coding agent users", on martinfowler.com.
  - 15 May 2026: Addy Osmani, "Agent Harness Engineering", on O'Reilly Radar.
  - June 2026: Self-Harness and Harness-1 reported by VentureBeat.
- LangChain, "Improving Deep Agents with harness engineering", 17 Feb 2026. [V-primary] — [LangChain](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)
- Anthropic uses "agent harness" (Nov 2025) for the Claude Agent SDK. [V-primary] — [Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Can Bölük, "…Only the harness changed" ("The harness problem"), 12 Feb 2026. [V-primary] — [Stencil](https://stencil.so/blog/the-harness-problem)
- Academic papers using "harness" as a research object. Titles were seen in search results [V-secondary unless noted]:
  - "Natural-Language Agent Harnesses" (arXiv 2603.25723, Mar 2026). [V-primary abstract] — [arXiv](https://arxiv.org/abs/2603.25723)
  - "Meta-Harness: End-to-End Optimization of Model Harnesses" (Lee et al., Stanford IRIS, arXiv 2603.28052, Mar 2026). — [arXiv](https://arxiv.org/abs/2603.28052)
  - "SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment" (arXiv 2604.13630). — [arXiv](https://arxiv.org/pdf/2604.13630)
  - "Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF)" (arXiv 2604.17025). — [arXiv](https://arxiv.org/pdf/2604.17025)
  - "Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents" (arXiv 2605.30621). — [arXiv](https://arxiv.org/pdf/2605.30621)
  - "Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents" (arXiv 2606.20631). — [arXiv](https://arxiv.org/pdf/2606.20631)
  - "From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents" (arXiv 2607.08028). — [arXiv](https://arxiv.org/pdf/2607.08028)
  - "Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories" (arXiv 2608.02276). — [arXiv](https://arxiv.org/pdf/2608.02276)
  - "Harness Engineering for Predictable Agentic Systems: An Empirical Study of Deterministic Execution Constraints" (arXiv 2608.26197). — [arXiv](https://arxiv.org/pdf/2608.26197)
  - "Harness-Zero: Harness Distillation via Agent-as-Harness" (arXiv 2609.24974). — [arXiv](https://arxiv.org/pdf/2609.24974)
- The search-engine summary also referenced "AutoHarness" (automatic synthesis of code harnesses) and "Agentic Harness Engineering" (evolving harnesses from observability data). I did not confirm these. [V-secondary, unconfirmed]
- Peer-reviewed venues treat scaffold as an explicit evaluation axis: HAL (ICLR 2026: models × scaffolds × benchmarks) and Terminal-Bench 2.0 (ICLR 2026: 6 agents × 16 models). [V-primary/secondary] — [HAL](https://iclr.cc/virtual/2026/poster/10006806); [Terminal-Bench 2.0](https://arxiv.org/html/2601.11868v1)

### Inferences
- A committee-defensible framing:
  - **"Scaffold"** is the older academic term, used by AI Security Institute (2023), SWE-agent and HAL.
  - **"Agent harness"** is the 2025–2026 industry term, used by Anthropic and LangChain.
  - **"Harness engineering"** is the 2026 name for the practice.
  - Since March 2026, academic work has treated harnesses as optimisable, ablatable, transferable artefacts (NLAH, Meta-Harness, Harness-R1, "Harness Updating Is Not Harness Benefit").
- Together with peer-reviewed same-model deltas (Terminal-Bench 2.0, SWE-agent), this supports "a harness is a distinct, measurable research variable". The student should also concede the published counterpoint that model choice usually matters more.

### Gaps
- I did not read the full text of most 2026 "harness" arXiv papers. Only titles were seen (except NLAH's abstract and Meta-Harness snippets), so their findings are not summarised here and their content should be verified before citing.
- I could not verify the OpenAI post (HTTP 403), the Hashimoto post or the Osmani O'Reilly article directly. Exact dates and wording come from Wikipedia.
- I found no evidence that a formal academic venue or workshop is named "harness engineering". It appears as a practice term and in paper titles, not as an established subfield with its own venue.
