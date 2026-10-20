# Capstone Council v3 — Frontier paradigms (Claude × Codex × Gemini, philosopher-council, 2026-10-20)

# ROUND 1

## CLAUDE — Round 1

## Claude — Round 1 (frontier paradigms; council applied)

### 1. DoseLoop — bounded recursive self-improvement where the reward is *checkable*
- **Pitch:** A 7B model teaches itself Thai clinical dose calculation by generating problems, solving them, verifying the answers with code, and retraining on its own verified successes, and we measure exactly when the self-improvement plateaus or collapses.
- **Paradigm & RQ (RSI):** STaR/ReST-EM-style self-training usually relies on noisy LLM judges. *In a domain with an exact programmatic verifier, does iterated self-training in a low-resource language keep improving, and does it diverge from (or collapse relative to) a judge-based loop after N rounds?* Falsifiable: accuracy curves of verifier-gated vs LLM-judge-gated loops over 6–8 iterations, on a fixed held-out human-written test set.
- **Thai testbed:** weight-based paediatric dosing, renal dose adjustment, infusion-rate and unit conversions, written in Thai with Thai drug names and units and mixed Thai/Arabic numerals. Errors are dangerous, and correctness can be computed. Thai is low-resource enough that the base model actually starts weak (unverified, so measure it).
- **Laptop experiment:** Qwen2.5-7B / Typhoon-class 7–8B, QLoRA 4-bit (~10–12 GB VRAM). A Python verifier built from dosing formulas taken from public drug labels. Baselines: few-shot, single SFT on synthetic data, judge-gated loop. About 8–15 GPU-hours per iteration × 8 iterations ≈ 100 GPU-hours. Metrics: exact-match accuracy, "confident wrong" rate, diversity of the generated problems (to detect mode collapse).
- **Socratic test:** *The model's self-generated problems stay diverse enough to keep teaching it.* Month 1: run 2 iterations and measure problem-template entropy. If it collapses, add a curriculum generator (agent that targets failure clusters), which becomes the contribution.

### 2. FloorJEPA — latent world models for falls in a floor-living culture
- **Pitch:** Test whether JEPA-style predictive pretraining anticipates falls better than reconstruction or contrastive pretraining when "normal" daily movement includes sitting on and rising from the floor, as it does in many Thai homes.
- **Paradigm & RQ (V-JEPA):** *Under a posture distribution shift (floor sitting, squatting, getting up from mats), does a latent-predictive video encoder give lower false-alarm rates for fall detection and earlier fall anticipation than VideoMAE (pixel reconstruction) and contrastive baselines, given equal compute and few labels?*
- **Thai testbed:** an ageing society, many elders alone at home during the day (unverified prevalence), floor-level living, and squat toilets. These are exactly the postures Western fall datasets treat as anomalies.
- **Laptop experiment:** Pretrain ViT-S/16 JEPA on unlabeled video: public activity datasets + **simulated humans in MuJoCo/Genesis** performing floor transitions and falls (randomised bodies, cameras, lighting). Fine-tune with few labels on public fall datasets plus a small set of recorded floor-transition clips. About 150–250 GPU-hours. Metrics: AUROC, false alarms/day at fixed recall, anticipation lead time. Privacy bonus: inference keeps only latents, no stored video.
- **Socratic test:** *Simulated floor transitions transfer to real video.* Month 1: train a tiny probe on sim-only vs real-only clips and measure the cross-domain gap.

### 3. Masked diffusion vs autoregressive LMs for safety-constrained Thai medication instructions
- **Pitch:** Can a discrete-diffusion LM, which revises the whole sentence globally, satisfy hard clinical constraints (dose, frequency, timing relative to meals) better than an autoregressive LM of equal size?
- **Paradigm & RQ (diffusion LM):** *At matched parameters and training tokens, does a masked diffusion LM (MDLM/LLaDA-style) achieve a lower constraint-violation rate on constrained infilling than an AR transformer, and does that advantage survive Thai's unsegmented script?*
- **Thai testbed:** ฉลากยา (Thai medication label instructions) such as "รับประทานครั้งละ 1 เม็ด วันละ 2 ครั้ง หลังอาหารเช้า-เย็น". The structure is rigid, a single slot error is harmful, and Thai has no spaces between words, which stresses tokenisation.
- **Laptop experiment:** Train ~150M AR vs ~150M MDLM from scratch on a Thai corpus plus a synthetic instruction corpus (~40 GPU-hours each). Also run LLaDA-8B (4-bit) zero-shot. Metrics: constraint-violation rate, slot accuracy, fluency (pharmacist rating on a sample), and tokenizer ablation (character vs subword).
- **Socratic test:** *Synthetic instructions cover real label variety.* Month 1: collect 200 real label strings (photos, typed out) and check coverage.

### 4. Sachet-VLA — sim-augmented vision-language-action policy for packing elders' weekly pill organisers
- **Pitch:** A low-cost robot arm learns to pick pills from Thai hospital zip-lock sachets and place them into a 7-day organiser, comparing how much simulated data can replace real teleoperation.
- **Paradigm & RQ (physical AI):** *For transparent, deformable containers, what ratio of sim (Genesis/MuJoCo) to real demonstrations maximises the success rate of a small VLA under a fixed real-data budget?*
- **Laptop experiment:** SO-101 arm (~฿10k, an assumption), LeRobot, SmolVLA (~0.5B) or ACT policy fine-tuned in 16 GB. 50–200 real demos vs sim-augmented. Metrics: task success, wrong-compartment rate.
- **Socratic test:** *Transparent plastic is simulatable at useful fidelity.* Month 1: render tests plus 20 real grasps.

### 5. Calibrated generative agents of Thai health behaviour (bold)
- **Pitch:** Simulate villages of LLM agents (villagers, village health volunteers, clinic staff) to pre-test health messages, then measure whether the simulation's behaviour actually matches real Thai survey statistics.
- **RQ (agentic):** *Can locally run 8B agent populations be calibrated (persona conditioning + memory) to reproduce known Thai survey distributions within X%?* Run locally with vLLM at 4-bit.
- **Socratic test:** *A public Thai behavioural survey with micro-data exists for calibration.* If not, the project has no ground truth.

**If I were the student I'd pick #1 (DoseLoop)**: RSI is the hottest topic on the list, and the exact verifier makes it *measurable* rather than hand-wavy, all within about 100 GPU-hours. #2 is the best fit if you want physical/world-model work.

## CODEX — Round 1

Ranked by research value, nine-month feasibility, and strength of evaluation. These are **research proposals, not verified novelty claims**. Compute figures are estimates for each complete study, including baselines, ablations, and three seeds. Run models sequentially; benchmark sustained laptop throughput in month one. Stream datasets and cap stored checkpoints and processed data at 150 GB.

Thailand's ageing population and rehabilitation needs provide a supported motivation. Specific local deployment conditions below remain hypotheses until checked. [WHO Thailand health-system review](https://apo.who.int/publications/i/item/9789290620457)

1. **Rehabilitation JEPA that preserves impairment** — Learn movement representations that ignore camera corruption while retaining clinically meaningful movement differences.

   **Paradigm & research question:** JEPA-style predictive learning. Does separating nuisance prediction from joint-dynamics prediction improve robustness without erasing movement limitations, compared with ordinary latent prediction?

   **Thai healthcare testbed:** Home rehabilitation for older adults. Camera placement, occlusion, and low frame rates could obscure movement limitations. **Unverified:** their frequency in Thai home rehabilitation and whether available exercises match local practice.

   **Experiment on the laptop:** Use the published [KIMORE rehabilitation dataset](https://pubmed.ncbi.nlm.nih.gov/31217121/), subject to confirming download access. Train 5–15M-parameter skeleton encoders using the proposed objective, ordinary JEPA, masked reconstruction, and contrastive learning. This adapts [JEPA's feature-prediction principle](https://ai.meta.com/research/publications/revisiting-feature-prediction-for-learning-visual-representations-from-video/), without training a video foundation model. Measure clinical-score error, label efficiency, corruption robustness, and sensitivity to controlled movement changes. Split by participant. Budget **80–150 GPU-hours; 4–8 GB VRAM**, using short skeleton clips.

   **Socratic stress-test:** The decisive assumption is that nuisance invariance preserves impairment. **Month one:** compare camera perturbations against physiotherapist-reviewed movement perturbations. Stop if the representation treats both as equivalent.

2. **Self-improvement under an adversarial medication verifier** — Study when a small agent's self-generated curriculum produces transferable reasoning rather than verifier exploitation.

   **Paradigm & research question:** Bounded RSI and verifier-guided agents. Does training on independently verified counterexamples improve unseen medication-instruction consistency checks more than ordinary self-training at equal compute?

   **Thai healthcare testbed:** Thai/English medication instructions with quantities, units, timing, and negation. Language changes must preserve executable meaning. **Unverified:** representative local wording and error distributions; obtain pharmacist review.

   **Experiment on the laptop:** Use [Qwen2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B), four-bit weights, LoRA, 512-token contexts, and microbatch one. Generate 20,000 synthetic instructions with exact symbolic meanings; assess consistency rather than prescribing doses. Compare a frozen agent, static-data training, ordinary self-training, and three counterexample-driven rounds. Use independently implemented training and evaluation verifiers. Measure held-out compositional accuracy, verifier exploitation, and gain per GPU-hour. Budget **120–220 GPU-hours; 8–13 GB VRAM**.

   **Socratic stress-test:** The verifier must capture meaning rather than superficial arithmetic. **Month one:** audit 200 adversarial instructions with a pharmacist. Reject the project if ambiguous or incorrect oracle labels remain common.

3. **A state-space model that knows time passed during a sensor gap** — Modify recurrent state evolution so missing measurements do not masquerade as observed physiology.

   **Paradigm & research question:** Selective state-space models. Does elapsed-time-conditioned state propagation outperform ordinary Mamba plus imputation under long, activity-dependent sensor gaps, at matched training budgets?

   **Thai healthcare testbed:** Wearable monitoring during rehabilitation and daily activity. **Unverified:** Thai device dropout patterns and their relationship to activity; these must determine the corruption benchmark.

   **Experiment on the laptop:** Use [PPG-DaLiA](https://archive.ics.uci.edu/dataset/495/ppg-dalia), which includes physiological signals, activity, and ECG-derived heart-rate ground truth. Compare 1–5M-parameter [Mamba](https://arxiv.org/abs/2312.00752)-style models, the proposed transition, a temporal convolutional network, and a small Transformer. Measure heart-rate error, recovery after gaps, uncertainty coverage, latency, and memory across sequence lengths. Hold out participants and gap mechanisms. Budget **60–120 GPU-hours; 3–7 GB VRAM**, with bounded training windows.

   **Socratic stress-test:** Synthetic missingness must resemble actual device failures. **Month one:** obtain scripted, nonpatient device traces locally. Without realistic gap evidence, restrict the contribution to controlled missing-data analysis and reconsider its Thai relevance.

4. **World models that recognize unfamiliar wheelchair dynamics** — Learn when a simulated assistive controller should gather information before navigating a difficult passage.

   **Paradigm & research question:** Embodied AI and uncertainty-aware world models. Does disagreement-directed system identification reduce collisions on unseen wheelchair dynamics better than domain randomization alone, given equal interaction budgets?

   **Thai healthcare testbed:** Wheelchair mobility through locally measured rehabilitation-clinic or home layouts. **Unverified:** relevant doorway widths, thresholds, surfaces, and wheelchair specifications.

   **Experiment on the laptop:** Build a simplified differential-drive wheelchair in [MuJoCo](https://mujoco.org/), using proprioception and simulated range sensing. Run **8–16 CPU environments**, not a large photorealistic simulation. Compare a 2–5M-parameter dynamics ensemble with planning, a single dynamics model, randomized PPO, and calibrated physics-based control. Measure collisions, success, adaptation interactions, and uncertainty calibration on held-out geometry/dynamics combinations. Budget **100–200 GPU-hours plus CPU simulation; 3–8 GB VRAM**.

   **Socratic stress-test:** The simulator must contain the failure mechanisms that matter. **Month one:** validate geometry and wheel-contact behavior against measurements. Claim simulator generalization only unless real transfer becomes feasible.

5. **Evidence-preserving diffusion for Thai clinical timelines** — Test whether iterative denoising can repair conflicting temporal records without altering supported facts.

   **Paradigm & research question:** Discrete diffusion. Does freezing evidence-backed fields while selectively remasking conflicts improve factual consistency over unrestricted denoising and autoregressive repair at equal compute?

   **Thai healthcare testbed:** Thai/English symptom diaries with relative dates and changing symptoms. **Unverified:** representative wording, calendar conventions, and access to evaluation examples.

   **Experiment on the laptop:** Train matched 20–40M-parameter models on 50,000 synthetic, symbolically grounded diaries, capped at 256 tokens. Compare the proposed sampler, ordinary [masked diffusion](https://arxiv.org/abs/2406.07524), autoregressive repair, and deterministic rules. Measure temporal-relation accuracy, unsupported edits, abstention, and quality versus latency. Budget **100–180 GPU-hours; 5–10 GB VRAM**, with mixed precision and small batches.

   **Socratic stress-test:** Synthetic diaries may make the problem artificially easy. **Month one:** secure 100 independently annotated, representative examples. Drop this idea if performance collapses outside generator templates.

If I were the student I'd pick #1 because it offers a clear methodological question, existing clinical labels, and modest compute needs.  
Its strongest result could be a demonstrated failure boundary, even if the proposed objective does not win.
## GEMINI — Round 1

﻿### 1. **Speckle-JEPA** — Noise-invariant latent predictive pretraining for freehand point-of-care hepatobiliary ultrasound.

* **Paradigm & research question:** *Novel Model Families (JEPA Self-Supervised Predictive Architectures).* On B-mode ultrasound corrupted by multiplicative Rayleigh speckle and acoustic shadowing, does predicting masked target representations in latent space (I-JEPA/V-JEPA with variance-covariance regularization) yield significantly higher 1%–10% low-label lesion detection and segmentation efficiency than pixel-reconstruction (MAE), contrastive (DINOv2), and diffusion representations that waste capacity modeling stochastic speckle?
* **Thai healthcare testbed:** Northeast Thailand (Isan) has the world’s highest incidence of *Opisthorchis viverrini*-associated cholangiocarcinoma (CCA), screened via rural point-of-care ultrasound (POCUS) where operator skill varies and early periductal fibrosis labels are scarce (`[Unverified: direct access to Khon Kaen University CASCAP cine loops without an institutional MOU; public abdominal ultrasound datasets + physics-based acoustic simulation serve as the verified fallback]`). High aleatoric speckle noise breaks standard pixel-level objectives.
* **Experiment on the laptop:** Pretrain ViT-Small (22M) and ViT-Base (86M) backbones under I-JEPA, MAE, SimCLR, and DINOv2 on 150k unlabeled abdominal ultrasound frames (public sets + synthetic speckle/shadow sweeps generated on the 24-core i9 via the MUST acoustic simulator). Evaluate frozen linear probes and few-shot fine-tuning on liver fibrosis/mass classification and segmentation. **Metrics:** AUROC, Dice, Expected Calibration Error (ECE), and representation invariance across synthetic probe-pressure perturbations. **Compute fit:** ~9–12 GB VRAM (BF16, batch size 128, gradient checkpointing); ~35 GPU-hours per pretraining run (~220 GPU-hours total).
* **Socratic stress-test:** *Decisive assumption:* Latent prediction naturally discards high-frequency speckle rather than encoding probe-geometry shortcuts or collapsing. *Month-1 test:* Train 22M I-JEPA and MAE models for 10 GPU-hours on 20k frames with paired independent synthetic Rayleigh realizations of identical anatomical slices; if I-JEPA cosine invariance across realizations does not exceed MAE by $\ge 15\%$, introduce an explicit physics-informed speckle-invariance regularizer.

---

### 2. **VeriMed-RSI** — Sandboxed symbolic-verifier recursive self-improvement for bilingual Thai-English clinical prescribing safety.

* **Paradigm & research question:** *Recursive Self-Improvement (RSI) & Verifier-Guided Agentic Systems.* Can a 1.5B–3B language model recursively improve its multi-constraint clinical reasoning across $\ge 5$ self-play generations—where a Proposer synthesizes adversarial cases, a Solver generates treatment plans, and a deterministic symbolic Verifier (Z3/Python) supplies exact binary rewards—without suffering mode collapse or reward hacking on held-out clinician benchmarks?
* **Thai healthcare testbed:** Thai physicians write clinical notes in macaronic Thai-English code-switching (unsegmented Thai history interleaved with English drug names, labs, and shorthand) constrained by Thailand’s National List of Essential Medicines (NLEM) and renal/hepatic dosing rules (`[Unverified: existence of an open machine-readable Thai NLEM logic database; requires encoding ~150 deterministic rules from public Thai MOPH PDFs]`). Subword fragmentation in Thai plus multi-constraint drug interactions severely stress small models.
* **Experiment on the laptop:** Use Qwen2.5-1.5B and Llama-3.2-3B (4-bit QLoRA + GRPO via Unsloth/TRL and vLLM within 12–14 GB VRAM). Encode 150 NLEM formulary, drug-interaction, and KDIGO renal-dosing constraints in Z3. Over 6 RSI iterations, train the Proposer to maximize Solver pass-rate variance while satisfying Z3 clinical validity, and train the Solver via GRPO on verifier-checked traces. Compare against static SFT, unverified self-consistency, and frozen 8B baselines. **Metrics:** Constraint violation rate, pass@1 on held-out Thai medical licensing (NL1/NL2-style) items, and semantic Vendi diversity score. **Compute fit:** ~13 GB VRAM; ~25 GPU-hours per RSI generation (~160 GPU-hours total).
* **Socratic stress-test:** *Decisive assumption:* The Proposer will synthesize clinically realistic edge cases rather than degenerate linguistic riddles that exploit parser loopholes. *Month-1 test:* Run 2 RSI iterations on 20 renal-dosing rules (12 GPU-hours) and inspect 100 generated vignettes for perplexity drift and grammar validity; if $>25\%$ are syntactically unnatural, constrain Proposer sampling with a structured Bayesian physiological grammar.

---

### 3. **WaveTTT** — Test-time hidden-state training versus Mamba-2 for non-stationary hemodynamic waveform streams.

* **Paradigm & research question:** *Novel Model Families (Test-Time Training & State-Space Models).* Under acute non-stationary physiological drift and sensor artifacts, do Test-Time Training layers (TTT-Linear/TTT-MLP, which update hidden states via self-supervised gradient steps during inference) achieve lower long-horizon forecasting error and better shock-onset calibration than frozen Mamba-2 and Transformer models, or do motion artifacts corrupt test-time weight updates?
* **Thai healthcare testbed:** Continuous monitoring of Dengue Shock Syndrome (DSS) plasma leakage and sepsis in busy Thai provincial hospitals relies on low-cost photoplethysmography (PPG) and vital-sign monitors prone to motion noise and rapid hematocrit-driven waveform changes (`[Unverified: open availability of raw Thai hospital PPG waveforms; public MIMIC-IV Waveform and VitalDB streams with simulated plasma-leakage compliance drift serve as the verified testbed]`).
* **Experiment on the laptop:** Train parameter-matched 15M-parameter sequence models (TTT-Linear, TTT-MLP, Mamba-2, RoPE-Transformer, and switching Kalman filters) on 500 hours of 125 Hz PPG/arterial waveforms (8k–32k token contexts). Evaluate zero-shot test-time adaptation on held-out patients experiencing hypotensive decompensation and injected burst artifacts. **Metrics:** 15-minute hemodynamic trajectory MAE, shock-onset AUROC, ECE, and tokens/sec on RTX 4090. **Compute fit:** ~10 GB VRAM in BF16; ~120 GPU-hours total across seeds and ablations.
* **Socratic stress-test:** *Decisive assumption:* Inner-loop self-supervised gradient updates at test time adapt to true physiological drift rather than overfitting to transient motion artifacts. *Month-1 test:* Inject 10-second motion-artifact bursts into 50 clean PPG streams and measure recovery time of TTT prediction error post-burst; if error remains elevated for $>60\text{ s}$, add an entropy/gradient-norm surprise gate to freeze inner-loop updates during artifact spikes.

---

### 4. **CompliantFlow** — Force-bounded flow-matching visuomotor policies for autonomous ultrasound probe control.

* **Paradigm & research question:** *Physical / Embodied AI (Robot Learning in Simulation & Flow Matching).* In contact-rich surface tracking over deformable, breathing anatomy, does coupling a conditional Flow-Matching visuomotor policy with inference-time Control Barrier Function (CBF) force guidance reduce safety-threshold force violations by $>50\%$ at $>50\text{ Hz}$ control rates compared to DDIM Diffusion Policy, Action Chunking Transformers (ACT), and PPO?
* **Thai healthcare testbed:** Rapidly aging rural Thai demographics and sonographer shortages motivate semi-autonomous robotic POCUS triage (`[Unverified: access to physical robot hardware; project is strictly scoped as a sim-to-sim benchmark]`). Wide variance in patient BMI, rib-cage geometry, and respiratory excursion creates strict contact-force safety constraints.
* **Experiment on the laptop:** Build a GPU-vectorized MuJoCo (MJX) environment (512 parallel instances) with a 6-DOF arm tracking abdominal scan paths over procedural torso meshes with randomized respiratory motion, tissue stiffness, and friction. Train 25M-parameter Flow-Matching, Diffusion Policy, ACT, and PPO policies on 2,000 scripted expert trajectories using wrist RGB-D and 6-axis force-torque history. **Metrics:** Acoustic window coverage (%), force violations ($>15\text{ N}$), trajectory jerk, and inference latency (ms). **Compute fit:** ~8–10 GB VRAM; ~150 GPU-hours total.
* **Socratic stress-test:** *Decisive assumption:* MuJoCo’s soft-contact solver fidelity is sufficient that force-guided policy gains are not solver-specific artifacts. *Month-1 test:* Evaluate the MuJoCo-trained policy zero-shot in Isaac Lab / Genesis with mismatched contact solvers across 50 torso meshes; if baseline rankings invert, incorporate online latent compliance identification.

---

### 5. **EpiFlow-SSM** — Continuous-time graph flow matching for multi-resolution syndromic surge nowcasting.

* **Paradigm & research question:** *Novel Model Families (Flow Matching & Graph State-Space Models).* On sparse, right-censored spatio-temporal epidemiological graphs with abrupt climate/seasonal regime shifts, does conditional Flow Matching over a Graph-Mamba encoder yield superior tail-risk calibration and $4\times$ faster sampling than spatio-temporal diffusion (DiffSTG), Graph WaveNet, and hierarchical Bayesian (INLA) baselines?
* **Thai healthcare testbed:** Thailand’s R506 surveillance tracks weekly dengue across 77 provinces alongside Northern Thailand’s extreme seasonal PM2.5 respiratory surges (`[Unverified: public sub-provincial district R506 completeness; provincial R506 and PCD air-quality station archives are publicly accessible]`). Rural reporting backfills and El Niño monsoon shifts break stationary Gaussian assumptions.
* **Experiment on the laptop:** Construct a 15-year dataset combining provincial/station graphs, GISTDA/ERA5 climate covariates, PCD daily PM2.5, and R506 syndromic counts (<10 GB SSD). Train a 12M-parameter Graph-Mamba + Flow Matching model under realistic 1–4 week reporting-delay masks. **Metrics:** Continuous Ranked Probability Score (CRPS), 95th-percentile surge Brier score, and peak-week timing MAE. **Compute fit:** ~5 GB VRAM; ~45 GPU-hours total.
* **Socratic stress-test:** *Decisive assumption:* Deep generative graph flow matching outperforms tuned tabular/statistical baselines on 77-node weekly data. *Month-1 test:* Benchmark LightGBM + conformal prediction against a baseline GNN on 10 years of provincial dengue data (4 GPU-hours); if LightGBM wins, pivot the graph to daily multi-station PM2.5 + respiratory ER admissions (~500+ nodes) where high-frequency non-linear dynamics dominate.

---

If I were the student I'd pick **#1 (Speckle-JEPA)** or **#2 (VeriMed-RSI)**—with **#2** as my single top choice because bounded symbolic-verifier RSI is at the absolute frontier of post-training research, requires zero external clinical hardware or unverified private datasets, and turns a uniquely complex Thai bilingual clinical constraint problem into a clean, reproducible 16 GB VRAM benchmark. If the student prefers computer vision and medical imaging over LLMs/agents, **#1** offers an equally clean, publishable hypothesis testing JEPA’s core theoretical claim against real physical noise.

# ROUND 2

## CLAUDE — Round 2

## Claude — Round 2 (council)

### 1. Hume audit
1. **Gemini #4 CompliantFlow: "Acoustic window coverage (%)" as a metric in MuJoCo/MJX.** MuJoCo simulates contact, not ultrasound physics. Without an acoustic simulator in the loop, "coverage" is only a geometric proxy. Also, MJX needs JAX with GPU support, which on Windows means WSL2. That's workable, but it isn't stated.
2. **Gemini #1 Speckle-JEPA: "150k unlabeled abdominal ultrasound frames (public sets)."** Public abdominal ultrasound sets are small. 150k frames is only reachable from video, where frames are highly correlated, so the *effective* sample size is much lower. Simulating realistic speckle at that scale with MUST (a MATLAB toolbox) on CPU is also slow. It needs a time estimate.
3. **Gemini #2: "pass@1 on held-out Thai medical licensing (NL1/NL2-style) items."** Whether public Thai licensing items exist is unverified, and "-style" items written by the student are not an independent benchmark.
4. **Codex #1: JEPA pretraining on KIMORE.** KIMORE is small (tens of subjects, unverified exact number). JEPA's whole argument is about *pretraining at scale*, so pretraining on KIMORE alone tests a regime where JEPA is not expected to shine. It needs large unlabeled skeleton data (e.g. NTU RGB+D) for pretraining, with KIMORE only for evaluation.
5. **Gemini #3 WaveTTT: "simulated plasma-leakage compliance drift" as the dengue testbed.** That means inventing physiology. The Thai dengue link becomes decoration on MIMIC/VitalDB data, which is the thing the brief warns against.

### 2. Convergence verdict
- **RSI cluster: both strength and obviousness.** Verifiable reward is the textbook RSI setup (math, code), so we all reached for the nearest verifiable *healthcare* domain. That's the obvious part. The strong part is that medication logic is verifiable *outside* math and code, and Thai makes the base model start weak, so it tests whether self-improvement works from low competence.
  **Best variant: a merge.** Gemini's **Proposer–Solver self-play** (frontier, asymmetric), plus Codex's **independently implemented training vs evaluation verifiers**, plus my diversity and collapse tracking.
  **The design choice that makes it publishable:** measure the **verifier gap**. Train against verifier A, evaluate against an independent verifier B and pharmacist-written items, and report reward hacking *per iteration*. "When does RSI start fooling its own verifier?" is a real research result. "RSI improves dose accuracy" alone is a replication.
- **JEPA cluster: mostly obviousness.** "JEPA vs MAE on domain X" is a template. The one variant that tests **JEPA's core theoretical claim** (latent prediction discards unpredictable detail) with *controllable ground truth* is **Gemini's Speckle-JEPA**: paired independent speckle realizations of the same anatomy give an exact invariance test. That's the design choice that makes it publishable. My FloorJEPA depends on sim-to-real human video, and Codex's version is data-starved.

### 3. Socrates: most over-rated = Gemini #4 CompliantFlow
It breaks on the assumption that *a contact-only simulator captures what makes robotic ultrasound hard.* The hard part is image quality, which depends on acoustic coupling, angle and anatomy, and MuJoCo has none of that. Add scripted expert trajectories (which make imitation trivial) and no real robot, and the result is a force-control benchmark labelled as healthcare. My own Sachet-VLA has the opposite problem: real hardware is required, so it's a hardware risk.

### 4. Most under-rated: Codex #3, gap-aware state-space model
It beats my #5 (generative agents, which have no ground truth). It uses real public data (PPG-DaLiA), it's cheap, falsifiable, and makes a precise architectural claim. Novelty caveat: continuous-time SSMs (S4/S5-style irregular sampling) already handle Δt, so the claim must be about *activity-dependent missingness*, not just irregular timing. **Merge with Gemini #3**: a "Mamba-2 vs TTT vs gap-aware SSM under realistic dropout and artifacts" comparison is a clean, three-way architecture study.

### 5. Final top 3
| # | Project | Finish confidence | GPU-hours | Frontier-ness | Why |
|---|---|---|---|---|---|
| 1 | **Merged RSI: Proposer–Solver self-play with dual verifiers, Thai medication logic** | **70%** | 150–250 | **High** | The hottest topic on the board, fits 16 GB at 1.5–3B with QLoRA+GRPO, and the verifier gap gives a publishable result even if self-improvement stalls. |
| 2 | **Speckle-JEPA with a paired-realization invariance test** | **65%** | 150–220 | **Med–High** | It directly tests JEPA's founding claim with exact ground truth. The Thai link (Isan ultrasound screening) is motivation only unless Thai data appears. |
| 3 | **Gap-aware SSM vs TTT vs Mamba-2 on wearables (Codex #3 + Gemini #3)** | **70%** | 80–150 | **Med–High** | Real public data and a precise architectural comparison. Lowest risk, but the weakest Thai specificity. |

## CODEX — Round 2

**My verdict: retain rehabilitation JEPA first; narrow medication RSI substantially; promote a reduced WaveTTT project above my diffusion proposal.** Convergence supports tractability, but does not establish novelty.

**1. Hume audit**

1. **Claude:** “STaR/ReST-EM-style self-training usually relies on noisy LLM judges.” This mischaracterizes the cited precedents. STaR filters using answer correctness; ReST-EM explicitly generates samples and filters them using binary feedback. An executable verifier alone therefore does not distinguish DoseLoop from these methods. [STaR](https://research.google/pubs/star-self-taught-reasoner-bootstrapping-reasoning-with-reasoning/), [ReST-EM](https://arxiv.org/abs/2312.06585).

2. **Gemini:** “Z3 clinical validity.” Z3 establishes satisfaction of encoded constraints, conditional on correct rules and parsing. It cannot establish that those rules exhaust clinical correctness. Neither the 150-rule knowledge base nor its coverage is demonstrated. Licensing-exam performance is also an unverified transfer target for training on that narrow rule system.

3. **Gemini, Speckle-JEPA:** “~35 GPU-hours per pretraining run (~220 GPU-hours total).” Two backbone sizes across four named pretraining objectives already imply eight runs: **280 hours at one seed**, or 840 at three seeds, before ablations. The proposed 150,000-frame abdominal corpus is unnamed; “public sets” does not establish access, anatomical relevance, or independent patient counts. The batch-128 VRAM claim lacks image-resolution and masking details.

4. **Gemini, CompliantFlow:** “Acoustic window coverage (%).” The described contact simulator supplies no acoustic imaging model or validated visibility oracle. Geometric scan-path coverage could be measured; acoustic coverage remains undefined. Likewise, 512 rendered environments within 8–10 GB requires a benchmark, not an assertion.

5. **Gemini, WaveTTT:** “simulated plasma-leakage compliance drift serve as the verified testbed.” Simulation availability does not verify physiological fidelity or dengue transfer. VitalDB is a real, accessible dataset of **6,388 surgical patients**, supporting perioperative waveform research; it does not establish the proposed dengue-shock setting. [VitalDB documentation](https://vitaldb.net/docs/?documentId=OpenDataset%2FOverview.md).

**2. Convergence verdict**

**RSI: mostly obviousness at the paradigm level, strength at the experimental-design level.** Small-model self-training plus executable rewards is an established template. The best variant merges my adversarial-verifier proposal with Claude’s simpler dose/unit arithmetic scope, using bilingual instruction-consistency tasks rather than treatment planning.

The single publication-enabling choice is **holding out entire semantic composition families**, evaluated with independently implemented verifiers and pharmacist-audited wording. This can reveal whether recursive curricula improve transferable reasoning or merely exploit generator/verifier regularities. Compare against static training with equal generation and training budgets.

**JEPA: mixed convergence.** “Predict latents rather than noisy pixels” is an obvious template; the important research question is which information invariance destroys. Rehabilitation skeleton JEPA remains strongest because clinical movement scores provide an evaluation target without requiring large-scale video pretraining. KIMORE documents 78 participants, although download access remains to be confirmed. [KIMORE paper](https://pubmed.ncbi.nlm.nih.gov/31217121/).

The single publication-enabling choice is **paired evaluation of nuisance invariance and impairment sensitivity**: representations must ignore camera changes while retaining clinically meaningful movement changes. That supports a defensible failure-boundary study even without superior average accuracy.

**3. Socrates: most overrated**

**Gemini’s broad VeriMed-RSI.** Its decisive assumption is that satisfying a compact symbolic rule set adequately represents correctness of bilingual clinical treatment plans. If that fails, recursive optimization can increase verifier scores while degrading meaningful correctness. Restricting the task to explicitly specified instruction semantics rescues the research question; adding more self-play generations does not.

**4. Most underrated**

**Gemini’s WaveTTT, narrowed to artifact-induced adaptation failure**, beats my clinical-timeline diffusion idea. TTT-Linear and TTT-MLP are documented methods, and accessible waveforms offer observations beyond a synthetic language generator. [TTT paper](https://arxiv.org/abs/2407.04620).

The stronger project compares gated adaptation against Mamba and fixed predictors under held-out artifact and missingness mechanisms. Drop the dengue claim unless relevant evidence becomes available; Thai monitoring relevance still needs local corroboration.

**5. Final top three**

These are **subjective completion probabilities**, not measured frequencies. GPU budgets cover reduced studies with baselines, targeted ablations, and three seeds; no laptop throughput was measured.

| Rank and scoped project | Nine-month confidence | GPU-hours | Frontier-ness | Reasoning |
|---|---:|---:|---|---|
| **1. Impairment-preserving rehabilitation JEPA** | **82%** | **80–160** | **Medium** | A 5–15M skeleton encoder permits rigorous participant-held-out evaluation, with scientific value in identifying when invariance erases impairment. |
| **2. Verifier-transfer RSI for Thai/English medication instructions** | **76%** | **180–350** | **Medium** | A 1.5B LoRA model, short contexts, and three self-training rounds make semantic generalization and verifier exploitation measurable without broad prescribing claims. |
| **3. Artifact-gated TTT versus missingness-aware state-space models** | **72%** | **100–220** | **Medium** | Small 3–8M models with waveform patching can isolate adaptation’s recovery and failure mechanisms, provided patient separation and causal evaluation prevent leakage. |
## GEMINI — Round 2

﻿## Round 2 — Council Cross-Examination (Gemini)

### 1. Hume Audit: 5 Specific Claims from Claude & Codex

1. **Claude #1 (DoseLoop) — Understated GPU-hour budget for 7B–8B iterative self-training:**
   * *Claim:* `"Qwen2.5-7B / Typhoon-class 7–8B, QLoRA 4-bit (~10–12 GB VRAM)... About 8–15 GPU-hours per iteration × 8 iterations ≈ 100 GPU-hours."`
   * *Audit:* In STaR/ReST-EM loops, the compute bottleneck is not QLoRA weight updates; it is **autoregressive rollout generation** (sampling $K=8\text{–}16$ traces across thousands of problems per round) plus running the **LLM-judge baseline** across 8 iterations. On an RTX 4090 Laptop (16 GB VRAM, 150–175W thermal envelope), running two 8-round loops (verifier-gated vs. judge-gated) plus 3-seed baselines with 7B–8B models realistically requires **220–350 GPU-hours**, and co-hosting vLLM generation with QLoRA training in 16 GB VRAM causes frequent OOM fragmentation unless process-isolated. Scaling down to **1.5B–3B** (Codex #2 / Gemini #2) is required to fit the 100–180 GPU-hour envelope.

2. **Codex #1 (Rehabilitation JEPA) — Dataset size vs. compute mismatch on KIMORE:**
   * *Claim:* `"Use the published KIMORE rehabilitation dataset... Train 5–15M-parameter skeleton encoders... Budget 80–150 GPU-hours; 4–8 GB VRAM, using short skeleton clips."`
   * *Audit:* KIMORE contains only **78 participants** across 5 exercises (~390 short recordings total). Training a 5–15M-parameter skeleton model on <400 low-dimensional joint trajectories takes **<2 GPU-hours** on a 4090 Laptop, not 80–150. More critically, ~390 sequences is orders of magnitude too small for self-supervised JEPA pretraining to avoid memorization unless pretrained first on a large action corpus (e.g., NTU RGB+D 120).

3. **Claude #2 (FloorJEPA) — Unverified RGB sim-to-real transfer from MuJoCo/Genesis:**
   * *Claim:* `"Pretrain ViT-S/16 JEPA on unlabeled video: public activity datasets + simulated humans in MuJoCo/Genesis performing floor transitions and falls"`
   * *Audit:* Standard MuJoCo/Genesis rendering lacks realistic loose Thai home clothing (*pha sin*/sarongs), skin shading, and low-cost CCTV compression/lighting artifacts. Pretraining a pixel-level ViT-S/16 on synthetic RGB frames strongly risks learning renderer-specific texture shortcuts that fail to transfer to real home video.

4. **Claude #3 (Diffusion vs. AR LMs) — Confounded LLaDA-8B zero-shot and under-tokenized 150M scratch training:**
   * *Claim:* `"Train ~150M AR vs ~150M MDLM from scratch on a Thai corpus plus a synthetic instruction corpus (~40 GPU-hours each). Also run LLaDA-8B (4-bit) zero-shot."`
   * *Audit:* `LLaDA-8B` was pretrained overwhelmingly on English/Chinese; its zero-shot competence on unsegmented Thai script (`ฉลากยา`) is unverified and confounded by byte-fallback tokenization. Furthermore, 40 GPU-hours of from-scratch pretraining (~3–4B tokens) is below the compute threshold where masked diffusion LMs converge to match AR perplexity, creating an under-trained baseline.

5. **Codex #2 (Adversarial Verifier) — Miscalibrated VRAM and microbatching for 1.5B LoRA:**
   * *Claim:* `"Use Qwen2.5-1.5B, four-bit weights, LoRA, 512-token contexts, and microbatch one... Budget 120–220 GPU-hours; 8–13 GB VRAM."`
   * *Audit:* `Qwen2.5-1.5B` in 4-bit LoRA with 512-token context uses **<3.5 GB VRAM** at microbatch 1 (not 8–13 GB), starving the 4090's tensor cores. Microbatch 16–32 fits easily inside 10 GB VRAM and cuts wall-clock training time by $4\text{–}6\times$.

---

### 2. Convergence Verdict: RSI and JEPA Clusters

* **Strength or obviousness?** **Both.** Under the strict intersection of *frontier ML paradigm + single 16 GB laptop + zero wet-lab/clinical hardware*, the feasible space naturally funnels toward (a) small-LM post-training where clinical rules provide free programmatic rewards (**RSI**), and (b) compact self-supervised encoders where latent prediction addresses clinical noise/label scarcity (**JEPA**). The *topic* convergence is an obvious structural attractor of the prompt constraints; however, the *methodological* convergence on exact formal verifiers and nuisance-invariant latents is a genuine signal of 9-month solo feasibility.
* **RSI Cluster — Best Variant & Publishable Design Choice:**
  * *Best variant:* **Merged Codex #2 + Gemini #2 (`VeriMed-RSI` at 1.5B–3B)**, incorporating Claude #1's **verifier-gated vs. LLM-judge-gated** learning curve comparison. Pure dosing arithmetic (Claude #1) is too easily solved by tool-use/calculators; bilingual Thai-English multi-constraint prescribing/instruction consistency stresses compositional reasoning.
  * *Publishable design choice:* **Dual-verifier Goodhart auditing.** Train an adversarial Proposer + Solver loop against a *training* symbolic verifier (Z3/Python), but evaluate every iteration against an *independently implemented, held-out constraint verifier* and an LLM-judge baseline to pinpoint the exact iteration and curriculum pressure where self-improvement flips from compositional transfer to verifier exploitation.
* **JEPA Cluster — Best Variant & Publishable Design Choice:**
  * *Best variant:* **Merged Codex #1 (`Rehab-JEPA` framing) + Gemini #1 (`Speckle-JEPA` physics simulator).** Codex #1 identifies the sharpest theoretical flaw in medical JEPA—that invariance to nuisance can accidentally erase subtle clinical impairment/pathology—while Gemini #1 provides the large-scale unlabeled data + MUST acoustic physics simulator that KIMORE lacks.
  * *Publishable design choice:* **Factored nuisance-vs-pathology latent conditioning.** Explicitly condition the JEPA predictor on controlled nuisance parameters (acoustic speckle/probe pressure or camera viewpoint) while forcing the target encoder to preserve pathology, plotting the **invariance–sensitivity Pareto frontier** where vanilla JEPA collapses subtle clinical signals.

---

### 3. Socrates: Single Most Over-Rated Idea

* **Claude #2 (`FloorJEPA` — ranked #2 and co-recommended by Claude)** *(with Claude #4 `Sachet-VLA` a close second due to transparent deformable bag physics).*
* **The assumption that breaks it:** **That distinguishing floor-living postures from falls requires pixel-level V-JEPA video foundation pretraining on simulated humans rather than an off-the-shelf 2D/3D pose extractor.** In reality, running a frozen lightweight pose detector (e.g., RTMPose/YOLOv8-Pose) converts raw video into 17-joint coordinates, eliminating lighting, clothing, privacy, and MuJoCo RGB sim-to-real gaps at once. On 16 GB VRAM, pixel-level V-JEPA pretrained on synthetic human renders will spend 200 GPU-hours overfitting to renderer textures and lose to a 2M-parameter temporal model trained on extracted pose skeletons in 3 GPU-hours.

---

### 4. Most Under-Rated Idea from Another Advisor

* **Codex #3 (`Elapsed-Time-Conditioned Selective SSM / Mamba`)** beats **Gemini #5 (`EpiFlow-SSM`)** (and my simulator-dependent **Gemini #4 `CompliantFlow`**).
* **Why it wins:** My `EpiFlow-SSM` faces a classic tabular trap: on 77 Thai provinces over 780 weeks, tuned LightGBM + conformal prediction likely matches a 12M Graph-Mamba Flow-Matching model. In contrast, Codex #3 targets a genuine mathematical blind spot in Mamba—whose discretization step $\Delta_t$ depends only on input token $x_t$ and conflates missing sensor gaps with contiguous steps—using compact 1–5M models on public physiological streams (`PPG-DaLiA`).

---

### 5. Final Top 3 Recommendations

1. **Adversarial Dual-Verifier RSI for Bilingual Thai Clinical Constraints** *(Merged Gemini #2 + Codex #2 + Claude #1)*
   * **Confidence:** 90% | **Realistic GPU-hours:** 140–180h | **Frontier-ness:** High
   * **Reasoning:** Combining 1.5B–3B GRPO self-play, adversarial problem generation, Claude’s verifier-vs-judge curve, and Codex’s held-out evaluation verifier yields a rigorous study of reward hacking vs. compositional generalization with zero external data bottlenecks.

2. **Gap-Aware TTT-Mamba for Non-Stationary Clinical Waveforms** *(Merged Codex #3 + Gemini #3)*
   * **Confidence:** 92% | **Realistic GPU-hours:** 80–120h | **Frontier-ness:** High
   * **Reasoning:** Unifying Codex’s elapsed-time-conditioned Mamba state transitions with Gemini’s surprise-gated Test-Time Training directly solves how sequence models adapt to physiological drift (e.g., dengue shock) without corrupting weights during sensor dropouts or motion artifacts.

3. **Pathology-Preserving Factored JEPA (`Speckle/Rehab-JEPA`)** *(Merged Codex #1 + Gemini #1)*
   * **Confidence:** 82% | **Realistic GPU-hours:** 110–190h | **Frontier-ness:** Med–High
   * **Reasoning:** Merging Codex’s nuisance-vs-impairment disentanglement objective with Gemini’s physics-simulated ultrasound perturbations (or NTU-pretrained pose skeletons) turns a standard JEPA application into a principled test of when latent prediction erases clinical signal.
