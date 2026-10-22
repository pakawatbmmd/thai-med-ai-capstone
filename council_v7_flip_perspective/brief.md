# Council v7 brief: decision models in the health system, "flip the perspective"

## The student's framing
How to use a **decision model** in the healthcare system, thinking with the frame **"flip the perspective"**, rather than building a plain screening or triage system.

## What "decision model" may mean (both are in scope)
1. **Clinical decision model:** predicts or chooses an action for a patient (screen, triage, refer, treat, discharge), including sequential and decision-theoretic models.
2. **Health-economic decision model:** the decision-analytic models (decision trees, Markov or microsimulation) used in HTA to decide what a health system pays for. Thailand's HITAP is a globally recognised HTA body that informs the UC benefit package. [Check HITAP's current role before citing.]

## What "plain" means (the anti-pattern)
A patient presents, a model labels the disease or picks a route, and the model is scored by accuracy against a label. Screening and triage chatbots, risk scores, and "AI says refer / don't refer".

## Possible axes to flip (starting points, not a menu)
- **Direction:** who should come in → who can safely leave or step down (reverse triage).
- **Initiative:** triage whoever shows up → whom the system should reach first (outreach).
- **Subject:** the patient's disease → the patient's *decision* (seek care, delay, adhere, drop out), or the *clinician's / system's* decision.
- **Threshold:** one risk cut-off → a decision that depends on context (access, cost, capacity, values).
- **Decider / level:** a model decides about patients → a model decides what the *system* buys or where it puts capacity.
- **Output:** a label → the next most valuable question or test, or "what would have to be true to change this decision".
- **Default:** the human decides unless AI flags → AI handles unless it abstains (or the reverse), with an explicit competence model.

## Context the advisors already have
- `README.md`: the student, constraints, rejected ideas, the audit-first / RSI direction.
- Other research reports exist on branches `claude/physical-ai-med-ed-research`, `claude/medical-harness-research` and `claude/future-of-care-research`. The last one (McKinsey frame; capability has outrun *permission*; AI Residency; ask-or-act Navigator) is the most relevant. Read `reports/AI care vectors for Thailand.md` on that branch if you can.
- Key Thai facts used before (all sourced in earlier notes):
  - NHSO covers ~47.5M UC members; the payer is already an "orchestrator".
  - Infrastructure: Health Link (~20k service points), 43-file data, the 32-symptom pharmacy scheme, telemedicine at all 10,910 รพ.สต., ~1.07M อสม.
  - Doctor density is ~1:462 in Bangkok vs ~1:5,000 in Bueng Kan; NHSO runs weekly quotas for the pharmacy and clinic channels.

## Student constraints
Chula master's (Medicine + Engineering committee). The idea may be ambitious; the deliverable is a POC/MVP in ~9 months on one RTX 4090 Laptop (16 GB), with API models allowed on synthetic data. Wants frontier ML plus real Thai impact. Already rejected: "safe" admin/claims ideas, VenomSight, dysarthria.
