# Clinical decision models: five scientific flips, ranked

## Part A — Which assumptions deserve flipping?  
*105 words*

A plain predictor assumes: the disease label is the right objective; today’s measurements are sufficient; uncertainty should become a probability rather than another measurement; intervention effects resemble observed outcomes; and one held-out dataset adequately tests decisions. Scientifically valuable flips are to learn **when evidence is sufficient**, preserve **action-relevant rather than reconstructive information**, search for **patients that falsify a decision**, optimize **joint treatment consequences**, and model **stopping rather than starting**. Merely renaming a risk score “decision intelligence,” adding explanations, thresholding an unchanged classifier, or wrapping it in an agent is relabelling. Predicting clinicians’ actions is not automatically learning good clinical decisions; generating counterfactual patients is not automatically identifying treatment effects.

## Evidence and feasibility rules

- These are **ranked research proposals**, not claims of established novelty. Prior art establishes the bar; a current literature search must establish the remaining gap.
- Parameter counts are proposed architectures. All runtime estimates are **[UNVERIFIED planning estimates]**, assuming mixed precision, small batches, and sequential experiments on the specified laptop.
- Public retrospective data and simulators can establish methodological results—not improved patient outcomes. Thai transportability is **[UNVERIFIED]** without Thai validation.
- Each project follows the same nine-month structure: month 1 feasibility gate; months 2–3 data and strong baselines; months 4–6 method development; months 7–8 locked evaluation and ablations; month 9 thesis and reproducibility.

---

## #1 — Decision-Sufficient MRI: acquire evidence until the clinical decision stabilizes

### 1. Name, flip, and pitch

**Normal:** “How accurately can we reconstruct a fully sampled image?”  
**Flipped:** “Which additional measurement could still change the lesion-review decision—and when can acquisition stop?”

Develop an adaptive acquisition model whose latent representation preserves evidence for a specific pathology decision, rather than optimizing image similarity alone.

### 2. Paradigm and research question

**Paradigm:** decision-conditioned JEPA plus sequential acquisition and calibrated stopping.

**Falsifiable RQ:** On held-out knee MRI examinations, can decision-conditioned acquisition use **at least 20% fewer phase-encoding lines** than the strongest fixed-mask baseline at **matched ≥95% empirical sensitivity for meniscal-tear review**, without reducing specificity by more than two percentage points?

Compare:

1. Fixed masks plus reconstruction and classification.
2. Reconstruction-driven adaptive acquisition.
3. Task-driven acquisition without JEPA.
4. Proposed decision-conditioned JEPA, with identical acquisition budgets and backbone sizes.

Report sensitivity with patient-level confidence intervals, specificity, acquired-line fraction, and performance by tear subtype. A calibrated stopping rule must be evaluated as a **whole sequential policy**; repeatedly applying an ordinary confidence threshold does not establish a stopping guarantee.

### 3. Clinical relevance

**Intended beneficiary:** patients undergoing knee MRI and clinicians interpreting suspected meniscal pathology. The direct model action is **acquire another line or stop the experimental acquisition sequence and flag for review**.

Clinical relevance is measured through missed annotated tears and unnecessary review flags. Acquired-line reduction is an acquisition proxy—not proof of shorter complete examinations or equivalent clinical diagnosis. Thai usefulness is **[UNVERIFIED]**; no Thai disease-prevalence assumption is necessary.

### 4. POC/MVP

- **Data:** [fastMRI](https://arxiv.org/abs/1811.08839), linked to [fastMRI+ pathology annotations](https://github.com/microsoft/fastmri-plus).
- **Scope:** one knee sequence and one pathology family; patient-disjoint splits. Start with a restricted, explicitly retrospective acquisition emulator—not scanner deployment.
- **Models:** 2D reconstruction network approximately **8M parameters**; JEPA encoder approximately **6M**; acquisition/stopping head below **0.5M**. Train stages separately, freezing reconstruction initially.
- **Compute:** approximately **180–300 GPU-hours**, with cached low-resolution reconstructions and batch sizes of 1–4.
- **Nine-month proof:** a reproducible decision–measurement frontier and an ablation showing whether the representation objective adds value beyond supervised task-driven sampling.

### 5. Prior art to beat

Adaptive MRI acquisition already exists: [active-mri-acquisition](https://github.com/facebookresearch/active-mri-acquisition). Strong reconstruction baselines include [End-to-End Variational Networks](https://arxiv.org/abs/2004.06688). [Conformal Risk Control](https://arxiv.org/abs/2208.02814) supplies relevant calibration machinery, not automatic validity for arbitrary adaptive stopping.

**Novelty burden:** demonstrate better decision sufficiency, not simply another adaptive sampling policy.

### 6. Socratic stress-test

**Decisive assumption:** the selected pathology decision becomes reliable substantially before full acquisition, and the annotations support examination-level evaluation.

**Month-1 test:** link at least **100 positive and 200 negative examinations**, train a full-data baseline, and evaluate fixed acquisition fractions. **Kill or change pathology** if the full-data model has AUROC below **0.85**, or if no reduced-data setting saves **≥15% of lines** while staying within **three sensitivity points** of the full-data model at matched specificity.

---

## #2 — Counterexample Patient: try to break an insulin decision before trusting it

### 1. Name, flip, and pitch

**Normal:** “Which insulin controller has the best average glucose outcomes?”  
**Flipped:** “Which plausible patient trajectory makes this controller fail—and does that failure transfer to another controller?”

Build a physiological adversary that searches for clinically interpretable combinations of meals, insulin sensitivity, and sensor disturbance, rather than generating unconstrained adversarial inputs.

### 2. Paradigm and research question

**Paradigm:** constrained adversarial reinforcement learning over a mechanistic patient simulator, with held-out-controller transfer.

**Falsifiable RQ:** With the same simulator-call budget and disturbance envelope, does a learned adversary discover **≥1.5 times as many severe-hypoglycaemia episodes** as the better of random search and CMA-ES, including on an unseen controller?

Predefine an episode as simulated glucose below **54 mg/dL for at least 15 consecutive minutes**. The duration is a study definition; glucose thresholds and time-in-range metrics follow the [international consensus](https://doi.org/10.2337/dci19-0028).

Report event-discovery rate, time below range, time in range, scenario plausibility, and transfer—not just adversarial reward.

### 3. Clinical relevance

**Intended beneficiary:** people with type 1 diabetes using automated insulin delivery. The tested clinical action is insulin dosing; the contribution is a stronger **preclinical test of dosing decisions**.

This project proves failure discovery in a simulator, not clinical protection. Applicability to Thai patients, meals, and device use is **[UNVERIFIED]** and must not be inferred from simulator success.

### 4. POC/MVP

- **Data/environment:** open-source [simglucose](https://github.com/jxx123/simglucose), with its documented virtual-patient model.
- **Controllers:** a reproducible basal–bolus baseline, a simple predictive controller, and a held-out controller.
- **Models:** constrained PPO adversary approximately **0.3–1M parameters**; optional shared patient-history encoder below **1M**.
- **Compute:** approximately **20–60 GPU-hours**; CPU simulator throughput may dominate. Benchmark it in week 1.
- **Nine-month proof:** a frozen scenario generator that finds transferable failures within a prespecified physiological envelope, plus a catalogue of mechanisms such as delayed meals or sensitivity changes. No hardware or patient experiment is required.

### 5. Prior art to beat

Adversarial disturbance training is established: [Robust Adversarial Reinforcement Learning](https://arxiv.org/abs/1703.02702). A strong non-neural search baseline is [CMA-ES](https://arxiv.org/abs/1604.00772).

**Novelty burden:** constrained, interpretable, cross-controller failure discovery—not “RL finds bad cases.”

### 6. Socratic stress-test

**Decisive assumption:** the discovered failures represent plausible physiological interactions rather than simulator loopholes.

**Month-1 test:** generate 30 candidate scenarios and obtain blinded clinical review. Require **≥27/30** to be judged plausible under explicitly stated assumptions. On held-out seeds, require optimized search to find **≥1.5 times** the failures found by random search at equal calls. **Kill or tighten the scope** if either condition fails; do not expand the disturbance envelope merely to manufacture failures.

---

## #3 — Pathology-or-Sensor? A decision-preserving alarm representation

### 1. Name, flip, and pitch

**Normal:** “Does this waveform contain a dangerous rhythm?”  
**Flipped:** “Is the apparent danger physiological, a corrupted sensor, or unresolved disagreement requiring another channel?”

Learn a representation that changes when clinically important rhythm evidence changes, but remains stable when an irrelevant channel is corrupted. Its output is **confirm, suppress, or request additional signal review**.

### 2. Paradigm and research question

**Paradigm:** multiview JEPA with selective nuisance invariance and action-conditioned abstention.

**Falsifiable RQ:** At **≥95% empirical sensitivity for annotated true alarms**, does the proposed representation improve false-alarm rejection by **≥10 percentage points** over a supervised multichannel model receiving the same data augmentations?

Compare against ECG-only classification, supervised multichannel fusion, masked reconstruction, and JEPA without decision-preservation losses. Evaluate clean records, held-out artifact types, and missing-channel conditions.

Crucially, if all channels lose diagnostic information, the correct action is **defer**, not an invariant confident prediction.

### 3. Clinical relevance

**Intended beneficiary:** monitored patients whose rhythm alarms require rapid interpretation. The clinical endpoint proxy is missed true alarms; the secondary measure is false alarms rejected at matched true-alarm sensitivity.

The [PhysioNet 2015 Challenge](https://physionet.org/content/challenge-2015/1.0.0/) provides annotated alarm events and associated signals. Its labels do **not** establish whether an intervention was necessary or whether suppressing an alarm improves outcomes. Thai transfer is **[UNVERIFIED]**.

### 4. POC/MVP

- **Data:** labelled public Challenge 2015 records; independent ECG pretraining using [MIT-BIH Arrhythmia](https://physionet.org/content/mitdb/1.0.0/); controlled artifact tests using the [MIT-BIH Noise Stress Test Database](https://physionet.org/content/nstdb/1.0.0/).
- **Models:** separate ECG and pulse-wave encoders totaling approximately **3–5M parameters**; cross-channel latent predictor approximately **1M**; three-action head below **0.1M**.
- **Compute:** approximately **60–120 GPU-hours**, using one-dimensional signals rather than large language models.
- **Nine-month proof:** decision-preserving invariance under prespecified corruptions, with an explicit abstention frontier.
- Use patient-disjoint splits where identifiers permit; otherwise disclose record-level splitting and possible residual dependence. The small labelled cohort limits subtype claims.

### 5. Prior art to beat

The Challenge already established multichannel alarm discrimination as a task; its published overview is [Clifford et al., 2016](https://doi.org/10.1088/0967-3334/37/8/E5). Predictive latent representations themselves are not novel: [I-JEPA](https://arxiv.org/abs/2301.08243).

**Novelty burden:** show that selective invariance preserves true pathology better than ordinary augmentation and fusion.

### 6. Socratic stress-test

**Decisive assumption:** another channel contains recoverable information when one channel becomes misleading.

**Month-1 test:** compare simple ECG-only and multichannel classifiers on locked validation records. If multichannel input improves false-alarm rejection by **less than five percentage points** at matched **≥95% sensitivity**, **kill the cross-channel method or narrow to an alarm subtype**. Without complementary evidence, a sophisticated latent model has little to exploit.

---

## #4 — Antibiotic Decisions from Joint Possibilities, Not Independent Resistance Scores

### 1. Name, flip, and pitch

**Normal:** “What is the probability this organism resists each antibiotic?”  
**Flipped:** “Across plausible joint susceptibility patterns, which treatment choice remains microbiologically defensible?”

Learn a joint susceptibility distribution and select among a small, clinically prespecified antibiotic set, rather than independently thresholding resistance predictions.

### 2. Paradigm and research question

**Paradigm:** partially observed categorical generative modelling plus risk-controlled, decision-focused selection.

**Falsifiable RQ:** Among eligible bloodstream isolates with complete reference panels, can the joint model reduce a prespecified antibiotic-spectrum score by **≥10%** relative to independent calibrated resistance models, while keeping the selected-drug nonsusceptibility rate **≤5% empirically**?

Compare:

1. Population susceptibility frequencies.
2. CatBoost per-drug predictions.
3. Independent neural predictions with the **same decision rule**.
4. Joint model with decision-focused training.

Report nonsusceptibility with confidence intervals, decision coverage, spectrum score, and results under panel-missingness shifts. The spectrum score is a clinician-defined study construct, not a universal ordering of antibiotics.

### 3. Clinical relevance

**Intended beneficiary:** patients with identified Gram-negative bloodstream organisms while susceptibility results remain pending. The action is antibiotic selection from a constrained candidate set.

Use microbiological activity as the endpoint—not cure, mortality, or treatment-effect claims. Allergy, infection source, dosing, and organ function constrain real prescribing; the POC must not imply autonomous prescribing.

Potential Thai relevance is locally different susceptibility patterns **[UNVERIFIED for this project]**. US-trained probabilities cannot be assumed applicable in Thailand.

### 4. POC/MVP

- **Data:** [MIMIC-IV microbiology and prior clinical history](https://doi.org/10.1038/s41597-022-01899-x).
- **Scope:** one organism family and three antibiotics selected after a panel-availability audit. Deduplicate episodes and split chronologically by patient.
- Simulate a **post-identification/pre-susceptibility snapshot** with organism identity explicitly supplied. Do not pretend specimen timestamps prove when clinicians actually knew the organism.
- **Models:** masked categorical transformer or discrete denoising model approximately **1–3M parameters**; small decision head.
- **Compute:** approximately **40–100 GPU-hours**.
- **Nine-month proof:** whether modelling susceptibility dependence improves actual drug selection beyond equally calibrated independent models. Evaluate only where reference susceptibility is observed; do not label untested drugs susceptible.

### 5. Prior art to beat

Patient-history prediction of resistance is established: [Yelin et al., 2019](https://doi.org/10.1038/s41591-019-0503-6). Risk calibration can draw on [Conformal Risk Control](https://arxiv.org/abs/2208.02814).

**Novelty burden:** a joint-distribution advantage for decisions under incomplete panels—not another resistance AUROC improvement.

### 6. Socratic stress-test

**Decisive assumption:** routine testing leaves enough jointly observed susceptibility information to evaluate competing choices without inventing labels.

**Month-1 test:** require **≥500 independent complete-panel episodes**, including **≥50 episodes nonsusceptible to the least-broad candidate**, and audit whether complete-panel patients differ materially from others. **Kill or restrict the target population** if counts fail or complete-panel status is predicted from baseline features with AUROC **>0.80**. That threshold flags serious selection concerns; it does not prove their absence below 0.80.

---

## #5 — Recovery Before Risk: learning when ventilation can stop

### 1. Name, flip, and pitch

**Normal:** “Who is likely to deteriorate or fail extubation?”  
**Flipped:** “For whom would another six hours of ventilation improve the outcome enough to justify waiting?”

Develop a support-aware model of **extubate now versus continue temporarily**, with explicit uncertainty about counterfactual outcomes. This is the most clinically ambitious idea—and the least identifiable from routine data.

### 2. Paradigm and research question

**Paradigm:** action-conditioned state-space world model, target-trial emulation, and sensitivity-aware abstention.

Because real counterfactuals are unavailable, use two evidential tiers:

- **Primary methodological RQ:** in semi-synthetic experiments using real patient histories and known treatment-response mechanisms, does support-aware abstention reduce policy regret by **≥10%** versus a causal-transformer baseline at matched **70% decision coverage**?
- **Real-data analysis:** estimate associations and supported decision regions for extubation now versus six-hour delay. Prespecify reintubation/death within 48 hours and ventilation exposure over 72 hours as study outcomes.

No real-data result establishes treatment benefit without additional causal assumptions.

### 3. Clinical relevance

**Intended beneficiary:** patients approaching liberation from invasive ventilation. The relevant competing outcomes are failed liberation and unnecessary continued ventilation.

Thai ICU applicability is **[UNVERIFIED]**. The project should be presented as counterfactual-method development, not a validated extubation recommendation system.

### 4. POC/MVP

- **Data:** MIMIC-IV; exploratory external variable mapping in [eICU](https://doi.org/10.1038/sdata.2018.178), not assumed interchangeable.
- **Design:** repeated hourly eligibility landmarks; include all eligible patients at each landmark rather than selecting patients based on later successful extubation. Distinguish planned extubation from other ventilation cessation wherever records permit.
- **Models:** action-conditioned GRU or compact state-space model approximately **2–4M parameters**; causal-transformer baseline approximately **3M**; small propensity and outcome heads.
- **Compute:** approximately **80–160 GPU-hours**.
- **Nine-month proof:** calibrated counterfactual uncertainty under controlled mechanisms, plus an honest map of where the clinical data cannot support the decision.

### 5. Prior art to beat

Time-varying counterfactual modelling includes [Counterfactual Recurrent Networks](https://arxiv.org/abs/2002.04083) and [Causal Transformer](https://arxiv.org/abs/2204.07258). Study design should follow target-trial principles: [Hernán and Robins, 2016](https://doi.org/10.1093/aje/kwv254).

**Novelty burden:** detecting unsupported decisions and surviving omitted-confounder stress—not merely fitting another treatment-conditioned predictor.

### 6. Socratic stress-test

**Decisive assumption:** the chart captures enough readiness information to make “extubate versus wait” comparisons meaningful.

**Month-1 test:** audit at least 100 eligible episodes. Require usable consciousness/sedation and respiratory-readiness variables in **≥80%**, plus estimated treatment propensities between **0.1 and 0.9 for ≥70%** of the proposed target population. **Abandon causal recommendation claims** if either gate fails. Airway protection and clinician judgement remain possible unmeasured confounders even if both gates pass; the defensible pivot is a noncausal readiness-uncertainty model.

---

If I were the student I'd pick #1

It offers a genuine perception-to-action flip, strong public-data evaluation, and frontier representation learning without making unidentifiable claims about treatment benefit.