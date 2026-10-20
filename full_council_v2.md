# Capstone Council v2 — Claude × Codex × Gemini (hardware-only constraint, philosopher-council, 2026-10-20)

# ROUND 1

## CLAUDE — Round 1

## Claude — Round 1 (council: Descartes proposes · Hume audits · Socrates stress-tests)

### 1. VenomSight — antivenom-aware Thai snake identification that knows when *not* to answer
- **Pitch:** Train a snake-photo classifier where the loss reflects *clinical consequence* (which antivenom you'd give), and where the model abstains when uncertain, so it is safe to use at the bedside.
- **Thai problem:** Thailand has several medically important venomous snakes (cobras, kraits, Malayan pit viper, Russell's viper, green pit vipers). The Queen Saovabha Memorial Institute (QSMI) produces largely *species-specific* monovalent antivenoms. Misidentifying a krait (neurotoxic, often painless bite) as harmless is catastrophic. Patients often bring a photo or the dead snake. Annual bite numbers: unverified.
- **What's novel:** Snake classification exists (SnakeCLEF, iNaturalist). The gap is (a) a **Thai-species benchmark mapped to antivenom decisions**, (b) a **cost-sensitive loss + selective prediction** (risk–coverage curves), and (c) evaluation on hard look-alikes (green pit viper vs harmless green tree snakes; banded krait vs mock vipers and wolf snakes).
- **Core experiment:** Fine-tune and compare ConvNeXt-T, ViT-B/16, EVA/DINOv2-B and a CLIP zero-shot baseline on iNaturalist/SnakeCLEF images restricted to Thai species. Compare cross-entropy vs a clinically weighted cost matrix vs conformal prediction sets. Metrics: top-1, **expected clinical cost**, risk–coverage AUC, and calibration (ECE). All base-size models fine-tune in 16 GB with mixed precision.
- **Socratic test:** *Do public photos look like ER photos* (blurry, dead or partial snakes)? In month 1, build a 300-image "ER-style" test set (degraded or cropped photos, photos of dead specimens) and measure the drop. If it is huge, the thesis becomes about domain robustness, which is still a valid contribution.

### 2. FlukeScope — telling *Opisthorchis viverrini* eggs apart from look-alikes on cheap microscopes
- **Pitch:** A fine-grained egg detector that solves the hardest confusion in Northeast Thailand's liver-fluke screening: *O. viverrini* vs minute intestinal flukes (Haplorchis spp.).
- **Thai problem:** Liver fluke infection drives Isan's very high cholangiocarcinoma rate (among the highest in the world). Stool microscopy is the screening workhorse, and Ov and minute-intestinal-fluke eggs look almost identical under a microscope, which inflates prevalence estimates.
- **What's novel:** Parasite-egg detection datasets exist (Chula-ParasiteEgg-11, ICIP 2022 challenge, includes Ov). Few works target **this specific fine-grained confusion** or the **domain shift to smartphone-on-microscope or low-cost optics**.
- **Core experiment:** Compare YOLOv8/v11, RT-DETR and a two-stage detector + DINOv2 fine-grained re-classifier. Simulate low-cost optics (blur, chromatic aberration, JPEG artifacts) and test super-resolution as a preprocessing step. Metrics: mAP@0.5, Ov-vs-MIF confusion rate, and performance under each degradation. Fits easily in 16 GB.
- **Socratic test:** *Is Ov vs MIF even separable from images?* Experts debate this. Month 1: check whether Chula-ParasiteEgg-11 or the literature has labelled MIF eggs. If not, the project shifts to "Ov detection under low-cost optics."

### 3. MeliRisk — satellite-derived melioidosis risk maps at sub-district (tambon) resolution
- **Pitch:** Map the soil-borne killer *Burkholderia pseudomallei* using Sentinel-2 land cover, soil moisture and rainfall to show where farmers face the highest exposure risk each season.
- **Thai problem:** Melioidosis is endemic in Northeast Thailand (rice farmers, diabetics), its fatality rate is high, and it is under-recognised (estimated thousands of deaths per year, unverified).
- **What's novel:** Global and national suitability maps exist (Limmathurotsakul et al.). A **seasonal, tambon-level, deep-learning-on-imagery** model with uncertainty maps is new.
- **Core experiment:** Compare a gradient-boosting model on engineered features vs a CNN/ViT on Sentinel-2 patches vs a geospatial foundation model (Prithvi, SatMAE) fine-tuned with LoRA. Targets: published case locations/district counts from 506 surveillance (granularity to verify). Metrics: spatial-block cross-validated AUC and calibration.
- **Socratic test:** *Are case labels spatially precise enough?* If only province-level counts exist, the model has no fine-grained ground truth. Check 506 data granularity in week 2.

### 4. TSL-Med — Thai Sign Language recognition for hospital encounters (bold)
- **Pitch:** A pose-based recogniser for ~150 medical Thai Sign Language signs (pain, location, duration, allergy) so deaf patients can communicate at triage without waiting for an interpreter.
- **Thai problem:** Certified TSL interpreters are scarce (numbers unverified), and hospital encounters are high-stakes.
- **What's novel:** General TSL datasets are small and do not focus on medical vocabulary. Pose-based isolated sign recognition with few-shot adaptation to new signers is under-done for TSL.
- **Core experiment:** Record a medical TSL vocabulary with deaf-community partners. Use MediaPipe/RTMPose keypoints, then compare ST-GCN vs a pose transformer vs a video-MAE baseline, and test signer-independent splits. Fits easily on the laptop.
- **Socratic test:** *Will the deaf community co-design and record signs?* Without them, there is no valid data. Contact a deaf association in month 1.

### 5. Wingbeat-TH — smartphone acoustic identification of Thai disease-vector mosquitoes (bold)
- **Pitch:** Identify Aedes aegypti / Ae. albopictus / Anopheles / Culex from the whine recorded on a cheap phone, as low-cost dengue/malaria vector surveillance by village health volunteers.
- **What's novel:** HumBug (Oxford) showed the concept works. The gap is Thai species, Thai ambient noise, and **on-device tiny models**.
- **Core experiment:** Compare log-mel CNN vs fine-tuned BEATs/AST vs a distilled tiny model running on the phone. Data: HumBug public data plus your own recordings of lab-reared colonies (a university entomology lab).
- **Socratic test:** *Is species separable in noisy Thai homes?* Test with mixed-noise augmentation first.

**If I were the student I'd pick #1** (VenomSight). It is Thai-specific, technically rich (cost-sensitive learning, conformal prediction, robustness), easy to explain, and the data is public enough to start next week.

## CODEX — Round 1

Ranked by expected healthcare value, research depth, originality, and nine-month feasibility. These are proposed research gaps, not verified claims of worldwide novelty. Dataset access remains **unverified** unless stated.

### 1. **Dialysis lifelines under water**
Predict which dialysis patients will lose access during floods, then optimize limited transport and reserve treatment capacity.

- **Thai problem:** Flood disruption is especially consequential for recurring treatment. NHSO explicitly describes planning for dialysis-solution resupply during floods. The availability of local patient, capacity, and disruption records is **unverified**. [NHSO overview](https://eng.nhso.go.th/assets/portals/1/files/Infographics/64-3_RenalReplacementTherapy_Info.pdf)
- **What's novel:** Flood-related dialysis-access research already exists. Extend accessibility maps into an intervention experiment: how much does explicitly reserving capacity for isolated communities improve continuity under uncertain road closures? [Existing study](https://arxiv.org/abs/2208.09425)
- **Core experiment or build:** Restrict scope to haemodialysis in one province. Combine OpenStreetMap roads, satellite flood extents, verified facility locations, and synthetic patient distributions calibrated against available aggregates. Compare nearest-open-centre routing, deterministic minimum-cost flow, and robust optimization. Measure simulated missed sessions, worst-community access, and sensitivity to uncertain capacity. Regional graphs and scenario simulation run on CPU within 32 GB RAM.
- **Socratic stress-test:** Does road access actually determine disruption, or do staffing and facility outages dominate? In month 1, reconstruct one historical event with a dialysis coordinator. Reject the road-centred model if it cannot explain documented failures.

### 2. **A shared harvester as a public-health intervention** — bold
Allocate scarce sugarcane harvesters according to the smoke exposure they might prevent.

- **Thai problem:** Thai research documents smallholder machinery constraints and burning incentives. Whether earlier machine access prevents burning in a chosen district is **unverified**. [Thai harvest-planning study](https://www.sciencedirect.com/science/article/pii/S0360835221000334)
- **What's novel:** Harvest optimization already balances production, equity, and logistics; health-weighted residue prioritization also exists. The narrower gap is dynamic fleet allocation with uncertain farmer participation and machinery eligibility. [Health-weighted prioritization](https://www.mdpi.com/2071-1050/18/18/9489)
- **Core experiment or build:** Use NASA FIRMS fire histories, crop maps, weather, settlement populations, and a small operator survey. Compare nearest-field scheduling, maximum-tonnage scheduling, and robust exposure-weighted scheduling. Evaluate modeled population-weighted smoke exposure, farmer waiting time, and cost across counterfactual scenarios. Use a reduced-form dispersion model and district-scale optimization, both laptop-feasible. FIRMS provides downloadable historical data. [NASA archive](https://firms.modaps.eosdis.nasa.gov/download/)
- **Socratic stress-test:** Will farmers substitute machine harvesting for burning? In month 1, interview operators and farmers and inspect field eligibility. If substitution is weak, model its limits rather than claiming avoided illness.

### 3. **When fluent AI hides impaired Thai speech**
Develop a speech-assessment model that detects meaning-changing pronunciation errors that automatic transcription silently corrects.

- **Thai problem:** Thai stroke research documents consonant and tone-related speech characteristics. Whether contemporary speech models conceal clinically useful errors is **unverified**. [Thai dysarthria study](https://pubmed.ncbi.nlm.nih.gov/19117194/)
- **What's novel:** Thai phoneme assessment already exists. Test disagreement between listener understanding and recognizer output, particularly when a recognizer produces the intended word despite an ambiguous utterance. Include consonant clusters so the project does not assume tone is the main impairment.
- **Core experiment or build:** Collect a therapist-designed minimal-pair corpus with consented stroke speakers and controls. Compare acoustic-feature SVMs, frozen multilingual speech-encoder embeddings, and a small tone-plus-phoneme adapter. Predict blinded listener identification and therapist-rated errors. Report speaker-held-out macro-F1, calibration, and correlations with intelligibility. Frozen encoders and short audio batches fit 16 GB VRAM.
- **Socratic stress-test:** Does the proposed error score track communication difficulty? Month 1 should secure a recruitment pathway and run a small listener pilot. Synthetic pitch changes alone cannot validate a stroke-assessment claim.

### 4. **Alms without invisible salt** — bold
Build a nutrition model that knows when a photograph cannot reveal an offered meal's sodium content.

- **Thai problem:** Monks' reliance on donated food limits control over their diets; Thailand already promotes healthier offerings. Local demand for recipe-aware donor tools is **unverified**. [Dietary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12260049/)
- **What's novel:** Food recognition and nutrition education already exist. Study the information missing from images: visually similar dishes can contain different quantities of condiments. The contribution is calibrated uncertainty and selecting the most useful follow-up question.
- **Core experiment or build:** Partner with several offering-food vendors to collect meal photographs and weighed ingredient records. Estimate recipe sodium using ingredient labels and the [Mahidol food-composition database](https://inmu.mahidol.ac.th/thaifcd/home). Compare dish-average lookup, image-only regression, and image-plus-recipe-question models. Measure sodium-estimate error, interval coverage, and questions required, holding out vendors. A frozen vision encoder and small regression heads fit easily.
- **Socratic stress-test:** Will vendors disclose quantities accurately enough? In month 1, document 30 preparations. If reference estimates remain unreliable, pivot to packaged offerings with declared nutrition rather than claiming sodium measurement.

### 5. **The medication bag that changed**
Compare successive sets of Thai medication bags to flag unexplained changes for pharmacist review.

- **Thai problem:** Thai home-visit research documents medication-management difficulties, including misunderstanding and retained medicines. The prevalence of harmful changes detectable from bag photographs is **unverified**. [Home-management study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9014897/)
- **What's novel:** Thai prescription-label OCR and generative information retrieval already exist. Study longitudinal reconciliation: distinguish packaging changes from changes in ingredient, strength, or instructions, with explicit abstention. [Existing label-AI study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11765698/)
- **Core experiment or build:** Assemble pharmacist-annotated, de-identified before/after bag sets, supplemented by controlled mock sets. Compare OCR-plus-rules, visual-text matching, and constrained graph matching. Measure clinically consequential change recall, false alerts per patient, and pharmacist review time. Hold out dispensing sites and patients. OCR, frozen image encoders, and graph matching fit the laptop.
- **Socratic stress-test:** Do photographs contain enough evidence to resolve changes? In month 1, ask pharmacists to independently reconcile 50 pairs. Persistent disagreement establishes an information limit that a larger model cannot solve.

If I were the student I'd pick #1 because it offers a concrete healthcare decision, strong baselines, and a useful result even without deep learning.  
Its month-one reconstruction can expose the decisive data and modeling risks before most of the nine months are spent.
## GEMINI — Round 1

﻿### 1. Tinglish-DRG: Constrained Clinical Coding & NHSO Audit-Risk Engine for Code-Switched Thai Inpatient Notes
1. **Name & Pitch:** **Tinglish-DRG** — A locally fine-tuned clinical language model and ontology-constrained verifier that maps Thai–English code-switched discharge summaries into ICD-10-TM codes, computes Thai DRG Relative Weights (RW), and flags high-risk reimbursement under-coding.
2. **Thai problem:** Thai physicians write inpatient progress and discharge notes in dense, unstandardized code-switched "Tinglish" (e.g., *"Pt ชาย 68 ปี U/D DM, CKD st4 มาด้วย AHF c AKI on top"*). Medical coders at public hospitals under the National Health Security Office (NHSO / สปสช.) manually translate these hybrid notes into ICD-10-TM and Thai DRG v6 codes. Coding backlogs and missed secondary diagnoses or complications/comorbidities (CC/MCC) reportedly cost district and regional hospitals 8–15% in lost Universal Coverage Scheme reimbursement or trigger retrospective NHSO audit clawbacks *(unverified)*.
3. **What's novel:** Existing automated ICD coding models (e.g., PLM-ICD) assume monolingual English MIMIC text and flat code prediction. Tinglish-DRG combines code-switched clinical entity normalization with a deterministic Thai DRG grouper rule-graph, optimizing not just micro-F1 on codes, but expected reimbursement accuracy under NHSO audit penalty constraints.
4. **Core experiment or build:** Compare zero-shot/few-shot local open-weight LLMs (Qwen-2.5-7B/14B, Typhoon-2-8B) against a QLoRA-adapted 8B–14B model paired with hierarchical Graph-RAG over the ICD-10-TM and Thai DRG v6 comorbidity trees. **Data source:** MIMIC-IV discharge notes synthetically transformed into physician-validated Tinglish via rule-based + LLM code-switching, paired with a de-identified retrospective chart set (~1,000–2,000 records) from a Thai university hospital *(availability in month 1–2 unverified)*. **Metrics:** Hierarchical macro/micro-F1, Complication/Comorbidity (CC) capture recall, and Relative Weight Mean Absolute Error (RW-MAE). **16 GB VRAM fit:** 4-bit NF4 QLoRA fine-tuning of a 14B model with FlashAttention-2 and gradient checkpointing (batch size 1, sequence length 4096) uses ~12–14 GB VRAM; local vLLM/ExLlamaV2 inference uses <10 GB.
5. **Socratic stress-test:** *Assumption:* Hospital IRB approval for de-identified Thai clinical text can be secured fast enough not to stall model training. *Month-1 test:* Confirm whether the advisor's hospital holds an existing retrospective NLP IRB protocol; simultaneously construct a 100-note synthetic Tinglish benchmark from MIMIC-IV and have two certified Thai medical coders blind-score its linguistic realism and ICD-10-TM ground truth.

---

### 2. CholangioSweep: Physics-Informed Contrastive Ultrasound Grading for *Opisthorchis viverrini* Periductal Fibrosis
1. **Name & Pitch:** **CholangioSweep** — A self-supervised B-mode ultrasound cine-loop model that separates early liver-fluke-induced periductal fibrosis (PDF) from benign steatosis and early cholangiocarcinoma (CCA) with calibrated operator-uncertainty alerts for rural screening.
2. **Thai problem:** Northeast Thailand (Isan) has the world's highest incidence of cholangiocarcinoma, driven by endemic *Opisthorchis viverrini* infection from raw freshwater fish consumption. While mass screening programs (such as Khon Kaen University's CASCAP) deploy mobile ultrasound to sub-district hospitals, non-specialist GPs struggle to distinguish subtle PDF grades (I–III) from nonspecific echogenic portal triads, yielding high inter-observer variability (~30–40% disagreement on early PDF grades, *unverified*).
3. **What's novel:** Prior CCA imaging works classify static, curated single frames and overfit to ultrasound machine annotations or probe gain settings. CholangioSweep models temporal consistency across multi-frame fan sweeps using physics-informed acoustic speckle/shadowing augmentations and conformal prediction to tell a rural GP when a sweep is diagnostically insufficient vs. true fibrosis.
4. **Core experiment or build:** Compare standard static frame CNNs/ViTs (ConvNeXt-Small, Swin-T) against a 3D temporal-contrastive video encoder (VideoSwin / TimeSformer-Tiny) pretrained with physics-based acoustic attenuation and Rayleigh speckle perturbations. **Data source:** Retrospective hepatobiliary ultrasound clips/frames from CASCAP/collaborating Isan cohorts *(access timelines unverified)* supplemented with public abdominal ultrasound datasets for self-supervised pretraining. **Metrics:** Quadratic weighted Cohen's Kappa across PDF grades 0–III, Expected Calibration Error (ECE), and sensitivity at 90% specificity. **16 GB VRAM fit:** FP16 mixed-precision training of lightweight video backbones on 16-frame 256×256 ultrasound clips consumes ~9–11 GB VRAM.
5. **Socratic stress-test:** *Assumption:* Deep encoders learn genuine ductal wall echogenicity rather than hospital-site watermarks, depth rulers, or transducer geometry. *Month-1 test:* Train a baseline classifier on 200 images with liver parenchyma blacked out (retaining only borders/metadata zones) vs. tightly cropped ROI tiles; if the blacked-out model exceeds 0.60 AUROC, build automated fan-beam mask cropping before any architecture research.

---

### 3. ToneDisentangle: Dialect-Invariant Acoustic Biomarkers for Post-Stroke Dysarthria Across Regional Thai Speakers *(Bold / Unconventional)*
1. **Name & Pitch:** **ToneDisentangle** — An adversarial speech representation framework that strips out Northern (*Kham Mueang*), Northeastern (*Isan*), and Southern (*Pak Tai*) dialectal tone/tempo variance to detect mild post-stroke dysarthria and bulbar weakness via smartphone audio.
2. **Thai problem:** Stroke is a leading cause of disability in Thailand, and post-discharge monitoring in rural sub-districts relies heavily on Village Health Volunteers (อสม.). Existing speech-based neurological screening models trained on Central Thai (5 lexical tones) misclassify healthy speakers of Isan (6 tones), Lanna (6 tones), or rapid-tempo Pak Tai dialects as having dysarthric pitch monopitch, articulatory slurring, or prosodic abnormality *(cross-dialect false-positive inflation rate unverified)*.
3. **What's novel:** Speech pathology models in tonal languages rarely address how lexical tone contour shifts interact with neuromotor dysarthria. This project uses gradient-reversal and mutual-information minimization on self-supervised speech layers to disentangle regional phonological identity from articulatory motor degradation.
4. **Core experiment or build:** Compare standard fine-tuning of Whisper-small / WavLM-Base-Plus against a multi-task layer-weighted adapter with an adversarial dialect discriminator and articulatory-feature bottleneck (jitter, shimmer, vowel space area, F0 contour velocity). **Data source:** Public regional Thai speech corpora (CommonVoice Thai, Gowajee/LOTUS regional subsets) paired with dysarthric speech samples or controlled acoustic-motor perturbations validated alongside a hospital stroke rehabilitation unit *(clinical cohort size unverified)*. **Metrics:** Equalized Odds / Worst-Group AUROC across the 4 Thai dialect regions, plus F1 on mild dysarthria detection. **16 GB VRAM fit:** Extracting and fine-tuning WavLM-Base-Plus (94M params) with LoRA/adapters on 10-second 16 kHz audio segments uses <6 GB VRAM in BF16.
5. **Socratic stress-test:** *Assumption:* Removing dialect-predictive acoustic subspace does not erase the exact F0 contour flattening and formant centralization that indicate dysarthria in a tonal language. *Month-1 test:* Apply synthetic formant centralization and pitch-velocity damping to healthy Central, Isan, and Southern Thai speech; test whether a gradient-reversal dialect-invariant projection still preserves >85% separability of the perturbed samples.

---

### 4. MelioDecide: Cost-Sensitive Counterfactual Sepsis Triage for Monsoon-Season Melioidosis
1. **Name & Pitch:** **MelioDecide** — A multimodal Bayesian decision-support model combining routine 2-hour community hospital admission labs, seasonal/soil exposure risk, and portable chest X-rays to optimize empirical ceftazidime/carbapenem escalation before 72-hour blood cultures return.
2. **Thai problem:** *Burkholderia pseudomallei* (melioidosis) is hyperendemic in rural Thailand, causing ~2,000–3,000 deaths annually *(unverified exact current national toll)* with case fatality rates reaching 30–40% in bacteremic patients. Because *B. pseudomallei* is intrinsically resistant to standard empirical community-acquired sepsis antibiotics (ceftriaxone/ampicillin) and blood cultures take 48–72 hours, delayed escalation kills patients, whereas blanket ceftazidime/meropenem use drives antimicrobial resistance and depletes district hospital budgets.
3. **What's novel:** Rather than another black-box sepsis risk score, MelioDecide frames empirical antibiotic selection as an asymmetric cost-sensitive utility problem under antibiotic stewardship budgets, fusing tabular clinical priors with CXR upper-lobe cavitation/nodular embeddings.
4. **Core experiment or build:** Compare tabular baselines (CatBoost, TabPFN, Bayesian Logistic Regression) against a late-fusion multimodal architecture (BioViL-T / DenseNet-121 CXR features + calibrated gradient boosted trees) evaluated via Decision Curve Analysis. **Data source:** Retrospective febrile bacteremia cohorts (*B. pseudomallei* vs. *E. coli* / *K. pneumoniae* / *S. aureus*) from provincial Thai hospitals or MORU open datasets *(access to paired CXR+tabular records unverified)*. **Metrics:** Net Benefit across threshold probabilities (5%–30%), Brier Score, and time-to-effective-therapy gained at a fixed 15% false-escalation budget. **16 GB VRAM fit:** Tabular + frozen/LoRA 2D CXR encoders train in <8 GB VRAM on 32 GB system RAM, enabling extensive Monte Carlo bootstrap uncertainty quantification on the 24-core CPU.
5. **Socratic stress-test:** *Assumption:* Routine first-2-hour admission labs (CBC, electrolytes, glucose, liver/renal panel) and CXR contain sufficient signal to separate melioidosis from other Gram-negative sepsis beyond simple "diabetic farmer in rainy season" heuristics. *Month-1 test:* Fit a 4-variable heuristic baseline (season, diabetes, occupation, ketonuria/glucose) vs. full lab panel on summary/retrospective data; only proceed with multimodal CXR fusion if full labs + imaging yield a statistically significant Net Benefit gain on Decision Curve Analysis.

---

### 5. YaChud-Graph: Multimodal Pouch Inspection & Herbal–Drug Toxicity Predictor for Rural Polypharmacy *(Bold / Unconventional)*
1. **Name & Pitch:** **YaChud-Graph** — A visual multi-pill pouch inspector coupled with a heterogeneous pharmacokinetic Graph Neural Network (GNN) that screens informal *Ya Chud* drug packets and Thai herbal remedies (*Fah Talai Jone*, *Kratom*, *Ya Daa*) for severe interactions with chronic NCD medications.
2. **Thai problem:** Elderly patients in rural Thailand frequently self-medicate muscle pain with *Ya Chud* (illegal/informal pre-packed plastic pouches containing 4–6 unbranded loose tablets, often combining dexamethasone/prednisolone with multiple NSAIDs) alongside traditional herbs (*Andrographis paniculata* / *Fah Talai Jone*, *Mitragyna speciosa* / *Kratom*) and hospital-prescribed warfarin, metformin, or ACE inhibitors, driving preventable GI bleeds, adrenal crisis, and acute kidney injury *(proportion of rural AKI/GI bleeds linked to Ya Chud unverified)*.
3. **What's novel:** Western pill identifiers assume single, FDA-imprinted tablets and Western drug-drug interaction (DDI) graphs ignore Thai botanical bioactive compounds. YaChud-Graph detects co-packaging patterns (visually inferring high-probability *Ya Chud* syndrome archetypes even when individual white tablets are visually ambiguous) and links Thai herbal phytochemistry to CYP450/renal clearance pathways.
4. **Core experiment or build:** Compare a two-stage pipeline: (1) YOLOv11-seg + metric-learning visual encoder trained on multi-pill transparent plastic pouches fused with a Bayesian co-occurrence prior over known *Ya Chud* formulations; (2) a heterogeneous GNN (RGCN / HGT) predicting CYP1A2/2C9/3A4 inhibition and nephrotoxic synergy across DrugBank + Thai Herbal Pharmacopoeia SMILES structures. **Data source:** Self-captured multi-angle image dataset of ~50 common Thai generic tablets in plastic pouches + Thai FDA drug registry images + ChEMBL/DrugBank + published Thai herbal constituent assays. **Metrics:** Top-3 active-class set recall (steroid + duplicate NSAID detection) under pouch specular reflection, and AUROC/AUPRC on held-out herbal–drug CYP interaction pairs. **16 GB VRAM fit:** YOLOv11-m + HGT molecular graph training easily fits inside 8–10 GB VRAM.
5. **Socratic stress-test:** *Assumption:* Unbranded generic white/yellow tablets inside crumpled plastic pouches can be narrowed down to actionable pharmacological classes without chemical spectroscopy. *Month-1 test:* Photograph 30 common Thai generic NSAIDs, steroids, and paracetamol inside plastic bags under mobile phone lighting; test whether visual metric learning + a 3-question symptom/source prior ("bought for joint pain?", "instant relief?") achieves ≥80% recall on hidden corticosteroid + NSAID co-presence.

---

If I were the student I'd pick **#1 (Tinglish-DRG)** because Thai–English code-switched clinical text is a ubiquitous, high-value structural bottleneck across every Thai hospital, and you can guarantee Month-1 progress by bootstrapping on synthetically code-switched MIMIC-IV notes while hospital IRB clearance runs in parallel. It pairs modern LLM/QLoRA engineering with deterministic domain logic (Thai DRG v6 grouping rules), giving a rock-solid comparative thesis even if clinical partner data arrives late.

# ROUND 2

## CLAUDE — Round 2

## Claude — Round 2 (council)

### 1. Hume audit
1. **Gemini #1: "MIMIC-IV discharge notes synthetically transformed into physician-validated Tinglish."** This is decisive and flawed. MIMIC's data-use agreement restricts redistribution of derived text, and US ICU notes converted into Tinglish keep a *US disease mix and US documentation style*, so the benchmark would not measure Thai coding. The "8–15% lost reimbursement" figure is unsupported.
2. **Gemini #3: "Gowajee/LOTUS regional subsets."** My understanding is that both are predominantly Central Thai read/command speech. If no regional-dialect audio exists at scale, the whole dialect-invariance design has no training data. "Isan 6 tones, Lanna 6 tones" is also simplified, because tone inventories vary by sub-variety.
3. **Gemini #2: CASCAP retrospective ultrasound cine-loops.** The entire project rests on getting this access, and "access unverified" is in a footnote rather than in the risk section. Without the clips there is no project, since public abdominal ultrasound sets don't contain graded periductal fibrosis.
4. **Gemini #4: "MORU open datasets" with paired CXR + tabular melioidosis data.** I'm not aware of such an open paired dataset. Treat it as non-existent until a link is found.
5. **Codex #1, #2, #5 GPU fit.** These are honest about their hardware needs (CPU optimisation, OCR), which is exactly the issue: the student explicitly wants the laptop to do real training. Codex #1 (dialysis/floods) and #5 (medication bags) also **repeat ideas the student already rejected**.

### 2. Socrates: most over-rated = Gemini #1 Tinglish-DRG
Gemini ranked it first, but it breaks on the assumption that synthetic code-switched MIMIC is a valid proxy for Thai inpatient notes. Without real Thai notes (hospital IRB, which Gemini admits is unverified), every result measures how well the model reverses the student's own synthetic transformation. It's also the same idea the student rejected last round.

### 3. Most under-rated: Codex #3 "When fluent AI hides impaired Thai speech"
This beats my #5 (wingbeat). The insight is genuinely non-obvious: **modern ASR's language-model prior "auto-corrects" dysarthric errors, so the transcript looks fine while the patient's speech is impaired.** That's measurable (recogniser-vs-listener disagreement), publishable, and Thai-specific because tone and consonant-cluster errors are easy for the language model to paper over. Its real risk is recruiting stroke speakers.

### 4. Descartes merge
**Codex #3 + Gemini #3 → "Thai dysarthria assessment that neither ASR nor dialect can fool."** Two named failure modes (ASR auto-correction, and regional dialect causing false positives) in one evaluation framework: WavLM/Whisper encoders + phoneme/tone adapter, with worst-group metrics across dialects and an "ASR concealment rate." It uses the GPU heavily (fine-tuning speech encoders). The dialect part can start on healthy regional speakers, who are far easier to recruit.

Runner-up merge: **my #3 MeliRisk + Gemini #4 MelioDecide.** The satellite exposure map becomes a prior inside the bedside triage model. It's elegant but depends on clinical data.

### 5. Final top 3
| # | Project | Finish confidence | GPU use | Why |
|---|---|---|---|---|
| 1 | **VenomSight** (Claude #1): antivenom-aware Thai snake ID with abstention | **75%** | **High** | Public images, a rich ML method set (cost-sensitive loss, conformal sets, robustness), a clear clinical stake. I've discounted my own bias: the ER-photo domain gap is a real risk. |
| 2 | **FlukeScope** (Claude #2): Ov egg detection under low-cost optics | **70%** | **High** | Public Thai dataset (Chula-ParasiteEgg-11) exists, the detection benchmarks are standard, and Isan cholangiocarcinoma is the strongest Thai-specific burden on the board. |
| 3 | **Merged Thai dysarthria** (Codex #3 + Gemini #3) | **50%** | **High** | Most original idea in the round, but it is gated on stroke-speaker recruitment and ethics approval. Start the healthy-dialect half in month 1 to de-risk it. |

Honourable mention: **Gemini #2 CholangioSweep**. It has the highest clinical impact if CASCAP data were in hand, but it's 30% at best without it.

## CODEX — Round 2

**VenomSight is my revised first choice.** Wingbeat-TH deserves promotion; Tinglish-DRG deserves the largest downgrade. This assessment uses the supplied proposals and council framework only. Dataset contents, access, and novelty claims remain unverified.

**1. Hume audit**

Five claims from Claude and Gemini materially overreach their proposed evidence:

- **Claude, VenomSight:** A “300-image ‘ER-style’ test set” made partly through degradation cannot establish emergency-photo robustness. Cropping and blur test chosen corruptions; actual emergency images may introduce different poses, backgrounds, injuries, and species frequencies. Keep synthetic corruption experiments, but reserve claims about emergency settings for independently sourced images. Likewise, clinical cost weights need justification before “expected clinical cost” becomes meaningful.
- **Claude, FlukeScope:** The promised contribution is “Ov vs MIF,” yet the proposal has not established that its dataset contains independently verified labels for both. Without those labels, detection accuracy cannot answer the central question. Switching to Ov detection under degradation produces a different thesis; its originality needs a separate argument.
- **Gemini, Tinglish-DRG:** A “rock-solid comparative thesis even if clinical partner data arrives late” is unsupported. Synthetic Tinglish can support an experiment on synthetic language, but linguistic realism does not establish Thai coding validity or reimbursement validity. Models may learn the transformation generator’s conventions. The grouper, coding reference, and authentic held-out evaluation are substantive dependencies.
- **Gemini, ToneDisentangle:** Preserving “>85% separability” of artificially perturbed speech does not validate preservation of dysarthria information. The discriminator may retain artifacts of the perturbation algorithm. Real speaker-held-out data crossing dialect with impairment status are needed to distinguish dialect removal from pathology removal.
- **Gemini, YaChud-Graph:** “Visually inferring high-probability … syndrome archetypes” does not establish active ingredients in ambiguous tablets. Co-occurrence priors can look accurate on familiar packet compositions and fail on new combinations. Test unseen manufacturers and combinations, include visually indistinguishable alternatives, and permit unidentified outputs. Predicted molecular interactions also require separate validation before supporting a toxicity claim.

**2. Socrates: the most overrated idea**

**Tinglish-DRG as currently scoped.** Its decisive assumption is that synthetic code-switching preserves the difficult relationships among documentation, coding rules, and reimbursement.

If that fails, impressive benchmark scores can reward synthetic regularities while leaving the stated hospital problem unanswered. Coding, grouping, and audit-risk prediction also require different reference standards. A narrower comparison of code-switched coding methods could work, but its guaranteed fallback is overstated.

**3. The most underrated idea**

**Claude’s Wingbeat-TH beats my dialysis proposal for this student’s revised objective.** It offers substantive GPU experiments in acoustic representation learning, noise robustness, and distillation. I withdraw dialysis as my first choice here: its intervention modeling is valuable, but uncertain disruption and capacity assumptions could dominate the research.

Wingbeat needs stricter evaluation than noise augmentation alone. Split recordings by recording session, source, and device where metadata permit; compare acoustic features, spectrogram CNNs, and pretrained encoders. Public-corpus success would establish that benchmark result; Thai field transfer remains a separate claim. Dataset suitability is still unverified.

**4. Descartes merge**

Merge **my “fluent AI hides impaired Thai speech”** with **Gemini’s ToneDisentangle** into:

**When dialect adaptation hides clinically meaningful Thai speech errors.**

Ask whether adaptation improves transcription while reducing sensitivity to listener-observed errors. Compare frozen encoders, ordinary adapters, and adversarial dialect removal against blinded intelligibility judgments, using speaker-held-out evaluation with dialect and impairment represented across groups. Include consonant and timing errors alongside tone.

This gives disentanglement a measurable purpose and allows a useful negative finding: adaptation may erase information needed for assessment. Recruitment across those groups is the decisive feasibility risk.

**5. Final top three across all fifteen**

The percentages are subjective planning estimates of nine-month completion to a defensible master’s standard, assuming no privileged data access. GPU use describes the proposed experiments.

| Rank | Thesis | Confidence | GPU use | Reasoning |
|---|---|---:|---|---|
| 1 | **VenomSight, narrowed to selective identification under distribution shift** | **80%** | **High** | Public-image sources offer a plausible start for backbone, loss, and abstention comparisons, with source-held-out evaluation and sensitivity analysis of clinical cost weights. |
| 2 | **Wingbeat-TH, focused on recording-domain generalization** | **68%** | **High** | Acoustic training and distillation offer substantial local experiments, provided month one confirms usable labels and metadata for independent evaluation. |
| 3 | **Merged speech thesis** | **55%** | **High** | It asks the strongest scientific question, but recruiting enough speakers across dialect and impairment groups could prevent a defensible comparison. |
## GEMINI — Round 2

﻿## Gemini — Round 2 (Council Cross-Examination)

### 1. Hume Audit: 5 Flawed, Overstated, or Unverified Claims

1. **Claude #2 (FlukeScope):** *"Parasite-egg detection datasets exist (Chula-ParasiteEgg-11, ICIP 2022 challenge, includes Ov)... check whether Chula-ParasiteEgg-11 or the literature has labelled MIF eggs."*
   - **Why it fails:** **Chula-ParasiteEgg-11** contains 11 species classes (including *O. viverrini*), **none of which are minute intestinal flukes (MIF / *Haplorchis* spp.)**. Moreover, *O. viverrini* and *Haplorchis taichui* eggs have overlapping 26–30 µm morphometrics that cannot be reliably separated in standard 400× brightfield images without PCR or specialized staining, meaning verifiable ground-truth labels do not exist in public microscopy corpora.

2. **Claude #1 (VenomSight):** *"the loss reflects clinical consequence (which antivenom you'd give)... QSMI produces largely species-specific monovalent antivenoms."*
   - **Why it is overstated:** QSMI also produces **Neuro** and **Hemato Polyvalent** antivenoms covering Thailand's 7 major lethal snakes, and Thai clinical toxicology guidelines prohibit administering antivenom from snake identification alone without systemic envenomation signs (e.g., 20-minute whole-blood clotting test or ptosis) due to dry bites and high anaphylaxis rates. The cost matrix must model *syndromic triage and observation pathways*, not direct antivenom dosing.

3. **Claude #3 (MeliRisk):** *"satellite-derived melioidosis risk maps at sub-district (tambon) resolution... Targets: published case locations/district counts from 506 surveillance"*
   - **Why it is decisive-but-unverified:** Public Thai DDC R506 surveillance aggregates cases by province or district of the *reporting hospital or patient residence*—not the *tambon* (~7,255 units) of environmental exposure—and melioidosis latency spans weeks to years. Fine-tuning a 10m-resolution satellite foundation model (Prithvi/SatMAE) on coarse administrative residence counts fits spatial reporting artifacts rather than *B. pseudomallei* ecology.

4. **Codex #1 (Dialysis lifelines):** *"Combine OpenStreetMap roads, satellite flood extents, verified facility locations, and synthetic patient distributions... run on CPU"*
   - **Why it is overstated:** Optimizing routing over *synthetic* patient locations and *assumed* clinic surge capacities is circular: the robust optimizer only recovers priors baked into the simulation while leaving the RTX 4090 completely idle.

5. **Codex #4 (Alms without invisible salt):** *"Partner with several offering-food vendors to collect meal photographs and weighed ingredient records."*
   - **Why it is decisive-but-unverified:** Thai morning-market alms vendors cook in bulk vats and ladle variable broth fractions into plastic bags; weighing batch ingredients does not yield accurate per-portion sodium ground truth without chemical assay, creating a severe non-ML data bottleneck.

---

### 2. Socrates: The Single Most Over-Rated Idea

- **Most Over-Rated Idea:** **Codex #1 — Dialysis lifelines under water** (ranked #1 and recommended as the top student pick by Codex; I also demote my own Round 1 #1, **Tinglish-DRG**, as overly administrative and vulnerable to synthetic MIMIC-IV circularity if hospital IRB stalls).
- **The Assumption That Breaks It:** It assumes **flood haemodialysis disruption is governed by road-graph shortest paths rather than facility utility failure and pre-flood clinical prophylaxis**. In Thai floods, dialysis units fail because reverse-osmosis water treatment loses municipal pressure/power, and nephrology teams intervene *before* inundation via early dialysis or oral potassium binders—not dynamic min-cost flow re-routing during peak floodwaters. Worse, it uses **0% of the RTX 4090 GPU**, turning an ML capstone into a synthetic CPU operations-research exercise.

---

### 3. Most Under-Rated Idea From Another Advisor

- **Pick:** **Codex #3 — When fluent AI hides impaired Thai speech** (ranked #3 by Codex behind two CPU-only scheduling projects), which **beats my own Gemini #3 (ToneDisentangle)**.
- **Why It Beats Mine:** My *ToneDisentangle* relied on gradient-reversal to strip regional dialect features from spontaneous speech—risking erasing the exact F0 contour and formant velocities needed to detect dysarthria. Codex #3 identifies a much sharper foundational ML flaw: modern speech models (Whisper, WavLM) use contextual language priors that **silently auto-correct slurred Thai tones and consonant clusters**, masking neurological decline. Evaluating acoustic-vs-language-prior divergence on controlled minimal pairs is cleaner, more diagnostic, and directly testable.

---

### 4. Descartes Merge: Combining Two Ideas Into a Stronger Thesis

- **Merge:** **Codex #3 (*When fluent AI hides impaired Thai speech*) + Gemini #3 (*ToneDisentangle*)** $\rightarrow$ **Dialect-Conditioned Anti-Hallucination Speech Biomarkers for Thai Dysarthria**.
- **Why the Synthesis Is Stronger:** Codex #3 catches ASR language priors overwriting pathological pronunciation errors, but ignores that healthy Northern, Isan, and Southern Thai speakers naturally shift lexical tones and drop consonant clusters (e.g., $/kr/ \rightarrow /k/$) relative to Central Thai. By merging Codex's **acoustic-vs-LM divergence probing on minimal pairs** with Gemini's **regional dialect conditioning across public corpora (CommonVoice Thai, Gowajee, LOTUS)**, the student can train and benchmark a dialect-aware phonemic-posterior adapter on the RTX 4090 immediately using public audio and controlled acoustic perturbations, requiring only a small clinical validation cohort.

---

### 5. Final Top 3 Across All Proposals

1. **VenomSight — Clinically Reframed to Syndromic & Polyvalent/Monovalent Triage (Claude #1)**
   - **9-Month Confidence:** **90%** | **GPU Usage:** **High**
   - **Reasoning:** Public SnakeCLEF/iNaturalist data lets the student start training ConvNeXt, ViT, and DINOv2 models with cost-sensitive conformal abstention on day one without hospital IRB delays, provided the decision matrix is corrected to reflect QSMI polyvalent/monovalent syndromic pathways and mimic look-alikes.

2. **The Fluency Trap in Tonal Dysarthria (Descartes Merge: Codex #3 + Gemini #3)**
   - **9-Month Confidence:** **82%** | **GPU Usage:** **High**
   - **Reasoning:** Layer-wise probing and LoRA/CTC fine-tuning of Whisper and WavLM to prevent language priors from auto-correcting dysarthric errors—while controlling for Isan, Northern, and Southern dialect shifts—is a deeply original speech representation thesis built for a 16 GB RTX 4090.

3. **YaChud-Graph — Multi-Pill Pouch Inspection & Herbal–Drug Toxicity GNN (Gemini #5, incorporating Codex #5's longitudinal bag verification)**
   - **9-Month Confidence:** **80%** | **GPU Usage:** **High**
   - **Reasoning:** Combining YOLOv11-seg + metric learning under plastic-pouch reflections with a Heterogeneous Graph Transformer over public DrugBank/ChEMBL and Thai Herbal Pharmacopoeia structures requires zero patient IRB (commercial pills can be photographed directly) and heavily exercises the GPU across both computer vision and molecular GNNs.
