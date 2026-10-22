# Council v7 — Codex, Round 2

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