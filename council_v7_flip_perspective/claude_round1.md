# Council v7: Flip the perspective on decision models. Claude, Round 1

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
