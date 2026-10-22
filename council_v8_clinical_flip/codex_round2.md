# Council v8 — Codex, Round 2

## 1. **Hume audit**

These are the five most consequential weaknesses in Claude’s and Gemini’s proposals. A research hypothesis is not a false claim; the problem is where the proposed evidence cannot support the advertised conclusion. No new literature search or runtime benchmarking was performed.

### 1. Gemini’s PivotDiff: reversing a model’s action is not establishing a safe clinical boundary

**Claim:** Physiologically plausible, action-flipping counterfactuals can directly generate discharge safety-netting instructions and solve unsafe home-discharge decisions.

**Why overstated:** A counterfactual explains the **classifier’s boundary**, not the patient’s safety boundary. An incorrect classifier can have perfectly plausible counterfactual explanations. Changing recorded history is also not equivalent to changing physiology through an intervention. Neither physiological constraints nor distance in an embedding establishes that discharge is safe below the generated threshold.

Novelty is additionally unverified: counterfactual explanation is established; substituting discrete diffusion must beat constrained search on more than sample appearance. The cited Thai-model failure and prior student report are not included in this repository view and cannot serve as verified evidence.

**What would verify it:** Separate model fidelity, feasibility, stability, and clinical validity. First beat constrained search on the first three. Clinical safety-netting would then require independent clinical criteria and adjudication—not agreement with the classifier being explained. Until then, label the output **“what changes this model’s recommendation,”** not “when home observation is safe.”

### 2. Claude’s and Gemini’s stopping models: predicting successful withdrawal does not identify the benefit of withdrawing now

**Claim:** Claude’s antibiotic stopping rule can shorten treatment without worse outcomes; Gemini’s WeanJEPA can reduce rebound failure and identify true readiness for withdrawal.

**Why overstated:** Recorded withdrawal decisions reflect clinician-observed readiness, including information absent from structured data. Predicting outcomes among patients clinicians chose to wean does not identify outcomes had other patients been weaned. Action-conditioned representations do not remove this selection problem.

Claude’s proposed 30-day outcomes also need a capture audit: post-discharge infection recurrence or readmission elsewhere is not automatically observable in MIMIC. Doubly robust estimators, negative controls, and E-values do not substitute for a defensible longitudinal causal design.

**What would verify it:** Define one therapy, eligibility, treatment strategies, time zero, rescue treatment, and observable outcomes. Audit readiness variables, longitudinal overlap, censoring, and effective sample size. Use known-mechanism experiments to test the method. Retain real-data causal claims only under explicitly defended assumptions; otherwise deliver a readiness predictor or supported-decision map.

### 3. Claude’s inverse modelling and Gemini’s ClinicianMirror: the proposed clinician state may not be recoverable

**Claim:** Public MIMIC data can recover stable clinician thresholds and separate baseline clinical utility from fatigue or crowding effects.

**Why overstated:** Provider attribution must first be established for the exact actions and release. A recorded provider identifier need not identify the clinician responsible for the decision.

More decisively, MIMIC’s patient-specific date shifting prevents naïve reconstruction of **actual department-wide simultaneous census across patients**. Time-of-day features are not a substitute for actual workload. Even with correct workload data, case mix, clinician assignment, and unrecorded findings can mimic a cognitive-load effect. Stable fitted thresholds establish reproducibility, not identification of preferences.

**What would verify it:** Audit identifiers, attribution, and temporal alignment before modelling. For crowding effects, obtain data preserving cross-patient simultaneity. Compare against case-mix-adjusted hierarchical action models and conduct assignment-confounding sensitivity analyses. Without those conditions, use the narrower description **“context-dependent recorded practice variation.”**

### 4. Gemini’s PhysioBreak-RSI, and partly Claude’s red team: a physiology engine is not a general clinical truth oracle

**Claim:** A mechanistic simulator supplies physiological truth or a sufficiently non-hackable reward for improving clinical decisions, including shock, hypoxia, and lethal drug interactions.

**Why overstated:** A simulator verifies consequences **inside its implemented equations, parameter range, and action interface**. It does not automatically model all advertised conditions or drug interactions. Optimizers can exploit those omissions. Plausible vital-sign traces do not establish valid treatment-response dynamics.

The feasibility claims are also unverified: millisecond simulation, simultaneous rollout/training infrastructure, and roughly 24-hour self-play experiments require measurement on the specified 16 GB laptop. Claude’s narrower counterexample search is more credible, but simulator-to-real transfer remains a separate hypothesis.

**What would verify it:** Select one implemented mechanism and audit its equations and action coverage. Benchmark simulation throughput, peak memory, and end-to-end training. Compare against random search, Bayesian optimization, and CMA-ES at equal simulator calls. Test held-out controllers and parameter regimes; reserve real-patient protection claims for independent evidence.

### 5. Claude’s Decision Fragility: analytic error and biological variation cannot simply be pooled as measurement noise

**Claim:** Perturbing observed labs using published analytic and biological coefficients of variation estimates the probability that measurement noise alone changes treatment.

**Why overstated:** Analytic imprecision, systematic device bias, pre-analytic error, and within-person biological change are different processes. A change over hours may represent genuine deterioration rather than noise. Published coefficients can depend on concentration, assay, population, and sampling interval. Independent perturbations can also destroy clinical correlations.

Moreover, sampling around an observed value is not automatically the posterior distribution of the patient’s true value. The proposed quantity is initially **decision sensitivity under an assumed error model**, not an empirically identified patient-specific probability.

**What would verify it:** Specify a measurement model with separate error components, justified correlations, and sensitivity ranges. Validate against paired measurements, quality-control data, or assay-specific evidence where available. Distinguish immediate repeat testing from later reassessment. Use the strongest probability language only where the measurement model is supported.

**Exclusion check:** None of these projects inherently violates the brief. ClinicianMirror would cross the boundary if its contribution became staffing or workforce redesign; contextual workload as a clinical covariate does not itself violate it. Likewise, active diagnostic inquiry is allowed, but procurement, reimbursement, or hospital-capacity optimization should not become its objective.

## 2. **Convergence verdict**

There is substantial **thematic convergence**, but limited evidence of independently discovered novelty. Stopping, inverse clinician modelling, decision-changing outputs, and mechanistic stress testing were explicitly suggested by the brief. Agreement on those themes is therefore mostly an attractor—not validation.

| Cluster | Converging proposals | Best variant |
|---|---|---|
| **Decision boundaries and stability** | Claude’s Decision Fragility; Gemini’s PivotDiff | **Decision Fragility**, with an explicit measurement model and a confirm/remeasure action. It has a cleaner estimand than a generated “safe discharge” boundary. These are related, not identical: noise robustness and counterfactual explanation answer different questions. |
| **Acquire evidence until sufficient** | Codex’s Decision-Sufficient MRI; Gemini’s Activebedside-TTT | **Decision-Sufficient MRI.** Retrospective k-space provides a much better-defined acquisition environment than imputing tests clinicians never ordered. Scanner deployment remains outside the POC. |
| **Stop rather than start** | Claude’s antibiotic stopping; Codex’s ventilation stopping; Gemini’s WeanJEPA | **Recovery Before Risk’s support-aware, two-tier design.** Known-mechanism evaluation plus an honest real-data support map is more defensible than claiming retrospective proof of safe de-escalation. |
| **Mechanistic adversarial evaluation** | All three advisors | **Counterexample Patient: insulin-controller red-teaming.** One physiological domain, bounded disturbances, concrete harm metrics, and held-out-controller transfer beat a general-purpose clinical simulator/LLM stack. |
| **Model clinician decisions** | Claude’s inverse decision modelling; Gemini’s ClinicianMirror | **Claude’s narrower descriptive threshold model**, conditional on attribution data. Recovering recorded decision variation is a tractable first question; identifying fatigue-induced irrationality is not. |

Two qualifications change my own ranking:

- **Decision-focused training needs a nontrivial decision problem.** For a binary label and fixed false-positive/false-negative costs, a calibrated probability plus the appropriate threshold is already Bayes-optimal. Claude’s objective flip needs finite-capacity benefits, uncertain harms, structured actions, or another concrete source of advantage—not a weak threshold baseline.
- **My joint-resistance proposal has an estimand problem.** When choosing one antibiotic and evaluating only its activity plus a drug-specific spectrum penalty, expected utility depends on marginal susceptibility probabilities. Joint dependence matters directly for combinations, contingent switching, or other coupled decisions. Otherwise, any benefit is a shared-modelling benefit, not proof that joint possibilities were necessary.

The strongest convergence signal is thus methodological: **make the action and evaluation environment precise before adding frontier architecture.**

## 3. **Socrates: the single most over-rated idea**

### Gemini’s **PivotDiff**

Its rank as the best project rests on this assumption:

> A plausible explanation of where a model changes its recommendation is a clinically valid boundary for changing patient management.

That assumption fails even with a perfect counterfactual generator. The generator may faithfully expose a wrong classifier. It can also produce unstable boundaries when several correlated features offer interchangeable routes across the decision surface.

This creates a damaging evaluation loop: train a decision model, generate changes that flip it, and count successful flips as evidence of useful clinical guidance. Clinician concordance helps, but does not establish safety or treatment benefit.

**The decisive test:** Construct cases where the model’s recommendation conflicts with an independently specified clinical criterion. Does PivotDiff expose the disagreement, or confidently verbalize the model’s mistake as a discharge instruction?

I would retain it only as **decision-boundary auditing**, compare diffusion against strong constrained search, and remove patient-facing instructions from the MVP. That is a legitimate project, but substantially smaller than the advertised clinical transformation.

## 4. **Most under-rated**

### Gemini’s **Activebedside-TTT**

Ranked fourth, it contains one of the best clinical questions:

> What additional evidence is worth obtaining before acting?

Unlike another risk score, this directly selects a clinical action. Its weak point is not the flip; it is the proposed retrospective environment and oversized world-model stack.

I would merge it with **Claude’s Decision Fragility** into **“Remeasure Before Acting.”**

- **Scope:** One noisy laboratory measurement and one prespecified decision.
- **Actions:** Act, request confirmation, or defer the automated recommendation.
- **Method:** Estimate which uncertainty is action-relevant, then select repeat measurement only when its expected decision value exceeds a prespecified delay or burden penalty.
- **ML contribution:** A decision-aware uncertainty representation and acquisition policy—not necessarily a billion-parameter language model.
- **Baselines:** Distance-to-threshold, conventional uncertainty sampling, analytical value-of-information where tractable, and a small supervised policy.
- **Evidence:** Paired measurements where available; otherwise explicitly labelled simulation under audited measurement-error assumptions. A second draw from the same arbitrary perturbation distribution is not independent clinical validation.

For broader test ordering, `charttime` and `storetime` must not be treated as universal order and result-availability timestamps without table-specific verification. Complete-workup cohorts can support a restricted retrospective experiment, but do not remove selection bias or reveal outcomes under earlier treatment.

This merger preserves the scientific ambition while avoiding unsupported “35% fewer tests” and faster-treatment claims.

## 5. **Final top 3**

Scores concern the **proposed contribution if successful**, not established novelty or demonstrated patient benefit. Finish probabilities are subjective planning estimates for a defensible nine-month POC, assuming authorized dataset access; they are not clinical-success probabilities.

| # | Project | Flip | Novelty (1–5) | Clinical impact (1–5) | ML depth (1–5) | POC finish confidence (%) | Data gate | Why |
|---|---|---|---:|---:|---:|---:|---|---|
| **1** | **Remeasure Before Acting** — Decision Fragility plus selective confirmation | Treat inputs as uncertain evidence; decide whether another measurement is needed before acting | **3** | **4** | **4** | **80%** | One defensible assay-error model; sufficient relevant cases; material instability under plausible assumptions. Paired-measurement validation is preferred; otherwise conclusions remain simulation-based. | Best balance of clinical interpretability, manageable compute, early falsification, and a genuine action output. Robust training plus selective acquisition makes it more than a perturbation dashboard. |
| **2** | **Counterexample Patient** — constrained insulin-controller red-teaming | Search for plausible failures instead of optimizing average performance | **3** | **3** | **4** | **80%** | Working simulator/controller interfaces; adequate CPU throughput; clinically defensible disturbance bounds; failures not already saturated by simple search | Cleanest ambitious experimental environment. Equal-budget search comparisons and held-out-controller transfer offer strong falsification without pretending to identify real-patient treatment effects. |
| **3** | **Decision-Sufficient MRI** | Acquire evidence for a pathology decision, not image similarity alone | **4** | **4** | **5** | **60%** | Linkable k-space and pathology labels; adequate patient-disjoint positives; useful full-data classifier; fixed-mask pilot showing a decision–measurement trade-off | Strongest representation-learning project, but data linkage, acquisition constraints, and reconstruction compute make it less finishable than my round-one ranking implied. JEPA must earn its place against task-driven sampling. |

### Moonshot pick: **Decision-Sufficient MRI**

Pursue an acquisition-and-stopping policy that preserves pathology sensitivity under realistic sampling constraints. The moonshot is the demonstrated **decision–measurement frontier**, not assuming scanner-time savings or clinical equivalence.

### Safe ambitious pick: **Remeasure Before Acting**

Start with one assay and one action. Establish a defensible uncertainty model and a meaningful instability burden before building the acquisition policy. If realistic error rarely changes relevant decisions, stop early rather than inflate the perturbations.

**Final recommendation:** Choose **Remeasure Before Acting** for the strongest medicine–engineering thesis balance. Choose **Decision-Sufficient MRI** if the month-one data and compute gates pass and the student prioritizes representation-learning depth over finish confidence.