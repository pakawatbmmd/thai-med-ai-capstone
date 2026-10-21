# Vector 2: Personalised and optimised care pathways. Foundation models of patient trajectories, causal treatment optimisation and Thai data assets (as of Oct 2026)

Scope: McKinsey's second vector ("AI trained on large volumes of individual history and outcomes data … picks the best treatment for each individual"). The McKinsey piece only names this vector and gives it no analysis (see `00_guidance_mckinsey_summary.md`). These notes supply the technical frontier.

Verification legend:
- **[V]** means I opened the primary page or abstract this session.
- **[S]** means it comes from a search-engine summary or secondary coverage that I did not open in full.
- **[K]** means background from my prior knowledge that I did not re-verify this session. Treat [K] as a pointer to check, not as a citable fact.

Recency is marked as (2024), (2025), (2026), or "OLDER" for anything before 2024.

---

## Q1. Generative and foundation models of patient trajectories: scale, data, what they predict, performance, compute

### Takeaway
The field has split into two camps:
- **Small "natural-history" models.** Delphi-2M has about 2M parameters and trained in 1 GPU-hour on 0.4M UK Biobank (UKB) participants. It forecasts more than 1,000 diseases with an average AUC of about 0.76 internally and about 0.67 in Danish external validation.
- **Industrial-scale generative event models.** Epic's CoMET (renamed "Curiosity" in arXiv v3) uses 118M patients, 115B events and up to 1B parameters. MarketScan-based ReClaim uses 43.8B claims events, more than 200M enrollees and up to 1.7B parameters. Both follow power-law scaling.

The industrial models match or beat task-specific supervised models zero-shot on many tasks. However, their **calibration and subgroup performance are weak**, and none has been shown to change outcomes prospectively. Every model is trained on one health system, and almost all of those systems are in high-income countries (HICs).

### Cited Findings

**Delphi-2M (Shmatko, Gerstung et al., Nature, published online 17 Sep 2025; print 647:248–256)**
- **Architecture:** a modified GPT that models disease progression and competing risks. Trained on about 0.4M UKB participants and validated, with no parameter changes, on 1.9M Danish individuals. Predicts rates of more than 1,000 diseases "with accuracy comparable to that of existing single-disease models" — [DKFZ record](https://inrepo02.dkfz.de/record/304606); [UK Biobank](https://www.ukbiobank.ac.uk/publications/learning-the-natural-history-of-human-disease-with-generative-transformers/) [S]
- **Performance:** average AUC about 0.76 across diagnoses and about 0.97 for death (internal). Danish external average AUC about 0.67 versus about 0.69 for UKB longitudinal testing. Per-disease performance was highly correlated across the two countries — [Conexiant](https://conexiant.com/internal-medicine/articles/ai-model-predicts-multiple-disease-risk/) [S]
- **Horizon decay:** average AUC falls from about 0.76 to about 0.70 at 10 years, as quoted from the paper — [Decrypt](https://decrypt.co/340776/new-ai-system-predicts-risk-1000-diseases-years-advance) [S]
- **Data quirks:** Danish validation showed the model had learned UK-specific data-collection quirks — secondary report in [search summary of Delphi coverage](https://makingpharmaindustry.it/en/?p=24841) [S, weak source]
- **Compute and licence:**
  - The original model trained in **1 GPU-hour on one NVIDIA V100**. A demo trains in about 10 minutes on a single GPU, and in about 10 hours on an Apple M1.
  - Code is MIT-licensed. The weights are CC BY-NC-ND 4.0 and distributed only through UK Biobank controlled access. A patent application is noted.
  - Other datasets can be used if formatted per `data/README.md`. A small model-generated synthetic dataset ships for code testing.
  - Source: [GitHub gerstung-lab/Delphi](https://github.com/gerstung-lab/Delphi) [V]
- **Parameter count:** DT-Transformer's authors describe Delphi as GPT-style, and they reimplemented it at about 2.2M parameters, 12 layers and 120-dimensional embeddings (that is DT-Transformer's own configuration) — [arXiv 2605.14227](https://arxiv.org/html/2605.14227v1) [V]. "Delphi-2M" refers to about 2M parameters [K].
- **Synthetic data:** the model can generate synthetic trajectories up to 20 years ahead — [Conexiant](https://conexiant.com/internal-medicine/articles/ai-model-predicts-multiple-disease-risk/) [S]. The paper reports that a model trained only on Delphi-generated synthetic data loses only a few AUC points (about 0.74 vs 0.76) [K, check Fig. in paper].

**Epic CoMET → "Curiosity" (Epic, Microsoft, Yale; arXiv 2508.12104, Aug 2025, v3 Nov 2025)**
- **Data:** Epic Cosmos holds 16.3B encounters, more than 300M patients and 310 health systems. Pretraining used **118M patients and 115B medical events (151B tokens)**.
- **Model and results:**
  - Decoder-only, compute-optimal models of **up to 1B parameters**.
  - Evaluated on **78 tasks** (diagnosis, prognosis, operations). It "generally outperformed or matched task-specific supervised models" with no fine-tuning or few-shot examples.
  - The abstract reports no GPU-hours and no weight release.
  - Source: [arXiv 2508.12104](https://arxiv.org/abs/2508.12104) [V]
- **Architecture details:** Qwen2 architecture with random initialisation. Described as the largest scaling-law study on medical events, with power laws for compute, tokens and parameters. Epic UGM material says 136B tokens while the paper says 151B — [arXiv PDF / search summary](https://arxiv.org/pdf/2508.12104) [S]. Epic planned access via the "Cosmos AI Lab" from Feb 2026 — [Surety Systems UGM recap](https://www.suretysystems.com/insights/epic-ugm-2025-highlights-and-insights-surety-systems) [S]
- **First independent-ish clinical evaluation (medRxiv, May 2026):**
  - **Setting:** 1B-parameter Curiosity, zero-shot, 3,000 discharged emergency department (ED) abdominal-pain patients, 50 simulated 30-day trajectories each.
  - **Primary endpoint:** AUROC **0.83 vs 0.76** for a tuned XGBoost trained on 100k patients (P=.002) for 30-day admit-revisit. AUPRC 0.37 vs 0.22.
  - **Other endpoints:** significant on only 5 of 9 outcome-horizon pairs. No gain for discharge-revisit.
  - **Calibration:** calibration-in-the-large was negative on all 9 endpoints (−0.84 to −0.42), so it **over-predicts absolute risk**. XGBoost was better calibrated.
  - **Subgroups:** AUROC **0.64 for Hispanic/Latino, 0.58 for self-pay, 0.56 for "other race"**, with calibration slopes of 0.29–0.48.
  - **Limits:** the test cohort came from the same network as pretraining, and the model uses coded events only.
  - Source: [medRxiv 2026.05.18.26353199](https://www.medrxiv.org/content/10.64898/2026.05.18.26353199v2.full) [V]

**ReClaim, a generative claims foundation model (arXiv 2605.02740, May 2026)**
- Trained on **43.8B medical events from more than 200M MarketScan enrollees (2008–2022)**, at 140M, 700M and 1.7B parameters. Disease-onset prediction comes through post-training. Reported to beat strong baselines in-domain (claims) and out-of-domain (EHR) — [arXiv 2605.02740](https://arxiv.org/html/2605.02740v1) [S]. This is the closest analogue to what an NHSO-claims model would be.

**DT-Transformer (Mass General Brigham; arXiv 2605.14227, May 2026)**
- **Data:** 57.1M diagnosis events, about 1.79M patients, 11 hospitals plus more than 200 clinics, 1,375 ICD categories. About 2.2M parameters with a 93-token context. Compute not reported.
- **Held-out median AUC** (vs age-sex baseline): next-event **0.871** (0.657), 6 months 0.788, 1 year 0.767, 2 years 0.733, 3 years 0.706.
- **Prospective 2024 test:** median AUC **0.713 across 898 diseases**, beating the baseline for 80% of them.
- **Subgroups:** consistently better in females than males.
- **vs Delphi-2M:** stronger near-term discrimination but faster long-horizon decay, attributed to EHR data density and leakage (care outside the MGB network is unobserved).
- Source: [arXiv 2605.14227](https://arxiv.org/html/2605.14227v1) [V]

**Foresight (KCL/UCL; Lancet Digital Health 2024; national NHS version 2025)**
- **2024 hospital model:** trained on about 1M King's College Hospital patients, about 20k from South London and Maudsley (SLaM) and 50k from MIMIC-III. Next-concept precision@10 was 0.80, 0.81 and 0.91. Next-disorder precision@10 was 0.68, 0.76 and 0.88 in the preprint. Five clinicians judged the top forecast disorder relevant in 97% of 34 synthetic timelines — [arXiv 2212.08072](https://arxiv.org/pdf/2212.08072); [UCL Discovery](https://discovery-pp.ucl.ac.uk/id/eprint/10190262) [S]
- **2025 national model:** trained on NHS England data for **57M people** (GP, hospital, prescriptions, vaccination) inside the NHS England Secure Data Environment (SDE). **Paused in June 2025** after the BMA/RCGP objected that GP data collected for COVID research (GDPPR) was used without their knowledge, and an ICO complaint was prepared. I found no confirmed resumption — [Digital Health](https://www.digitalhealth.net/2025/06/ai-project-to-predict-health-outcomes-paused-over-gp-data-concern); [Pulse](https://www.pulsetoday.co.uk/news/technology/nhs-england-pauses-ground-breaking-ai-project-following-gp-data-concerns/) [S]. This is a cautionary governance precedent directly relevant to any NHSO-scale model.

**Stanford CLMBR / MOTOR / EHRSHOT (Shah lab)**
- **MOTOR (ICLR 2024):** a self-supervised time-to-event foundation model on EHR and claims, scaled to **55M patient records (9B events)**. Evaluated on 19 tasks across 3 databases (Stanford EHR, MIMIC-IV, Merative claims). Time-dependent C-statistic up 4.6% over prior state of the art, up to 95% better label efficiency, and more robust to temporal shift. A **143M-parameter model is released on Hugging Face** — [arXiv 2301.03150](https://arxiv.org/abs/2301.03150v3) [S]
- **EHRSHOT (NeurIPS 2023 D&B, OLDER):** 6,739 Stanford patients, 41.6M events, 921,499 encounters, 15 few-shot tasks. Released **CLMBR-T-base (141M parameters, pretrained on 2.57M patients)**. The foundation model generally beats a count-based gradient-boosted machine (GBM) few-shot, **except on "assignment of new diagnoses", where the GBM wins** — [EHRSHOT](https://ehrshot.stanford.edu/); [arXiv 2307.02028](https://www.alphaxiv.org/abs/2307.02028) [S]

**ETHOS (Renc, Sitek et al., npj Digit Med 2024)**
- A zero-shot "patient timeline simulator" trained on single-hospital MIMIC-IV [K]. An independent re-evaluation on MIMIC-IV found it "underperforms substantially across all metrics, largely because it cannot predict many EHR event types". A 2026 follow-up reports that a 9M "ETHOS-DAPO" (RL-tuned) model beats the 56M ETHOS-PT on readmission AUROC — [EHR2Path arXiv 2506.04831](https://arxiv.org/pdf/2506.04831); [arXiv 2509.25591](https://arxiv.org/pdf/2509.25591) [S]

**Older baselines (OLDER, all [K])**
- **Med-BERT:** BERT on structured codes, 28M patients (Cerner), npj Digit Med 2021 — [npj](https://www.nature.com/articles/s41746-021-00455-y)
- **TransformEHR:** encoder-decoder, 6.5M US Veterans Affairs (VA) patients, Nat Commun 2023 — [Nat Commun](https://www.nature.com/articles/s41467-023-43715-z)
- **CLMBR:** autoregressive code-level pretraining on Stanford EHR, 2021.
- None was re-verified this session.

**Other 2025–2026 successors and variants**
- **"The Watcher":** a generative foundation model for structured trajectories from a **Japanese** university hospital, built on a national HL7 message standard. This is the only Asian generative-trajectory model I found — [PMC12099423](https://pmc.ncbi.nlm.nih.gov/articles/PMC12099423/) [S]
- **RL fine-tuning of EHR foundation models (arXiv 2609.12277, Sep 2026):** treats the foundation model as a generative policy over trajectories, with time-aware rollout rewards. Claims smaller RL-tuned models beat larger pretrained ones in data-limited regimes. **No numbers in the abstract** — [arXiv 2609.12277](https://arxiv.org/abs/2609.12277) [V]
- **SCOPE/REACH estimators (arXiv 2602.03730):** make generative (Monte-Carlo rollout) prediction cheaper — [arXiv](https://arxiv.org/pdf/2602.03730) [S]
- **Other variants:** tokenisation trade-offs (arXiv 2603.15644), token-level explainability X-FEMR (arXiv 2607.06163), and a multimodal oncology longitudinal model (arXiv 2608.24688, which notes Delphi-2M and MOTOR introduced time-to-event objectives) — [arXiv 2603.15644](https://arxiv.org/pdf/2603.15644); [arXiv 2607.06163](https://arxiv.org/pdf/2607.06163); [arXiv 2608.24688](https://arxiv.org/html/2608.24688v1) [S]

### Inferences
- **Small scale works for disease-code trajectories.** Delphi-2M and DT-Transformer are each about 2M parameters. A Delphi-class model on Thai data is **trivially trainable on an RTX 4090 Laptop (16 GB)**: Delphi needed 1 V100-hour. Even a 100–150M MOTOR or CLMBR-class model can be fine-tuned on 16 GB. Compute is therefore not the binding constraint for a POC. **Data access is.**
- **Zero-shot gains come with calibration debts.** Industrial generative models' zero-shot wins coexist with poor calibration and subgroup collapse (Curiosity: self-pay 0.58). For "picking the best treatment" (McKinsey vector 2), calibration and subgroup validity matter more than average AUROC. This is an under-served evaluation niche.
- **All flagship models are prognostic, not prescriptive.** They predict "what happens next under usual care". None estimates "what would happen under treatment A vs B" with causal validity. That is the gap between the trajectory models and McKinsey's "optimised pathways".

### Gaps
- Exact Delphi-2M per-disease Danish AUC distribution, calibration plots and the synthetic-training AUC could not be read (Nature paywall redirect). The 0.74 synthetic figure is [K].
- No GPU-hour figures for CoMET/Curiosity or ReClaim, and no weight release for either.
- Whether NHS England's Foresight resumed after the 2025 DPO review: no source found.
- I did not open the ETHOS, Med-BERT or TransformEHR primary papers this session.

---

## Q2. Causal and treatment optimisation: target trial emulation with ML, counterfactual trajectories, causal foundation models, offline RL and DTRs, conformal uncertainty, known failures

### Takeaway
Treatment *optimisation* lags far behind trajectory *prediction*:
- **Target trial emulation (TTE)** is the accepted causal workhorse. It is becoming federated and "agentic", but remains classical (inverse probability weighting (IPW), TMLE, MSMs).
- **Causal foundation models** (Do-PFN) are proven only on synthetic and semi-synthetic benchmarks.
- **Offline RL for treatment policies** is under explicit methodological attack: random baselines sometimes match it on sepsis.
- **Conformal methods** for EHR foundation models only appeared in 2026, and only for prediction, **not for individual treatment effects**.

The specific combination — a generative trajectory foundation model used as a counterfactual simulator under a TTE protocol, with calibrated individual uncertainty — appears to be named as an open research topic but **not yet solved**.

### Cited Findings

**Target trial emulation + ML**
- **Federated TTE (npj Digit Med 2025):** estimates survival-outcome treatment effects across distributed EHRs without pooling data. Not generative — [npj Digit Med](https://www.nature.com/articles/s41746-025-01803-y) [S]
- **"Agentic trial emulation" (medRxiv, Feb 2026):** treats the randomised controlled trial (RCT) estimate and the local EHR estimate as noisy readings of a latent effect. Outputs a distribution (local effect, system-level uncertainty, probability that benefit persists) to learn **health-system-specific** effects — [medRxiv 2026.02.19.26346539](https://www.medrxiv.org/content/10.64898/2026.02.19.26346539v1.full.pdf) [S]. This is directly relevant to "does a UK/US trial effect hold in Thailand?"
- **Methods papers:**
  - Longitudinal TMLE with joint calibrated weights for per-protocol effects — [arXiv 2606.04673](https://arxiv.org/pdf/2606.04673) [S]
  - "Information Set Emulation", giving causal certificates for AI-derived EHR features — [arXiv 2609.17777](https://arxiv.org/pdf/2609.17777) [S]
  - Tooling: R `TrialEmulation` ([arXiv 2402.12083](https://arxiv.org/pdf/2402.12083)) and R `TTE` tutorial ([arXiv 2608.01625](https://arxiv.org/pdf/2608.01625)) [S]
- **NeurIPS 2026 workshop on world models for high-stakes health:** lists counterfactual outcome prediction, treatment-effect modelling, TTE and "patient world models" from longitudinal data as open topics. This signals that it is frontier, not solved — [WMHS NeurIPS 2026](https://wmhs-neurips.github.io/WMHS/) [S]

**Causal foundation models**
- **Do-PFN (Robertson, Hollmann, Hutter, Schölkopf et al.; NeurIPS 2025):** a prior-data fitted network pretrained on synthetic structural causal models with interventions. It predicts conditional interventional outcomes from observational data in-context, without the true graph. Validated **only on synthetic and semi-synthetic benchmarks** — [arXiv 2506.06039](https://arxiv.org/abs/2506.06039v2); [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ff997469ac66cf893c4183efeb22212a-Abstract-Conference.html) [S]
- **CausalPFN (2025):** an amortised CATE estimator in the same family [K, not found in search]. Tabular foundation models are also being applied to claims (TabPFN on health-insurance claims, R² 0.978) — [PMC13352762](https://pmc.ncbi.nlm.nih.gov/articles/PMC13352762/) [S]
- **Counterfactual sequence models:** Causal Transformer (Melnychuk et al., ICML 2022), G-Net and CRN are the standard OLDER counterfactual-trajectory baselines. They are mostly validated on simulated tumour-growth or MIMIC semi-synthetic data [K].

**Offline RL and dynamic treatment regimes (DTRs)**
- **Luo et al., ICML 2024 position paper:** more than 17,000 experiments on a public sepsis dataset. RL conclusions flip with the evaluation metric and MDP formulation, and **random baselines sometimes match or beat RL**. The authors call for naive and supervised baselines and consistent off-policy evaluation (OPE) — [PMLR v235](https://proceedings.mlr.press/v235/luo24f.html); [arXiv 2405.18556](https://arxiv.org/html/2405.18556v2) [S]
- **ICLR 2024:** retrospective metrics imply lower mortality under RL sepsis policies, but clinician studies find the recommendations often spurious, owing to limited action and outcome diversity in the data — [ICLR 2024](https://iclr.cc/virtual/2024/23559) [S]
- **Model-based roll-out critique of AI Clinician-style policies (2020, OLDER):** bias toward discharge, preference for high vasopressor doses, implausible discharge without weaning — [arXiv 2010.04279](https://arxiv.org/pdf/2010.04279.pdf) [S]
- **Gottesman et al., Nat Med 2019, guidelines (OLDER):** reward definition, confounding and long-horizon OPE pitfalls — [PDF](https://finale.seas.harvard.edu/sites/scholar.harvard.edu/files/finale/files/guidelines_for_reinforcement_learning_in_healthcare.pdf) [S]. Original AI Clinician: Komorowski et al., Nat Med 2018 [K].

**Conformal and uncertainty for individual predictions**
- **StratCP ("Act or Defer", ICML 2026):** stratified conformal control of false-discovery rate for patients an **EHR foundation model** selects for action, plus coverage-targeted sets for deferred patients — [ICML 2026](https://icml.cc/virtual/2026/71791) [S]
- **THCM-CAL (EMNLP Findings 2025):** causal and conformal calibration for multi-label risk. Notes that conformal clinical forecasting mostly targets single labels — [arXiv 2506.17844](https://arxiv.org/pdf/2506.17844) [S]
- **Exchangeability:** conformal guarantees assume exchangeability, which covariate shift and missingness in health data violate — [Frontiers Bioinform 2025](https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2025.1507448/full) [S]
- I found **no work on conformal intervals for counterfactual or generative trajectories or for individual treatment effects inside EHR foundation models** (search returned none).

**Known failure modes (documented above)**
- Confounding by indication and lack of action diversity (sepsis RL).
- Evaluation-metric fragility (Luo 2024).
- Within-network data leakage and censoring (Curiosity, DT-Transformer).
- Learned data-collection artefacts (Delphi in Denmark).
- Subgroup calibration collapse (Curiosity).
- Temporal shift (MOTOR explicitly tests robustness to it).

### Inferences
- **The most defensible "novel" causal contribution is an evaluation-plus-guardrail layer, not a new RL policy.** For example:
  - use a trajectory foundation model as a *simulator* inside an explicit TTE protocol (eligibility, time zero, treatment strategies, per-protocol estimand);
  - benchmark it against a classical IPW/TMLE emulation of the same target trial;
  - wrap the output in conformal or abstention ("act or defer") rules.

  Each piece exists; the composition, especially in an LMIC single-payer setting, does not appear in the literature I found.
- **Thailand's structure is an identification asset.** It has a single dominant payer with national-ID linkage and policy changes that are natural experiments: 30-baht "treat anywhere" in 2024–2025, benefit-package changes, and the Siriraj chest X-ray AI benefit rolled out to 610 hospitals. That makes quasi-experimental designs (difference-in-differences, regression discontinuity, interrupted time series) available to validate counterfactual simulators. This is something UKB/Delphi cannot offer as easily.
- **Recommendation:** avoid offline RL for treatment policy as the capstone core unless you include the Luo-2024 baselines. Committee reviewers who know that literature will attack it.

### Gaps
- No primary source verified for CausalPFN, Causal Transformer or G-Net this session.
- No published example found of Delphi-class or CoMET-class models used for treatment-effect estimation with validation against RCT results. This absence is itself informative but not proof.
- No 2025–2026 systematic review of offline RL in DTRs was found. The newest critiques are from 2024.

---

## Q3. Thai data assets, access rules, Thai trajectory/foundation models, federated learning

### Takeaway
Thailand has unusually complete, **national-ID-linked, code-based** data:
- NHSO UCS claims for about **47.5M** people (the THIP warehouse);
- the MOPH HDC "43 files" from all MOPH facilities;
- Health Link (about 20,000 service points), now being merged with NHSO claims under an April 2026 NHSO–BDI agreement;
- CSMBS (Comptroller-General) and SSO data;
- population-based cancer registries since 1986.

However:
- **No researcher-facing access pathway is publicly documented**; individual-level data are restricted.
- **I found no Thai generative trajectory or foundation model** on any of these sources.
- **I found no Thai federated-learning EHR study.**

Existing Thai ML on these data is classical (random forest, logistic regression) on single-region extracts.

### Cited Findings

**NHSO / UCS claims**
- **Size:** NHSO manages the budget for **more than 47.5M** UCS ("gold card") members. It has an MoU with the Comptroller-General's Department to harmonise national reimbursement databases across schemes — Thai search summary of [Matichon](https://www.matichon.co.th/local/quality-life/news_5825885) / [Hfocus](https://www.hfocus.org/content/2026/07/38920) [S]
- **Identifiers:** UCS membership uses the 13-digit national ID, so all individual records are ID-linked. NHSO publishes aggregate statistics only; individual utilisation records are not public — [WHO Kobe case study](https://wkc.who.int/docs/librariesprovider24/wkc-projects-documents/2-8-case-study-thailand.pdf); [Thailand HiT 2024](https://ihppthaigov.net/sa22/publication/download/fl_1721879588746.pdf) [S]
- **Research use exists via THIP:**
  - THIP, the NHSO data warehouse, supplied anonymised individual inpatient claims for 2017–2022 (chronic liver disease, Sci Rep 2025).
  - THIP was also used for TB readmission 2016–2022 (2026) and diarrhoea 2014–2022 (Lancet Reg Health SEA 2026).
  - THIP holds **UCS admissions only**. The MOPH database adds SSS, CSMBS and self-pay admissions.
  - An older heart-failure study (2008–2013, OLDER) linked national IDs to the civil death registry across CSMBS, SSS and UCS.
  - Sources: [Sci Rep 2025](https://www.nature.com/articles/s41598-025-16645-7); [IDP 2026](https://link.springer.com/article/10.1186/s40249-026-01467-0); [Lancet Reg Health SEA](https://www.thelancet.com/journals/lansea/article/PIIS2772-3682(26)00046-6/fulltext); [RSV-HAT 2026](https://onlinelibrary.wiley.com/doi/10.1111/irv.70263); [BMC CVD 2022](https://link.springer.com/article/10.1186/s12872-022-02629-2) [S]
- **Telemedicine e-claims (Dec 2020–Aug 2022):** analysed with interrupted time series (ITS) and logistic regression, not ML — [PMC11056088](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11056088/) [S]

**Health Link / NHSO–BDI integration (2026)**
- Health Link launched in 2023 and went national with the Public Health Cloud in 2024. It reaches **nearly 20,000 service points** (more than 10,000 NHSO units and about 8,500 clinics and pharmacies). Records cover identity, diagnoses and procedures, labs, dispensed drugs and referrals.
- **Nov 2025:** the MOPH committee approved linking MOPH and BMA data (Health Link, Mor Prom, Public Health Cloud), linking to Ministry of Labour data, and a framework for a **Digital Health Act** (not yet enacted).
- **27 Apr 2026:** NHSO and BDI agreed to upgrade Health Link, **integrate it with the NHSO claims database**, add **AI pre-audit of outpatient claims**, give patients history access via the Thang Rath app, and pilot e-Referral in Bangkok.
- Source: [Jonda Health summary citing Thairath / Healthcare IT News](https://www.jonda.health/articles/thailand-health-link-nhso-ai-claims) [V; secondary aggregator]

**MOPH HDC "43 files"**
- MOPH hospitals must regularly export the standardised 43-file dataset (PERSON, SERVICE, DIAGNOSIS_OPD, …) to the HDC. An open-source validator exists — [GitHub niratorn/MOPH_HDC_Validation](https://github.com/niratorn/MOPH_HDC_Validation) [S]
- **Example ML use:** 60,903 type 2 diabetes (T2DM) patients (2016–2023, southern Thailand) from 43 files. Random forest was best for predicting uncontrolled diabetes — [Chula J Health Res](https://digital.car.chula.ac.th/cgi/viewcontent.cgi?article=1144&context=jhr) [S]
- **Aggregated open data:** the MOPH Open Data portal provides aggregated HDC tables, for example a province-level hypertension panel for FY2017–2025 — [Zenodo](https://zenodo.org/records/23096107) [S]
- **Data quality:** an HDC-based cancer-hospitalisation trend study covers 2007–2023 — [BMC Public Health 2025](https://link.springer.com/article/10.1186/s12889-025-25682-w) [S]. The BMJ Open learning-health-system trial protocol (Chiang Mai/Lamphun, 16 primary care units (PCUs); HT → T2DM → CKD) notes HDC data are collected mainly for administrative reporting, not local learning — [NCT06873243](https://clinicaltrials.gov/study/NCT06873243); [BMJ Open](https://bmjopen.bmj.com/content/16/7/e109261) [S]

**Thai cancer registries**
- Population-based registries started in Chiang Mai (1986), Khon Kaen (1988), Bangkok (1990) and Lampang (1993). Coverage was about 27% of the population in Vol. IV (1998–2000), and 13 registries contributed by Vol. V (2001–2003). The Thai Pediatric Oncology Group runs a separate national childhood register — [NCI Thailand, Cancer in Thailand IV/V/VIII](https://www.nci.go.th/NCI_Old/th/File_download/Nci%20Cancer%20Registry/Cancer%20in%20Thailand%20VIII.pdf) [S]

**NCD (DM/HT)**
- HITAP and WHO-CCS have a planning project on which AI tools fit Thailand's DM/HT programmes. It is not a results study — [HITAP](https://www.hitap.net/?p=43927) [S]
- A Thai ML study predicts reduced kidney function in T2DM with a simplified model — [PMC12250820](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12250820/) [S]

**Access rules**
- Individual-level NHSO and HDC data are restricted. Typical requirements are institutional IRB approval plus a data-owner request. Siriraj's patient-data request form, for example, requires a confidentiality pledge and EC approval before any query — [Siriraj SIRB form](https://www.si.mahidol.ac.th/th/division/sirb/files/form/ขออนุญาตใช้ข้อมูลผู้ป่วย.doc) [S]
- NHSO published a Royal Gazette notice on criteria for **linking service-user health data under "30 baht treat anywhere"**. Its research provisions are unverified — Thai search summary [S]
- **PDPA enforcement:** more than THB 21.5M in fines by 2025, including THB 1.21M against a private hospital for exposing more than 1,000 patient records — [Jonda](https://www.jonda.health/articles/thailand-health-link-nhso-ai-claims) [S]

**Thai trajectory/foundation models and federated learning**
- Targeted searches found **no Thai generative or foundation trajectory model** on NHSO, HDC, Health Link or hospital EHR data. The closest Asian work is Japan's "Watcher" (single hospital) and Taiwan NHIRD → US transfer — [PMC12099423](https://pmc.ncbi.nlm.nih.gov/articles/PMC12099423/); [arXiv 2610.04946](https://arxiv.org/html/2610.04946) [S/V]
- **No Thai federated-learning EHR study** was found in English searches. The best transferable template is **federated generative event models across 3 health systems** (122,251 ICU stays, CLIF format, 12 tasks):
  - GEMs' cross-site AUROC penalty was **0.025 vs 0.079 for LightGBM**;
  - FedAvg approached centralised performance within a few rounds;
  - multi-site training helps most when local data are scarce;
  - **no formal privacy analysis** was reported.
  - Source: [arXiv 2608.02939](https://arxiv.org/abs/2608.02939) [V]
- **Prior Thai LLM notes:** the Thai AI ecosystem is LLM- and scribe-centred (Cariva, PresScribe, Eir-8B, Typhoon-Si-Med). Nothing touches structured trajectory modelling — `research_notes/Thai medical LLM landscape/thai_health_llm_products.md` (internal).

### Inferences
- **A "Thai-Delphi" or "Thai CoMET" is genuinely unclaimed territory.** Thailand's national-ID linkage across UCS, CSMBS, SSO, HDC, death registry and cancer registry is structurally closer to Denmark (Delphi's validation set) or Taiwan NHIRD than to US EHRs. It could support whole-population, low-leakage trajectories, which is DT-Transformer's stated weakness.
- **Realistic POC data routes, from least to most effort:**
  1. Train on public/synthetic data (MIMIC-IV, EHRSHOT, Delphi's synthetic UKB set, Synthea) and **zero-shot or fine-tune evaluate on a Thai hospital extract** (Chula/KCMH HIS or a 43-file export, under IRB).
  2. Request a THIP extract via NHSO (UCS inpatient only).
  3. Run federated training across a few MOPH hospitals' 43-file exports. Their common schema is a natural "CLIF-like" harmonisation layer.
- **Governance:** the Foresight pause and Thailand's PDPA fines mean governance design (consent, SDE-style enclave, DPO review) should be part of the capstone deliverable, not an afterthought. This also matches McKinsey's "progressive disclosure" theme.

### Gaps
- **No primary source found** for: NHSO's formal researcher data-request procedure, fees or timelines; HDC individual-level access rules; whether CSMBS and SSO data are obtainable for research in 2025–2026; or the Royal Gazette notice's research clauses. The student should ask NHSO, HISO or the Chula faculty data office directly.
- No source for record volumes (rows per year) in THIP, HDC or Health Link.
- Thai-language searches for federated learning (e.g., "การเรียนรู้แบบสหพันธ์ โรงพยาบาล") were not run because of time. A Thai FL study may exist.
- No verified information on whether the NHSO AI pre-audit is ML-based or rule-based, or on its accuracy.

---

## Q4. Unsolved problems named in 2025–2026: cross-country generalisation, fairness, calibration, actionability, synthetic data and privacy, language-free (code-based) models

### Takeaway
Cross-national transfer is **measurable and partial**:
- Delphi lost about 0.02 AUC from UK to Denmark (two HIC registries);
- Taiwan NHIRD → MIMIC transfer recovers most of the in-domain gain;
- portable "language-grounded" code embeddings (GRASP, PORTER) are the 2026 answer to vocabulary mismatch.

The open problems are:
- calibration and subgroup validity (Curiosity: self-pay AUROC 0.58);
- actionability (prognosis ≠ treatment choice);
- synthetic-data privacy audits (memorisation), now being demanded at NeurIPS 2026.

**No study tests transfer of a Delphi, CoMET or MOTOR-class model into an LMIC or Southeast Asian health system.** This is the clearest novelty hook for a Thai capstone.

### Cited Findings

**Cross-country and cross-system transfer**
- **Delphi:** UK → Denmark average AUC about 0.69 → 0.67, with UK data-collection quirks learned — [Conexiant](https://conexiant.com/internal-medicine/articles/ai-model-predicts-multiple-disease-risk/) [S]
- **Taiwan NHIRD → US (arXiv 2610.04946, Oct 2026)**
  - **Source:** **3.99M patients, 1996–2013, about 1.44B visits, 7.92B tokens**, 4-layer transformer.
  - **MIMIC-IV AUROC, from scratch → NHIRD-transferred → in-domain:**
    - 90-day mortality: 0.888 → **0.914** → 0.924
    - Long length of stay (LOS): 0.785 → **0.833** → 0.855
    - 30-day readmission: 0.625 → 0.633 → 0.637
  - **Where transfer fails:** operational outcomes such as ICU admission (EHRSHOT AUPRC 0.090 vs 0.181 baseline).
  - **Code mapping:** cross-vocabulary mapping used LLM embeddings (Qwen3-Embedding-8B + FAISS, cosine ≥ 0.8). Only 72% of SNOMED mappings were collision-free at 0.8.
  - **Not reported:** subgroup or calibration results.
  - Source: [arXiv 2610.04946](https://arxiv.org/html/2610.04946) [V]
- **GRASP (npj Digit Med, Jan 2026):** LLM-derived embeddings of medical-history codes improve transfer of disease-prediction models across the UK, Finland and the US (more than 1M people, 21 diseases plus mortality) and across coding systems — [npj Digit Med s41746-026-02363-5](https://www.nature.com/articles/s41746-026-02363-5) [S; paywall redirect]
- **PORTER (arXiv 2606.24102):** fixed-vocabulary event tokens cannot represent unseen concepts. Language-grounded event representations make structured-EHR foundation models portable across institutions — [arXiv 2606.24102](https://arxiv.org/html/2606.24102) [S]
- **US CLMBR-T-base → Italian hospital** (LOS prediction; Frontiers Digital Health 2026) tests cross-system generalisability — [Frontiers](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1956993/full) [S]. Transferability dynamics are also covered in [arXiv 2504.10422](https://arxiv.org/abs/2504.10422) [S]
- **Federated GEMs** transfer across sites far better than LightGBM (AUROC penalty 0.025 vs 0.079) — [arXiv 2608.02939](https://arxiv.org/abs/2608.02939) [V]

**Fairness and calibration**
- **Curiosity:** subgroup AUROC 0.56–0.64 with calibration slopes of 0.29–0.48 for Hispanic, self-pay and other-race patients, and systematic over-prediction of absolute risk — [medRxiv](https://www.medrxiv.org/content/10.64898/2026.05.18.26353199v2.full) [V]
- **DT-Transformer:** better in females than males, with the gap widening over the horizon. Authors call for a fairness evaluation before deployment — [arXiv 2605.14227](https://arxiv.org/html/2605.14227v1) [V]

**Actionability**
- All flagship models predict under usual care. The NeurIPS 2026 WMHS workshop frames counterfactual and treatment-effect "world models" as open problems — [WMHS](https://wmhs-neurips.github.io/WMHS/) [S]
- "Act or defer" conformal policies (StratCP) are the first error-controlled decision layer on EHR foundation models — [ICML 2026](https://icml.cc/virtual/2026/71791) [S]

**Synthetic data and privacy**
- **Delphi:** releases model-generated synthetic UKB data, but only for code testing — [GitHub](https://github.com/gerstung-lab/Delphi) [V]
- **NeurIPS 2026 position paper:** autoregressive EHR generators should be **audited like LLMs for memorisation**, using record-level membership inference and canaries — [NeurIPS 2026](https://neurips.cc/virtual/2026/177671) [S]
- **MIMIC-IV generator plus LLM audit (Mar 2026):** clinicians found inconsistencies in **45–60%** of sampled synthetic records despite good statistical fidelity. Membership inference F1 was 0.51, near random — [arXiv 2603.06720](https://arxiv.org/abs/2603.06720v1) [S]
- **FedEHR-Gen:** federated synthetic time-series EHR — [arXiv 2605.27892](https://arxiv.org/pdf/2605.27892) [S]
- **EHR-Safe (Google):** privacy-preserving synthetic EHR (OLDER) — [Google Research](https://research.google/blog/ehr-safe-generating-high-fidelity-and-privacy-preserving-synthetic-electronic-health-records/) [S]

**Language-free (code-based) models as a route around Thai-language scarcity**
- Delphi, DT-Transformer, CoMET/Curiosity, ReClaim, MOTOR and Taiwan NHIRD models consume **only coded events** (ICD-10, procedures, drugs, labs, time). They need no clinical text — sources above [V/S].
- **Thai coding systems:**
  - Thai claims and HDC use ICD-10 (ICD-10-TM in Thailand) [K].
  - Drugs use TMT/24-digit codes [K].
  - Therefore the main transfer barrier is **code-vocabulary mismatch, not language**. That is exactly what GRASP, PORTER and LLM-embedding mapping (arXiv 2610.04946) address.

### Inferences
- **Candidate novel capstone directions**, ranked by novelty × feasibility on a 16 GB GPU:
  1. **"Does Delphi transfer to Thailand?"**
     - Run the first LMIC / Southeast Asian external validation of a trajectory foundation model (Delphi-architecture retrained, or CLMBR-T or MOTOR weights) on Thai coded data.
     - Map ICD-10-TM and TMT with LLM embeddings.
     - Report discrimination, calibration and subgroup results by insurance scheme (UCS / SSO / CSMBS), region and urban–rural.
     - The scheme dimension is a uniquely Thai fairness axis, an analogue of Curiosity's "self-pay" collapse.
  2. **"Thai trajectory model as a counterfactual simulator, checked against target trial emulation"** for one NCD pathway (e.g., T2DM: SGLT2i vs sulfonylurea → CKD/CVD, or HT control → stroke).
     - Validate simulated contrasts against classical TTE and published RCT effects, with conformal "act/defer".
     - This turns McKinsey vector 2 from prognosis into an auditable pathway recommender.
  3. **Federated Thai GEM over 43-file exports**, plus an LLM-style memorisation audit of synthetic trajectories, as a privacy-preserving data asset for Thai researchers. This directly answers the Foresight-pause governance lesson.
- **Option 1 is the most defensible "first"**: no Southeast Asian validation exists in what I found, and it is compute-trivial. Option 2 is the most "groundbreaking" but carries the highest causal-validity risk. Option 3 has the highest data-engineering load.
- **Ranking caveat:** these rankings are my inference and need validation against the parallel Thai-data-access and LLM notes.

### Gaps
- I could not open the GRASP paper (paywall) for exact transfer deltas.
- No source confirms that Thai claims use ICD-10-TM throughout, or what the TMT drug-code coverage in HDC is. Both are marked [K].
- No source found on Delphi, MOTOR or CoMET being evaluated in any LMIC.
- No Thai fairness audit of any clinical prediction model by insurance scheme was found. It may exist in Thai-language journals that were not searched.
