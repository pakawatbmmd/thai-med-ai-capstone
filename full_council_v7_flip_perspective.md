# Capstone Council v7: Flip the perspective on decision models (Claude × Codex × Gemini, philosopher-council, 2026-10-22)

**Brief:** `council_v7_flip_perspective/brief.md`. How to use a decision model (clinical *or* health-economic) in the Thai health system with a "flip the perspective" frame, rather than a plain screening or triage system.

**Models:**
- Claude, in the cloud session.
- Codex: `gpt-6.1-sol`, high reasoning effort, via the OpenAI Responses API.
- Gemini: `gemini-4-argon` via the Gemini API.

Codex and Gemini ran through `tools/run_council.py` with every allowed file inlined. Each Round 1 was written without seeing the others; each Round 2 saw all three Round 1s but no Round 2.

## Synthesis (Claude, after all six files)

**Agreement across all three Round 2 top-3 lists**

| Project | Claude R2 | Codex R2 | Gemini R2 | Verdict |
|---|---|---|---|---|
| **Evidence Before Algorithms**: an HTA decision model that chooses *which evidence Thailand should buy before funding an AI*, ideally with access-aware district thresholds | #1 (system half) + moonshot | #1 + moonshot | #3 + moonshot | **Unanimous moonshot.** All three made it the moonshot. |
| **Revocable AI Leases**: learned competence gate + randomised logged audits + promotion/revocation (+ human-backstop probes) | #2 | #2 | #1 (safe ambitious) | **Unanimous finalist.** Highest finish confidence (70 / 80 / 88%). |
| Third slot | Benefit-based outreach for อสม. | Access-aware policy frontier (Claude #4) | Decision-regret ask-or-act navigator (Codex #2 + Gemini #1) | **No consensus.** |

**Cross-critique**
- **Most over-rated:** Gemini's UC-QuotaRouter (Claude and Codex). Both say it is the plain triage chatbot with a cost term, and its result would mostly reflect the simulator. Gemini instead named Claude #3 (care-seeking vignettes and LLM personas), because stated preferences don't match real emergency behaviour.
- **Most under-rated:** both Codex and Gemini independently picked **Claude #4, access-adjusted thresholds** ("same risk, different decision"). Both proposed merging it into the HTA value-of-information engine. Claude picked Codex #2 (ask only what could change management).
- **Shared warning (Codex, Gemini, Claude):** a learned or neural policy is justified only where classical EVSI/GP methods are too slow or the design space is large. Gemini argues that allocating thresholds and pilots across 77 provinces creates that scale. Codex wants classical baselines first.
- **Retracted or narrowed:**
  - Reverse triage: Claude withdrew it as lead, and Codex showed that conformal bounds on historical data are not a counterfactual safety guarantee.
  - Outreach uplift: all three agree it dies without randomised or known-propensity outreach data.

**The emerging thesis.** One decision-theoretic idea at two scales. *Value of information measured against the decision (regret), not against accuracy*, applied to:
- the **system** decision (which AI to fund, at which operating point per district, after which pilot); and
- optionally the **bedside** decision (which question could change management).

**Revocable AI Leases** is the safe-ambitious alternative with no data-access gate.

**Open gates before choosing**
1. Will the Engineering advisor accept decision-analytic modelling plus amortised experimental design as the ML core? All three advisors flag this.
2. Can one published Thai screening model (DR or chest X-ray AI) be re-implemented from the paper? (Gemini: check whether HITAP publishes model files.)
3. An HTA collaborator, and one clinician pathway owner.

---

# ROUND 1

## CLAUDE: Round 1

**Brief:** `council_v7_flip_perspective/brief.md`. Descartes proposes, Hume audits, Socrates stress-tests. No new deep research was done for this round; claims marked [UNVERIFIED] need checking before a proposal.

**Opening position (Descartes).** A plain triage model answers one question at one moment: *given this patient who showed up, what label or route?* That bakes in four hidden assumptions:
- the patient initiates;
- the model judges the patient, not the system;
- one threshold fits everyone;
- the output is a verdict.

Every assumption can be flipped, and each flip gives a different research object. The strongest flips do two things: they change *who benefits* (capacity, the patient's agency, the payer's purchasing), and they make a quantity measurable that nobody measures today.

### 1. Network-scale reverse triage: "who can safely leave?" (flip: direction)
- **Pitch:** Don't decide who gets into the tertiary hospital. Decide who can safely *step down* today: from ward to home, from tertiary OPD follow-up to รพ.สต. telemedicine, from specialist to pharmacy refill. It comes with a statistical guarantee on missed deterioration and respects the receiving unit's capacity.
- **Paradigm & research question:** Selective prediction with conformal / risk-controlling guarantees, plus capacity-constrained assignment. *For a fixed guaranteed rate of 30-day bounce-back or deterioration (e.g., ≤2%), how much tertiary capacity can a step-down policy free? Does a network-aware policy, which knows each receiving unit's capability, free more than a patient-only risk score at the same guarantee?*
- **Thai testbed:** Thai tertiary OPDs are congested and many stable NCD patients are followed up at tertiary level [UNVERIFIED share]. Telemedicine exists at all 10,910 รพ.สต. and the 30-baht-anywhere network can receive them. "Reverse triage" is an established disaster-medicine idea (Kelen et al., Lancet 2006 [UNVERIFIED citation]); the flip is doing it *continuously, at network scale, with a guarantee*.
- **POC:**
  - **Data and models:** a step-down model on a retrospective KCMH or 43-file-shaped extract (or MIMIC-IV ED/hospital data as a public stand-in), using gradient boosting or a small sequence model on the laptop.
  - **Guarantee:** conformal risk control.
  - **Assignment:** a capacity-aware solver.
  - **Output:** a Pareto curve of capacity freed against guaranteed risk.
- **Prior art to beat:** discharge-readiness and readmission models; reverse triage (Kelen); conformal risk control; capacity-aware referral optimisation. The novelty is guarantee + network + step-down direction together [negative search pending].
- **Socratic test:** *Enough stable, low-risk patients exist at tertiary level for step-down to matter.* Month 1: on any accessible cohort, estimate the share of follow-up visits with a predicted 30-day deterioration below 2%. **Kill** if it is below 10% of visits (too little capacity to free).

### 2. Outreach allocation for อสม.: "whom should the system go to first?" (flip: initiative)
- **Pitch:** Instead of triaging whoever arrives, decide each week which households ~1.07M village health volunteers should visit, and with which intervention, to prevent the most avoidable admissions.
- **Paradigm & research question:** Restless multi-armed bandits / budgeted sequential allocation under uncertainty. *Does a household-level, multi-condition allocation policy prevent more avoidable hospitalisations per visit than (a) current routine schedules and (b) single-condition risk ranking?*
- **Thai testbed:** อสม. are paid, organised, and already use the Smart อสม. app, with no AI found. Outcomes could later come from Health Link and claims.
- **POC:** A simulator calibrated to public Thai NCD prevalence and admission rates; a bandit policy; comparison against the baselines; optionally a small retrospective test if a district shares visit logs.
- **Prior art to beat:** **ARMMAN / Google's restless bandits for maternal-health call scheduling in India**, which was deployed and studied (Mate et al. and follow-ups [UNVERIFIED details]). This is strong prior art, so the novelty must be *household-level, multi-condition, in-person visits with Thai outcome linkage*.
- **Socratic test:** *Visits change outcomes enough to be worth allocating.* Month 1: find any Thai evidence that อสม. home visits reduce admissions or improve control. **Pivot to a pure simulation-methods contribution** if none exists.

### 3. Modelling the patient's decision: "what will make them come?" (flip: subject)
- **Pitch:** For time-critical conditions (stroke, STEMI, sepsis, obstetric haemorrhage), the killer in rural Thailand is often *delay in deciding to seek care* [UNVERIFIED for Thailand], not misdiagnosis. Model the patient's and family's *decision*: costs, distance, beliefs, who decides in the household. Find the message or action that shortens the delay.
- **Paradigm & research question:** A discrete-choice model of care-seeking, fused with LLM persona simulation, then counterfactual messaging. *Can a hybrid model fitted to Thai survey or vignette responses predict delay better than a demographic baseline? Does it identify messages that shift stated choices in a randomised vignette experiment?*
- **Thai testbed:** 1669 coverage gaps; stroke fast-track networks; family decision-making in rural households.
- **POC:** A vignette survey (n≈300–500, online or with อสม.) with randomised messages; a choice model plus LLM-persona comparison (do LLM personas reproduce real Thai choices?); a recommended message per segment.
- **Prior art to beat:** Care-seeking delay literature; health-belief models; LLM "silicon samples" in social science (persona fidelity is contested).
- **Socratic test:** *Stated choices in vignettes are informative about real delay.* Month 1: pilot 60 respondents. **Kill the LLM-persona half** if persona choices correlate with real respondents at r < 0.3.

### 4. Access-adjusted thresholds: "same risk, different decision" (flip: threshold)
- **Pitch:** Show that one national threshold for referral or screening (e.g., a CVD risk cut-off, a diabetic retinopathy referral grade, a chest X-ray abnormality score) is the wrong *decision* when the cost of acting differs tenfold between districts. Derive decision-theoretic **threshold maps** that equalise net benefit, not risk.
- **Paradigm & research question:** Decision-curve analysis and expected-utility thresholds with context-dependent costs (travel time, lost wages, capacity), and fairness under a single payer. *How much net benefit, in QALYs or avoided late presentations per 100k people, does an access-adjusted threshold policy gain over a uniform threshold, and who gains?*
- **Thai testbed:** Doctor density ranges from ~1:462 (Bangkok) to ~1:5,000 (Bueng Kan). NHSO funds Perceptra chest X-ray AI in 445+ hospitals with, presumably, one operating point [UNVERIFIED].
- **POC:** Public risk model + published diagnostic accuracy + Thai geography (travel-time rasters, facility locations) → district threshold maps + an equity analysis. Fully laptop-feasible.
- **Prior art to beat:** Decision-curve analysis (Vickers); context-specific thresholds in global-health screening; spatial accessibility models. The novelty is *operating-point policy for a national AI rollout*.
- **Socratic test:** *Access costs are large enough to move the optimal threshold.* Month 1: compute the threshold shift for one use case. **Kill** if the optimal threshold moves by less than the model's calibration error across districts.

### 5. Living HTA: AI agents that build and update the system's decision models (flip: decider) — moonshot
- **Pitch:** Turn the decision model on the *system itself*. Agents build HITAP-style decision-analytic models (decision trees, Markov, microsimulation) from evidence plus Thai costs and claims, then re-run them as new data arrives. The first use case is deciding *which AI products NHSO should buy*, since its innovation budget is growing from THB 2.9B toward 10B.
- **Paradigm & research question:** Agentic scientific modelling with verification. *Can an agent reproduce published HITAP or Thai cost-effectiveness models within ±10% of reported ICERs, given only the paper's inputs? Can it flag which inputs drive the decision?*
- **Thai testbed:** HITAP is a world reference for HTA in LMICs [check current status]. NHSO is buying AI per hospital without, as far as we found, an AI-specific HTA method.
- **POC:** A replication benchmark of 10–20 published Thai CEA models; agent-built models in Python (e.g., a Markov cohort); a verification harness (unit tests on transition matrices, half-cycle correction); an ICER error distribution; one prospective model of an AI product (e.g., chest X-ray AI expansion from 445 to 887 hospitals).
- **Prior art to beat:** Recent work using GPT-4-class models to replicate or automate health-economic models and network meta-analyses (e.g., Reason et al. 2024 [UNVERIFIED]); HTA automation pilots at NICE and others [UNVERIFIED].
- **Socratic test:** *Published Thai models report enough detail to be replicated.* Month 1: attempt by hand to replicate 3 HITAP models. **Kill** if fewer than 2 are replicable from the published paper (the benchmark has no ground truth).

---

**If I were the student, I'd pick #1, network-scale reverse triage.** It is the cleanest flip: the model *gives capacity back* instead of rationing access. It has a hard, measurable output (capacity freed at a guaranteed risk), and it can borrow the conformal-guarantee machinery from the AI Residency idea. **#4 is the safest high-quality paper.** **#5 is the moonshot**, and the strongest fit if "decision model" means health-economic models.

**The question I'd put to the student before Round 2:** did "decision model" mean a model that makes clinical decisions, or the decision-analytic models HTA uses? Ideas #1–#4 assume the first; #5 assumes the second.

## CODEX (gpt-6.1-sol): Round 1

## Part A — What should “flipping” mean? *(126 words)*

A genuine flip changes **whose decision is optimized, which actions are available, or what counts as success**. Start with the decision, consequences, constraints and uncertainty; only then ask whether prediction is needed.

Plain screening hides assumptions worth reversing: higher risk means greater benefit from intervention; more information is always useful; accurate recommendations are actionable; capacity is unlimited; patient preferences equal population-average utilities; and an AI either deserves trust everywhere or nowhere.

Better questions include: **Which evidence should Thailand buy before buying AI? Which question could change management? Where does intervention change outcomes? When should AI lose permission to act?**

Gimmicks include renaming low-risk classification “reverse triage,” adding agents to an unchanged classifier, or attaching invented monetary weights to accuracy. A flip matters only when it changes an action and has a measurable consequence.

## Part B — Five ranked ideas

**Evidence discipline.** These are research proposals, not established effects. Numeric improvement targets and budgets below are proposed preregistration targets, not factual claims. GPU-hour allocations are planning budgets, not measured throughput. API spending is optional, capped, and restricted to synthetic material. No proposal assumes access to NHSO or Health Link. Current access arrangements, procurement rules and potential Thai partnerships are **[UNVERIFIED]**.

The earlier report’s deployment counts and broad novelty claims need independent checking; none is essential to the ranking below.

---

## #1 — Evidence Before Algorithms: an HTA agent that decides what Thailand should learn next

### 1. Name, flip and pitch

**Normal:** “Is this screening AI cost-effective?”  
**Flipped:** “Which uncertainty should we resolve before deciding whether—and how—to fund it?”

Build a decision model that chooses between **adoption, rejection and a targeted evidence-generating pilot**. Its output is a study recommendation and a conditional funding decision, not another screening score.

### 2. Paradigm and falsifiable research question

**Paradigm:** health-economic decision analysis plus amortized Bayesian experimental design.

Use diabetic-retinopathy screening as one bounded example. Compare:

- existing screening;
- AI-assisted screening;
- AI plus referral-completion support.

Explicitly model the pathway from invitation through image acquisition, referral, treatment and visual outcomes. Diagnostic performance is an input, not the endpoint.

Let net monetary benefit be:

\[
NMB(a,\theta)=\lambda QALYs(a,\theta)-Cost(a,\theta)
\]

Treat willingness to pay, capacity and uptake as scenario variables—not invented official Thai constants.

**RQ:** Across held-out simulated local contexts, can a learned sequential study-selection policy reduce expected net opportunity loss by **at least 25%**, at the same evidence budget, versus conventional EVSI-based greedy selection and a Gaussian-process surrogate?

Evaluate against high-precision reference calculations, including Monte Carlo uncertainty. Test amortization honestly: distinguish upfront training cost from cost per subsequent decision.

### 3. Thai testbed and impact

A plausible testbed is one Thai diabetic-eye-screening pathway, with an ophthalmology partner and an HTA collaborator. Local collaboration and parameter availability are **[UNVERIFIED]**.

A human-centred evaluation of a diabetic-retinopathy deep-learning system deployed in Thai clinics already demonstrates why workflow—not just classifier performance—belongs in the model: [Beede et al., CHI 2020](https://doi.org/10.1145/3313831.3376718).

**Beneficiaries:** patients facing incomplete pathways and decision-makers choosing between software and implementation support.

**Measures:** decision regret, expected net benefit of sampling after study costs, budget impact, referral completion assumptions and distribution of benefits across access groups. These are **modelled consequences**, not demonstrated patient benefits.

HITAP is a potential methodological collaborator; its current involvement or authority in this particular procurement decision must not be assumed: [HITAP](https://www.hitap.net/en/).

### 4. Nine-month POC/MVP

- **Data:** published pathway and economic inputs; a small partner-reviewed local parameter table; explicit wide priors where Thai evidence is absent. Every parameter receives a provenance and transferability label.
- **Model:** an executable decision tree plus Markov model; a small belief-state Transformer choosing among candidate studies. Studies might estimate imageability, referral completion or local resource use.
- **Compute:** CPU probabilistic sensitivity analysis; **60 GPU-hours** allocated to the learned policy. No foundation-model pretraining.
- **API:** **US$0 required**; optional **≤US$30** for synthetic document-format testing. An LLM must not invent probabilities, utilities or costs.
- **Proof:** whether decision-focused experimental design improves study allocation *inside an audited simulator*. It does not establish that a Thai payer should adopt the technology.

The neural method must beat strong classical methods. A neural wrapper around an easy economic model is not a contribution.

### 5. Prior art to beat

- Conventional value-of-information methods and practical implementations: [SAVI](https://savi.shef.ac.uk/SAVI/).
- Amortized sequential experimental design: [Foster et al., *Deep Adaptive Design*, ICML 2021](https://proceedings.mlr.press/v139/foster21a.html).
- Transparent economic reporting: [CHEERS 2022](https://www.bmj.com/content/376/bmj-2021-067975).

**Novelty to establish:** decision-regret-aware study selection under uncertain pathway completion and capacity—not “the first AI that does HTA.”

### 6. Socratic stress-test

**Decisive assumption:** uncertainty that a feasible local study can resolve actually changes the adoption decision.

**Month-1 test:** build the conventional model first and run 1,000 probabilistic simulations in each of 20 plausible local contexts. Calculate a partial-EVPI ceiling for locally learnable parameters.

**Kill or pivot** if that ceiling is below the cheapest feasible pilot’s cost in **at least 18/20 contexts**. If information cannot be worth its price even under perfect learning, do not build an agent to acquire it.

---

## #2 — Ask Only What Could Change Care: decision-sensitive information acquisition

### 1. Name, flip and pitch

**Normal:** “Which question makes the diagnosis more certain?”  
**Flipped:** “Which question, record field or test could change the best action?”

An agent should stop collecting information when further certainty would not change management. Conversely, it should ask a seemingly minor question when that answer could reverse the decision.

### 2. Paradigm and falsifiable research question

**Paradigm:** risk-sensitive POMDP with decision-focused representation learning.

Choose one clinician-approved outpatient pathway—for example, adult lower urinary symptoms. The action set could include empirical treatment, obtaining a culture before selecting treatment, or withholding treatment pending clinical review. Local clinical policy must define the permitted actions.

**RQ:** Can a learned acquisition policy use **at least 20% fewer information acquisitions** than a fixed checklist and an entropy-reduction policy, while satisfying the same **2% unsafe-action cap in the simulator**?

Define “unsafe” prospectively with clinicians. Report the complete safety–burden frontier rather than hiding trade-offs inside one weighted score.

A separate clinician-authored test evaluates transfer. It does **not** certify a 2% real-world harm rate.

### 3. Thai testbed and impact

A KCMH outpatient or clinical-pharmacy partner could define the pathway and locally appropriate treatment constraints; availability is **[UNVERIFIED]**.

**Beneficiaries:** patients answering repeated questions or undergoing unnecessary tests, and clinicians managing incomplete histories.

**Measures:** number and burden of acquisitions, management agreement with an adjudicated reference, unsafe omissions and performance on Thai paraphrases.

[NICE NG109](https://www.nice.org.uk/guidance/ng109) provides an external clinical reference, **not** a substitute for Thai antimicrobial guidance or a local antibiogram.

### 4. Nine-month POC/MVP

- **Data:** approximately 300 clinician-authored case families, including counterfactual variants in which one answer changes management; additional synthetic cases generated from an explicit clinical state model.
- **Model:** a compact belief-state acquisition policy; optionally a 1.5–4B language model for Thai question realization. Keep clinical state, acquisition choices and wording separate.
- **Compute:** **80 GPU-hours**; quantized inference and, if justified, QLoRA rather than full fine-tuning. QLoRA is an established memory-efficient approach: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314).
- **API:** **US$0 required**; optional **≤US$50** for synthetic paraphrases.
- **Proof:** whether the policy learns *decision-relevant* information acquisition and generalizes beyond its simulator. No live treatment recommendations.

Hold out entire case families and authors. Randomly splitting paraphrases would overstate generalization.

### 5. Prior art to beat

- Dynamic feature acquisition: [EDDI, arXiv:1809.11142](https://arxiv.org/abs/1809.11142).
- Cost-aware sequential diagnosis: [Microsoft’s sequential-diagnosis work](https://www.microsoft.com/en-us/research/publication/sequential-diagnosis-with-language-models/). Treat its reported performance as a comparator claim, not independently established superiority.
- Essential non-neural baseline: a clinician-designed checklist with early stopping.

The proposed distinction is **management regret rather than diagnostic entropy**.

### 6. Socratic stress-test

**Decisive assumption:** selective information acquisition has meaningful headroom over a short fixed checklist.

**Month-1 test:** clinicians adjudicate 100 diverse cases using complete information, then evaluate the best fixed three-question checklist.

**Kill or pivot** if those three questions reproduce **at least 95%** of full-information management decisions without additional unsafe decisions. In that setting, a learned agent is unnecessary complexity.

---

## #3 — Revocable AI Leases: model the permission to act, not just the action

### 1. Name, flip and pitch

**Normal:** “Does this AI pass a validation benchmark?”  
**Flipped:** “For which cases may it act today, how much auditing does it need, and what evidence revokes that permission?”

The model’s decision is **allocation of autonomy and human review**. The underlying classifier is replaceable.

### 2. Paradigm and falsifiable research question

**Paradigm:** learned selective prediction plus sequential statistical monitoring and adaptive audit allocation.

Use a narrow task such as releasing an apparently non-referable retinal result. Learn a competence gate, but grant automation only where an independent audit supports the prespecified risk condition.

**RQ:** At a **1% upper-bound target for referable disease among automatically released negative cases**, can the learned protocol reduce human review by **at least 20%** relative to a static confidence threshold and fixed audit schedule?

Report missed referable disease separately, so a favourable denominator cannot hide failures. Under injected shifts, measure demotion delay empirically.

Any statistical guarantee must state its assumptions. It cannot guarantee future safety under arbitrary distribution shift.

### 3. Thai testbed and impact

Potential eventual users are a Thai screening programme, hospital governance committee or purchaser. Access to Thai images and adjudicated outcomes is **[UNVERIFIED]**.

The POC can begin with [EyePACS competition data](https://www.kaggle.com/competitions/diabetic-retinopathy-detection/data) and [IDRiD](https://doi.org/10.3390/data3030025), subject to their access and licensing conditions.

**Measures:** automated coverage at a stated risk bound, reviews required, audit burden, subgroup coverage and delay after deteriorating performance.

Foreign datasets cannot establish a Thai autonomy credential, and retrospective labels measure task errors—not the full incidence of clinical harm.

### 4. Nine-month POC/MVP

- **Data:** patient-separated development, calibration and evaluation partitions; external-dataset testing; synthetic changes in prevalence, image quality and error rates.
- **Model:** one frozen image encoder/classifier, a small learned competence gate and an executable audit/promotion/revocation engine.
- **Compute:** **50 GPU-hours**; cache image embeddings rather than repeatedly train a large vision model.
- **API:** **US$0**.
- **Proof:** whether adaptive permission allocation improves the review–risk trade-off under declared conditions.

Random audit probabilities must be logged and bounded away from zero. Do not treat selectively reviewed cases as an unbiased sample. Do not claim that hierarchical pooling creates evidence for an unobserved subgroup.

### 5. Prior art to beat

- [SelectiveNet, arXiv:1901.09192](https://arxiv.org/abs/1901.09192).
- Learning to defer to experts: [Mozannar and Sontag, arXiv:2006.01862](https://arxiv.org/abs/2006.01862).
- Time-uniform statistical inference: [Howard et al., arXiv:1810.08240](https://arxiv.org/abs/1810.08240).

The contribution must be the **joint learned gate and auditable, revocable permission policy**, not another uncertainty score.

### 6. Socratic stress-test

**Decisive assumption:** useful automation remains after demanding evidence strong enough to support the risk target.

**Month-1 test:** freeze an existing classifier, construct the gate on development data, and evaluate it on up to 3,000 separately labelled cases.

**Kill or pivot** if no permissible gate releases **at least 20%** of cases while meeting the prespecified one-sided risk bound, with appropriate allowance for selection and multiple strata.

For scale: zero errors in approximately 300 independent observations only supports an approximately 1% fixed-time upper bound; sequential monitoring and multiple strata require additional care. Evidence requirements cannot be wished away by ML.

---

## #4 — Reach the Changeable, Not Merely the High-Risk: benefit-based outreach

### 1. Name, flip and pitch

**Normal:** “Which patients are most likely to miss care or deteriorate?”  
**Flipped:** “For whom would one available outreach intervention actually change the outcome?”

Allocate scarce calls, home visits or transport support by estimated **incremental benefit**, subject to explicit clinical-priority and equity constraints—not simply predicted risk.

### 2. Paradigm and falsifiable research question

**Paradigm:** causal policy learning with constrained allocation.

Bound the first task to one intervention, such as invitations for overdue diabetes follow-up. Distinguish:

- baseline probability of attendance;
- effect of receiving outreach;
- longer-term clinical benefit, which the POC does not automatically identify.

**RQ:** At **100 outreach offers per week**, does a cross-fitted, doubly robust allocation policy produce **at least 10 additional verified follow-up completions per 100 offers** versus risk-ranked outreach, with a lower 95% confidence bound above zero?

Compare against random allocation and a causal-forest policy. Prespecify minimum allocation to clinically urgent groups; responsiveness must not become an excuse to abandon harder-to-reach patients.

### 3. Thai testbed and impact

A primary-care diabetes service with previously randomized outreach—or a genuinely randomized allocation mechanism—is the preferred testbed. Such a dataset or partner is **[UNVERIFIED]**.

**Beneficiaries:** patients whose missed care is preventable and staff with limited outreach capacity.

**Measures:** incremental completed follow-ups, cost per additional completion, allocation by access group and overlap diagnostics.

Attendance is the initial endpoint. It is not proof of improved glycaemic control, avoided complications or QALYs.

### 4. Nine-month POC/MVP

- **Data:** target at least 2,000 eligible episodes with covariates, known outreach-assignment probabilities and verified outcomes. More observations may be needed; this is an access gate, not a power guarantee.
- **Model:** small longitudinal state-space encoder plus an orthogonal policy-learning objective; compare with simple tabular methods.
- **Compute:** **40 GPU-hours**; nuisance estimation and cross-fitting mostly on CPU.
- **API:** **US$0**.
- **Proof:** retrospective policy value under identifiable assumptions, with uncertainty and sensitivity analysis.

If randomized data are unavailable, an explicit causal simulator can test algorithms—but cannot demonstrate Thai outreach effectiveness. Routine EHR trajectories alone do not identify the effect of making a call.

### 5. Prior art to beat

- Heterogeneous treatment-effect estimation: [Künzel et al., arXiv:1706.03461](https://arxiv.org/abs/1706.03461).
- Decision-focused causal allocation: [Athey and Wager, *Efficient Policy Learning*, arXiv:1702.02896](https://arxiv.org/abs/1702.02896).

A neural encoder is justified only if it improves **policy value**, not merely outcome prediction.

### 6. Socratic stress-test

**Decisive assumption:** intervention effects are identifiable from data obtainable within the capstone.

**Month-1 test:** obtain a data-owner-reviewed inventory and inspect an approved extract or aggregate feasibility table.

**Kill the clinical-effectiveness version** unless a partner can commit to data containing **at least 2,000 eligible episodes, known nonzero assignment probabilities, and at least 200 completed-follow-up events in each assignment arm**. Do not quietly replace missing causal evidence with LLM-generated patients.

---

## #5 — The Patient’s Trade-off Model: learn what makes a treatment acceptable

### 1. Name, flip and pitch

**Normal:** “Which treatment maximizes the model’s average utility?”  
**Flipped:** “Which trade-offs does this patient accept, and what must we ask before comparing treatments?”

Build a Thai shared-decision tool that elicits values rather than inferring them from demographics or presenting an authoritative recommendation.

### 2. Paradigm and falsifiable research question

**Paradigm:** Bayesian active preference elicitation with a learned latent utility model.

Choose one preference-sensitive decision, such as elective knee replacement versus continued non-operative management. Clinicians supply the admissible options and evidence; the model learns trade-offs among pain, function, recovery burden and uncertainty.

**RQ:** Can adaptive elicitation achieve **at least 85% agreement with held-out choices using 30% fewer questions** than a fixed 12-question instrument, while outperforming a Gaussian-process preference model?

Also measure test–retest agreement and sensitivity to wording. Choice prediction is a limited validation target—not proof of decision quality or “true” utility.

### 3. Thai testbed and impact

A Chula orthopaedic/shared-decision partner and Thai participants would be needed; recruitment is **[UNVERIFIED]**.

**Beneficiaries:** patients whose priorities differ from the model’s default assumptions and clinicians trying to surface disagreements.

**Measures:** elicitation burden, comprehension, held-out choice agreement, framing sensitivity and ability to explain *why* an option’s ranking changes.

[NICE NG226](https://www.nice.org.uk/guidance/ng226) can help define an evidence framework; Thai options, access constraints and outcome estimates require local review.

### 4. Nine-month POC/MVP

- **Data:** clinician-reviewed Thai outcome cards; approximately 60 participants completing repeated hypothetical decisions, including a second session. Any patient recruitment requires appropriate ethics approval.
- **Model:** small Bayesian latent-utility network pretrained on synthetic preference populations, then calibrated locally; an active question selector. The Thai interface can use a compact language model, but all clinical claims come from approved cards.
- **Compute:** **30 GPU-hours**; most preference inference is small-scale.
- **API:** **US$0 required**; optional **≤US$30** for synthetic phrasing candidates reviewed before use.
- **Proof:** whether adaptive elicitation is efficient and sufficiently stable in this setting. A hypothetical-choice study cannot establish better actual treatment decisions.

Allow “undecided” and changing preferences. Never translate model uncertainty into pressure to choose.

### 5. Prior art to beat

- Established patient-decision-aid standards: [IPDAS](https://ipdas.ohri.ca/).
- Evidence synthesis on decision aids: [Cochrane, patient decision aids](https://doi.org/10.1002/14651858.CD001431.pub6).
- Mandatory technical comparators: fixed elicitation, Bayesian logistic utility and Gaussian-process preference learning.

The novelty must be robust, efficient elicitation—not putting a chatbot in front of an existing decision aid.

### 6. Socratic stress-test

**Decisive assumption:** preferences are stable enough over the elicitation period to support a useful individualized model.

**Month-1 test:** after ethics clearance, 20 Thai adults repeat eight matched hypothetical choices one week apart, with randomized presentation order.

**Kill the stable-utility formulation** if median within-person inconsistency exceeds **25%**. Pivot to explaining uncertainty and facilitating deliberation, rather than claiming to have recovered a person’s utility function.

---

If I were the student I'd pick #1  
It makes the strongest genuine perspective flip, supports a frontier sequential-learning contribution on the laptop, and gives the committee a concrete decision: which evidence Thailand should buy before committing to AI.

## GEMINI (gemini-4-argon): Round 1

## Part A: What "Flipping the Perspective" Means

A plain screening or triage model assumes a passive, episodic, unconstrained encounter: a patient presents, an oracle outputs a static label ($Y$), and an infinite-capacity health system executes the route. 

**Worthwhile flips** dismantle these hidden operational assumptions:
1. **Encounter $\rightarrow$ System / Payer:** Optimising for NHSO’s network capacity, weekly quotas, and capitation budgets rather than unconstrained individual utility.
2. **Label $\rightarrow$ Information / Action Threshold:** Outputting the *minimal evidence* required to alter a clinical or HTA decision (Expected Value of Information) rather than a diagnosis.
3. **Model Decides $\rightarrow$ Model Earns Permission:** Deciding *when the AI or non-physician is statistically permitted to act alone* versus deferring.
4. **Inflow $\rightarrow$ Outflow:** Deciding who can safely *step down* from crowded tertiary hospitals to primary nodes.

**Gimmicks to avoid:** Simply predicting the inverse class ("healthy" instead of "sick"), reversing prompt roles ("patient quizzes doctor"), or applying black-box offline RL to clinical treatment policies—which fails under confounding and evaluation metric sensitivity ([PMLR v235/luo24f](https://proceedings.mlr.press/v235/luo24f.html)).

---

## Part B: Five Flipped Decision-Model Proposals (Ranked)

### 1. Quota-Aware Ask-or-Act Orchestrator (Flip: Encounter Accuracy $\rightarrow$ Network Resource Allocation)
1. **Name, the flip, and pitch:** **UC-QuotaRouter.** Flips the *level and threshold* of the decision. *Normal question:* "What disease does this patient have, and should they go to the ER?" $\rightarrow$ *Flipped question:* "Given live NHSO weekly quotas and regional doctor scarcity, what is the single highest-value clarifying question to ask, and which network node (Self-care, 32-symptom Pharmacy, รพ.สต. telemedicine, Hospital, 1669) minimises system cost at a fixed safety floor?"
2. **Paradigm and research question:** Sequential decision-making / POMDP trained via Group Relative Policy Optimization (GRPO) with asymmetric cost rewards. *RQ:* Does a 4B Thai LLM trained with GRPO in a quota-constrained network simulator achieve a $\ge 25\%$ reduction in simulated Hospital/ED routing cost at an equal or lower missed-escalation rate ($\le 2\%$) and higher ask-before-act rate than prompted frontier models and `ThaiLLM-27B-Prescreen` on clinician-labelled multi-turn vignettes?
3. **Thai testbed and impact:** Benefits NHSO (~47.5M UC members) and overcrowded public OPDs ([Hfocus 2026](https://www.hfocus.org/content/2026/07/38920)). In July 2026, demand forced NHSO to cap pharmacy/clinic "30-baht anywhere" innovation units with strict weekly quotas ([Hfocus 2026](https://www.hfocus.org/content/2026/07/38840)). Meanwhile, `ThaiLLM-27B-Prescreen` has an F1 of 0.00 for "Observe at Home" ([Model Card](https://huggingface.co/ThaiLLM/ThaiLLM-27B-Prescreen)). Measured by expected NHSO capitation/quota burn and under-triage rate on a KCMH clinician-validated test set. Real-world patient outcome impact is [UNVERIFIED] within a 9-month scope.
4. **POC/MVP (9 months, 1x RTX 4090 16GB):** 
   - *Data:* 300 seed clinical vignettes across 6 routing tiers, expanded into multi-turn dialogues via API patient-actors across 4 Thai dialects (Central, Isan, Northern, Southern), combined with synthetic NHSO quota states.
   - *Models:* `pai1/tma1-medgemma-4b` vs `Qwen3-4B` (4-bit QLoRA + GRPO). Note: must test 8-bit/bf16 fallback if 4-bit AWQ corrupts Thai tone marks ([arXiv:2608.22917](https://arxiv.org/abs/2608.22917)).
   - *Compute & Cost:* Simulator rollout and GRPO training fit in 16GB VRAM (~40–60 GPU hours per run). API cost for synthetic patient-actor generation and baseline evaluation: ~\$150–\$250.
5. **Prior art to beat:** Google AMIE (which lost to physicians on practicality $p=0.003$ and cost-effectiveness $p=0.004$; [arXiv:2603.08448](https://arxiv.org/abs/2603.08448)), CARE-Bench (where models asked clarifying questions only 33.5% of the time; [arXiv:2608.03731](https://arxiv.org/abs/2608.03731)), Microsoft MAI-DxO ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/sequential-diagnosis-with-language-models/)), and `ThaiLLM-27B-Prescreen`.
6. **Socratic stress-test:** *Decisive assumption:* Clinicians agree on what constitutes a safe "step-down" route (Pharmacy vs รพ.สต. vs Hospital), and frontier models cannot already do this via simple context prompting. *Month-1 test:* Two KCMH clinicians independently label 100 multi-turn vignettes across the 6 NHSO routes; evaluate zero-shot GPT-5/Claude-4 given a 1-page NHSO benefit/quota system prompt. *Kill/pivot threshold:* Kill if clinician inter-rater reliability $\kappa < 0.60$ (no ground truth exists) OR if the prompted frontier baseline already achieves $\le 5\%$ missed escalation and $\ge 80\%$ ask-before-act accuracy.

---

### 2. Anytime-Valid Autonomy Credentialing & Anti-Deskilling Engine (Flip: Deciding the Patient $\rightarrow$ Deciding AI Permission)
1. **Name, the flip, and pitch:** **Residency-as-Code.** Flips the *subject and default* of the decision model. *Normal question:* "What is the clinical decision for this patient?" $\rightarrow$ *Flipped question:* "Has the AI+Pharmacist dyad accumulated enough statistical evidence in this specific symptom stratum to act autonomously today, or must it defer to a physician—and is the human overseer deskilling?"
2. **Paradigm and research question:** Anytime-valid sequential hypothesis testing (conformal martingales / e-values) with hierarchical Bayesian pooling across strata, paired with Adversarial Verifier Self-Play. *RQ:* Does a hierarchical e-value credentialing engine reduce the sample size required to certify a $\le 1\%$ missed-escalation floor across NHSO's 32 pharmacy symptom groups by $\ge 50\%$ compared to fixed-count ladders (Utah's 250/1,000 rule), while detecting injected dialect-paraphrase drift and human automation bias within $\le 50$ audited encounters?
3. **Thai testbed and impact:** Benefits the Thai FDA (อย.), NHSO, and the Pharmacy Council (~6,000 pharmacies handling ~8M consults over two years; [Thansettakij 2025](https://www.thansettakij.com/health-wellness/health/627965)). The Thai Medical Council is currently suing NHSO over non-physician scope of practice in the 32 symptom groups ([Isranews](https://www.isranews.org/article/isranews/133298-isra-28.html)). An auditable mathematical protocol for granting and revoking AI-assisted autonomy directly addresses this regulatory deadlock. Actual adoption by อย. or the Medical Council is [UNVERIFIED].
4. **POC/MVP (9 months, 1x RTX 4090 16GB):**
   - *Data:* Stream of simulated encounters across the 32 pharmacy symptom groups, injected with dialect red-flag paraphrases (Isan/Northern) where rule-based detectors collapse from 1.00 to 0.00 recall ([arXiv:2610.21270](https://arxiv.org/html/2610.21270)), plus a 20-participant vignette study with Chula pharmacy students/pharmacists containing 20% seeded wrong AI advice.
   - *Models:* Local 4B triage model (`tma1-medgemma-4b`) + lightweight conformal e-value monitor (CPU/GPU negligible) + GRPO dialect-adversarial attacker.
   - *Compute & Cost:* 16GB VRAM is used to train the dialect-paraphrase attacker/verifier pair; statistical replay takes minutes on CPU. API cost: ~\$100.
5. **Prior art to beat:** Utah's Doctronic fixed 250/1,000 prescription renewal rule ([JAMA Health Forum](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2846947)), WATCH weighted conformal martingales ([arXiv:2505.04608](https://arxiv.org/pdf/2505.04608)), conformal selective prediction ([Sci Rep 2026](https://www.nature.com/articles/s41598-026-40637-w)), and colonoscopy deskilling observational studies ([Warwick WRAP](https://wrap.warwick.ac.uk/id/eprint/191005)).
6. **Socratic stress-test:** *Decisive assumption:* Rare red-flag events in primary care pharmacies occur frequently enough when pooled across 32 strata to statistically certify a 1% error bound in months rather than decades, and human overseers exhibit measurable automation bias on vignettes. *Month-1 test:* Run a Monte Carlo sample-size simulation using realistic NHSO pharmacy consult volumes (~670/pharmacy/year) and pilot 30 vignettes (6 with deliberate AI errors) on 10 Chula pharmacy students. *Kill/pivot threshold:* Kill the hierarchical engine if simulated time-to-promotion exceeds 12 months even at national pooling; kill the human-backstop monitor if students accept $<10\%$ of seeded wrong AI recommendations.

---

### 3. Living HTA Value-of-Information Engine (Flip: Clinical Triage $\rightarrow$ Payer Coverage & Trial Design)
1. **Name, the flip, and pitch:** **Living-HTA-VOI.** Flips the *definition of "decision model" from clinical to health-economic (HTA)* and flips the *output from a coverage verdict to an evidence-acquisition directive*. *Normal question:* "Should this patient be screened for disease X?" $\rightarrow$ *Flipped question:* "As NHSO deploys a new AI or drug benefit across Thailand, which sub-population's parameter uncertainty creates the highest financial and QALY risk of a wrong national reimbursement decision (Expected Value of Partial Perfect Information—EVPPI), and where should the next 500 registry audits be targeted?"
2. **Paradigm and research question:** Differentiable microsimulation / amortised Bayesian inference (Neural Posterior Estimation / TabPFN-style surrogates) for health-economic decision-analytic modelling. *RQ:* Can a neural surrogate trained on synthetic MOPH 43-file trajectories compute subgroup-specific EVPPI and optimal ICER (Incremental Cost-Effectiveness Ratio) price thresholds $100\times$ faster than standard nested Monte Carlo Markov models, while staying within $\le 3\%$ approximation error of gold-standard probabilistic sensitivity analysis (PSA)?
3. **Thai testbed and impact:** Directly targets **HITAP** (Health Intervention and Technology Assessment Program, which evaluates technologies for the UC benefit package [verify current 2026 NHSO innovation-list workflow before citing]) and NHSO's Thai Innovation budget—which is scaling from THB 2.9B (FY2568–69) to a target of THB 10B by FY2571, already funding Perceptra chest X-ray AI at THB 135M/year across 445 hospitals ([PostToday](https://www.posttoday.com/smart-life/739294); [Hfocus](https://www.hfocus.org/content/2025/07/34642)). Prevents payer bankruptcies from uncalibrated AI cascades (e.g., incidental chest X-ray findings triggering expensive follow-ups under capitation). Impact on actual NHSO price negotiations is [UNVERIFIED].
4. **POC/MVP (9 months, 1x RTX 4090 16GB):**
   - *Data:* Published HITAP/Thai economic parameters (costs, utilities, transition probabilities for Chest X-ray AI screening + TB/lung nodule cascades, and Diabetic Retinopathy AI screening; [NCT05166122](https://clinicaltrials.gov/study/NCT05166122)), combined with synthetic cohort distributions matching MOPH 43-file demographics ([GitHub validator](https://github.com/niratorn/MOPH_HDC_Validation)).
   - *Models:* PyTorch differentiable discrete-event microsimulation + Normalizing Flows / Amortised Neural EVPPI estimator + LLM agent that parses published Thai clinical trial PDFs into prior distributions.
   - *Compute & Cost:* 100% trainable on the 16GB 4090 Laptop (microsimulation tensors and neural density estimators take <8GB VRAM). API cost: ~\$50.
5. **Prior art to beat:** Standard R/heemod andSAVi (Sheffield Accelerated Value of Information) Gaussian Process surrogates, traditional static HITAP Markov models, and prognostic-only trajectory models like Delphi-2M ([DKFZ](https://inrepo02.dkfz.de/record/304606)) that lack QALY/cost/ICER mechanics.
6. **Socratic stress-test:** *Decisive assumption:* The medical + engineering capstone committee will accept a health-economic decision-analytic surrogate + active data-acquisition engine as "frontier AI", and parameter uncertainty in Thai AI deployment actually flips the ICER decision across provinces. *Month-1 test:* Re-implement one published Thai screening Markov model (e.g., DR or CXR screening) in PyTorch, run a 10,000-draw PSA across 5 regional prevalence/cost strata, and pitch the 1-page abstract to one Engineering and one Medicine committee member. *Kill/pivot threshold:* Kill if EVPPI across Thai regional strata is $< 5\%$ of total net monetary benefit (meaning uniform national policy is already optimal) OR if the engineering advisor flags it as "operations research, not frontier ML."

---

### 4. Reverse-Triage & Safe De-escalation Engine (Flip: Who Comes In $\rightarrow$ Who Safely Steps Down)
1. **Name, the flip, and pitch:** **KCMH-StepDown.** Flips the *direction* of clinical triage from inflow to outflow. *Normal question:* "Should this community patient be referred up to a tertiary hospital?" $\rightarrow$ *Flipped question:* "Which chronic or post-acute patients currently occupying KCMH specialist OPD slots or inpatient beds can safely step down to a รพ.สต. telemedicine node or community pharmacy for the next 6 months with a conformal guarantee of $\le 2\%$ 30-day unplanned bounce-back?"
2. **Paradigm and research question:** Longitudinal EHR Event Foundation Model (Delphi-2M / DT-Transformer architecture) wrapped in Split Conformal Risk Control with counterfactual step-down conditioning. *RQ:* On longitudinal patient trajectories, does a conformal-gated small event transformer identify a $\ge 25\%$ "safe step-down" outpatient/discharge cohort while maintaining the empirical 30-day unplanned revisit/readmission rate strictly below a user-specified $\alpha = 0.02$ bound across insurance schemes (UCS, SSO, CSMBS)?
3. **Thai testbed and impact:** Targets tertiary hospital overcrowding at KCMH and regional MOPH referral centres, bridging the 1:462 (Bangkok) vs 1:5,000 (Bueng Kan) doctor density gap ([Nation Thailand](https://www.nationthailand.com/blogs/news/policy/40058001)) by pushing stable patients back to the 10,910 telemedicine-enabled รพ.สต. ([Hfocus](https://www.hfocus.org/content/2026/02/37141)). Directly tests and fixes the subgroup calibration collapse seen in Epic's Curiosity model (where AUROC fell to 0.58 for self-pay; [medRxiv 2026](https://www.medrxiv.org/content/10.64898/2026.05.18.26353199v2.full)). Real-world bed/slot liberation is [UNVERIFIED] without prospective trial.
4. **POC/MVP (9 months, 1x RTX 4090 16GB):**
   - *Data:* Retrospective de-identified KCMH outpatient/discharge coded extract (ICD-10, labs, meds, 30-day bounce-back) under expedited IRB; fallback/pretraining on MIMIC-IV + synthetic Thai 43-file trajectories.
   - *Models:* 5M–20M parameter autoregressive event transformer (Delphi-2M took 1 V100 hour; [GitHub](https://github.com/gerstung-lab/Delphi)) + Hierarchical Conformal Risk Control layer.
   - *Compute & Cost:* Trains in <5 hours on a 16GB RTX 4090. API cost: \$0.
5. **Prior art to beat:** Epic CoMET/Curiosity ([arXiv:2508.12104](https://arxiv.org/abs/2508.12104); [medRxiv 2026](https://www.medrxiv.org/content/10.64898/2026.05.18.26353199v2.full)), DT-Transformer ([arXiv:2605.14227](https://arxiv.org/html/2605.14227v1)), Taiwan NHIRD-to-MIMIC transfer ([arXiv:2610.04946](https://arxiv.org/html/2610.04946)), and Oxipit ChestLink's high-specificity autonomous rule-out paradigm ([PMC13353222](https://pmc.ncbi.nlm.nih.gov/articles/PMC13353222/)).
6. **Socratic stress-test:** *Decisive assumption:* KCMH EHR data access can be secured in time, and historical data contains enough natural variance in follow-up intervals/step-downs to separate safe step-down from confounding by indication. *Month-1 test:* Meet KCMH clinical partner to request a de-identified coded extract of $\ge 20,000$ encounters, and run the conformal step-down pipeline on MIMIC-IV discharges to measure valid cohort yield at $\alpha = 0.02$. *Kill/pivot threshold:* Kill immediately at Day 30 if KCMH data owner will not co-sign an IRB submission; pivot if conformal calibration on MIMIC-IV yields $< 10\%$ step-down volume at the 2% risk bound.

---

### 5. Proactive Drop-Out & Care-Seeking Pre-emptor (Flip: Passive Triage $\rightarrow$ Outbound อสม. Outreach)
1. **Name, the flip, and pitch:** **VHV-Outreach-Allocator.** Flips *initiative and subject*: instead of waiting for a patient to present and diagnosing their disease, the system predicts *the patient's decision to silently drop out of chronic care or delay seeking care* and allocates scarce Village Health Volunteer (อสม.) home visits. *Normal question:* "How do we triage the patients who walk into the clinic today?" $\rightarrow$ *Flipped question:* "Given a rural อสม. who can only make 5 home visits this week, which silent patients in the village will suffer the largest preventable 1-year complication spike if we do not knock on their door today?"
2. **Paradigm and research question:** Uplift / Counterfactual Time-Series Forecasting with Constrained Restless Multi-Armed Bandits (RMAB) or Whittle Index policy learning. *RQ:* Does a Whittle-index outreach policy driven by a counterfactual trajectory model prevent $\ge 20\%$ more simulated 1-year acute complications (e.g., DKA, stroke, renal crash) under a strict 5-visit/week อสม. budget than standard risk-score ranking (highest absolute risk first) or rule-based overdue-appointment lists?
3. **Thai testbed and impact:** Built for Thailand's ~1.07M อสม. (Village Health Volunteers) and 10,910 รพ.สต. managing rural NCDs (diabetes/hypertension), where อสม. already use smartphone apps like RiskOCA ([JMIR mHealth 2026](https://mhealth.jmir.org/2026/1/e83738)). Standard risk models waste outreach on "always-adherers" or "unsaveable high-risk" patients rather than targeting *marginal uplift* (patients whose decision to adhere flips when visited). Real-world อสม. adherence lift in Thailand is [UNVERIFIED].
4. **POC/MVP (9 months, 1x RTX 4090 16GB):**
   - *Data:* Public/synthetic longitudinal NCD refill and clinic attendance trajectories calibrated to MOPH HDC public provincial diabetes/hypertension control rates ([MOPH HDC](https://github.com/niratorn/MOPH_HDC_Validation)), or retrospective KCMH/provincial NCD clinic logs if available.
   - *Models:* Neural uplift trajectory model (Causal Transformer / Do-PFN variant; [arXiv:2506.06039](https://arxiv.org/abs/2506.06039v2)) + Neural Whittle Index allocator trained on 4090.
   - *Compute & Cost:* Lightweight tabular/event sequences; full training <10 GPU hours on 16GB VRAM. API cost: <\$50.
5. **Prior art to beat:** Google Research's maternal-health RMABs (ARMMAN in India), Do-PFN causal foundation models ([arXiv:2506.06039](https://arxiv.org/abs/2506.06039v2)), RiskOCA VHV screening app ([JMIR mHealth 2026](https://mhealth.jmir.org/2026/1/e83738)), and prognostic-only EHR risk scores.
6. **Socratic stress-test:** *Decisive assumption:* We can estimate heterogeneous treatment effects (uplift of an อสม. home visit on medication adherence) without a historical randomised outreach trial in Thailand, avoiding the offline-RL evaluation trap ([PMLR v235/luo24f](https://proceedings.mlr.press/v235/luo24f.html)). *Month-1 test:* Formulate the semi-synthetic uplift DGP from published ARMMAN / Thai NCD refill delay statistics and test whether Whittle-index allocation beats simple "days-since-last-refill" heuristics across 10 confounding regimes. *Kill/pivot threshold:* Kill if simple "overdue > 30 days" rules capture $\ge 90\%$ of the Whittle-index policy's complication reduction, or if the clinical partner cannot provide any real refill-gap distribution data.

---

**If I were the student I'd pick #1 (UC-QuotaRouter), paired with #2's dialect-verifier audit as Chapter 1:** it preserves your audit-first/GRPO momentum on the 4090 laptop, requires zero retrospective hospital EHR governance delays, and flips a toy clinical chatbot into a national payer-orchestration decision model built specifically for NHSO's 2026 quota crisis.

---

# ROUND 2

## CLAUDE: Round 2

**Read:** `claude_round1.md`, `codex_round1.md`, `gemini_round1.md`. No Round 2 file was read.

**Provenance note.** Gemini's Round 1 leans heavily on `reports/AI care vectors for Thailand.md`: four of its five ideas are that report's directions, re-labelled as flips. Codex used the same report sparingly and built from decision theory outward. That difference matters for the convergence verdict below.

## 1. Hume audit: five load-bearing claims that are wrong, unverified or overstated

1. **Gemini #2: "realistic NHSO pharmacy consult volumes (~670/pharmacy/year)".**
   - *Problem:* the figure is the earlier report's own arithmetic. It comes from a May 2025 ministerial claim of ~8M consults over an unclear period across ~6,000 pharmacies, combined with a *hypothetical* 5% must-escalate prevalence. Gemini presents it as an empirical input.
   - *Verify:* NHSO's published pharmacy-32 claim counts by month and symptom group; a real red-flag prevalence from any pharmacy triage audit.
2. **Gemini #4: "KCMH-StepDown ... directly tests and fixes the subgroup calibration collapse seen in Epic's Curiosity".**
   - *Problem:* a 5–20M-parameter event model on one hospital's extract cannot "fix" a 118M-patient model's collapse. At best it reports its own calibration by scheme. The KCMH extract of ≥20,000 encounters under expedited review is also unverified, and step-down labels in retrospective data are confounded by indication. Gemini names this risk itself, then sets a POC target that assumes it away.
   - *Verify:* a co-signed data request, and how many historical step-down decisions actually occurred in the extract.
3. **Gemini #5: estimating the uplift of an อสม. visit "from published ARMMAN / Thai NCD refill delay statistics".**
   - *Problem:* a semi-synthetic data-generating process can rank algorithms; it cannot establish a Thai visit effect. The Whittle-index policy also needs indexability, which is assumed, not shown. Codex #4 makes the right demand: known non-zero assignment probabilities, or the clinical-effectiveness version is dead.
   - *Verify:* whether any Thai district randomised or lottery-allocated outreach, or logged allocation probabilities.
4. **Gemini #3: a neural EVPPI surrogate "100× faster ... within ≤3% error" that "prevents payer bankruptcies".**
   - *Problem:* speed-ups over nested Monte Carlo are already delivered by GP and regression EVPPI methods (SAVI, Strong–Oakley–Brennan). So 100× against *nested* MC is the wrong baseline, and "bankruptcies" is rhetoric.
   - *Verify:* benchmark against the regression-based EVPPI in SAVI or BCEA, not against nested MC.
5. **Codex #1: a learned sequential study-selection policy beating EVSI-greedy by ≥25% in net opportunity loss.**
   - *Problem:* plausible as a target, but with a small menu of candidate pilots (3–6 study designs × sample sizes), exhaustive or greedy EVSI is cheap and near-optimal. Amortised design (Deep Adaptive Design) mainly buys *speed* in large or continuous design spaces. The neural policy may have nothing to beat.
   - *Verify:* in month 1, count the decision-relevant design space. If exhaustive EVSI over it runs in minutes, drop the learned policy and keep the decision model.

Minor: Gemini #1 benchmarks against "GPT-5/Claude-4", which are not current frontier baselines in Oct 2026. Several ideas assume `pai1/tma1-medgemma-4b`, whose gated HAI-DEF licence the README already flagged as unchecked.

## 2. Convergence verdict

| Cluster | Who | Signal or attractor? | Best variant | What makes it publishable |
|---|---|---|---|---|
| **Value of information: decide what to learn before deciding** | Codex #1, #2; Gemini #3; Claude #5 | **Real signal.** Codex reached it from first principles ("start with the decision, then ask whether prediction is needed"), not from the report. | Codex #1 (adopt / reject / *pilot first*) + Codex #2 (management regret, not diagnostic entropy) | The objective is **decision regret**, not accuracy or entropy, and the action set includes "gather evidence". |
| **Permission to act** | Codex #3; Gemini #2; Claude (v6 AI Residency) | Partly attractor. Gemini imported it from the report, but Codex independently made it the decision variable. | Codex #3's learned gate + randomised, logged audit probabilities, plus Gemini #2's human-backstop probes | Honest guarantees: logged audit probabilities, no claims for unobserved strata, measured demotion delay. |
| **Outreach by benefit, not risk** | Codex #4; Gemini #5; Claude #2 | Real signal, but **identification-gated** | Codex #4 (doubly robust policy learning; known assignment probabilities) | It is publishable only with randomised or known-propensity data; otherwise it is a simulator paper. |
| **Reverse triage / step-down** | Claude #1; Gemini #4 | Attractor. Codex's warning stands: "renaming low-risk classification 'reverse triage'" is a gimmick unless capacity enters the decision. | None in current form | It would need a capacity-constrained assignment *and* a guarantee, and both proposals are gated on data access. |
| **Patient's own decision** | Codex #5 (preferences); Claude #3 (care-seeking) | Real but separate | Codex #5 | Test–retest stability as the kill test is the right instinct. |

**Self-correction:** I withdraw my Round 1 pick (#1 reverse triage) as the lead. Codex's gimmick test is fair. Without a capacity-constrained assignment problem and a data owner, it is a low-risk classifier with a better name.

## 3. Socrates: most over-rated idea, Gemini #1 UC-QuotaRouter

It breaks on the assumption that **a policy trained against a synthetic quota-and-patient simulator produces a result about the Thai network**. Its headline RQ ("≥25% reduction in simulated Hospital/ED routing cost") is a property of the simulator's cost table, which the student writes. And conceptually it is the plain triage chatbot the student asked to escape, with a cost term added: it still answers "where should this patient go?" The genuinely flipped part, *which question to ask*, is done more cleanly by Codex #2 without the network simulator's unverifiable assumptions.

## 4. Most under-rated: Codex #2 "Ask only what could change care"

It is the purest flip on the board. It changes the *objective* from diagnostic certainty to **management regret**. It is laptop-feasible, needs no data-access miracle (clinician-authored case families plus counterfactual variants), and has a decisive month-1 kill test (a 3-question checklist reproducing ≥95% of management decisions).

**The merge that makes it a thesis.** Codex #1 and Codex #2 are *the same mathematics at two scales*: expected value of information with respect to a decision. At the **bedside** the question is "which question or test could change this patient's management?" At the **system** level it is "which pilot study could change Thailand's decision to fund this AI?" A single framework, a decision model with an explicit "acquire information" action scored by regret, applied at both scales, also answers the student's open question about which kind of "decision model" is meant: **both, unified by one idea**.

## 5. Final top 3

| # | Project | Flip | Novelty (1–5) | Thai impact (1–5) | POC finish confidence | Gate / dependency | Why |
|---|---|---|---|---|---|---|---|
| 1 | **Decision-relevant information at two scales**: a regret-based VOI decision model choosing the next question (bedside, Codex #2) and the next pilot before funding AI (system, Codex #1 + Gemini #3 + Claude #5) | Output: label → *what to learn next*; objective: accuracy → regret | 4 | 4 | 70% | One clinician pathway (≈100–300 case families) and one published Thai HTA model to re-implement; an HTA collaborator (HITAP contact [UNVERIFIED]) | It answers both meanings of "decision model" with one idea, has a hard non-ML baseline at each scale, and speaks to NHSO's growing AI budget. |
| 2 | **Revocable AI leases**: a learned competence gate + randomised audit + promotion/revocation, with human-backstop probes (Codex #3 + Gemini #2 + Claude v6) | Decider: model decides → model *earns permission* | 4 | 5 | 70% | Public retinal data first (EyePACS/IDRiD licences); Thai data later | It is the strongest Thai-policy story (Medical Council vs NHSO scope fight) and has honest statistics. |
| 3 | **Benefit-based outreach for อสม.** (Codex #4 + Gemini #5 + Claude #2) | Initiative + risk → benefit | 3 | 4 | 40% | Known assignment probabilities or randomised outreach data | Highest real-world leverage, but dies without identification. |

- **Moonshot:** *Living HTA for NHSO's AI procurement.* The system-scale half of #1 grown into a continuously updated model of every AI on the Thai-innovation benefit list, telling NHSO which to fund, which to pilot first, and which evidence to buy (Gemini #3 + Codex #1 + Claude #5).
- **Safe ambitious:** *The bedside half of #1.* Codex #2's decision-regret question selection on one clinician-owned pathway, with the fixed-checklist baseline. It can be finished on the laptop with no data-access dependency.

## CODEX (gpt-6.1-sol): Round 2

## 1. **Hume audit**

I used only the supplied Round-1 material. Linked sources have not been independently checked. Proposed improvement targets are not reported results; the audit below concerns the assumptions supporting those targets.

### 1. Reverse triage: a conformal readmission bound is not a guarantee of safe transfer

**Claim:** Claude’s #1 and Gemini’s #4 propose identifying patients who can safely step down with a guaranteed deterioration or bounce-back rate. Gemini adds “counterfactual step-down conditioning.”

**Why overstated:** Historical outcomes under tertiary care do not identify outcomes after withdrawing that care. Adding a proposed destination to a model does not create the missing counterfactual. Conformal risk control can bound a specified loss under its sampling assumptions; it does not remove confounding, establish safety under a changed care pathway, or automatically provide guarantees for every insurance subgroup. Nor does a 30-day endpoint establish safety over Gemini’s six-month transfer horizon.

Claude’s low-*predicted*-risk yield test also cannot establish how many patients are genuinely safe to transfer.

**What would verify it:** Define the transfer intervention, receiving capabilities, outcome horizon and estimand. Establish sufficiently complete cross-facility follow-up and usable variation in actual transfers. Perform causal evaluation under explicit identification assumptions. A retrospective POC can establish feasibility and uncertainty; a prospective comparative evaluation is needed for a credible clinical safety claim.

### 2. Autonomy credentialing: pooling cannot manufacture subgroup evidence

**Claim:** Gemini’s #2 presents hierarchical pooling plus anytime-valid testing as a feasible route to substantially faster certification of a ≤1% error rate across 32 symptom groups, with rapid drift detection.

**Why overstated:** The missing ingredient is an information-budget calculation, not another verifier. With zero errors, approximately 300 independent observations support a roughly 1% one-sided, fixed-time 95% upper bound for **one population**. Simultaneous subgroup claims, selective auditing and repeated monitoring require additional care. Hierarchical shrinkage does not, by itself, confer a frequentist guarantee on each sparsely observed group.

“Missed escalation” must also specify its denominator: all encounters, autonomous encounters, or genuinely urgent encounters. Those are very different evidence requirements. Detection within 50 audits depends on the size and location of the deterioration.

**What would verify it:** A precise risk definition, formal validity argument, logged randomized audit probabilities, and simulations covering heterogeneous subgroup errors, audit scarcity and small shifts. Benchmark against strong sequential methods at matched error control—not only a fixed-count licensing ladder.

### 3. QuotaRouter: national infrastructure and policy citations do not establish an executable routing environment

**Claim:** Gemini’s #1 treats weekly NHSO quotas and available alternative channels as the basis for a live national orchestration problem.

**Why unverified:** The supplied text does not establish the current operational rules, which providers and services are covered, whether capacity is observable, or whether a recommended destination can actually accept that patient. Gemini’s precise July 2026 policy narrative and linked benchmark claims remain unverified here. Claude’s national telemedicine deployment count likewise does not establish receiving-site readiness.

A synthetic quota variable is useful for an experiment, but it is not an operational capacity feed. Quota consumption, reimbursement and marginal system cost are also not interchangeable.

**What would verify it:** An authoritative policy document, a partner-reviewed service-and-eligibility matrix, realistic capacity/acceptance traces, and a costing specification. Until then, describe the result as **simulation-based constrained routing**, not demonstrated NHSO orchestration or savings.

### 4. Outreach: prevalence-calibrated simulation does not identify the benefit of a visit

**Claim:** Claude’s #2 and Gemini’s #5 propose allocating visits to prevent admissions or complications using simulators calibrated to Thai disease and attendance statistics.

**Why overstated:** Marginal prevalence, refill gaps and admission rates do not identify how an อสม. visit changes outcomes—or for whom. Many intervention-effect models can reproduce those same statistics while recommending opposite allocations. Gemini’s confounding-regime experiments test robustness within an invented data-generating process; they do not validate Thai treatment effects.

A Whittle-index policy also needs an appropriate dynamic model and justification of indexability, or an honest characterization as a heuristic.

**What would verify it:** Randomized outreach data, or a defensible observational identification strategy with adequate overlap and sensitivity analysis. Without that, test methods across explicitly varied intervention-effect models and report simulated benefit only. Start with completed follow-up, not an assumed reduction in one-year complications.

### 5. Living HTA: low relative EVPPI does not imply uniform national policy is optimal

**Claim:** Gemini’s #3 proposes killing the project if regional EVPPI is below 5% of total net monetary benefit, interpreting this as evidence that uniform national policy is already optimal.

**Why wrong:** EVPPI measures the value of resolving uncertainty about selected parameters. It does not measure the value of tailoring policy to known regional differences. Regional policies can differ optimally even when EVPPI is zero. Dividing by total NMB does not repair that distinction.

Likewise, subgroup EVPPI alone does not determine where the next 500 audits should go: that requires a finite-study observation model, expected information gain, decision consequences and study costs.

**What would verify it:** Compare uniform and region-specific policies directly. Use EVPPI as an upper bound on the value of learning selected parameters, then calculate EVSI and expected net benefit of sampling for feasible studies. Validate approximations against **decision regret and study ranking**, not only percentage error in economic outputs.

## 2. **Convergence verdict**

The convergence is meaningful as a **problem shortlist**, but weak evidence of independent discovery. The brief explicitly supplied most axes, and the advisors shared the same Thai infrastructure narrative and prior “permission” framing. Agreement is not a novelty search.

| Cluster | Convergence | Best variant |
|---|---|---|
| **Payer decides what to learn or buy** | Claude #5, Codex #1, Gemini #3 | **Codex #1, Evidence Before Algorithms**, supported by Claude’s executable-model verification harness. Choose evidence by its expected effect on the decision; add Gemini’s acceleration only if conventional computation is genuinely limiting. |
| **Inflow → safe outflow** | Claude #1, Gemini #4 | **Claude #1, network-aware reverse triage.** Receiving capacity is a more consequential extension than choosing a larger trajectory model. The safety claim must first be narrowed as above. |
| **Passive attendance → proactive outreach** | All three | **Codex #4, benefit-based outreach**, initially one intervention and an identifiable attendance endpoint. Claude/Gemini’s sequential bandit extension becomes worthwhile only after intervention dynamics are supported. |
| **Diagnosis → decision-relevant information** | Codex #2, Gemini #1 | **Codex #2, Ask Only What Could Change Care.** It isolates information acquisition from wording, quotas and routing, making the contribution much easier to evaluate. |
| **Patient decision → permission to automate** | Codex #3, Gemini #2 | **Codex #3, Revocable AI Leases**, with Gemini’s adversarial tests as stress tests—not as statistical evidence of population safety. |

Two apparent convergences need separating:

- **Access-adjusted thresholds:** Claude #4 and Gemini #1 both make context matter, but patient access costs and payer quotas are not the same objective. **Claude #4** is the cleaner formulation.
- **Modelling human decisions:** Claude #3 models care-seeking; Codex #5 elicits treatment preferences; Gemini #5 predicts and attempts to change attendance. These are distinct research problems, not three endorsements of one method. For a bounded human-subject POC, **Codex #5’s explicit elicitation** is preferable to assuming LLM personas reproduce Thai choices.

The strongest common insight is therefore not “build reverse triage.” It is: **make the action, constraints and consequences explicit before selecting the predictive model.**

## 3. **Socrates**

### Most over-rated: Gemini’s **UC-QuotaRouter**

Its appeal is understandable: a Thai-language model, constrained resources, sequential questions and a nationally relevant setting. But it bundles several unvalidated components into one reward-driven system.

**The assumption it breaks on:** clinically acceptable, lower-cost substitutes exist for enough encounters—and their suitability and availability can be represented faithfully in the simulator.

If that assumption fails, GRPO can learn to exploit synthetic costs and adjudication rules rather than improve care. A low average missed-escalation rate can also conceal concentrated harm in a dialect, symptom group or low-access population. Asking more questions is not intrinsically better.

The first experiment should therefore use **no learned dialogue policy**:

1. Clinicians define admissible destinations for a bounded set of cases.
2. A simple constrained optimizer assigns only among admissible, available destinations.
3. Compare it with a short checklist and fixed routing rules at matched safety.

If meaningful savings survive realistic receiving-capacity constraints, investigate whether learned questioning adds value. Otherwise, the national orchestrator is mostly a triage chatbot with quota-shaped rewards. Adding the autonomy and anti-deskilling project as a second chapter makes the nine-month execution risk worse.

## 4. **Most under-rated**

### Claude’s **Access-adjusted thresholds**

This is less spectacular than agentic HTA or national routing, but it asks a consequential question: **does the same model score justify the same action when completing that action is radically harder for some patients?**

I would improve it into an **access-aware policy frontier**, rather than immediately producing a map of “optimal” thresholds.

Compare:

- a uniform referral threshold;
- district-specific thresholds;
- a uniform threshold plus transport or referral-completion support;
- capacity- and equity-constrained versions of those policies.

Model referral completion and treatment consequences explicitly. Otherwise, higher travel costs can mechanically justify *less* referral for already disadvantaged patients—the opposite of the intended impact. Report who loses access, not just aggregate net benefit.

**Merge:** use Codex #1’s value-of-information framework to identify which local measurements would change the policy: referral completion, treatment delay, travel burden or downstream capacity.

This combination has a strong fallback: even if tailored thresholds are not justified, it can establish that improving access is more valuable than changing the classifier’s operating point. Its weakness is frontier-ML novelty; that needs an honest committee discussion, not a decorative neural network.

## 5. **Final top 3**

Scores are provisional judgments, not literature-validated novelty claims. **Thai impact** means potential impact if validated and adopted. **POC finish confidence** is my subjective chance of completing a defensible, reproducible nine-month study—including a negative result—not obtaining clinical approval or demonstrating patient benefit.

| # | Project | Flip | Novelty (1–5) | Thai impact (1–5) | POC finish confidence (%) | Gate/dependency | Why |
|---|---|---|---:|---:|---:|---|---|
| **1** | **Evidence Before Algorithms — audited HTA evidence-allocation engine** | “Should we buy AI?” → “Which evidence could change the funding decision?” | **4** | **4** | **80%** | Month 1: reproduce one bounded economic model, obtain HTA review, and show that feasible learning could be worth its cost. Learned selection must face strong classical baselines. | Strongest genuine decision-model flip. Public parameters and explicit priors support a POC without claiming access to national records. Claude’s verification harness makes the economic foundation auditable. |
| **2** | **Revocable AI Leases — narrow-task autonomy and audit allocation** | Validate a classifier once → allocate and revoke permission continuously | **4** | **4** | **80%** | Accessible labelled data; one precisely defined risk target; sufficient independent audit evidence. Subgroup and sequential claims require explicit validity conditions. | Strong fit to the student’s audit-first direction. A frozen predictor keeps the project focused on learned permission allocation and monitoring rather than foundation-model training. Foreign data support methodology, not Thai authorization. |
| **3** | **Access-Aware Policy Frontier — thresholds versus access support** | Same risk, same action → compare actions under unequal access and capacity | **3** | **4** | **85%** | One reviewed clinical pathway, credible calibration/accuracy inputs and plausible uptake/cost ranges. Committee acceptance of the methodological contribution is an early gate. | Best scope-to-impact balance among the other advisors’ ideas. It can compare software adjustment with practical access support and expose distributional harms hidden by aggregate optimization. |

**Moonshot:** **#1**, expanded into a living, multi-site evidence-allocation engine that recommends conditional coverage and targeted studies as evidence arrives. Keep economic assumptions and reimbursement decisions under human review.

**Safe ambitious:** **#3**, bounded to one pathway and a transparent uncertainty-and-equity analysis. It remains a useful result if the answer is “retain the national threshold and improve referral completion instead.”

## GEMINI (gemini-4-argon): Round 2

## 1. Hume Audit: 5 Load-Bearing Claims to Challenge

1. **Claude #1 & #4 (Network-scale step-down & Access-adjusted thresholds): Unverified assumption that observational EHRs or published tables identify the risk of stepping down or delaying referral.**
   - *Why it is overstated/unverified:* In Claude #1, historical KCMH/43-file data only records outcomes for patients under the care tier they *actually received*. Applying conformal risk control to observational discharges/follow-ups guarantees error rates under the *historical assignment regime* (which is heavily confounded by clinician judgment), not the counterfactual intervention of stepping a tertiary patient down to a รพ.สต. Similarly, Claude #4 assumes we know the QALY loss of raising a screening threshold in Bueng Kan vs. Bangkok; without untreated natural-history progression rates, expected-utility maps rest on invented penalty weights.
   - *What would verify it:* For #1, an audit of KCMH outpatient records showing natural quasi-random variance in follow-up intervals (e.g., holiday clinic closures or physician scheduling shocks) to identify counterfactual step-down risk. For #4, a published Thai disease-progression Markov model with validated stage-specific utility weights and delay hazards.

2. **Codex #4 (Benefit-based outreach via causal policy learning): Unfeasible data gate for a 9-month Master’s capstone.**
   - *Why it is overstated/unverified:* Codex admirably states the exact condition required for doubly robust causal policy learning—at least 2,000 eligible episodes with *known, nonzero outreach-assignment probabilities* (i.e., a historical randomized trial or logged propensity scores) and $\ge 200$ verified events per arm. However, routine Thai primary-care EHRs and Smart อสม. logs do not log randomized outreach probabilities. Treating this as a realistic 9-month clinical-effectiveness POC sets the student up for an immediate Month-1 kill.
   - *What would verify it:* A signed letter of commitment from a Chula/MOPH diabetes clinic confirming an existing randomized outreach dataset or an active IRB allowing randomized SMS/phone allocation within Month 1.

3. **Claude #5 (Living HTA via LLM replication of 10–20 published HITAP models): Overstates published reporting completeness in Thai HTA papers.**
   - *Why it is overstated/unverified:* Claude proposes benchmarking an LLM agent by reproducing 10–20 published Thai CEA models within $\pm 10\%$ of reported ICERs from the paper text alone. In health economics, published manuscripts routinely omit full variance-covariance matrices, age-stratified background mortality tables, or exact Excel tunnel-state formulas. When an agent misses the ICER by 30%, you cannot distinguish LLM coding failure from unstated author assumptions.
   - *What would verify it:* Manually extracting 3 published HITAP papers (and checking if HITAP provides open-source Excel/R model files alongside their reports) before writing a single line of agent code.

4. **Codex #1 (Learned belief-state Transformer for HTA EVSI study selection): Overstated ML necessity ("neural wrapper" risk).**
   - *Why it is overstated/unverified:* In a standard diabetic retinopathy HTA pathway, there are fewer than a dozen candidate local studies (e.g., audit referral completion, measure rural prevalence, time clinic workflow) and a low-dimensional parameter space. Training a 60-GPU-hour belief-state Transformer to select among $\sim 5\text{–}10$ discrete study designs will almost certainly be matched by a 10-line Gaussian Process surrogate (SAVi) or greedy myopic EVSI, violating Codex's own rule against putting a neural wrapper around an easy economic problem.
   - *What would verify it:* Running a baseline myopic EVSI / Gaussian Process surrogate on the DR Markov model in Month 1; a learned sequential policy is only justified if the study-selection horizon is $\ge 3$ sequential stages with combinatorial spatial/subgroup allocation (e.g., allocating registry audits across 77 provinces).

5. **Claude #3 (Care-seeking delay via online/อสม. vignette surveys + LLM "silicon samples"): Overstated validity of hypothetical stated delay and LLM personas.**
   - *Why it is overstated/unverified:* Acute care-seeking delay in rural stroke or sepsis is governed by visceral symptom ambiguity, panic, midnight transport friction, and acute cash/family hierarchy constraints. Asking healthy respondents in a calm vignette survey "when would you go to the hospital?" suffers from massive hypothetical bias, and current literature shows LLM "silicon samples" fail to replicate sub-national rural socio-economic variance in low-resource languages.
   - *What would verify it:* Comparing vignette-predicted delay distributions against actual arrival-time logs (onset-to-door time) in the KCMH or regional Stroke Fast Track registry across districts.

---

## 2. Convergence Verdict

The three advisors converged strongly on **four distinct perspective flips**:

1. **The HTA / System-Buyer Flip (Clinical Triage $\rightarrow$ Health-Economic Value of Information):**
   - *Proposals:* Claude #5 (Living HTA agent replicating models), Codex #1 (Amortized Bayesian experimental design / EVSI for DR pathways), Gemini #3 (Differentiable microsimulation + neural EVPPI surrogate for NHSO AI procurement).
   - *Verdict:* **Genuine high-value signal.** The brief explicitly invited HTA decision models, and NHSO's rapid expansion of the Thai Innovation budget (THB 2.9B $\rightarrow$ 10B) without AI-specific HTA guardrails makes this a massive real-world gap.
   - *Best variant:* **A synthesis of Codex #1 and Gemini #3 (with Claude #5's NHSO AI-purchasing target).** Codex's framing ("what local study should Thailand buy before buying the AI?") is the sharpest decision question; Gemini's differentiable microsimulation + regional subgroup EVPPI provides the high-dimensional complexity where neural amortization actually beats classical SAVi.

2. **The Autonomy / Competence-Gating Flip (Deciding the Patient $\rightarrow$ Deciding AI Permission to Act):**
   - *Proposals:* Codex #3 (Revocable AI Leases via selective prediction + sequential monitoring), Gemini #2 (Residency-as-Code: anytime-valid hierarchical e-values + dialect drift/deskilling audit), and implicitly Claude #1 (conformal risk-controlled step-down).
   - *Verdict:* **Genuine signal anchored in the student's prior research.** It directly operationalizes the "capability has outrun permission" thesis and Thailand's 32-symptom pharmacy scope-of-practice dispute.
   - *Best variant:* **Codex #3 merged with Gemini #2.** Codex #3 provides immaculate statistical hygiene (explicitly logging non-zero random audit probabilities to avoid selection bias and bounding sample-size reality), while Gemini #2 grounds it in Thailand's 32 pharmacy symptom strata, dialect shift, and human overseer deskilling.

3. **The Proactive Outreach Flip (Passive Inflow $\rightarrow$ Marginal Uplift / RMAB Allocation):**
   - *Proposals:* Claude #2 (อสม. restless bandits), Codex #4 (Doubly robust causal policy learning for outreach), Gemini #5 (Whittle-index RMAB + counterfactual uplift trajectory model).
   - *Verdict:* **Obvious attractor of the brief with a fatal data trap.** While intellectually clean, every advisor hit the same wall: without randomized historical outreach logs in Thailand, causal uplift / RMAB effectiveness cannot be proven on real patients in 9 months.
   - *Best variant:* **Codex #4's methodological honesty + Claude #2's अสม. framing**, kept strictly as a backup unless randomized outreach data materializes.

4. **The Sequential Information-Acquisition / Quota-Aware Flip (Static Diagnosis $\rightarrow$ Cost- & Action-Sensitive Questioning):**
   - *Proposals:* Codex #2 (Decision-sensitive POMDP: ask only what changes management), Gemini #1 (Quota-aware Ask-or-Act Orchestrator via GRPO), Claude #4 (Access-adjusted operating thresholds).
   - *Verdict:* **Genuine signal.** Flipping from "minimize diagnostic entropy" to "minimize management regret under local capacity/access constraints" turns a standard medical LLM/classifier into a true decision-theoretic agent.
   - *Best variant:* **Gemini #1 + Codex #2's management-regret objective + Claude #4's spatial access costs.**

---

## 3. Socrates: Single Most Over-Rated Idea

**Claude #3 — Modelling the patient's decision: "what will make them come?" (Discrete-choice vignette survey + LLM persona simulation for acute care-seeking delay).**

- **Why it is over-rated:** It sounds empathetically compelling ("flip from the doctor's diagnosis to the patient's choice"), but as a 9-month Engineering + Medicine Master's thesis, it is a trap. First, running a 300–500 person rural/อสม. survey requires behavioural IRB approval and field logistics that will consume 4–6 months before any ML begins. Second, testing whether LLM personas correlate with human survey responses on 5-point Likert vignettes is a saturated social-science benchmark, not frontier engineering.
- **The decisive assumption it breaks on:** *Stated hypothetical preference $\neq$ visceral emergency behaviour.* When a rural patient in Isan has chest pain or slurred speech at 11 PM, the delay is driven by symptom denial, fear of burdening adult children, and lack of night transport—none of which are faithfully captured by a daytime multiple-choice vignette or an LLM role-playing a rural farmer.

---

## 4. Most Under-Rated Idea and How to Merge/Improve It

**Claude #4 — Access-adjusted thresholds: "same risk, different decision" (Spatial decision-curve analysis for national AI rollouts).**

- **Why it is under-rated:** Both Codex and Gemini focused heavily on complex sequential architectures (POMDPs, Transformers, e-value martingales), whereas Claude #4 identified a devastatingly simple, high-impact truth: **NHSO is deploying screening AI (like Perceptra Chest X-ray AI across 445+ hospitals and DR screening) using a single uniform operating threshold across provinces whose doctor densities and patient travel costs differ by $10\times$.** A false positive in Bangkok costs a 20-minute metro ride; a false positive in Bueng Kan costs a day's agricultural wages and clogs a 1:5,000 doctor bottleneck.
- **How to improve and merge it:** On its own, Claude #4 is a static health-economics calculation (potentially too thin for an Engineering thesis). However, if we **merge Claude #4 into Codex #1 + Gemini #3 (The Living HTA & Value-of-Information Engine)**, it becomes extraordinary:
  1. Instead of optimizing a single national accept/reject decision, the HTA engine jointly optimizes **district-level AI operating thresholds ($\tau_d$)** and **targeted local evidence-generation pilots (EVSI)** across Thailand's 77 provinces.
  2. This solves Codex #1's dimensionality problem (allocating multi-site calibration/workflow studies and thresholds across a spatial network genuinely requires amortized neural experimental design over simple SAVi) and gives Claude #4 a rigorous health-economic simulator (QALYs, NHSO capitation cascades, referral completion from Beede et al. CHI 2020).

---

## 5. Final Top 3 Project Recommendations

| # | Project | Flip | Novelty (1–5) | Thai Impact (1–5) | POC Finish Confidence (%) | Gate / Dependency | Why |
| :- | :--- | :--- | :-: | :-: | :-: | :--- | :--- |
| **1** | **Revocable AI Leases & Autonomy Engine** *(Merge: Codex #3 + Gemini #2 + Claude #1 conformal layer)* | **Static Validation $\rightarrow$ Dynamic Permission to Act:** Decides *when* an AI (or AI+Pharmacist/Step-down node) has earned statistical permission to act autonomously vs. deferring, and how much random audit it requires under distribution/dialect shift. | 5 | 5 | **88%** | **Zero hospital EHR gate.** Uses public/partner DR images (EyePACS/IDRiD) or 32-symptom pharmacy vignettes + injected dialect/prevalence shifts. | Solves the hardest deployment problem in clinical AI (how regulators like อย. and NHSO safely grant and revoke autonomy). Combines learned selective competence gates with anytime-valid sequential auditing (e-values) and explicit random-audit logging on a 16GB 4090. |
| **2** | **Decision-Regret & Quota-Aware Ask-or-Act Navigator** *(Merge: Codex #2 + Gemini #1)* | **Diagnostic Entropy $\rightarrow$ Management Regret under Quotas:** Stops asking questions when answers won't change the route; asks the single question that flips management under live NHSO weekly quotas. | 4 | 5 | **85%** | **Clinician adjudication gate:** Needs 1–2 KCMH clinicians to define the allowed action space and adjudicate 100–300 counterfactual case families in Month 1. | Avoids retrospective EHR delays while delivering genuine frontier ML (risk-sensitive POMDP / GRPO on a 4B Thai LLM). Directly fixes the failure of diagnostic chatbots that over-question and over-refer into NHSO's quota-capped 30-baht network. |
| **3** | **Evidence Before Algorithms: Spatial HTA & Threshold Engine** *(Merge: Codex #1 + Gemini #3 + Claude #4 & #5)* | **Patient Triage $\rightarrow$ Payer Study & Threshold Selection:** Decides *which local pilot study Thailand should fund next* (EVSI) and sets *access-adjusted provincial AI thresholds* before scaling NHSO AI procurement. | 5 | 5 | **80%** | **Committee alignment gate:** Must confirm in Month 1 that the Engineering advisor accepts amortized Bayesian experimental design + differentiable microsimulation as core ML. | The ultimate system-level flip. Directly serves HITAP and NHSO's THB 2.9B$\rightarrow$10B innovation fund using real published Thai DR/CXR screening parameters, 100% free of patient-privacy bottlenecks. |

---

### Final Picks

- **The "Safe Ambitious" Pick: Project #1 (Revocable AI Leases & Autonomy Engine) or Project #2 (Decision-Regret & Quota-Aware Navigator).**  
  Both are 100% insulated from KCMH retrospective EHR delays, fit comfortably on the 16GB RTX 4090 Laptop under a \$200 API budget, and have crisp Month-1 Socratic kill tests. **Project #1** is the strongest statistical-ML paper (anytime-valid sequential auditing + learned deferral); **Project #2** is the strongest LLM/RL paper (management-regret POMDP via GRPO).

- **The "Moonshot" Pick: Project #3 (Evidence Before Algorithms: Spatial HTA & Threshold Engine).**  
  Flipping the decision model from the *patient* to the *national purchaser (NHSO/HITAP)*—using amortized Bayesian experimental design to decide which local implementation trial Thailand should run next and how operating thresholds should flex from Bangkok to Bueng Kan—is the boldest perspective shift in the council. If the Engineering advisor signs off on amortized sequential experimental design as the ML core in Month 1, this could redefine how LMIC single payers evaluate and buy medical AI.
