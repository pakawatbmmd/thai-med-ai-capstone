# Council v8: Clinical / scientific flips on decision models. Claude, Round 2

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
