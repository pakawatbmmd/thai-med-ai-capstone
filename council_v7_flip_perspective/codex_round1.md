# Flip the perspective: model the decision, not merely the patient

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