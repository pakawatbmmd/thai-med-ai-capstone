# Council v8 brief: flip the perspective on decision models, clinical / scientific / model-development only

## Why this round exists
Council v7 converged on system-level ideas (HTA "Evidence Before Algorithms", revocable AI autonomy leases, payer thresholds). The student liked the ideas but **does not want the project to involve health-system policy, law/regulation, payment or reimbursement, procurement, or governance**. This round keeps the **"flip the perspective"** frame on **decision models** but restricts it to **clinical, scientific and model-development** work.

## Hard exclusions (do not propose)
- Payer / NHSO / reimbursement / HTA / cost-effectiveness / budget or procurement decisions.
- Legal, regulatory, licensing, credentialing, scope-of-practice or governance mechanisms (including "AI residency" or autonomy-lease ideas whose core is permission granting).
- Health-system routing, quotas, capacity planning or workforce redesign as the main contribution.
- Already rejected: "safe" admin/claims ideas, VenomSight, dysarthria.

## What is wanted
- A **decision model** (a model whose output is or directly drives a clinical action: test, treat, refer, stop, escalate, measure, wait) where the **perspective is flipped** relative to a plain screening or triage classifier.
- The core contribution is **clinical science, ML science, or a new model, method or agent**, publishable at a clinical-ML or ML venue (e.g. MLHC, CHIL, MICCAI, NeurIPS/ICML workshops, npj Digital Medicine, Lancet Digital Health).
- Thai relevance is welcome where it is clinical or scientific: Thai patients, Thai-language clinical text, Thai disease patterns, rural point-of-care conditions. It must not be policy or payment.

## Examples of flips that stay clinical (starting points, not a menu)
- **Objective:** train for the *decision* (regret, harm) rather than the label (accuracy/AUROC).
- **Output:** "what would change this decision?" or decision stability, rather than a risk score.
- **Subject:** model the *clinician's* decision (inverse decision modelling) or the *patient's* response, rather than the disease.
- **Direction:** when to *stop*, de-escalate or not test, rather than when to start.
- **Evaluation:** stress-test the decision model with mechanistic or generative patients, rather than a held-out label set.

## Student constraints
Chula master's (Medicine + Engineering committee). The idea may be ambitious; the deliverable is a POC/MVP in ~9 months on one RTX 4090 Laptop (16 GB VRAM, 32 GB RAM), with public datasets (MIMIC-IV, eICU, etc.) or local data under IRB, and API models allowed on synthetic data. Wants frontier ML plus real clinical impact.
