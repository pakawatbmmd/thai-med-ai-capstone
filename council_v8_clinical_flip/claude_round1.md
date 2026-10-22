# Council v8: Clinical / scientific flips on decision models. Claude, Round 1

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
