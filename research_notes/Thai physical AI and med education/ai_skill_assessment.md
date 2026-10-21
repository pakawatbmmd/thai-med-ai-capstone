# AI for Assessing and Coaching Clinical Procedural Skills (surgical/procedural skill assessment, egocentric procedural understanding, AI coaching) — state as of Oct 2026

Scope note: Research done 21 Oct 2026 with web search and page fetches (about 20 tool calls; Firecrawl hit its rate limit, so most retrieval used WebSearch/WebFetch). "Verified" means I read the claim on the cited page, or in an abstract or excerpt of it, this session. Items marked **[UNVERIFIED]** come from background knowledge and were not checked this session; they sit in the Gaps sections for the report writer to confirm or drop. Items from before 2024 are marked **[pre-2024]**.

---

## Q1. Datasets: sizes, licences, access conditions

### Takeaway
The public skill-labelled corpora are still small and fragmented, at roughly 100–1,300 videos each. Robotic JIGSAWS (103 videos, 8 surgeons) is the legacy benchmark, but its labels look unreliable. Newer dry-lab datasets from the Dresden/Aachen group (AIxSuture/OSS open suturing, 314 videos; LASANA laparoscopic, 1,270 stereo videos) are the best skill-score targets for a laptop-scale project. Medical tasks are almost absent from large egocentric proficiency benchmarks, which is a real gap.

### Cited Findings
**Skill-labelled surgical datasets**
- **JIGSAWS** [pre-2024, 2014]: da Vinci recordings of 8 surgeons at different skill levels, each doing 5 repetitions of suturing, knot-tying and needle-passing on a bench-top model. It has stereo endoscopic video and kinematics, and access is through an access form. — [JHU CIRL JIGSAWS page](https://cirl.lcsr.jhu.edu/research/hmm/datasets/jigsaws_release/); [Finspire13 repo noting the access form](https://github.com/Finspire13/Towards-Unified-Surgical-Skill-Assessment)
- JIGSAWS has 103 videos (39 suturing, 36 knot tying, 28 needle passing) with OSATS-style modified GRS labels (range 6–30). — [Hoffmann et al., arXiv 2608.17519](https://arxiv.org/html/2608.17519v1)
- JIGSAWS annotations look inconsistent; for example, some experts receive low scores. A 2024 IEEE RA-L paper (Hendricks et al.) statistically analysed the dataset's limitations. — [arXiv 2608.17519](https://arxiv.org/html/2608.17519v1)
- An unofficial JIGSAWS mirror exists on Kaggle. Its licence status relative to the official access form is unclear. — [Kaggle](https://www.kaggle.com/datasets/aditya9790/jigsaws-skill-assessment-working-set/data)
- **AIxSuture** (IJCARS 2024): 314 videos of about 5 minutes each. 157 students did open suturing before and after a 1-hour training course at University Hospital Aachen. Labels are OSATS across 8 components scored 1–5. Benchmark accuracy and F1 reach about 75%. The data is hosted on Zenodo. — [Springer IJCARS](https://link.springer.com/article/10.1007/s11548-024-03093-3); [PubMed 38526613](https://pubmed.ncbi.nlm.nih.gov/38526613/); [Zenodo 7940583](https://zenodo.org/records/7940583)
- **OSS – Open Suturing Skills challenge 2024–2025** (MICCAI challenge; arXiv May 2026, 57 authors, submitted to MedIA). Videos show open suturing in a dry lab, filmed by a static GoPro, with instrument trajectories. Tasks were (1) 4-class skill level, (2) full OSATS prediction over 8 categories, and (3) hand and tool tracking. Dataset size was not stated on the abstract page. — [arXiv 2605.22200](https://arxiv.org/abs/2605.22200)
- **LASANA** (Funke et al., arXiv Feb 2026, under review): 1,270 stereo recordings of 4 basic laparoscopic tasks, mostly from a training course, so skill varies naturally. Each recording has a structured skill rating aggregated from 3 independent raters, binary task-specific error labels, and predefined splits. — [arXiv 2602.09927](https://arxiv.org/abs/2602.09927)
- A separate reading of LASANA's suture-and-knot subset reports 314 videos from 70 participants (58 students, 12 clinicians), a modified GOALS score averaged over 4 assessors, and a 232/32/50 split. **Conflict:** 4 assessors here versus "three independent raters" in the LASANA abstract. — [arXiv 2608.17519](https://arxiv.org/html/2608.17519v1) vs [arXiv 2602.09927](https://arxiv.org/abs/2602.09927)
- **SimSurgSkill** (EndoVis 2021 sub-challenge): virtual-reality surgical tasks, with instrument localisation and skill prediction. The data is on Google Cloud Storage; size and kinematics were not confirmed. — [EndoVis site](https://endovis.grand-challenge.org/)
- **PETRAW** (EndoVis 2021, "PEg TRAnsfer Workflow recognition by different modalities"). No size details found this session. — [EndoVis site](https://endovis.grand-challenge.org/)
- **SAR-RARP50** (EndoVis 2022): 50 in-vivo suturing segments from robot-assisted radical prostatectomy, for action recognition and instrument segmentation. Described as the first multimodal public in-vivo dataset for these tasks. It is hosted on the UCL research data repository, and 12 teams took part. — [arXiv 2401.00496](https://arxiv.org/pdf/2401.00496); [UCL RDR](https://rdr.ucl.ac.uk/projects/SAR-RARP50_Segmentation_of_surgical_instrumentation_and_Action_Recognition_on_Robot-Assisted_Radical_Prostatectomy_Challenge/191091)
- **SurgSkill-Bench** (arXiv 2608.30872, 2026): a multimodal surgical skill assessment benchmark that pairs video with evaluator comments (see Q2 for results). — [arXiv 2608.30872](https://arxiv.org/pdf/2608.30872)

**Egocentric / procedural datasets**
- **EgoSurgery-Phase** (Keio): about 15 hours of real open surgery from a head-mounted camera, 9 phases, plus eye-gaze. Described as the first public real open-surgery phase dataset. — [arXiv 2405.19644](https://arxiv.org/html/2405.19644v3)
- **EgoSurgery-Tool**: over 49K tool boxes across 15 categories and over 46K hand boxes (wearer and other surgeons, left and right), with 9 detectors benchmarked. — [arXiv 2406.03095](https://arxiv.org/pdf/2406.03095)
- **EgoSurgery-HTS**: pixel-level hand, tool and hand-tool segmentation over 14 tool types; journal version December 2025. — [arXiv 2503.18755](https://arxiv.org/abs/2503.18755); [PMC12686825](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12686825/)
- **Ego-Exo4D**: 1,286 hours of ego and exo video from 740 participants in 13 cities, over 123 scene contexts. Benchmarks are fine-grained keystep, proficiency estimation, cross-view translation, and 3D hand/body pose. The IJCV version was published December 2025. — [arXiv 2311.18259](https://arxiv.org/abs/2311.18259); [IJCV](https://link.springer.com/article/10.1007/s11263-025-02557-6)
- Ego-Exo4D's procedural scenarios include "Cooking, Bike Repair, Health". The docs page does not break Health down further. — [Ego-Exo4D docs](https://docs.ego-exo4d-data.org/)
- The Ego-Exo4D **demonstrator proficiency** subset covers 6 domains (cooking, basketball, soccer, dancing, music, bouldering). It uses 4 labels (Novice, Early, Intermediate, Late Expert) plus free-form expert commentary, and reports top-1 accuracy. **Health is not in the demonstrator proficiency subset.** — [arXiv 2605.03848 via search excerpt](https://arxiv.org/pdf/2605.03848)
- **EgoEMS** (arXiv 2511.09894): a "high-fidelity multimodal egocentric dataset for cognitive assistance in Emergency Medical Services". Details were not fetched. — [arXiv 2511.09894](https://arxiv.org/pdf/2511.09894)

**CPR / medical-action datasets**
- **CPREval-6k** (AAAI 2026): a "multi-view, multi-label medical action benchmark" with 6,372 expert-annotated chest-compression videos and 22 clinical labels. Availability and licence were not stated in the abstract. — [arXiv 2511.10060](https://arxiv.org/abs/2511.10060)
- An RWTH Aachen dataset has 42 video sequences showing 7 typical CPR errors. It was used in a 2025 randomised human-rating study with 90 paramedics and physicians, so it is not an ML training set. — [RWTH publications](https://publications.rwth-aachen.de/record/1000384/export/he?ln=en)
- A smartphone-CPR deep-learning repository estimates compression count, depth, release and hand position from video. No public dataset is clearly released. — [GitHub seongjiko/CPR-estimator](https://github.com/seongjiko/CPR-estimator/blob/main/README.md)
- [pre-2024] Earlier smartphone CPR work used optical flow or FFT to estimate compression rate rather than deep learning. — [PMC4982121](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982121/); [CMU RI](https://ri.cmu.edu/publications/analysis-of-smart-phone-video-footage-classifies-chest-compression-rate-during-simulated-cpr)

### Inferences
- For a laptop project, AIxSuture/OSS and LASANA are the most attractive skill-regression targets. They are recent and multi-rater (LASANA), come from cheap static cameras (GoPro or box trainer), are about the right size for frozen-feature work, and come from the same group that publishes the cross-rubric transfer analysis.
- JIGSAWS is useful mainly as a legacy comparison point. Results tuned to it should be treated with suspicion given the documented label issues.
- Ego-Exo4D gives a large proficiency-estimation testbed outside medicine, but no medical proficiency labels. A "Health" scenario exists in the dataset, so pulling the Health takes and studying keystep or proficiency transfer into medicine is a possible novelty angle, pending confirmation of content and labels.
- CPR is the most tractable non-surgical procedure. Skeleton-based methods reach high accuracy (see Q2), and a phone camera plus a manikin is cheap. The limiting factor is whether CPREval-6k is downloadable.

### Gaps
- **Licences not verified this session:** AIxSuture on Zenodo (I believe CC BY-NC-SA 4.0 [UNVERIFIED]); LASANA; OSS challenge data; SAR-RARP50 (believed CC BY-NC-SA [UNVERIFIED]); Ego-Exo4D (requires signing a licence agreement and getting AWS credentials [UNVERIFIED]); EgoSurgery (release status "will be released at project page" in the papers, current status unconfirmed).
- **[UNVERIFIED] background numbers to confirm:** Cholec80 has 80 cholecystectomy videos with phase and tool labels (CAMMA, non-commercial). CholecT50 has 50 videos with action-triplet labels. HeiChole has 33 videos with phase, action, tool and skill ratings (EndoVis 2019). PETRAW has about 150 peg-transfer trials with video, kinematics and segmentation. HoloAssist (Microsoft, ICCV 2023) has about 166 hours, 350 instructor-performer pairs and 20 tasks, with mistake and intervention labels and no medical tasks. Ego-Exo4D Health is said to include COVID-19 antigen test and CPR scenarios. None of these were checked this session.
- I found no public OSCE video dataset with skill labels, and no public ultrasound-probe-handling or IV-insertion video dataset with proficiency labels. This looks like a real gap, but my search depth was limited.
- Full LASANA task list, participant counts per task and access terms were not retrieved.

---

## Q2. Methods and reported performance

### Takeaway
State-of-the-art methods are general spatiotemporal video backbones (3D-CNN, VideoMAE, V-JEPA-type, ViViT) with light temporal heads. In-domain scores are good (CCC about 0.8 on LASANA). Cross-dataset or cross-rubric transfer is poor (CCC 0.06–0.20 into JIGSAWS; Spearman about 0.4–0.46 for domain adaptation). Video-only VLMs remain weak at fine-grained temporal surgical reasoning. Surgical world models have appeared (2025–2026) but face a "plausibility gap" in surgical semantics.

### Cited Findings
**Skill-score regression / classification**
- Cross-rubric transfer study (Hoffmann, von Bechtolsheim, Speidel, Hisey; arXiv 2608.17519, 2026). Architecture: X3D (Kinetics-400 pretrained) with an LSTM, average pooling and multi-head linear outputs, using 16-frame clips sampled every 5th frame. Compared: supervised (Huber loss), ASAM, VICReg SSL and triplet contrastive learning. Metric: CCC. — [arXiv 2608.17519](https://arxiv.org/html/2608.17519v1)
  - LASANA in-domain CCC: Kinetics-only 0.78, supervised 0.81, ASAM 0.74, SSL 0.78, CL 0.80.
  - LASANA-to-JIGSAWS transfer CCC: 0.06–0.20 (best was CL at 0.20). JIGSAWS in-domain CCC was only −0.03 to 0.22.
  - JIGSAWS-to-LASANA transfer CCC: 0.77–0.80.
  - A Kinetics-only backbone already reaches 0.78 on LASANA, which suggests the task heads carry most of the skill prediction. VRAM and compute were not reported.
- **CoRe-DA** (Anastasiou et al., 2026, arXiv 2603.29666): contrastive regression for unsupervised domain adaptation in skill assessment, with reported Spearman 0.46 and 0.41 (as cited by 2608.17519). Anastasiou et al. 2025 also studied cross-domain pre-training for few-shot skill assessment. — [arXiv 2608.17519 citing them](https://arxiv.org/html/2608.17519v1)
- **AIxSuture** benchmark: accuracy and F1 up to about 75% on skill classification. — [PubMed 38526613](https://pubmed.ncbi.nlm.nih.gov/38526613/)
- **OSS challenge:** "general-purpose spatiotemporal video models performed best consistently". Fine-grained OSATS prediction remains hard but "benefits substantially from more training data". Keypoint tracking is hindered by occlusion and objects leaving the frame. — [arXiv 2605.22200](https://arxiv.org/abs/2605.22200)
- [pre-2024] An I3D on JIGSAWS clips reported 95.1–100% skill-class accuracy (2019). This kind of saturation on tiny splits is one reason JIGSAWS classification numbers are not considered informative. — [arXiv 1903.02306](https://arxiv.org/pdf/1903.02306)
- [pre-2024] A video-based formative and summative assessment model (Sci Rep 2023) produced feedback as heatmaps of features correlated with performance. — [Nature Sci Rep](https://www.nature.com/articles/s41598-022-26367-9)
- **ZEAL** (arXiv 2407.02738, 2024): skill assessment with zero-shot tool inference using a unified foundation model. — [arXiv 2407.02738](https://arxiv.org/pdf/2407.02738)

**Video foundation models**
- **SurgSkill-Bench** (arXiv 2608.30872): with CA-Frame frame selection, VideoMAE rose from about 0.57 to 0.86 AUROC and ViViT from 0.55 to 0.85. With key-frame inputs, ViViT and V-JEPA 2 both reached a best mean AUROC of about 0.88. The authors warn that the "assisted" setting uses evaluator comments and is not autonomous video-only assessment. — [arXiv 2608.30872](https://arxiv.org/pdf/2608.30872)
- **SurgRec** (arXiv 2603.29966): surgical pretraining in MAE and JEPA variants on 10,535 videos, evaluated across 16 downstream datasets. It finds VLMs unreliable for fine-grained temporal recognition. — [arXiv 2603.29966](https://arxiv.org/html/2603.29966v2)
- **JHU-VPT (JEPA)** (MIDL 2025): a cataract-surgery JEPA model evaluated on step recognition, surgical feedback and skill assessment, which performs well with attentive probing on a frozen encoder. — [MLAnthology MIDL 2025](https://mlanthology.org/midl/2025/shah2025midl-vision/)
- **Large-scale self-supervised surgical video foundation model** (arXiv 2506.02692) and **SurgBench** (arXiv 2506.07603). SurgBench covers phase, tool and action recognition but not skill. — [arXiv 2506.02692](https://arxiv.org/pdf/2506.02692); [arXiv 2506.07603](https://arxiv.org/pdf/2506.07603v2)
- A V-JEPA v1 encoder was adapted to surgical clinical prediction (not skill), supporting the claim that generic video foundation models transfer to surgery. — [arXiv 2509.06831](https://arxiv.org/html/2509.06831v1)
- **ZEN** (arXiv 2602.13633, 2026): a surgical video foundation model evaluated with frozen-backbone, few-shot and zero-shot protocols, including skill assessment (search excerpt only). — [arXiv 2602.13633](https://www.arxiv.org/pdf/2602.13633)

**Egocentric proficiency estimation (Ego-Exo4D)**
- CVPR 2025 challenge entries: Sapiens-2B multi-task reached 43.6% top-1, and zero-shot scenario recognition plus view-specific VideoMAE reached 47.8% (4-class demonstrator proficiency). — [arXiv 2507.08022 via search](https://web3.arxiv.org/pdf/2507.08022)
- **SkillFormer** (parameter-efficient multi-view fusion), **PATS** (proficiency-aware temporal sampling) and **ProfVLM** (proficiency as conditional generation, outputting a label plus expert-style feedback through a gated cross-view projector and a compact LM). They claim SOTA with up to 20x fewer trainable parameters and 3x fewer epochs than video-transformer baselines. Exact accuracies were not on the abstract page. — [arXiv 2605.03848](https://arxiv.org/abs/2605.03848)

**Medical action (CPR) evaluation**
- **GaussMedAct** (AAAI 2026): skeleton joints are tokenised as adaptive anisotropic 3D Gaussians with dual-stream joint and bone encoding. It reaches 92.1% top-1 on CPREval-6k, +5.9% over a baseline at 10% of the FLOPs, runs in real time, and is reported to be more robust across datasets. — [arXiv 2511.10060](https://arxiv.org/abs/2511.10060)

**VLMs for procedural feedback**
- Rau et al. evaluated 11 VLMs on 17 surgical tasks, including skill assessment. Tasks needing spatial or temporal reasoning remained difficult. — [arXiv 2504.02799](https://arxiv.org/html/2504.02799v1)
- Nasriddinov, Kocielnik, Anandkumar, Hung (arXiv 2511.15159, Nov 2025) learned a surgical action ontology from trainer-to-trainee feedback transcripts across 33 surgeries. They fine-tuned a video-to-triplet model (instrument, action, target) and used the triplets to condition GPT-4o's feedback text. This is a "structured perception leads to LLM feedback" pipeline. — [arXiv 2511.15159](https://arxiv.org/html/2511.15159v1)
- SurgVLM (arXiv 2506.02555) and Halsted (arXiv 2603.22583) are large surgical VLMs, but they do not focus on skill feedback. — [arXiv 2506.02555](https://arxiv.org/abs/2506.02555v1); [arXiv 2603.22583](https://arxiv.org/pdf/2603.22583)

**World models / surgical video generation**
- **SurgVeo** benchmark, "How Far Are Surgeons from Surgical World Models?" (arXiv 2511.01775, Nov 2025): expert-rated zero-shot Veo-3 surgical video. It found a "plausibility gap": high visual plausibility, but critical failure on instrument operation, feedback and surgical intent. — [arXiv 2511.01775](https://arxiv.org/html/2511.01775v1)
- **SurgWorld** (arXiv 2512.23162, Dec 2025): built on NVIDIA Cosmos 2.5 with a Surgical Action-Text Alignment dataset. An inverse-dynamics model infers pseudo-kinematics from synthetic video, and a robot policy trained with the augmented data beat one trained on real-only data. — [arXiv 2512.23162](https://arxiv.org/pdf/2512.23162v1); [alphaXiv](https://alphaxiv.org/overview/2512.23162v3)
- **SAW** (JHU and NVIDIA, arXiv 2603.13024, Mar 2026): a video diffusion model for surgical actions, conditioned on language, a reference scene, a tissue-affordance mask and 2D tool-tip trajectories. Adding synthetic clips improved rare-action recognition on real data. — [arXiv 2603.13024](https://arxiv.org/abs/2603.13024)
- A survey, "Surgical Video Generation From Diffusion to World Models" (arXiv 2608.26214), names SWoMo (rule-based simulator plus scene graph plus diffusion renderer) as a representative world model. It states that explicit state-transition modelling is "an emerging direction with only preliminary demonstrations". — [arXiv 2608.26214](https://arxiv.org/pdf/2608.26214)

### Inferences
- A frozen backbone plus a light head is both the dominant recipe and laptop-feasible. The finding that a Kinetics-only X3D reaches CCC 0.78 on LASANA implies that systematic frozen-feature comparisons (V-JEPA 2, VideoMAE v2, surgical JEPA/MAE models) are informative and cheap to run, because features can be precomputed once.
- Generation-for-assessment is underexplored. Current world-model work uses synthetic video for recognition or robot policy, not for skill assessment or counterfactual feedback ("what would the expert have done here?"). A small-scale latent-dynamics or V-JEPA-2-style action-conditioned predictor trained on suturing data, with prediction error used as a skill or anomaly signal, would be a novel angle that fits a laptop (inference: not shown in any source).
- Structured perception outputs (triplets, tool trajectories, hand keypoints) fed to an LLM look like the most defensible route to explainable feedback, given VLMs' temporal weakness.

### Gaps
- [UNVERIFIED] Specific VRAM figures: V-JEPA 2 ViT-L (300M) and ViT-g (1B) inference with fp16 and small batches; VideoMAE v2 ViT-B/L. I believe ViT-L feature extraction fits easily in 16 GB and ViT-g fits with fp16 and short clips, but this was not checked. InternVideo2 skill-assessment results were not found in any source.
- Kinematics plus video fusion: no 2024–2026 numbers retrieved (the OSS challenge provides trajectories, but fusion results were not on the abstract page).
- I could not obtain exact Ego-Exo4D proficiency accuracies for SkillFormer, PATS or ProfVLM, or the official baseline numbers.
- Gesture-recognition SOTA on JIGSAWS and SAR-RARP50 (action-recognition F1 and accuracy) was not retrieved.

---

## Q3. Coaching/feedback: does AI feedback improve trainee learning?

### Takeaway
There is RCT-level evidence, concentrated in one group (McGill Neurosurgical Simulation and AI Learning Centre), that real-time or post-hoc AI feedback in VR neurosurgical simulation improves skill acquisition over no feedback and, in some designs, over expert instruction. Evidence for video-based explainable AI feedback on suturing is weaker: one 2025 study found no difference from video coaching on performance gaps.

### Cited Findings
- Fazlollahi et al., "Effect of Artificial Intelligence Tutoring vs Expert Instruction on Learning Simulated Surgical Skills Among Medical Students: A Randomized Clinical Trial", JAMA Netw Open 2022;5(2):e2149008 [pre-2024]. Instructor-blinded RCT of medical students (pre-clinical years 0–2) from 4 Canadian institutions, Jan–Apr 2021, intention-to-treat. One 75-minute VR brain-tumour resection session with 5 practice resections, each followed by 5-minute feedback. The VOA (Virtual Operative Assistant) gave automated audiovisual metric-based feedback; comparators were remote expert verbal instruction and no feedback. About 70 students were randomised (conference abstract). Outcomes were skill (deep-learning score and blinded OSATS), affective and cognitive. — [Stony Brook record](https://researchconnect.stonybrook.edu/en/publications/effect-of-artificial-intelligence-tutoring-vs-expert-instruction-/); [McGill NeuroSim](https://neurosim.mcgill.ca/publication-of-the-voa-trial)
- A 2025 randomised crossover trial (npj AI, Nature portfolio, s44387-025-00032-8) studied combined real-time AI and in-person expert instruction in simulated surgery. The full text was paywalled and not read. — [Nature](https://www.nature.com/articles/s44387-025-00032-8)
- News coverage of a McGill RCT reports that "trainees who received AI instruction performed significantly better than those who received expert instruction and no real-time instruction." This is a secondary source. — [AXIS Medical Education](https://axismeded.com/news/ai-guided-feedback-outperforms-human-instructors-in-neurosurgical-training-study/2468079/)
- An RCT on feedback modality in simulated surgical skills found learners acquire skills with autonomous computer feedback, and visual feedback improved learning outcomes (J Surg Educ, 2023/24). — [ScienceDirect S1931720423004099](https://www.sciencedirect.com/science/article/abs/pii/S1931720423004099)
- Gomez, Seenivasan, …, Unberath (JHU; arXiv 2508.02593, Aug 2025): a prospective study of explainable-AI, user-specific feedback (skill proxies tied to primitive actions, compared to expert benchmarks) versus traditional video-based coaching for medical students' suturing. Cognitive load and confidence improved, but there was **no difference between feedback types in reducing performance gaps or in practice adjustments**. Trends favoured the XAI group, and N was not stated in the abstract. — [arXiv 2508.02593](https://arxiv.org/abs/2508.02593)
- A JMIR 2025 review found that AI-enhanced training environments provided automated skill assessment, personalised feedback and adaptive learning trajectories. — [JMIR 2025 e58966](https://www.jmir.org/2025/1/e58966/)
- A PMC systematic review covers AI-derived performance metrics in surgical simulation. — [PMC12807625](https://pmc.ncbi.nlm.nih.gov/articles/PMC12807625/)
- A 2025 randomised training study with 90 paramedics and physicians used 42 videos of 7 CPR errors to train error recognition (not AI feedback). — [RWTH](https://publications.rwth-aachen.de/record/1000384/export/he?ln=en)

### Inferences
- The strongest RCT evidence is for VR simulators with rich, built-in instrument telemetry, not for camera-only, low-cost setups. A capstone that shows camera-only AI feedback works on a box trainer, even as a small pilot crossover study, would fill a recognised gap.
- The null result on performance in the JHU XAI-suturing study suggests that the *content and actionability* of feedback, not just its existence, is the open question. This makes "what feedback to generate" a research question in its own right.

### Gaps
- Effect sizes for the VOA RCT, the 2025 npj crossover trial and the J Surg Educ modality trial were not retrieved (paywalls).
- [UNVERIFIED] CPR real-time feedback devices (e.g., accelerometer-based "CPRmeter" or QCPR manikins) have meta-analytic evidence of improved compression quality in training (AHA guidelines endorse feedback devices). Not checked this session.
- No RCT found for LLM- or VLM-generated natural-language procedural feedback.

---

## Q4. Low-cost hardware setups used in research

### Takeaway
Dry-lab skill datasets are already captured with cheap fixed cameras (GoPro for OSS/AIxSuture; standard box-trainer laparoscopes for LASANA). Peer-reviewed evidence for skill scoring from smartphones and markerless hand tracking (MediaPipe) is thin and mostly proof-of-concept, which leaves an opening for a validated cheap pipeline.

### Cited Findings
- The OSS challenge used a static GoPro in a dry lab with instrument trajectories. — [arXiv 2605.22200](https://arxiv.org/abs/2605.22200)
- A SAGES abstract describes a smartphone and box-trainer motion platform combining accelerometers with optical colour tracking of instrument tips (OpenCV, coloured tape). It was a proof-of-concept followed by a construct-validity feasibility study. — [SAGES abstract](https://sages.org/meetings/annual-meeting/abstracts-archive/a-motion-analysis-platform-for-real-time-laparoscopic-performance-using-mobile-and-wearable-technology)
- An XR training project tracks hand posture during suturing with MediaPipe on RGB-D, capturing and replaying trajectories on a rigged hand. It is preliminary and does not score skill. — [Uni Bremen XR4OR PDF](https://cgvr.cs.uni-bremen.de/xr4or/pdf/1022.pdf)
- An ASU student capstone validated MediaPipe markerless 3D hand trajectories against a marker-based PhaseSpace system. It is not peer-reviewed, but it is a close analogue of a student project. — [ASU capstone poster](https://capstones.engineering.asu.edu/wp-content/uploads/2025/04/team15markerlessquantification_809029_107455057_Capstone-Digital-Poster.pdf)
- GMH-D (IEEE ICDH 2022) [pre-2024]: a single RGB-D camera plus MediaPipe Hands for remote hand-motor assessment, validated against real 3D trajectories, with classifiers separating normal from altered performance. — [GMH-D PDF](https://researchgate.net/profile/Gianluca-Amprimo-3/publication/362922577_GMH-D_Combining_Google_MediaPipe_and_RGB-Depth_Cameras_for_Hand_Motor_Skills_Remote_Assessment/links/66125f02a7c907287a4a4acd/GMH-D-Combining-Google-MediaPipe-and-RGB-Depth-Cameras-for-Hand-Motor-Skills-Remote-Assessment.pdf)
- EgoSurgery datasets were captured with a head-mounted egocentric camera in real open surgery. — [arXiv 2405.19644](https://arxiv.org/html/2405.19644v3)

### Inferences
- A phone or GoPro over a suturing pad, plus MediaPipe or a hand-pose model, plus a frozen video backbone is a credible, cheap acquisition stack that matches the OSS/AIxSuture capture setup. That alignment lets public data serve as pretraining and benchmark, and local Thai trainee data as an external validation set.

### Gaps
- No 2024–2026 peer-reviewed papers retrieved on IMU gloves, Leap Motion, or Meta Quest hand tracking for suturing or laparoscopic skill scoring. [UNVERIFIED] Such studies exist (Leap Motion for laparoscopic motion metrics; Quest/HoloLens hand tracking in XR surgical training), but they were not verified this session.
- The accuracy of MediaPipe hand keypoints under glove or instrument occlusion for surgical tasks is not quantified in any retrieved source. The OSS paper notes occlusion makes tracking hard.

---

## Q5. Open problems named in 2025–2026 reviews and challenge reports

### Takeaway
The open problems that recur across 2025–2026 sources are cross-dataset and cross-rubric generalisation, label quality and scarcity, fine-grained OSATS sub-score prediction, hand and tool tracking under occlusion, a temporal-reasoning deficit in VLMs, a semantic "plausibility gap" in surgical world models, and missing evidence of clinical impact on learning.

### Cited Findings
- Cross-rubric and cross-dataset transfer fails into JIGSAWS (CCC ≤0.20). The visual domain gap (da Vinci vs box trainer), the construct mismatch (OSATS vs GOALS) and annotation noise are confounded. The authors call for re-annotation with multiple raters and replication on more well-annotated datasets. — [arXiv 2608.17519](https://arxiv.org/html/2608.17519v1)
- Domain adaptation reaches only about 0.41–0.46 Spearman (CoRe-DA). — [arXiv 2608.17519 citing 2603.29666](https://arxiv.org/html/2608.17519v1)
- The OSS challenge names three problems: fine-grained OSATS prediction is hard and data-hungry; keypoint tracking is hard because of occlusion and objects leaving the frame; and "more work is needed to move automated skill assessment toward clinical impact". — [arXiv 2605.22200](https://arxiv.org/abs/2605.22200)
- LASANA frames the core gap as the limited size of annotated datasets. — [arXiv 2602.09927](https://arxiv.org/abs/2602.09927)
- VLMs struggle with spatial and temporal surgical reasoning, including skill assessment. — [arXiv 2504.02799](https://arxiv.org/html/2504.02799v1); [SurgRec arXiv 2603.29966](https://arxiv.org/html/2603.29966v2)
- In surgical world models, explicit state-transition modelling has "only preliminary demonstrations", and Veo-3 fails on instrument operation and surgical intent. — [arXiv 2608.26214](https://arxiv.org/pdf/2608.26214); [arXiv 2511.01775](https://arxiv.org/html/2511.01775v1)
- In SurgSkill-Bench, strong results depend on evaluator comments (the "assisted" setting), not autonomous video-only assessment. — [arXiv 2608.30872](https://arxiv.org/pdf/2608.30872)
- Explainable feedback has not yet beaten video coaching on performance outcomes. — [arXiv 2508.02593](https://arxiv.org/abs/2508.02593)
- A thesis notes deep models for video-based skill assessment are "data-hungry and restricted to their training domain". — [RPI thesis](https://dspace.rpi.edu/items/26bc67d0-5ce2-4de4-8fa6-00c811e63de4)

### Inferences
- Validity against OSATS and GOALS is undermined by inter-rater noise. A model's ceiling is bounded by rater agreement, so projects should report CCC or ICC against rater agreement, not just Spearman.

### Gaps
- No MICCAI 2025 or 2026 EndoVis challenge summary retrieved, other than OSS. The 2025–2026 EndoVis challenge list was not checked.
- No 2025–2026 systematic review of construct validity (AI score vs OSATS vs patient outcome) was retrieved.

---

## Q6. Implications for a laptop-feasible (RTX 4090 Laptop, 16 GB) 9-month capstone

### Takeaway
The sources point to a feasible, publishable frontier project. Precompute frozen features from several video foundation models (general and surgical) on AIxSuture/OSS and LASANA. Study cross-dataset and cross-rubric transfer, and/or a predictive (JEPA or world-model) signal for skill. Then generate structured, explainable feedback, and validate on a small locally collected phone-camera set.

### Cited Findings
- Frozen-encoder probing works well for surgical skill (JHU-VPT JEPA attentive probe; Kinetics-only X3D CCC 0.78 on LASANA). — [MIDL 2025](https://mlanthology.org/midl/2025/shah2025midl-vision/); [arXiv 2608.17519](https://arxiv.org/html/2608.17519v1)
- Parameter-efficient proficiency estimation (SkillFormer/PATS/ProfVLM) claims SOTA with up to 20x fewer trainable parameters, and ProfVLM jointly generates feedback text. — [arXiv 2605.03848](https://arxiv.org/abs/2605.03848)
- Skeleton-based CPR evaluation runs in real time with low FLOPs (92.1% top-1). — [arXiv 2511.10060](https://arxiv.org/abs/2511.10060)
- Cross-dataset transfer is the most clearly stated unsolved problem with ready public datasets. — [arXiv 2608.17519](https://arxiv.org/html/2608.17519v1); [arXiv 2605.22200](https://arxiv.org/abs/2605.22200)

### Inferences
Candidate capstones, in order of feasibility, are listed below. All are inferences, not claims from sources.
1. **Frozen-foundation-model benchmark for open-suturing OSATS plus cross-dataset transfer.** Compare V-JEPA 2, VideoMAE v2 and surgical JEPA/MAE features on AIxSuture/OSS, then on LASANA, with a ProfVLM-style small LM head that emits OSATS sub-scores and rationale. Laptop-feasible because features are precomputed.
2. **Predictive-world-model skill signal.** Train a small action-conditioned latent predictor (V-JEPA-2-AC style, or on hand and tool keypoint trajectories) on expert suturing, and use prediction error or "distance to expert dynamics" as an unsupervised skill score and a localised feedback cue. Novel relative to SurgWorld/SAW, which use generation only for recognition or policy.
3. **Low-cost Thai validation.** Collect phone or GoPro suturing (or CPR-on-manikin) video from Thai students, rated by 2–3 raters on OSATS, as an external test set. This directly addresses cross-site generalisation and gives a small pilot of AI feedback versus video coaching (cf. JHU null result).

### Gaps
- No source gives measured VRAM or throughput for these backbones on a 16 GB laptop GPU. This should be benchmarked in month 1.
- Dataset licences (mostly believed non-commercial) must be confirmed before use, and Thai IRB requirements for collecting trainee video are outside this note's scope.
