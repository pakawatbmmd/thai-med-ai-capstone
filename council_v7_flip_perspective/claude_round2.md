# Council v7: Flip the perspective on decision models. Claude, Round 2

**Read:** `claude_round1.md`, `codex_round1.md`, `gemini_round1.md`. No Round 2 file was read.

**Provenance note.** Gemini's Round 1 leans heavily on `reports/AI care vectors for Thailand.md`: four of its five ideas are that report's directions, re-labelled as flips. Codex used the same report sparingly and built from decision theory outward. That difference matters for the convergence verdict below.

## 1. Hume audit: five load-bearing claims that are wrong, unverified or overstated

1. **Gemini #2: "realistic NHSO pharmacy consult volumes (~670/pharmacy/year)".**
   - *Problem:* the figure is the earlier report's own arithmetic. It comes from a May 2025 ministerial claim of ~8M consults over an unclear period across ~6,000 pharmacies, combined with a *hypothetical* 5% must-escalate prevalence. Gemini presents it as an empirical input.
   - *Verify:* NHSO's published pharmacy-32 claim counts by month and symptom group; a real red-flag prevalence from any pharmacy triage audit.
2. **Gemini #4: "KCMH-StepDown ... directly tests and fixes the subgroup calibration collapse seen in Epic's Curiosity".**
   - *Problem:* a 5–20M-parameter event model on one hospital's extract cannot "fix" a 118M-patient model's collapse. At best it reports its own calibration by scheme. The KCMH extract of ≥20,000 encounters under expedited review is also unverified, and step-down labels in retrospective data are confounded by indication. Gemini names this risk itself, then sets a POC target that assumes it away.
   - *Verify:* a co-signed data request, and how many historical step-down decisions actually occurred in the extract.
3. **Gemini #5: estimating the uplift of an อสม. visit "from published ARMMAN / Thai NCD refill delay statistics".**
   - *Problem:* a semi-synthetic data-generating process can rank algorithms; it cannot establish a Thai visit effect. The Whittle-index policy also needs indexability, which is assumed, not shown. Codex #4 makes the right demand: known non-zero assignment probabilities, or the clinical-effectiveness version is dead.
   - *Verify:* whether any Thai district randomised or lottery-allocated outreach, or logged allocation probabilities.
4. **Gemini #3: a neural EVPPI surrogate "100× faster ... within ≤3% error" that "prevents payer bankruptcies".**
   - *Problem:* speed-ups over nested Monte Carlo are already delivered by GP and regression EVPPI methods (SAVI, Strong–Oakley–Brennan). So 100× against *nested* MC is the wrong baseline, and "bankruptcies" is rhetoric.
   - *Verify:* benchmark against the regression-based EVPPI in SAVI or BCEA, not against nested MC.
5. **Codex #1: a learned sequential study-selection policy beating EVSI-greedy by ≥25% in net opportunity loss.**
   - *Problem:* plausible as a target, but with a small menu of candidate pilots (3–6 study designs × sample sizes), exhaustive or greedy EVSI is cheap and near-optimal. Amortised design (Deep Adaptive Design) mainly buys *speed* in large or continuous design spaces. The neural policy may have nothing to beat.
   - *Verify:* in month 1, count the decision-relevant design space. If exhaustive EVSI over it runs in minutes, drop the learned policy and keep the decision model.

Minor: Gemini #1 benchmarks against "GPT-5/Claude-4", which are not current frontier baselines in Oct 2026. Several ideas assume `pai1/tma1-medgemma-4b`, whose gated HAI-DEF licence the README already flagged as unchecked.

## 2. Convergence verdict

| Cluster | Who | Signal or attractor? | Best variant | What makes it publishable |
|---|---|---|---|---|
| **Value of information: decide what to learn before deciding** | Codex #1, #2; Gemini #3; Claude #5 | **Real signal.** Codex reached it from first principles ("start with the decision, then ask whether prediction is needed"), not from the report. | Codex #1 (adopt / reject / *pilot first*) + Codex #2 (management regret, not diagnostic entropy) | The objective is **decision regret**, not accuracy or entropy, and the action set includes "gather evidence". |
| **Permission to act** | Codex #3; Gemini #2; Claude (v6 AI Residency) | Partly attractor. Gemini imported it from the report, but Codex independently made it the decision variable. | Codex #3's learned gate + randomised, logged audit probabilities, plus Gemini #2's human-backstop probes | Honest guarantees: logged audit probabilities, no claims for unobserved strata, measured demotion delay. |
| **Outreach by benefit, not risk** | Codex #4; Gemini #5; Claude #2 | Real signal, but **identification-gated** | Codex #4 (doubly robust policy learning; known assignment probabilities) | It is publishable only with randomised or known-propensity data; otherwise it is a simulator paper. |
| **Reverse triage / step-down** | Claude #1; Gemini #4 | Attractor. Codex's warning stands: "renaming low-risk classification 'reverse triage'" is a gimmick unless capacity enters the decision. | None in current form | It would need a capacity-constrained assignment *and* a guarantee, and both proposals are gated on data access. |
| **Patient's own decision** | Codex #5 (preferences); Claude #3 (care-seeking) | Real but separate | Codex #5 | Test–retest stability as the kill test is the right instinct. |

**Self-correction:** I withdraw my Round 1 pick (#1 reverse triage) as the lead. Codex's gimmick test is fair. Without a capacity-constrained assignment problem and a data owner, it is a low-risk classifier with a better name.

## 3. Socrates: most over-rated idea, Gemini #1 UC-QuotaRouter

It breaks on the assumption that **a policy trained against a synthetic quota-and-patient simulator produces a result about the Thai network**. Its headline RQ ("≥25% reduction in simulated Hospital/ED routing cost") is a property of the simulator's cost table, which the student writes. And conceptually it is the plain triage chatbot the student asked to escape, with a cost term added: it still answers "where should this patient go?" The genuinely flipped part, *which question to ask*, is done more cleanly by Codex #2 without the network simulator's unverifiable assumptions.

## 4. Most under-rated: Codex #2 "Ask only what could change care"

It is the purest flip on the board. It changes the *objective* from diagnostic certainty to **management regret**. It is laptop-feasible, needs no data-access miracle (clinician-authored case families plus counterfactual variants), and has a decisive month-1 kill test (a 3-question checklist reproducing ≥95% of management decisions).

**The merge that makes it a thesis.** Codex #1 and Codex #2 are *the same mathematics at two scales*: expected value of information with respect to a decision. At the **bedside** the question is "which question or test could change this patient's management?" At the **system** level it is "which pilot study could change Thailand's decision to fund this AI?" A single framework, a decision model with an explicit "acquire information" action scored by regret, applied at both scales, also answers the student's open question about which kind of "decision model" is meant: **both, unified by one idea**.

## 5. Final top 3

| # | Project | Flip | Novelty (1–5) | Thai impact (1–5) | POC finish confidence | Gate / dependency | Why |
|---|---|---|---|---|---|---|---|
| 1 | **Decision-relevant information at two scales**: a regret-based VOI decision model choosing the next question (bedside, Codex #2) and the next pilot before funding AI (system, Codex #1 + Gemini #3 + Claude #5) | Output: label → *what to learn next*; objective: accuracy → regret | 4 | 4 | 70% | One clinician pathway (≈100–300 case families) and one published Thai HTA model to re-implement; an HTA collaborator (HITAP contact [UNVERIFIED]) | It answers both meanings of "decision model" with one idea, has a hard non-ML baseline at each scale, and speaks to NHSO's growing AI budget. |
| 2 | **Revocable AI leases**: a learned competence gate + randomised audit + promotion/revocation, with human-backstop probes (Codex #3 + Gemini #2 + Claude v6) | Decider: model decides → model *earns permission* | 4 | 5 | 70% | Public retinal data first (EyePACS/IDRiD licences); Thai data later | It is the strongest Thai-policy story (Medical Council vs NHSO scope fight) and has honest statistics. |
| 3 | **Benefit-based outreach for อสม.** (Codex #4 + Gemini #5 + Claude #2) | Initiative + risk → benefit | 3 | 4 | 40% | Known assignment probabilities or randomised outreach data | Highest real-world leverage, but dies without identification. |

- **Moonshot:** *Living HTA for NHSO's AI procurement.* The system-scale half of #1 grown into a continuously updated model of every AI on the Thai-innovation benefit list, telling NHSO which to fund, which to pilot first, and which evidence to buy (Gemini #3 + Codex #1 + Claude #5).
- **Safe ambitious:** *The bedside half of #1.* Codex #2's decision-regret question selection on one clinician-owned pathway, with the fixed-checklist baseline. It can be finished on the laptop with no data-access dependency.
