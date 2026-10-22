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