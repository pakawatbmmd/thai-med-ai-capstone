# Council v6: Aim high (McKinsey "AI-powered future of care" as the frame). Claude, Round 1

**Evidence base:**
- `reports/AI care vectors for Thailand.md`
- `research_notes/AI care vectors for Thailand/` (including `00_guidance_mckinsey_summary.md`)

**Brief:** groundbreaking, globally novel; a new model, a new agent, or a new way of using AI. The 9-month deliverable may be a POC or MVP. Descartes proposes, Hume audits, Socrates stress-tests. Two of these five sharpen the report's directions; three are new.

**Opening position (Descartes).** The report's central finding is the right foundation: *capability has outrun permission*. AMIE gets the diagnosis into its differential 90% of the time. Yet models ask a needed question only 33.5% of the time and miss 32–97% of required escalations. No one has a rule for when an AI has *earned* the right to act. McKinsey's three vectors are written for a fragmented US market. Thailand already has their preconditions: one payer, one data spine, a funded non-physician front door, and AI paid for as a benefit. So the most ambitious move is not a better Thai chatbot. It is to **invent the institutions, models and tests that let a national system safely hand work to AI**, and to show that some of them are *only possible* at single-payer scale.

### 1. The AI Residency: licensing clinical AI the way Thailand licenses doctors
- **Novel claim:** Clinical AI should earn autonomy the way a doctor does: a licensing exam, supervised residency, and revocable privileges. The protocol works per symptom group, per site and per human supervisor. It uses anytime-valid sequential statistics, and it certifies the *human backstop* as well as the AI. Plus one counter-intuitive, publishable claim: **a 1% missed-escalation floor is statistically certifiable within weeks across a national single-payer network, but would take years at any single site.**
  - The report's own arithmetic: ~670 consults per pharmacy per year; 5% prevalence is a hypothetical. [UNVERIFIED volume figures, from a May 2025 ministerial claim]
- **What is new versus the report's direction #2:**
  - The **"NL for AI"**: an OSCE-style licensing exam for agents. Simulated Thai standardized patients in 4 dialects play the stations, built on the format of the National License Step 3 OSCE (CMA).
  - **Residency privileges** gated on *both* the AI's sequential evidence *and* the supervising pharmacist's or อสม.'s measured unaided competence, using seeded known-answer probes. This turns McKinsey's unspecified deskilling countermeasure into a credential condition.
- **Vector / signal:** Vector 3 (autonomy), plus vector 1's performance floor. Signals: regulatory boundary expansion, and payer acceptance of AI decisions. The Thai analogue is a conditional-autonomy clause in NHSO's Thai-innovation benefit listing.
- **Why Thailand:**
  - The pharmacy-32 scheme's symptom groups are natural credential strata (Utah gates per medication group).
  - The Medical Council is suing over pharmacists' scope. An auditable, revocable protocol is the only politically viable route to *any* AI autonomy.
  - A Chula Medicine committee trains residents for a living; the metaphor is native to them.
- **Full vision:** A national registry at NHSO and Thai FDA. Every deployed clinical AI (Perceptra chest X-ray, diabetic-retinopathy screening, any front door) is examined, runs in shadow mode, is promoted per stratum, sampled at random, and demoted on drift. Its supervisors' unaided skill is part of the credential.
- **What the 9-month POC proves:**
  1. **A licensing-exam harness.** 60–100 OSCE stations with LLM patient actors and clinician-written rubrics, run against 4–6 models; the results report which stations each model "passes".
  2. **An open-source promotion/demotion engine** (e-values or test martingales, hierarchical pooling across strata, conformal risk bounds). It is replay-evaluated on simulated Thai volumes and on a public retinal or chest X-ray dataset with injected site shift.
     - Target: faster promotion than Utah's fixed 250/1,000 ladder at an equal guaranteed miss rate.
     - Target: bounded time to demotion after drift.
  3. **A 10–20-person probe pilot** with pharmacy students.
- **Prior art to beat:**
  - Utah's Doctronic ladder (Mello, JAMA Health Forum 2026); FDA predetermined change control plans (PCCPs).
  - WATCH (conformal martingales); conformal selective prediction.
  - LaRocco's prescriber survey; the Lancet staged-certification proposal [not read]; levels-of-autonomy papers.
  - AMIE and OSCE-style AI evaluations (AMIE used OSCE formats; the novelty is the *licensing-to-privilege pipeline*, not the exam alone).
- **Key risk:** It may be read as "statistics, not AI". Answer: the exam harness *is* an agent-evaluation system, and the engine governs agents. Also, no real deployment log exists to replay.
- **Month-1 falsification test:** A sample-size simulation at Thai volumes, with 2 clinicians co-writing 20 OSCE stations. **Kill the network-scale claim** if hierarchical pooling still needs more than 12 months to promote most strata. **Kill the exam** if 2 clinicians' pass/fail agreement on AI transcripts is κ < 0.6.

### 2. UC-Navigator with one value-of-information policy: ask, fetch or act
- **Novel claim:** The first front-door agent whose every turn chooses among **asking the patient**, **fetching a record field from the national exchange**, or **acting** (routing to home, pharmacy-32, รพ.สต. telemedicine, hospital or 1669). It makes that choice with one value-of-information objective that prices **missed escalation, system load under real weekly quotas, and privacy cost** together. This merges the report's #1 (network-optimised routing) and #5 (progressive disclosure) into a single policy, the right abstraction because both are information-acquisition decisions.
- **Vector / signal:** Vector 1. Signals: visits diverted to AI; front-door AI run by a national payer; closed-loop referrals.
- **Why Thailand:**
  - One payer routes more than 47.5M members under one benefit rulebook and weekly quotas, with one exchange (Health Link) to fetch from.
  - Capitation makes diversion a saving, not lost revenue.
  - AMIE's real-patient weaknesses (practicality p=0.003, cost p=0.004) are exactly what network context fixes.
- **Full vision:** NHSO's conversational front door in LINE OA / Thang Rath. It speaks 4 dialects, books against quotas, discloses records progressively under consent-as-code, and its autonomy is credentialed by #1.
- **What the 9-month POC proves:**
  1. **UC-Gym:** an open simulator with LLM patient actors in 4 dialects, synthetic records in the 43-file / Health Link shape, and quotas and distances calibrated to public NHSO aggregates.
  2. **A 4B Thai policy** (QLoRA + GRPO on the 4090) trained on the environment's cost. On clinician-labelled held-out vignettes it beats prompted frontier models and ThaiLLM-Prescreen on missed escalations *and* ask-before-act, at equal over-triage.
  3. **A three-way Pareto surface:** safety × system load × fields disclosed.
- **Prior art to beat:** AMIE (including g-AMIE and longitudinal versions); MAI-DxO/SDBench (cost-aware test acquisition); MediQ; CARE-Bench; the October 2026 escalation audit; PreA; ThaiLLM-Prescreen.
- **Key risk:** Simulation-to-reality transfer. The Oxford study showed simulated users don't predict real use, and LLM patients are too cooperative and too Central-Thai. Mitigation: dialect red-teaming (the report's #3 becomes the Navigator's adversary) and a small real-user usability pilot.
- **Month-1 falsification test:** 2 clinicians route 150 vignettes into 6 routes. **Kill** if κ < 0.6. **Kill** if a frontier model prompted with a one-page network summary already reaches ≤5% missed escalation *and* ≥80% ask-before-act. **Kill the privacy half** if triage with no record ≈ triage with the full record.

### 3. ThaiTwin: an in-silico trial platform for AI front doors, validated against a real national policy change (new)
- **Novel claim:** Before any AI front door touches patients, run it through a **national synthetic population**: patients whose histories come from a trajectory model (vector 2), who talk through LLM actors (vector 1), inside a capacity model of the UC network. Then predict its system effects: diverted visits, ED load, missed escalations, cost.
  - The breakthrough is **validation**: back-test the twin on a policy change that already happened. Did it predict the shift in claims after the pharmacy-32 scheme started on 3 Sep 2024, or after 30-baht-anywhere phase 3?
  - No one has validated an in-silico trial of *conversational* clinical AI against a real national natural experiment. [Negative search result; re-check]
- **Vector / signal:** Couples vectors 1 and 2. Signal: the payer moves "from financing to orchestrating", because the payer can now pre-test what it buys.
- **Why Thailand:**
  - A single payer with ID-linked claims.
  - Recent, sharp, nationwide policy changes with known start dates.
  - NHSO already buys Thai AI per hospital (THB 2.9B rising toward 10B) and needs a way to evaluate it. In the US no single entity can see the whole network to validate against.
- **Full vision:** NHSO / Thai FDA's "regulatory sandbox as a service". Any vendor's AI front door is trialled in silico, then in shadow mode (#1), then promoted.
- **What the 9-month POC proves:**
  1. A synthetic population generator built from public aggregates (age/sex/region, disease prevalence, pharmacy-32 symptom mix).
  2. A network/capacity model.
  3. One back-test: predicted against reported changes in pharmacy-32 consult volume and in visits for the matching symptom groups after Sep 2024, using public NHSO/MOPH aggregates.
  4. A demonstration run of two candidate front-door policies (e.g., the #2 Navigator vs a prompted frontier model) showing they produce *different* predicted system outcomes.
- **Prior art to beat:**
  - Agent-based health-system simulation (classic operations research).
  - Generative-agent societies.
  - In-silico clinical trials for devices (FDA-accepted for some cardiac and diabetes simulators, e.g. the UVA/Padova T1D simulator [UNVERIFIED in this round]).
  - Delphi-2M synthetic cohorts; UC-Gym (#2) as the encounter-level piece.
- **Key risk:** Public aggregates may be too coarse to back-test anything (only national monthly totals). The twin could become an unfalsifiable "SimCity".
- **Month-1 falsification test:** Inventory public time series. **Kill** if fewer than 12 monthly data points either side of the pharmacy-32 start exist at province × symptom-group level or finer, **and** NHSO will not share a de-identified aggregate extract. Then the platform is untestable, so fall back to #2.

### 4. The 1669 co-dispatcher: a speech-native, dialect-robust red-flag model for emergency calls (new)
- **Novel claim:** A **speech-native** model (audio in, red-flag probabilities and a suggested question out) listens alongside 1669 dispatchers in Central, Isan, Northern and Southern Thai. It detects stroke, cardiac arrest, sepsis and obstetric emergencies from *what is said and how it sounds* (breathlessness, slurred speech, agonal breathing). It also recommends the next question to ask.
  - The hypothesis: **cascaded ASR → text → classifier loses red-flag signal in dialect, while speech-native modelling keeps it.** That is falsifiable and globally relevant to every low-resource-dialect emergency system.
- **Vector / signal:** Vector 1 at its highest stakes, with vector 3 autonomy at its lowest level (advisory only).
- **Why Thailand:**
  - 1669 receives dialect calls nationally; Isan alone has 20M+ speakers.
  - The EMS gap: 1,790 paramedics against a target of 7,500; 2,574 subdistricts lack adequate response units.
  - Typhoon Isan ASR and Typhoon2-Audio give open building blocks.
  - The October 2026 audit showed red-flag detectors collapsing on paraphrase. Dialect is paraphrase at national scale.
- **Full vision:** Every 1669 call has a co-dispatcher that never tires. It is credentialed per red-flag type by #1, and its outputs feed the Navigator's escalation hook.
- **What the 9-month POC proves:**
  - A synthetic-plus-real speech set: scripted emergency calls voiced by native speakers of 4 dialects (aim for 20–40 speakers), and TTS/voice-conversion augmentation, with **real 1669 audio only if NIEMS agrees**.
  - A comparison of cascaded ASR+LLM against a speech-LLM fine-tuned with LoRA on the 4090. The model size that fits is unverified; measure it in week 1.
  - Primary metric: red-flag recall by dialect.
- **Prior art to beat:**
  - Corti's ML cardiac-arrest detection in Copenhagen. Its RCT (Blomberg et al., Resuscitation 2021) found that alerts did **not** significantly improve dispatcher recognition [details UNVERIFIED this round].
  - The design must therefore address *dispatcher uptake*: suggest the next question rather than raise an alarm.
  - Also: Criteria Based Dispatch tools; the escalation audit; Thai dialect LLM evaluations.
- **Key risk:** Access to real calls (PDPA, NIEMS). Scripted calls lack real panic, noise and agonal-breathing acoustics. The Corti RCT shows that accuracy alone doesn't change outcomes.
- **Month-1 falsification test:** Record 100 scripted calls (25 per dialect) and run the cascaded pipeline. **Kill the speech-native thesis** if cascaded red-flag recall on dialect is already within 5 points of Central Thai. **Kill the project** if NIEMS/1669 gives no path to even 50 de-identified real calls for external validation by month 3.

### 5. AI-on-AI cascade stewardship: govern the downstream harm of NHSO's own chest X-ray AI (new)
- **Novel claim:** The first **second-order** clinical AI: a model that estimates, per patient, the *net value of the follow-up cascade* a first AI triggers. A trajectory model scores incidental findings flagged by chest X-ray AI to recommend *no follow-up*, *guideline follow-up* or *expedited referral*. It turns McKinsey's "AI can break low-value cascades" from an assertion into a mechanism.
  - The safety framing: **a national AI rollout's harms show up in other parts of the system** (CT queues, biopsies, anxiety), so the payer needs an AI to steward its AIs.
- **Vector / signal:** Vector 2 (personalised pathways) applied to vector 1/3 outputs. Signal: payer-orchestrated closed-loop care and cascade avoidance.
- **Why Thailand:**
  - NHSO pays for Perceptra chest X-ray AI in 445 hospitals in FY2569 (887 planned). The follow-up CT and referrals land in already congested tertiary hospitals, on the same payer's budget.
  - Capitation means cascades are a cost to NHSO, not revenue. The payer is uniquely motivated, and uniquely able to see the whole cascade in its claims.
- **Full vision:** A standing "cascade monitor" for every AI on NHSO's benefit list. It tracks each AI's downstream utilisation and outcomes in claims and adjusts follow-up recommendations, a post-market surveillance layer that the AI Residency (#1) can also use for demotion.
- **What the 9-month POC proves:**
  - Using public chest X-ray datasets with follow-up labels (e.g., NLST-style lung screening data, if accessible [UNVERIFIED access]) and Fleischner/Lung-RADS guideline logic, build a per-finding net-benefit model, and show decision-curve gains against guideline-only follow-up.
  - Plus a cascade simulation for Thai volumes: predicted CTs avoided per 100k X-rays at fixed missed-cancer risk.
- **Prior art to beat:** Ganguli's cascade literature; Lung-RADS / Fleischner; AI nodule-malignancy risk models (e.g., Sybil-style, LUMA-style; check specifics); Choosing Wisely. No "AI stewarding AI" design was found. [Negative search; re-check]
- **Key risk:** No Thai follow-up outcome data in 9 months, so the POC is US-data-based with a Thai simulation. Clinicians may see it as "rationing".
- **Month-1 falsification test:** Obtain one public dataset with incidental findings *and* downstream outcomes. **Kill** if none is accessible by week 4. Also **kill** if guideline-only follow-up already achieves net benefit within 2% of an oracle on that data (no headroom).

---

**If I were the student, I'd pick #1, the AI Residency, with #2 as the "resident" it credentials.** It is the only idea here whose core claim is *structurally* Thai: autonomy is certifiable only at single-payer scale. It turns McKinsey's two unanswered questions ("how do we reach the performance floor?" and "how do we design against deskilling?") into one executable protocol. And it speaks the committee's own language: exams, residency, privileges. The POC is a real system (exam harness + promotion engine + Navigator as trainee) and does not depend on a data-access miracle.

**#3 (ThaiTwin) is the boldest.** If a back-test against the pharmacy-32 rollout works, it is a paper on its own. But it lives or dies on data granularity, which month 1 can settle.

**Where I disagree with McKinsey:** "data availability, not model capability" is wrong for discursive care. The 2026 escalation evidence is a capability failure in sequential decision-making, and Thailand has more data than the US and still no safe triage layer. And in Thailand the regulatory boundary moves through *pharmacists and อสม.*, not through AI replacing physicians. Every idea above is designed for that.
