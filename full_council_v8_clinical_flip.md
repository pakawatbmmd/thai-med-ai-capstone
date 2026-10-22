# Capstone Council v8: Clinical / scientific flips on decision models (Claude × Codex × Gemini, philosopher-council, 2026-10-22)

**Brief:** `council_v8_clinical_flip/brief.md`. The same "flip the perspective" frame as v7, but **clinical, scientific or model-development only**. It excludes payer, HTA, legal, credentialing, payment and system routing.

**Models:**
- Claude, in the cloud session.
- Codex: `gpt-6.1-sol`, high effort, via the OpenAI API.
- Gemini: `gemini-4-argon` via the Gemini API.

Codex and Gemini ran through `tools/run_council.py`. Each Round 1 was independent; each Round 2 saw all three Round 1s but no Round 2.

## Synthesis (Claude, after all six files)

**Which projects reached each advisor's Round 2 top 3**

| Project | Claude R2 | Codex R2 | Gemini R2 | Verdict |
|---|---|---|---|---|
| **Remeasure Before Acting / Decision Fragility**: how likely measurement error alone flips a model's decision, and *whether to confirm with a repeat test before acting* (Claude #1 + Gemini #4 active inquiry; Codex's merge) | #2 + safe ambitious | **#1** + safe ambitious + final recommendation | #3 (merged with PivotDiff) | **The only project in all three top 3s.** Finish confidence 80 / 80 / 85%. |
| **Joint antibiotic decision model**: choose the narrowest still-active empiric antibiotic from a joint susceptibility model, trained on the decision (Codex #4 + Claude #2) | **#1** | not in top 3; Codex raised an estimand problem with its own idea | #2 + safe ambitious (92%) | **Strong, with one fix needed** (below). Claude and Gemini both named it most under-rated. |
| **Physiological red team**: constrained adversarial search for failures in a mechanistic simulator, with cross-model transfer (Codex #2 + Claude #5 + Gemini #3) | moonshot | #2 | **#1** (88%) | Consensus as a rigorous ambitious option. The simglucose / type 1 diabetes setting is weak for Thailand; a sepsis or haemorrhage model in Pulse is better. |
| Stop / de-escalation (extubation, vasopressors, antibiotics) | #3 | (endorsed only as two-tier design) | moonshot | High stakes; identifiable only with Codex's semi-synthetic + support-map design |
| Decision-sufficient MRI | – | #3 + moonshot | – | Codex only; weak Thai relevance |

**Cross-critique**
- **Most over-rated:**
  - **Gemini's PivotDiff** (Claude and Codex): a counterfactual shows *the model's* boundary, not a safe clinical boundary, so it must not become patient discharge instructions.
  - **Inverse modelling of clinicians** (Gemini): unrecorded bedside findings look like "clinician bias", and MIMIC lacks reliable provider attribution.
- **Most under-rated:** the joint antibiotic model (Claude, Gemini); Gemini's active bedside inquiry (Codex, which merged it into Remeasure Before Acting).
- **Corrections all three now accept:**
  - "Train for the decision, not the label" adds nothing for a single binary action with fixed costs, because a calibrated probability at the Bayes threshold is already optimal (Gemini, Codex). It needs a structured or joint decision.
  - **Codex on its own joint antibiotic idea:** if the action is one drug, scored by its own activity plus a drug-specific spectrum penalty, expected utility depends only on *marginal* susceptibilities. Joint dependence matters only for **combinations or contingent plans** (start drug A, switch to B when results arrive). **Fix:** define the action as an *empiric regimen plus its de-escalation/escalation contingency*, which is where joint resistance patterns (ESBL, AmpC, carbapenemase) truly matter.
  - **Decision fragility (Codex):** analytic error, bias, pre-analytic error and biological variation are different processes. The honest quantity is *decision sensitivity under a stated measurement model*, validated against paired or repeat measurements where possible.

**The council's answer**
1. **Safe ambitious, consensus:** *Remeasure Before Acting*. Pick one noisy lab and one decision. The model either acts, asks for a confirmatory repeat test, or defers, depending on whether the uncertainty is decision-relevant. It uses public data and the laptop, and has a falsifiable month-1 gate: *is the decision materially unstable under a defensible error model?*
2. **Highest clinical impact:** *Joint antibiotic regimen model*, re-specified as regimen + contingency so that joint resistance genuinely matters. Thai extension: a hospital's own microbiology data.
3. **Most rigorous ML environment:** *Physiological red team* on a Thai-relevant decision model.

---

# ROUND 1

## CLAUDE: Round 1

**Brief:** `council_v8_clinical_flip/brief.md`. Descartes proposes, Hume audits, Socrates stress-tests. No new deep research was done for this round, so [UNVERIFIED] marks claims to check.

**Opening position (Descartes).** A plain clinical prediction model is built in four silent steps:
1. predict a label;
2. score accuracy;
3. pick a threshold afterwards;
4. assume the inputs are exact and the clinician is a passive executor.

Each step hides a scientific question about *decisions*. Flipping any one of them gives a model-development contribution with no system, legal or payment layer. The test of a real flip: **the new object must be measurable, and it must disagree with the plain model on some patients in a way a clinician cares about.**

### 1. Decision Fragility: would measurement noise alone flip this patient's treatment? (flip: inputs are exact → inputs are uncertain measurements)
- **Pitch:** Every lab value has analytic and biological variation. For each patient, estimate the **probability that the model's decision flips purely because of measurement noise**: creatinine ±5%, lactate, troponin, point-of-care glucose. Use that probability as a first-class output: *decision fragility*.
- **Paradigm & research question:** Uncertainty propagation through clinical decision models (Monte Carlo over published analytic and biological CVs, plus learned surrogates for speed), and **fragility-aware training**. *What fraction of decisions made by published or replicated clinical models (sepsis alerts, AKI staging-triggered actions, ED disposition) are fragile (flip probability >10%) under realistic measurement error? Does fragility-aware training reduce fragile decisions without losing decision quality?*
- **Clinical / Thai relevance:** Point-of-care devices and rural labs have wider analytic error than central labs [UNVERIFIED magnitude for Thai รพ.สต. devices]. The same model is more fragile in exactly the settings with the fewest doctors. The finding is clinical and scientific (which decisions rest on noise), not policy.
- **POC:** MIMIC-IV and eICU; 3–4 decision models (replicated or published scores); CVs from the EFLM biological-variation database [check access]; a fragility estimator plus a fragility-aware objective. Laptop-only, ~30–80 GPU-hours.
- **Prior art to beat:** Input-uncertainty propagation in clinical ML; robustness to measurement noise; selective prediction. The "fragility index" name is already used for RCT results (Walsh 2014), so it needs a distinct name. To check: whether per-patient decision-flip probability under *lab-specific* CVs has been reported [negative search pending].
- **Socratic test:** *Realistic measurement noise moves decisions often enough to matter.* Month 1: on one model (e.g., AKI-triggered nephrotoxin hold), compute flip rates. **Kill** if fewer than 2% of decisions have flip probability above 10%.

### 2. Train for the decision, not the label: decision-focused learning for a clinical action (flip: objective)
- **Pitch:** Plain models are trained on cross-entropy and thresholded afterwards. Instead, train end-to-end on the **clinical decision loss**: the regret of giving or withholding the action, given asymmetric harms. Show where the two disagree.
- **Paradigm & research question:** Decision-focused learning / predict-then-optimise (SPO+-style surrogate losses, Elmachtoub & Grigas; Wilder et al.) applied to a clinical action, e.g. early antibiotics in suspected sepsis, ICU admission from ED, or imaging in minor head injury. *At matched AUROC, does decision-focused training reduce decision regret (and the high-harm error type) versus predict-then-threshold, and does the advantage survive calibration shift between hospitals?*
- **Clinical relevance:** The patients where the two models disagree are a clinically interpretable set ("near the threshold, high-harm"), worth showing to clinicians.
- **POC:** MIMIC-IV-ED to eICU (hospital shift). Gradient boosting + MLP baselines vs a decision-focused head. Harms elicited from 3–5 clinicians as ranges, with sensitivity analysis over them. ~40–80 GPU-hours.
- **Prior art to beat:** Decision-focused learning (mostly operations research); decision curve analysis (Vickers); cost-sensitive learning. Clinical applications of decision-focused learning are sparse [UNVERIFIED].
- **Socratic test:** *A real gap exists between predict-then-threshold and decision-focused training on clinical data.* Month 1: one task, both pipelines. **Kill** if regret differs by less than the bootstrap CI at every harm ratio clinicians consider plausible.

### 3. Model the doctor, not the disease: inverse decision modelling of clinical practice (flip: subject)
- **Pitch:** Rather than predicting outcomes, **recover the implicit decision rules clinicians actually use**: the risk threshold at which they order a CT, start antibiotics or admit. Then measure how those thresholds vary between clinicians, shifts and patient groups, and where they diverge from guidelines.
- **Paradigm & research question:** Inverse decision modelling / inverse RL with bounded rationality (Jarrett & van der Schaar, "Inverse Decision Modeling", ICML 2021 [UNVERIFIED citation details]). *Can implicit per-clinician thresholds be identified stably from routine data (test–retest across time splits)? Do they shift systematically with time of shift, crowding or patient characteristics?*
- **Clinical relevance:** Scientific insight into practice variation and possible bias. It feeds decision-support design without policy. A Thai version could use KCMH ED data under IRB later.
- **POC:** MIMIC-IV-ED, which has provider identifiers [check availability]. Choose one decision (CT head, blood cultures). Fit an outcome model plus an inverse decision model. Report threshold distributions and stability. Mostly CPU, some GPU.
- **Prior art to beat:** Practice-variation studies (regression-based); inverse RL in healthcare; "learning what clinicians value" papers.
- **Socratic test:** *Thresholds are identifiable, not confounded by unrecorded information.* Month 1: split each clinician's cases in half. **Kill** if the test–retest correlation of estimated thresholds is r < 0.5.

### 4. When is enough? Individualised stopping rules for antibiotic courses (flip: direction, start → stop)
- **Pitch:** Most models decide when to *start* treatment. Flip to **when to stop**: estimate, per patient and per day, the effect of stopping antibiotics now versus continuing, using a target trial emulated on ICU data.
- **Paradigm & research question:** Causal ML for dynamic treatment regimes: clone-censor-weight target trial emulation plus heterogeneous effects (causal forests / DR-learner). *Can an individualised stopping rule, evaluated with doubly robust off-policy estimates, shorten courses for a defined subgroup without worse 30-day outcomes, compared with fixed 7-day and 5-day rules?*
- **Clinical relevance:** Antimicrobial stewardship is a clinical priority everywhere, including Thai hospitals with high resistance [UNVERIFIED local data]. The contribution is a stopping model, not a policy.
- **POC:** MIMIC-IV (antibiotic administration plus culture data); emulated trial; sensitivity analyses (E-values, negative controls). Mostly CPU.
- **Prior art to beat:** RCTs on short vs long courses (many infections); offline-RL-for-treatment critiques (Luo et al., ICML 2024); target trial emulation literature.
- **Socratic test:** *There is enough natural variation in stop days, with overlap, to identify effects.* Month 1: check overlap of stop-day distributions within strata. **Kill** if fewer than 15% of patients have overlap in their stop-day propensities.

### 5. Stress-test decision models with mechanistic patients: a physiology-engine red team (flip: evaluation)
- **Pitch:** Held-out test sets only contain patients who happened to occur. Generate **mechanistically plausible patients** with an open physiology engine (e.g. the Pulse Physiology Engine [check licence]): haemorrhage, sepsis-like states, drug effects. **Search for the inputs where a clinical decision model makes the wrong call**, then use those failures as a training curriculum.
- **Paradigm & research question:** Simulation-based falsification / adversarial testing of clinical models, with mechanism-informed counterexample search (Bayesian optimisation over physiological parameters). *Does mechanistic red-teaming find failure modes that a large held-out set misses? Does a curriculum built from them improve real-data robustness on eICU (cross-hospital)?*
- **Clinical relevance:** Clinicians can read the failures ("model misses compensated shock in young patients"), which makes them clinically actionable.
- **POC:** Pulse + 2 early-warning or vital-sign decision models trained on MIMIC; a counterexample search loop; a curriculum retrain; an eICU external test. ~50–100 GPU-hours plus CPU simulation.
- **Prior art to beat:** Simulation-based testing in autonomous driving; adversarial robustness in clinical ML; physiological simulators for ventilator or anaesthesia research.
- **Socratic test:** *Simulated physiology is close enough to real vital-sign dynamics that the failures transfer.* Month 1: generate 200 haemorrhage trajectories and compare their vital-sign statistics with matched MIMIC cases. **Kill** if a simple classifier separates sim from real at AUROC > 0.95 *and* no simulated failure reproduces on real data.

---

**If I were the student, I'd pick #1, Decision Fragility.**
- It is a genuinely new *object*: per-patient decision-flip probability under real measurement error.
- It needs only public data and a laptop.
- Its first result is a clinically striking number in month 1 ("X% of these model-driven decisions rest on noise").
- It has a natural Thai, clinical, non-policy angle: point-of-care devices in rural care.

**#2 (decision-focused learning)** is the most ML-heavy alternative. **#3 (inverse decision modelling)** is the most scientifically surprising if identifiability holds.

## CODEX (gpt-6.1-sol): Round 1

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

## GEMINI (gemini-4-argon): Round 1

### Part A: The Scientific Flips vs. Cosmetic Relabelling

A plain clinical prediction model $P(Y \mid X)$ hides five defective assumptions:
1. **Passive observation:** features $X$ arrive for free, rather than being actively acquired under clinical time/harm constraints.
2. **Label-action isomorphism:** predicting an outcome $Y$ equals knowing the optimal intervention $a$, ignoring treatment-induced distribution shift.
3. **Unidirectional escalation:** decisions only *start* therapy or *admit*, treating *stopping* or *de-escalating* as a trivial inverse.
4. **Point-mass sufficiency:** outputting a scalar risk score rather than the *minimal clinical evidence required to flip the action*.
5. **Static i.i.d. evaluation:** testing on historical snapshots rather than adversarial physiological trajectories.

**Cosmetic relabelling to avoid:** Rewriting $P(Y \mid X)$ as $1 - P(Y \mid X)$ and calling it a "rule-out model", applying standard post-hoc SHAP values as "decision explanation", or merely adjusting a softmax decision threshold for "regret".

---

### Part B: Five Flipped Decision-Model Proposals (Ranked)

#### 1. Decision-Boundary Flip (Action-Reversal Counterfactuals via Discrete Diffusion)
1. **Name, the flip, and pitch:** **PivotDiff** — *From "What is this patient's risk score?" to "What is the minimal physiological or history change that would flip the clinical action from discharge to admit (or vice-versa)?"* Instead of a scalar probability that clinicians ignore or miscalibrate, the model outputs the exact, clinically plausible boundary condition (e.g., *"Safe to observe at home UNLESS lactate rises above 2.4 mmol/L or patient has unstated history of cirrhosis"*).
2. **Paradigm and research question:** **Discrete Diffusion Language/Tabular Models + Counterfactual Decision Analysis.** 
   * **RQ:** Does a masked discrete diffusion model trained to generate minimal, physiologically valid action-flipping perturbations achieve higher clinician decision concordance and lower counterfactual invalidity rates (measured by violated physiological constraints and Mahalanobis distance in a clinical encoder space) than gradient-based counterfactuals (DiCE) or autoregressive LLM prompting on emergency triage and ICU transfer decisions?
3. **Clinical relevance:** Directly generates *discharge safety-netting instructions* and *targeted bedside reassessment triggers*. In Thai emergency departments and bilingual triage (building on the finding that `ThaiLLM-27B-Prescreen` has $F_1 = 0$ on "Observe at Home"), it replaces unsafe blanket discharges with explicit physiological red-flag boundaries in Thai.
4. **POC/MVP (9 months, 1× RTX 4090 16GB):**
   * **Data:** MIMIC-IV-ED (v2.2, ~425k ED stays; Johnson et al., PhysioNet, `https://doi.org/10.13026/5ntk-km72`) + a 500-case bilingual Thai/English synthetic-and-clinician-curated triage vignette set.
   * **Models:** Train a 150M-parameter Masked Discrete Diffusion Model (MDLM architecture) on tabular + clinical note tokens to infill masked features conditioned on $a_{\text{target}} \neq a_{\text{current}}$, paired with a frozen 4B Thai medical LLM (`pai1/tma1-medgemma-4b` or `Qwen3-4B` in 4-bit) to verbalize the tabular boundary into Thai patient discharge instructions.
   * **Compute:** Pretraining/finetuning the 150M discrete diffusion model on MIMIC-IV-ED takes ~18 hours on 16GB VRAM (fp16).
5. **Prior art to beat:** 
   * Mothilal et al., *Explaining machine learning classifiers through diverse counterfactual explanations (DiCE)*, FAT* 2020 (`https://doi.org/10.1145/3351095.3356850`).
   * Sahoo et al., *Simple and Effective Masked Diffusion Language Models (MDLM)*, NeurIPS 2024 (`arXiv:2406.07524`).
   * Wachter et al., *Counterfactual Explanations without Opening the Black Box*, Harv. JL & Tech 2017 (`arXiv:1711.00399`).
6. **Socratic stress-test:**
   * **Decisive assumption:** Discrete diffusion generates counterfactuals that respect physiological couplings (e.g., MAP, SBP, DBP; anion gap and bicarbonate) rather than impossible Frankenstein states.
   * **Month-1 test & kill threshold:** Define 15 hard physiological coupling rules on MIMIC-IV-ED. Generate 1,000 action-flipping counterfactuals using a baseline diffusion prototype. **Kill/pivot if:** >10% violate hard physiological constraints after constrained decoding, OR if simple $L_1$-regularized tree search (DiCE) matches its validity and sparsity within 5%.

---

#### 2. Direction Flip (Latent-State Physiological Readiness for De-Escalation)
1. **Name, the flip, and pitch:** **WeanJEPA** — *From "Who is crashing and needs ICU escalation?" to "When has a critical patient achieved true homeostatic stability to safely STOP vasopressors, invasive ventilation, or empiric broad-spectrum antibiotics?"* Clinical AI is overwhelmingly biased toward initiation; this model learns a self-supervised representation of homeostatic recovery to trigger safe de-escalation without rebound failure.
2. **Paradigm and research question:** **Joint-Embedding Predictive Architecture (JEPA) + Selective Classification (Abstention-Aware Decision Making).**
   * **RQ:** Does pretraining a time-series JEPA to predict future latent physiological states across therapeutic step-downs reduce 48-hour rebound failure rates (re-intubation or vasopressor restart) at a fixed de-escalation sensitivity compared to supervised end-to-end transformers, SSMs, and clinical readiness scores (e.g., RSBI)?
3. **Clinical relevance:** Prevents iatrogenic harm from prolonged mechanical ventilation (ventilator-associated pneumonia, delirium) and catecholamine toxicity. Highly relevant to Thai tertiary ICUs (e.g., KCMH), where unnecessary prolonged ICU stays and extended broad-spectrum antibiotic courses drive severe multidrug-resistant *Acinetobacter baumannii* burden [UNVERIFIED exact KCMH local incidence rate, well-documented nationally].
4. **POC/MVP (9 months, 1× RTX 4090 16GB):**
   * **Data:** MIMIC-IV v3.1 (`https://doi.org/10.13026/kpb9-mt58`, ~94k ICU stays) for training/internal validation; eICU Collaborative Research Database (`https://doi.org/10.13026/C2WM1R`, ~200k stays) for zero-shot/external hospital generalization.
   * **Models:** Custom 45M-parameter Time-Series JEPA (context encoder + target EMA encoder + action-conditioned latent predictor that takes "step-down action $a_t$" as conditioning input) vs. 45M-parameter Mamba/Transformer supervised baselines.
   * **Compute:** ~12 hours per full MIMIC-IV pretraining run on 16GB VRAM using `bfloat16` and flash attention.
5. **Prior art to beat:**
   * Assran et al., *Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (I-JEPA)*, CVPR 2023 (`arXiv:2301.08243`).
   * Prasad et al., *A Reinforcement Learning Approach to Weaning of Mechanical Ventilation in Intensive Care Units*, UAI 2017 (`arXiv:1704.06300`).
   * Komorowski et al., *The Artificial Intelligence Clinician learns optimal treatment strategies for sepsis in intensive care*, Nature Medicine 2018 (`https://doi.org/10.1038/s41591-018-0213-5`).
6. **Socratic stress-test:**
   * **Decisive assumption:** Predicting future *latent representations* conditioned on treatment withdrawal avoids the representation collapse and noise-overfitting of token/value-level autoregressive forecasting in irregular ICU time series.
   * **Month-1 test & kill threshold:** Extract 20,000 vasopressor weaning attempts from MIMIC-IV (defined as norepinephrine drop to 0 for $\ge 4$h, label = restart within 48h). Train a prototype JEPA vs. XGBoost on engineered 6-hour rolling summaries. **Kill/pivot if:** JEPA linear-probe AUPRC for predicting successful weaning does not beat XGBoost by $\ge 0.03$ or fails to reduce false-positive safe-wean calls at 90% sensitivity.

---

#### 3. Evaluation & Optimization Flip (Mechanistic-Physiology Red-Teaming via RSI)
1. **Name, the flip, and pitch:** **PhysioBreak-RSI** — *From "How accurate is this clinical decision agent on a static test set?" to "Can a self-play adversary coupled to a differential-equation physiological simulator discover lethal blind spots in clinical decision models—and immunize them?"* Instead of evaluating on held-out historical records (which under-represent rare physiological edge cases), an adversarial Proposer generates realistic, evolving patient trajectories that trick a clinical Solver into harmful actions.
2. **Paradigm and research question:** **Recursive Self-Improvement (RSI) via Proposer-Solver Self-Play (GRPO) grounded in a Mechanistic Physiological Verifier.**
   * **RQ:** When a clinical decision LLM (Solver) is trained via GRPO against an adversarial trajectory generator (Proposer) constrained by a mechanistic cardiorespiratory/pharmacokinetic ODE simulator, does it reduce severe clinical harm rates (simulator-verified shock/hypoxia/lethal DDI) without inflating false-positive escalation (reward hacking), compared to static SFT or standard rule-based GRPO?
3. **Clinical relevance:** Directly upgrades the student's existing RSI audit direction from brittle string-matching checklists to *mechanistic physiological truth*. Solves the exact failure mode discovered in the student's deep-research report: Thai medical LLMs either miss red flags or reward-hack by sending 100% of patients to the ER.
4. **POC/MVP (9 months, 1× RTX 4090 16GB):**
   * **Data:** Seed patient states from MIMIC-IV-ED + open-source mechanistic physiology engines (e.g., Pulse Physiology Engine, `https://gitlab.kitware.com/physiology/engine`, or CVSim on PhysioNet, `https://doi.org/10.13026/C2X88N`) + Thai clinical vignettes.
   * **Models:** `Qwen3-4B` or `pai1/tma1-medgemma-4b` (4-bit QLoRA, r=32) for both Proposer and Solver roles.
   * **Compute:** CPU runs the fast C++/Python ODE physiological step verifier in milliseconds; GPU runs vLLM rollout generation and Unsloth GRPO updates (~24 hours per 4-round self-play experiment on 16GB VRAM).
5. **Prior art to beat:**
   * DeepSeek-AI (Shao et al.), *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO)*, 2024 (`arXiv:2402.03300`).
   * Perez et al., *Red Teaming Language Models with Language Models*, EMNLP 2022 (`arXiv:2202.03286`).
   * Gao et al., *Scaling Laws for Reward Model Overoptimization*, ICML 2023 (`arXiv:2210.10760`).
6. **Socratic stress-test:**
   * **Decisive assumption:** A mechanistic ODE simulator provides a dense, non-hackable clinical reward signal that transfers back to real human patient vignettes.
   * **Month-1 test & kill threshold:** Couple a fast hemodynamic ODE model (CVSim) to 200 real MIMIC-IV sepsis/hemorrhage cases. Run 1 round of Proposer-Solver search on `Qwen3-4B`. **Kill/pivot if:** The Proposer only finds unrealistic parameter combinations (rejected by a clinical sanity filter >50% of the time), OR if simulator-immunized models show $<5\%$ reduction in error rate on held-out real MIMIC-IV cases.

---

#### 4. Observation Flip (Test-Time Compute for Active Diagnostic Inquiry under Harm/Time Constraints)
1. **Name, the flip, and pitch:** **Activebedside-TTT** — *From "Given all 50 lab results and vitals, what is the diagnosis?" to "Given only a chief complaint and pulse ox, what is the single highest-yield question to ask or bedside test to run NEXT to minimize diagnostic regret?"* Standard classifiers cheat by conditioning on labs ordered hours into an admission; this agent optimizes the *sequential clinical information-gathering policy* itself.
2. **Paradigm and research question:** **Test-Time Training / Monte Carlo Tree Search over Latent World Models for Active Sensing.**
   * **RQ:** Does an active diagnostic agent that uses test-time compute (expected information gain minus clinical delay/invasiveness penalty over a learned latent patient state) reach the same diagnostic and disposition certainty with $\ge 35\%$ fewer diagnostic tests and faster simulated time-to-treatment than static all-feature classifiers and greedy LLM agents?
3. **Clinical relevance:** Mirrors actual clinical medicine, especially in rural Thai community hospitals (*โรงพยาบาลชุมชน*) where point-of-care tests (troponin, D-dimer, CT) are scarce or cause hours of diagnostic delay for conditions like dengue shock syndrome, leptospirosis, or melioidosis.
4. **POC/MVP (9 months, 1× RTX 4090 16GB):**
   * **Data:** MIMIC-IV-ED + MIMIC-IV (using exact timestamps of lab orders `charttime` / `storetime` to reconstruct real clinical delay penalties) + symcat/DDXPlus (`arXiv:2205.09148`, ~1.3M synthetic patients with ground-truth differential diagnosis and inquiry trees).
   * **Models:** A 1.5B–3B parameter backbone (`Llama-3.2-3B` or `Qwen2.5-3B`) fine-tuned as a Masked Patient World Model + a lightweight test-time MCTS planner over clinical actions $\{ \text{Ask}_i, \text{OrderLab}_j, \text{Treat}_k \}$.
   * **Compute:** Training the world model takes ~15 hours; test-time MCTS rollouts take ~3 seconds per clinical step on RTX 4090.
5. **Prior art to beat:**
   * Kachuee et al., *Opportunistic Learning: Budgeted Cost-Sensitive Learning from Data Streams*, ICLR 2019 (`arXiv:1805.10720`).
   * Li et al., *MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning*, NeurIPS 2024 (`arXiv:2406.00922`).
   * Yoon et al., *INVASE: Instance-wise Variable Selection using Neural Networks*, ICLR 2019 (`https://openreview.net/forum?id=BJg_roAcK7`).
6. **Socratic stress-test:**
   * **Decisive assumption:** Retrospective EHR datasets (where missing labs are missing-not-at-random because clinicians didn't order them) can still support valid evaluation of an active test-ordering agent without severe counterfactual bias.
   * **Month-1 test & kill threshold:** Build an evaluation sandbox from MIMIC-IV patients who received a *full* sepsis/cardiac workup (so all ground-truth lab values exist). Test if a baseline mutual-information selector beats random and clinician ordering sequence in time-to-correct-antibiotic. **Kill/pivot if:** The "complete-panel" sub-cohort is too small (<2,000 stays) or exhibits severe selection bias that invalidates off-policy evaluation.

---

#### 5. Subject Flip (Inverse Decision Modelling of Clinician Cognitive Heuristics & Blind Spots)
1. **Name, the flip, and pitch:** **ClinicianMirror (Contextual Inverse RL)** — *From "Predict the patient's disease" to "Predict the attending clinician's implicit reward function and alert them ONLY when their current trajectory deviates from their own rest-state standard of care."* Instead of acting as an arrogant oracle that spams alerts, the AI models the *clinician* under cognitive load (night shift, high ED crowding) to detect fatigue-induced diagnostic shortcuts.
2. **Paradigm and research question:** **Contextual Inverse Reinforcement Learning (IRL) / Behavioral Cloning with State-Dependent Irrationality.**
   * **RQ:** Can a contextual inverse decision model decompose historical clinician actions in the ED/ICU into a baseline clinical utility function plus a cognitive-load perturbation vector (time-of-day, concurrent patient census, prior alarm count), predicting clinically harmful human omissions (missed sepsis bundle steps or premature discharge) with higher precision and $\ge 50\%$ lower alert volume than patient-only risk scores?
3. **Clinical relevance:** Alert fatigue causes clinicians to override up to 90% of standard EHR CDSS alerts. For overburdened Thai public hospital interns/residents working >80-hour weeks, an agent that stays silent when the doctor is already on track—and speaks up only when cognitive overload causes a blind spot—transforms human-AI teaming.
4. **POC/MVP (9 months, 1× RTX 4090 16GB):**
   * **Data:** MIMIC-IV-ED + MIMIC-IV (reconstructing department-wide concurrent patient census, arrival rate, shift hour, and provider action sequences from timestamped events).
   * **Models:** A 25M-parameter State-Space Model (Mamba-2) encoding the joint (Patient State $\times$ ED Operational Load State) trained via Maximum Entropy Contextual IRL.
   * **Compute:** Fast tabular/sequence training; <6 hours per full experiment on 1× RTX 4090.
5. **Prior art to beat:**
   * Hüyük et al., *Explaining by Imitating: Understanding Decisions by Interpretable Policy Learning*, ICLR 2021 (`arXiv:2103.05526`).
   * Jarrett et al., *Inverse Decision Modeling: Learning Interpretable Representations of Behavior*, ICML 2021 (`arXiv:2106.03651`).
   * Gu & Dao, *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*, COLM 2024 (`arXiv:2312.00752`).
6. **Socratic stress-test:**
   * **Decisive assumption:** Public EHR timestamps (MIMIC-IV-ED) contain enough signal about environmental/cognitive load (crowding, shift time) and provider identity/actions to separate deliberate clinical judgment from fatigue-induced omission.
   * **Month-1 test & kill threshold:** Reconstruct hourly ED census and boarding load in MIMIC-IV-ED. Measure whether adding operational/shift context to a patient-state model significantly improves prediction of "delayed antibiotic administration (>3h)" or "72h bounce-back after discharge". **Kill/pivot if:** The ΔAUROC of adding clinician/context state over patient-only state is $<0.02$.

---

If I were the student I'd pick **#1 (PivotDiff: Action-Reversal Counterfactuals via Discrete Diffusion)** — or **#2 (WeanJEPA)** if you prefer continuous ICU signals — because #1 flips the clinical interface from an ignorable risk score to an actionable physiological boundary, uses frontier discrete diffusion that fits comfortably on a 16GB RTX 4090, and directly solves the "unsafe home discharge" failure mode you already uncovered in Thai medical LLMs.

---

# ROUND 2

## CLAUDE: Round 2

**Read:** `claude_round1.md`, `codex_round1.md`, `gemini_round1.md`. No Round 2 file was read. All three answers respect the brief's exclusions; none proposes policy, payment, HTA or permission schemes.

## 1. Hume audit: five load-bearing claims that are wrong, unverified or overstated

1. **Gemini #1 PivotDiff: "safe to observe at home UNLESS lactate rises above 2.4 mmol/L", generated as Thai discharge instructions.**
   - *Problem:* an action-flipping counterfactual describes **the model's decision boundary, not the patient's physiology**. Turning it into patient-facing safety-netting presumes the model is causally and clinically correct exactly where it is least reliable, at its own boundary.
   - *Problem:* "unstated history of cirrhosis" as a counterfactual is a missing-data statement, not a physiological perturbation.
   - *Exclusion check:* this is clinical and passes, but its clinical-safety claim needs clinician adjudication.
   - *Verify:* blinded clinicians rate whether generated boundaries are clinically true (not just model-true) on ≥100 cases, before any instruction generation.
2. **Gemini #1: a 150M masked discrete diffusion model on MIMIC-IV-ED "tabular + clinical note tokens", trained in ~18 h.**
   - *Problem:* MIMIC-IV-ED's own tables hold structured triage data and a chief-complaint string. Full narrative notes sit in the separately credentialed MIMIC-IV-Note module, mostly discharge and radiology notes [UNVERIFIED for ED-provider notes].
   - *Problem:* for low-dimensional tabular counterfactuals, exact minimal solutions (MILP / DiCE-style search) already exist, so a diffusion model needs to justify itself on validity, not novelty.
   - *Verify:* inventory which note types link to ED stays; benchmark against an exact MILP counterfactual on the same constraint set.
3. **Gemini #5 ClinicianMirror and Claude #3: per-clinician inference from MIMIC-IV-ED.**
   - *Problem:* both assume usable de-identified provider identifiers linked to ED decisions. MIMIC-IV added provider identifiers in later versions [UNVERIFIED for the ED module and for order-level linkage]. Without them, "clinician" collapses to "department × shift".
   - *Verify:* query the current schema for provider columns on ED orders and medication administrations.
4. **Codex #1 Decision-Sufficient MRI: framed as a gap against "adaptive acquisition already exists".**
   - *Problem:* task-driven k-space sampling *for downstream classification* (not reconstruction) already has a literature [UNVERIFIED specific citations, e.g. learned task-based sampling and reconstruction-free classification papers]. So the novelty rests on the JEPA representation and calibrated stopping, which Codex itself labels as the burden.
   - *Feasibility:* 180–300 GPU-hours on multi-coil knee k-space at 16 GB is tight.
   - *Thai relevance:* clinically weak; MRI acquisition time is not a documented Thai bottleneck.
   - *Verify:* a literature check for task-based MRI acquisition with stopping; a week-1 throughput test on one fastMRI volume.
5. **Gemini #2 WeanJEPA: "20,000 vasopressor weaning attempts" and "reduce 48-hour rebound failure rates".**
   - *Problem:* the count is plausible but unverified.
   - *Problem:* "reduce rebound failure" is a **causal** claim from observational weaning decisions, where clinicians weaned the patients they judged ready. A linear-probe AUPRC gain is a prediction result, not a reduction in failures.
   - *Problem:* JEPA rarely beats gradient boosting on irregular ICU tabular-like series, though the kill test is honest.
   - *Verify:* rephrase the RQ as prediction at matched sensitivity (as Codex #5 does), and count episodes with an explicit definition.

Minor:
- Codex #2's simglucose targets type 1 diabetes, which is far rarer in Thailand than type 2. Its clinical relevance to the student's setting is low, though the method transfers.
- Codex #4 is the only idea whose month-1 test explicitly audits selection bias in who gets tested (complete-panel AUROC > 0.80). That is good practice the others should copy.

## 2. Convergence verdict

| Cluster | Who | Signal or attractor? | Best variant |
|---|---|---|---|
| **Stop / de-escalate** | Claude #4 (antibiotic stop), Gemini #2 (vasopressor/ventilator wean), Codex #5 (extubate now vs wait) | Signal, but all three hit the same **identifiability wall** | **Codex #5**: two evidential tiers (semi-synthetic with known mechanisms + real-data supported regions) and support-aware abstention. It is the only design that cannot overclaim. |
| **Simulator red-teaming** | Claude #5 (Pulse, vital-sign models), Gemini #3 (LLM proposer–solver against an ODE simulator), Codex #2 (simglucose adversary) | Signal; the brief listed it, but all three made it concrete | **Codex #2** for rigour (constrained disturbances, clinician plausibility ≥27/30, cross-controller transfer). Gemini's LLM self-play adds a layer whose value is unshown. |
| **Decision boundary / stability** | Claude #1 (fragility under measurement noise), Gemini #1 (minimal action-flipping change) | Complementary, not duplicate: fragility asks *how likely* noise crosses the boundary; PivotDiff asks *where* the boundary is | **Merge:** one "decision-boundary audit" of clinical models, kept as a *model-property* study, not patient instructions |
| **Active acquisition** | Gemini #4 (next question/test), Codex #1 (MRI lines until the decision stabilises) | Real signal: "stop acquiring when the decision is stable" | Codex #1 is cleaner (complete data exists, so no missing-not-at-random problem) but has weaker Thai relevance; Gemini #4 has the MNAR evaluation trap |
| **Model the clinician** | Claude #3, Gemini #5 | Gated on provider IDs | Unresolved until the schema check |

## 3. Socrates: most over-rated idea, Gemini #1 PivotDiff

It breaks on the assumption that **the model's action boundary is clinically meaningful at the individual level**. Counterfactual explanations are faithful to the model, not to the patient. Near the boundary, where every counterfactual lives, the model is at its *least* calibrated, and that is exactly the measurement-noise region Claude #1 shows is fragile. Converting those boundaries into Thai discharge instructions takes a model-debugging tool and gives it a patient-safety role. The frontier-ML element (masked discrete diffusion) is also not needed for a ~20-feature tabular counterfactual.

## 4. Most under-rated: Codex #4, joint-susceptibility antibiotic decisions

It is the most clinically central decision on the board: which empiric antibiotic to choose while susceptibility results are pending. The flip is real and precise: from *per-drug marginal resistance scores* to *a joint distribution over susceptibility patterns*, scored on the drug actually chosen.
- **Data:** public MIMIC-IV microbiology.
- **Compute:** tiny models on the laptop.
- **Evaluation:** an honest selection-bias audit is built in.
- **Thai relevance:** strong and purely clinical. Thailand has high antimicrobial resistance (widely reported; [verify a specific source before citing]), and a Thai validation would use a hospital's own microbiology data, not policy.

**Merge:** it is the ideal application for Claude #2's *decision-focused learning*. The decision (choose the least-broad drug that is still active) is explicit, harms are asymmetric, and predict-then-threshold is the natural baseline. Add Claude #1's fragility lens as a secondary analysis: how often does the chosen drug flip under plausible uncertainty in the patient's prior-culture history?

## 5. Final top 3

| # | Project | Flip | Novelty (1–5) | Clinical impact (1–5) | ML depth (1–5) | POC finish confidence | Data gate | Why |
|---|---|---|---|---|---|---|---|---|
| 1 | **Decision-focused joint antibiogram**: choose the narrowest active empiric antibiotic from a learned joint susceptibility model, trained on decision regret (Codex #4 + Claude #2) | Marginal resistance scores → joint possibilities, scored on the *decision* | 4 | 5 | 4 | 70% | ≥500 complete-panel episodes with ≥50 resistant to the narrowest drug (MIMIC-IV); later a Thai hospital microbiology extract under IRB | The most important everyday decision, a clean flip, public data, tiny compute, and a direct Thai clinical extension |
| 2 | **Decision-boundary audit**: per-patient decision-flip probability under real lab measurement error, plus minimal action-flipping changes, with fragility-aware training (Claude #1 + Gemini #1 kept model-facing) | Exact inputs → uncertain measurements; score → boundary | 4 | 4 | 3 | 80% | MIMIC-IV / eICU + published analytic and biological CVs | A new measurable object with a striking month-1 number, and a rural point-of-care angle |
| 3 | **Stop decisions with support-aware abstention**: extubation, vasopressor or antibiotic stopping (Codex #5 + Gemini #2 + Claude #4) | Start → stop; recommend → say where data cannot support a recommendation | 3 | 5 | 4 | 55% | Overlap/propensity gates on MIMIC-IV | Highest clinical stakes; honest only with Codex's two-tier design |

- **Moonshot:** *constrained physiological red-teaming with cross-model transfer* (Codex #2's rigour applied to a Thai-relevant decision, e.g. a sepsis or haemorrhage early-warning model in Pulse rather than type 1 diabetes insulin).
- **Safe ambitious:** *#2, the decision-boundary audit.* Public data, laptop-only, and a publishable negative result is still informative ("these decisions are robust to measurement noise").

## CODEX (gpt-6.1-sol): Round 2

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

## GEMINI (gemini-4-argon): Round 2

### 1. Hume Audit: 5 Load-Bearing Claims by Claude & Codex

1. **Claude #3 (Inverse Decision Modelling): "POC: MIMIC-IV-ED, which has provider identifiers [check availability]."**
   * **Why it is wrong/overstated:** Public MIMIC-IV-ED (`edstays`, `triage`, `medrecon`, `pyxis`, `vitalsign`) does **not** release longitudinal, linkable physician/attending provider IDs for diagnostic orders (like CT head) that allow tracking an individual clinician's personal threshold across shifts. While MIMIC-IV v3.0+ added `caregiver_id` to certain ICU chartevents/emar tables, ED diagnostic ordering by specific individual doctors is largely unlinked or confounded by resident/attending sign-off practices.
   * **What would verify it:** Query `mimiciv_ed` and `mimiciv_hosp.poe` (Provider Order Entry) for `ord_provider_id` completeness, uniqueness per shift, and stability across time splits before committing to per-clinician test–retest correlation.

2. **Codex #1 (Decision-Sufficient MRI): "Linked to fastMRI+ pathology annotations... require at least 100 positive and 200 negative examinations [for meniscal tear]... train a 2D reconstruction network + JEPA encoder + acquisition head."**
   * **Why it is overstated/fragile:** `fastMRI+` provides bounding-box/slice-level annotations on a subset of fastMRI, but MRI k-space acquisition occurs slice-by-slice or volume-by-volume in phase-encoding lines, whereas clinical meniscal tear review is an *examination-level* 3D multi-slice decision. A 2D slice-level policy that stops acquiring k-space lines on Slice 14 when the tear is only visible on Slices 16–18 will fail at the patient level unless the sequential policy operates across the 3D volume—which blows up the memory footprint on a 16GB laptop GPU.
   * **What would verify it:** Check the exact slice-vs-volume label granularity in `fastMRI+` for coronal/sagittal knee sequences and benchmark peak VRAM of a multi-slice volumetric k-space simulator on 16GB VRAM.

3. **Claude #1 (Decision Fragility): "What fraction of decisions made by published or replicated clinical models... are fragile (flip probability >10%) under realistic measurement error? Does fragility-aware training reduce fragile decisions?"**
   * **Why it is overstated as a standalone ML thesis:** Under a continuous risk model $f(X)$ with a hard decision threshold $\tau$, the probability that Gaussian measurement noise $X + \epsilon$ flips the decision $\mathbb{I}[f(X+\epsilon) > \tau]$ is monotonically determined by the distance of $f(X)$ to the threshold $\tau$ normalized by the local gradient $\|\nabla_X f(X)\|_{\Sigma_\epsilon}$. Furthermore, "fragility-aware training" that penalizes flip probability near $\tau$ simply flattens the gradient near the decision boundary or pushes scores away from $\tau$ (destroying probability calibration).
   * **What would verify it:** Prove mathematically and empirically in Month 1 that "fragility-aware training" is not strictly equivalent to standard margin maximization / input-gradient regularization (e.g., Ross & Doshi-Velez, 2018) plus post-hoc conformal abstention near the threshold.

4. **Codex #3 (Pathology-or-Sensor Alarm Representation): "Data: labelled public PhysioNet Challenge 2015 records... 3–5M parameter encoders + multiview JEPA... improve false-alarm rejection by ≥10 percentage points."**
   * **Why it is infeasible/overstated:** The PhysioNet 2015 Challenge public training set contains only **750 recorded segments** across 5 arrhythmia classes (some classes having fewer than 40 true positives). Training a 5M-parameter multiview JEPA + cross-channel latent predictor on 750 short segments (even with MIT-BIH pretraining, which only has 48 patients and lacks matching ABP/PPG pulsatile waveforms!) will severely overfit compared to the hand-crafted signal-quality indices (SQIs) that won the 2015 challenge.
   * **What would verify it:** Check the exact number of paired ECG+PPG/ABP patients in MIMIC-III/IV Waveform Database for self-supervised pretraining, rather than relying on MIT-BIH (which is ECG-only) and the tiny 750-record Challenge 2015 training set.

5. **Claude #2 (Decision-Focused Learning / SPO+ for Clinical Actions): "At matched AUROC, does decision-focused training reduce decision regret... versus predict-then-threshold?"**
   * **Why the novelty claim is overstated:** In operations research (Elmachtoub & Grigas, 2022), SPO+ shines when predictions feed a *combinatorial linear program* (e.g., shortest path, bipartite matching) where errors interact across multiple variables. For a binary single-patient clinical action (give antibiotics vs. withhold) with linear asymmetric harms $c_{FN}, c_{FP}$, Bayes decision theory proves that the optimal decision rule is simply thresholding the true posterior probability at $\tau^* = \frac{c_{FP}}{c_{FP} + c_{FN}}$. Thus, for single-action binary decisions, "decision-focused learning" collapses into standard **cost-sensitive classification / asymmetric focal loss** + local calibration around $\tau^*$.
   * **What would verify it:** Formulate a *multi-action or constrained* clinical decision problem (such as Codex #4's joint antibiotic panel selection) where independent probabilities genuinely fail to capture combinatorial decision loss.

*Brief Exclusions Check:* **None** of the 15 proposals across Claude, Codex, or Gemini violated the brief's hard exclusions (all avoided NHSO/payers, legal/autonomy leases, and hospital routing/quotas).

---

### 2. Convergence Verdict

Four distinct clusters emerged across the three advisors:
1. **Mechanistic-Physiology Red-Teaming / Counterexample Search (3/3 converged):** Claude #5 (*Pulse Physiology Engine red-team*), Codex #2 (*Counterexample Patient in `simglucose`*), Gemini #3 (*PhysioBreak-RSI with ODE verifiers*).
2. **Direction Flip — Stopping / De-escalation Rules (3/3 converged):** Claude #4 (*Antibiotic stopping via target trial emulation*), Codex #5 (*Ventilation stopping via state-space world model*), Gemini #2 (*WeanJEPA for vasopressor/ventilation de-escalation*).
3. **Boundary / Uncertainty / Sufficiency near the Action Threshold (3/3 converged):** Claude #1 (*Decision Fragility under lab CV noise*), Gemini #1 (*PivotDiff action-reversal counterfactuals*), Codex #1 & #4 (*Decision sufficiency / risk-controlled joint antibiotic selection*).
4. **Subject Flip — Inverse Decision Modelling of the Clinician (2/3 converged):** Claude #3 (*Per-clinician threshold recovery*) and Gemini #5 (*ClinicianMirror Contextual IRL under cognitive load*).

**Real signal or brief attractor?** 
Both. The brief explicitly listed *Objective, Output, Subject, Direction,* and *Evaluation* as starting examples, which explains the structural alignment. However, the **convergence on Mechanistic Simulator Red-Teaming** and **ICU De-escalation (Weaning/Stopping)** is a genuine scientific signal: these are the two areas where public retrospective EHR data (MIMIC-IV) and open C++/Python physiological engines (`simglucose`, `Pulse`, `CVSim`) allow a single student on a 16GB laptop to do rigorous, falsifiable science without needing prospective clinical trials.

**Best variant in each cluster:**
* **Mechanistic Red-Teaming:** **A hybrid of Codex #2 and Gemini #3.** Codex #2's choice of `simglucose` (FDA-accepted UVA/Padova T1D simulator) with cross-controller transfer is the cleanest, most bulletproof sandbox, while Gemini #3's Proposer-Solver self-play loop (immunizing the decision model and testing transfer to MIMIC-IV) adds the strongest ML contribution.
* **Stopping / De-escalation:** **Codex #5 + Gemini #2 merged.** Gemini #2 provides the frontier representation architecture (Action-Conditioned Time-Series JEPA across vasopressor/ventilation step-downs), while Codex #5 provides the crucial *support-aware abstention and semi-synthetic causal identification discipline* so the student doesn't make indefensible causal claims from confounded ICU charts.
* **Boundary / Measurement Flip:** **Gemini #1 + Claude #1 merged.** Combining Claude's analytic/biological lab variation (EFLM CVs) with Gemini's discrete counterfactual boundary generation turns a diagnostic test into an actionable clinical output.
* **Decision-Focused Learning:** **Codex #4 (Joint Antibiotic Susceptibility Selection)** is vastly superior to Claude #2 because selecting an empiric antibiotic across correlated multi-drug resistance panels is a genuinely *joint* decision problem where independent per-drug probabilities fail.

---

### 3. Socrates: The Single Most Over-Rated Idea

**Claude #3 — "Model the doctor, not the disease: inverse decision modelling of clinical practice"** (and by extension, my own **Gemini #5 ClinicianMirror**).

* **The assumption it breaks on:** **Unobserved clinical confounding is indistinguishable from "clinician irrationality/threshold shift" in public EHR data.**
* **Why it breaks:** When Doctor A orders a head CT or starts sepsis antibiotics for a patient whose recorded vitals look identical to a patient Doctor B discharges, Inverse RL attributes this difference to Doctor A having a "lower risk threshold" or Doctor B being "fatigued." In reality, Doctor A saw the patient vomit in the room, noticed subtle neck stiffness, or heard a family member say the patient "isn't acting right"—none of which is coded in structured MIMIC-IV-ED tables. Furthermore, as noted in the Hume audit, public MIMIC-IV-ED does not reliably track individual physician identities across shifts without severe resident/attending attribution noise. A master's thesis built on recovering "per-doctor cognitive thresholds" from retrospective EHR data will be torn apart by the medical committee on day one for confounding unrecorded bedside exams with clinician bias.

---

### 4. Most Under-Rated Idea & How to Improve It

**Codex #4 — "Antibiotic Decisions from Joint Possibilities, Not Independent Resistance Scores"**

* **Why it is under-rated:** Codex ranked it #4, yet it solves the biggest mathematical flaw in Claude #2 (Decision-Focused Learning) and addresses a massive clinical problem in Thailand (empiric antibiotic selection for Gram-negative bacteremia/sepsis amidst high multidrug resistance). Standard ML predicts $P(\text{Resistant to Drug } A)$ and $P(\text{Resistant to Drug } B)$ independently. But resistance mechanisms (e.g., ESBL, AmpC, carbapenemases) induce strong **higher-order correlations** across the susceptibility panel, and microbiology labs only test a subset of drugs (masked/partial observation).
* **How to merge and improve it:** 
  Merge **Codex #4 (Joint Partially-Observed Susceptibility Generative Model)** with **Claude #2 (Decision-Focused Regret Loss)** and **Claude #4 (De-escalation/Stewardship)**:
  1. Train a **Masked Discrete Diffusion / Categorical Transformer** (from Gemini #1 / Codex #4) on partially observed MIMIC-IV (and local KCMH antibiogram data if IRB permits) microbiology panels to model the *joint distribution* of susceptibility across candidate antibiotics given patient history and Gram stain / rapid organism ID.
  2. Train the selection head end-to-end with a **Decision-Focused Regret Loss (Claude #2)** that explicitly trades off **Ecological/Spectrum Cost** (reserving carbapenems/colistin) against **Empirical Coverage Failure Risk** (conformal risk control $\le 5\%$ non-susceptibility).
  3. Include **Escalation vs. De-escalation flips** as the core clinical action. This runs in <50 GPU-hours on a laptop, uses 100% real ground-truth microbiology labels (zero unmeasured causal confounding!), and is immediately publishable at MLHC/CHIL or *Lancet Microbe*.

---

### 5. Final Top 3 Proposals

| # | Project | Flip | Novelty (1–5) | Clinical impact (1–5) | ML depth (1–5) | POC finish confidence (%) | Data gate | Why |
| :- | :--- | :--- | :-: | :-: | :-: | :-: | :--- | :--- |
| **1** | **PhysioRedTeam-RSI** *(Merge: Codex #2 + Gemini #3 + Claude #5)* | **Evaluation Flip:** From static test-set accuracy to constrained adversarial patient trajectories in a mechanistic physiology simulator (`simglucose` / `CVSim`) that break clinical controllers/agents and immunize them via self-play. | 5 | 4 | 5 | **88%** | **Week 2:** Verify simulator throughput & confirm learned adversary finds $\ge 1.5\times$ more severe failures than CMA-ES/random search within clinical plausibility bounds. | Zero EHR confounding; runs entirely on laptop CPU+GPU; combines rigorous control/ODE verification with frontier adversarial RL/GRPO self-play. |
| **2** | **JointAbx-DFL** *(Merge: Codex #4 + Claude #2)* | **Objective & Structure Flip:** From independent per-drug resistance AUROC to decision-focused empiric antibiotic selection over *joint* partially observed susceptibility distributions under conformal risk control. | 4 | 5 | 4 | **92%** | **Week 3:** Audit MIMIC-IV microbiology for $\ge 500$ complete-panel Gram-negative bloodstream episodes with $\ge 50$ non-susceptible to narrow-spectrum candidates. | Ground-truth microbiological labels eliminate causal identifiability headaches; solves a real multi-drug correlation problem; huge infectious-disease relevance in Thailand. |
| **3** | **FragileBoundary (PivotDiff-CV)** *(Merge: Gemini #1 + Claude #1)* | **Output & Input Flip:** From a point-mass risk score to a dual output: (1) *Decision Fragility* under realistic lab analytic/biological CVs, and (2) the *minimal physiological boundary* (via discrete diffusion) that flips disposition. | 4 | 5 | 4 | **85%** | **Week 3:** Verify that $>5\%$ of MIMIC-IV-ED triage/sepsis decisions flip under EFLM lab CVs and that discrete diffusion respects 15 hard physiological coupling rules ($>90\%$ validity). | Directly answers the bedside question *"Can I trust this decision given lab noise, and what red flag changes the plan?"* Works out-of-the-box on MIMIC-IV-ED. |

* **The "Moonshot" Pick:** **WeanJEPA-Causal (Merge of Gemini #2 + Codex #5 — Support-Aware Action-Conditioned JEPA for ICU Liberation).** Learning when to *stop* mechanical ventilation or vasopressors using an action-conditioned latent world model with explicit epistemic abstention when causal overlap fails. High reward (a flagship paper if the representation beats transformers and clinical scores on MIMIC-IV $\to$ eICU transfer), but carries causal-identifiability risk that requires Codex #5's semi-synthetic validation tier.
* **The "Safe Ambitious" Pick:** **JointAbx-DFL (#2 above)** (or **PhysioRedTeam-RSI (#1)** if the student prefers RL/simulators over tabular/discrete generative models). **JointAbx-DFL** has >90% finish confidence on a 16GB RTX 4090, uses rock-solid culture susceptibility labels in MIMIC-IV, combines discrete generative modeling with decision-focused conformal risk control, and addresses antimicrobial resistance—a top clinical priority at Chulalongkorn/KCMH.
