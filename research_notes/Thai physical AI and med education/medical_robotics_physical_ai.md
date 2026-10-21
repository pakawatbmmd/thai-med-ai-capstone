# Physical AI and Robotics for Healthcare and Medical/Surgical Training: State of the Art (2024 to Oct 2026) and Gaps a Single Master's Student Can Work On

Scope note: the research ran on 21 Oct 2026, mostly through WebSearch plus primary-page fetches (arXiv abstract/HTML pages, GitHub READMEs, Hugging Face paper pages). Firecrawl was rate-limited. Items from before 2025 are marked **[older]**. When a figure comes from a search-engine summary rather than a page I fetched, it is marked *(snippet-level)*. Hardware target: RTX 4090 Laptop GPU (16 GB VRAM), 32 GB RAM, SO-100/SO-101 arm, 9 months.

---

## 1. Surgical robot learning: autonomy, world models, benchmarks, public datasets and simulators

### Takeaway
Between 2024 and 2026 the field went from single subtasks on phantoms (SRT, CoRL 2024) to step-level autonomy on ex vivo tissue (SRT-H, Science Robotics, July 2025: 8/8 gallbladders). In 2026 it gained its first open multi-institution dataset (Open-H-Embodiment), its first medical VLA (GR00T-H) and action-conditioned surgical world models (Cosmos-Surg-dVRK, Cosmos-H-Surgical, Cosmos-H-Dreams). End-to-end suturing is still mostly unsolved: the best end-to-end success on SutureBot is ACT at 3/10, and GR00T-H reaches 25% on a structured suturing benchmark. Nearly all of this needs a dVRK or da Vinci system plus A100/H100-class training compute. A laptop-only student can still use the public datasets, the world models in evaluation-only mode, and the simulators.

### Cited Findings
**Autonomy milestones**
- **SRT-H** (Kim et al., Science Robotics, 9 Jul 2025, DOI 10.1126/scirobotics.adt5254; JHU/Stanford, senior authors include Krieger and Finn). Hierarchical design: a high-level policy plans in language, issuing task-level and *corrective* instructions, and a low-level policy generates trajectories. It achieved 100% success on 8 unseen ex vivo porcine gallbladders with no human intervention during the clipping-and-cutting phase. This is step-level autonomy, not a full operation, and it was not done in live animals or patients. — [arXiv 2505.10251](https://arxiv.org/abs/2505.10251); [GWU repository record](https://hsrc.himmelfarb.gwu.edu/gwhpubs/7621); [Neuroscience News coverage](https://neurosciencenews.com/robot-ai-surgery-neurotech-29435/)
- **Surgical Robot Transformer (SRT)** (Kim et al., CoRL 2024) **[older, 2024]**. Uses a relative action formulation, either tool-centric or hybrid-relative, because da Vinci forward kinematics are inaccurate. ACT-based, with 4 image inputs (stereo endoscope plus 2 wrist cameras) and a 20-D output. Success with relative actions: tissue lift 5/5, needle pickup and handover 9/9, knot-tying whole task 18/20. Absolute actions scored 0 on every task. Demonstration counts: 224 (tissue lift), 250 (needle), 500 (knot). Diffusion Policy performed worse than ACT. Stated limitations: the wrist cameras are not clinically relevant, the policy cannot take language input, and tissue generalization was mostly qualitative. — [arXiv 2407.12998 HTML](https://arxiv.org/html/2407.12998v1); [PMLR v270](https://proceedings.mlr.press/v270/kim25a.html)
- **SutureBot** (Haworth, Chen et al., JHU/NVIDIA/Stanford/Toronto, NeurIPS 2025 Datasets & Benchmarks). The authors call it the first fully autonomous end-to-end suturing pipeline on physical hardware (dVRK). The dataset has **1,890 demos**: 628 needle pickup, 310 throw and 952 knot tie, of which 454 are recovery demos. It is hosted at `huggingface.co/datasets/jchen396/suturebot`. Results over 10 trials each:

  | Model | Needle pickup | Knot tie | End-to-end | Insertion error |
  |---|---|---|---|---|
  | ACT | 9/10 | 9/10 | **3/10** | 1.5±0.8 mm |
  | π0 | 7/10 | 4/10 | 0/10 | 1.9 mm |
  | GR00T N1 | 1/10 | 1/10 | 0/10 | 2.3 mm |
  | OpenVLA-OFT | 0/10 | 0/10 | 0/10 | n/a |

  Goal conditioning improved targeting accuracy by 59–74%. Training ran on 8×A100 80 GB, and evaluation on 2×RTX 4090. — [arXiv 2510.20965 HTML](https://arxiv.org/html/2510.20965v1); [NeurIPS 2025 page](https://papers.nips.cc/paper_files/paper/2025/hash/4d6549ae9aa0ccfcfef1ad051f1278d8-Abstract-Datasets_and_Benchmarks_Track.html)
- The SutureBot authors list these limitations: only 10 trials per experiment; the high-level policy was evaluated only offline or with an oracle; performance drops under lighting and tool changes; target points are chosen manually; "clinical post-training did not significantly improve performance"; there are no clinical metrics (bite depth, tissue trauma, suture tension); and the policies have no memory, so needle position is uncertain while the needle is occluded inside tissue. — [arXiv 2510.20965 HTML](https://arxiv.org/html/2510.20965v1)

**Public datasets (robot kinematics plus video)**
- **Open-H-Embodiment** (arXiv 2604.21017, Apr 2026; dataset created Feb 2026; CC BY 4.0; LeRobot format on Hugging Face as `nvidia/PhysicalAI-Robotics-Open-H-Embodiment`). The authors describe it as the "largest open dataset of medical robotic video with synchronized kinematics to date". Contributors number more than 50 institutions; some versions of the paper say more than 49. Platforms include da Vinci, dVRK, CMR Versius, Rob Surgical BiTrack, Virtual Incision MIRA, Moon Surgical Maestro and custom systems. Tasks cover surgical manipulation, robotic ultrasound and endoscopy. The abstract gives no hour or episode count. — [arXiv 2604.21017](https://arxiv.org/abs/2604.21017); [HF dataset card](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment/blob/main/README.md)
- **GR00T-H**, released with Open-H-Embodiment, is presented as "the first open foundation VLA for medical robotics". It reached **25%** full end-to-end success on a structured suturing benchmark, where all other models scored 0%. Its average success across a 29-step ex vivo suturing sequence was **64%**. The parameter count is not stated in the abstract. — [arXiv 2604.21017](https://arxiv.org/abs/2604.21017)
- **ImitateCholec** (Scientific Data, 16 Jan 2026, DOI 10.1038/s41597-025-06526-z) contains **more than 18,000 demonstrations** from 34 ex vivo porcine cholecystectomies, about 20 h in total. The clipping-and-cutting phase is split into 17 tasks. It includes multi-camera endoscopic video and dVRK kinematics, and covers both optimal executions and recovery maneuvers. — [PMC12891575](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12891575/)
- **CRCD** (Comprehensive Robotic Cholecystectomy Dataset) **[older, 2023]**: dVRK kinematics, pedal signals and endoscopic video from ex vivo pig-liver procedures. — [arXiv 2312.01183](https://arxiv.org/pdf/2312.01183)
- **SurgVIL** (arXiv 2608.16058, Aug 2026) mixes kinematically labelled phantom demos with open-source and online surgical videos. Kinematics estimated from the videos serve as weak supervision. Tested backbones: ACT, π0 and GR00T-H on a da Vinci (needle pick-up, cholecystectomy cutting). The authors claim video "substantially improves generalization to real-tissue and OOD settings"; the abstract gives no numbers. — [arXiv 2608.16058](https://arxiv.org/abs/2608.16058)
- A related preprint reports that policies trained on kinematics *estimated from monocular video* reach success rates comparable to policies trained on ground truth. A Mixture-of-Experts/ACT preprint reports long-horizon learning from fewer than 150 demos using stereo endoscope images only *(snippet-level; exact papers not fetched)*. — [PMC12836364 review and related search results](https://pmc.ncbi.nlm.nih.gov/articles/PMC12836364)

**Surgical world models**
- **Cosmos-Surg-dVRK** (arXiv 2510.16240, Oct 2025) fine-tunes NVIDIA Cosmos into a surgical world model and pairs it with a V-JEPA 2-based video classifier, so dVRK policies can be evaluated *online and automatically*. Rollouts in the world model correlate strongly with real dVRK Si outcomes on suture-pad tasks. It also includes a preliminary ex vivo cholecystectomy experiment. — [arXiv 2510.16240](https://arxiv.org/html/2510.16240v2)
- **Cosmos-H-Surgical** (arXiv 2512.23162, Dec 2025) is a surgical world model for learning policies from video when paired kinematics are scarce. It introduces a dataset of 2,447 surgical video-text clips *(snippet-level)*. — [arXiv 2512.23162](https://arxiv.org/pdf/2512.23162)
- **Cosmos-H-Surgical-Simulator** is an action-conditioned world model that covers **9 robot platforms** from a single checkpoint and is used for in-silico policy evaluation and synthetic data. — [arXiv 2604.21017](https://arxiv.org/abs/2604.21017)
- **Cosmos-H-Dreams** (arXiv 2608.24199, Aug 2026; weights reportedly released Jul 2026) distills the teacher into a causal real-time student driven by a stream of kinematics. NVIDIA reports about 160 FPS on one RTX PRO 6000; this is a vendor claim I did not verify. Its tabletop suturing checkpoint is built on the Cosmos-Surg-dVRK suturing data. — [arXiv 2608.24199](https://arxiv.org/pdf/2608.24199); [HF blog](https://huggingface.co/blog/nvidia/cosmos-h-dreams)

**Simulators**
- **ORBIT-Surgical** (arXiv 2404.16027, ICRA 2024) **[older, 2024]** runs on Isaac Sim/Omniverse with photorealistic rendering. It offers **14 benchmark tasks** for dVRK and STAR that follow the FLS curriculum, with up to **8,000 parallel envs on one RTX 3090**. It supports sim-to-real transfer to a physical dVRK and is open source. In 2024, suturing and soft-tissue incision were listed as *future* features. — [arXiv 2404.16027](https://arxiv.org/pdf/2404.16027); [The Decoder](https://the-decoder.com/orbit-surgical-uses-nvidias-physics-simulation-and-ray-tracing-to-train-surgical-robots/)
- **SurRoL** **[older, 2021]** is PyBullet-based, RL-centred and dVRK-compatible. It has 10 tasks centred on PSM and ECM manipulation, with policies deployed to a real dVRK. — [arXiv 2108.13035](https://arxiv.org/pdf/2108.13035)
- **LapGym** (JMLR 2023, vol. 24) **[older]** is built on SOFA and has 12 environments in 4 tracks: Spatial Reasoning, Deformable Object Manipulation & Grasping, Dissection, and **Thread Manipulation**. Difficulty is parametrizable, PPO baselines are provided, and the code is at github.com/ScheiklP/lap_gym. — [JMLR](https://jmlr.org/papers/v24/23-0207.html); [SOFA page](https://www.sofa-framework.org/?p=23807)
- A PMC review covers levels of surgical autonomy from teleoperation to full autonomy, end-to-end RL and imitation learning, and surgical simulators. It names data scarcity, since public datasets are mostly segmentation and phase recognition, and poor generalization as the main bottlenecks. — [PMC12836364](https://pmc.ncbi.nlm.nih.gov/articles/PMC12836364)

### Inferences
- The current state of the art is ACT-family policies trained on hundreds to thousands of demos per subtask, with hierarchy or language correction for long horizons. Generalist VLAs (π0, GR00T N1, OpenVLA-OFT) performed *worse* than ACT on precise surgical subtasks in SutureBot. Small, task-specific policies are therefore still competitive, which favours a laptop budget.
- From 2025 on, world models are becoming the evaluation layer: replacing real-robot trials with world-model rollouts plus video classifiers. This shifts the open questions toward how well world-model scores predict real outcomes and how the world models fail, which can be studied without a dVRK.
- None of SurRoL, LapGym or ORBIT-Surgical (as of 2024) offered a validated end-to-end suturing benchmark in sim. Physical SutureBot is the reference. A sim suturing or knot-tying benchmark aligned with SutureBot's subtasks is still missing, as far as these sources show.

### Gaps
- I could not confirm the total hours or episodes of Open-H-Embodiment, or the parameter count and VRAM needs of GR00T-H.
- I could not confirm whether ORBIT-Surgical added suturing or knot-tying in 2025–2026 (I did not fetch the GitHub repo).
- Per-model numbers for SurgVIL and quantitative world-model correlation coefficients (Cosmos-Surg-dVRK) were not extracted.
- I did not check whether Cosmos-H-Dreams or Cosmos-H-Surgical checkpoints can run inference in 16 GB VRAM. Cosmos base models are multi-billion-parameter, so this is unlikely without quantization, but unverified.

---

## 2. Robots in medical education: patient simulators, teaching/assessing procedural skills, autonomous robotic ultrasound

### Takeaway
Evidence that *robots themselves* improve medical education is thin. Simulation in general (VR, mannequins) has meta-analytic support. Humanoid-robot patient simulators have only pilot data, and robotic-surgery simulator training shows face, content and construct validity but limited patient-level benefit evidence. Autonomous robotic ultrasound is the most mature learning-based clinical robot area. UltraBot (Nature Communications 2025) used 247k demos and reported more than 90% success. I found no 2025–2026 robots that teach CPR or IV insertion.

### Cited Findings
- **Humanoid robot vs. human actor as simulated patient** (OFFIS pilot, Dec 2025). The actor was rated more realistic, but differences in diagnostic outcomes were very small. The authors suggest humanoid robots as a supplement to patient simulators. This is a small pilot questionnaire study. — [OFFIS publication](https://www.offis.de/offis/publikation/comparing-patient-simulation-with-a-humanoid-robot-or-a-human-actor-in-terms-of-training-success-and-acceptance-pilot-questionnaire-study.html)
- **Virtual patient simulations meta-analysis** (Digital Health Education Collaboration, 2019) **[older]** and a 2024 JMIR meta-analysis of RCTs comparing virtual simulation with mannequins and real persons exist. I did not retrieve their effect sizes. — [PMC6632099](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6632099/); [JMIR 2024 e56195](https://jmir.org/2024/1/e56195/PDF)
- A 2025 systematic review of simulation for novice robotic general-surgery training found only **9 qualifying studies** and limited evidence of patient- or hospital-level benefit *(snippet-level; specific article not fetched)*. An older review found that VR robotic simulators (dVSS, dVT, RoSS, ProMIS, SEP) show face, content and construct validity for novices **[older]**. — [Corewell Health scholarly works](https://scholarlyworks.corewellhealth.org/pediatric_surgery_articles/65); [UCF STARS](https://stars.library.ucf.edu/facultybib2010/6641)
- **Visual haptic feedback for robotic suturing training** **[older, 2022]**. Teleoperated systems have no force feedback, and novices use excessive force. The paper adds colour-coded force cues to a VR suturing simulator. It is a technical paper, not an outcomes trial. — [Frontiers Robotics & AI 2022 / PMC8849007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8849007/)
- **Bimanual robotic epidural needle-insertion simulator** (Ben-Gurion University), a robot-based procedural trainer. — [BGU news](https://in.bgu.ac.il/en/engn/biomed/pages/news/nitsan2.aspx)
- **Ultrasound probe-handling training.** On an optical ultrasound simulator, novices' correct target-plane rates rose from 28–57% to 39–83% while experts did not improve **[older, 2021]**. A 2026 Frontiers in Digital Health study used an XR system with a pressure-sensing probe and modes for probe handling, spatial reconstruction and lesion localization; the sample was small. — [PMC8411749](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8411749/); [Frontiers Digital Health 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1761690/full)
- **UltraBot** (Jiang et al., Tsinghua/PLA General Hospital/BAAI, Nature Communications 2025, vol. 16) is a fully learning-based autonomous carotid ultrasound robot. It uses a unified imitation-learning framework trained on **247,000 expert demonstration samples** (a 100× scale-up) and "embodied foundation models". It reports **more than 90% success**, "expert-level accuracy" and up to **5.5× higher reproducibility** on "diverse unseen populations". The subject count is not given in the abstract. — [Nature Comms via RePEc](https://ideas.repec.org/a/nat/natcom/v16y2025i1d10.1038_s41467-025-62865-w.html)
- A 2025 IEEE Access survey of autonomous robotic ultrasound scanning covers more than 60 publications from 2022–2025. It identifies two gaps: poor handling of **surface-parallel force components**, and little use of **real-time US image feedback for path optimization** *(snippet-level)*. — [KFUPM listing](https://pure.kfupm.edu.sa/en/publications/a-survey-of-autonomous-robotic-ultrasound-scanning-systems/)
- Open-H-Embodiment includes robotic ultrasound data, so open learning data for US robots now exists. — [arXiv 2604.21017](https://arxiv.org/abs/2604.21017)

### Inferences
- Using a robot to *demonstrate, guide or assess* a trainee's ultrasound probe handling is under-explored. Autonomous US robots log exactly the variables a trainee assessment needs (probe pose, contact force, image quality), but the work I found uses them for autonomy, not education. An SO-101 arm holding a dummy probe over a phantom, with force estimated from motor current, could serve as a low-cost "haptic replay" or "expert trajectory comparison" tutor. The novelty is plausible but not verified.
- Evidence of educational effectiveness is a recurring weak point: validity studies are common and RCTs with skill-transfer or patient outcomes are rare. A master's project with a small randomized or crossover user study, even n of about 20 students, would address a stated gap.

### Gaps
- I found no 2025–2026 sources on robots that teach or assess CPR or IV/venipuncture insertion. I also found nothing on commercial robotic patient simulators such as Gaumard HAL or Showa Hanako with learning-based control.
- I did not extract effect sizes from the simulation meta-analyses.
- I could not determine the UltraBot subject count or whether its data and code are public.

---

## 3. Rehab, assistive and eldercare robotics; low-cost arms; which VLA/IL models fit 16 GB VRAM

### Takeaway
On a 16 GB RTX 4090 Laptop, **ACT and SmolVLA (450M parameters)** are the realistic options for *fine-tuning*. π0/π0.5 need more than 22.5 GB for LoRA and GR00T N1.7 recommends 40 GB+ for fine-tuning, so both fit for **inference only** at 8–16 GB or more. I found no published medical, surgical or ultrasound research on SO-100/SO-101. Learning-based assistive-care work (dressing, feeding) mostly predates 2025 and uses expensive arms. Both points are gaps.

### Cited Findings
**SmolVLA** (Hugging Face, arXiv 2506.01844, Jun 2025)
- About **450M parameters**, of which about 100M are the action expert. 0.24B and 2.25B variants also exist. It was pretrained on 481 community LeRobot datasets, about 22.9K episodes and 10.6M frames, using about 30K GPU-hours on 4 GPUs. The authors say it trains on a single GPU and runs on consumer GPUs or even a CPU.
- Results: LIBERO average 87.3% vs π0 (3.3B) 86.0%; Meta-World 57.3% vs 47.9%. On a **real SO-100 (pick-place, stack, sort) it averaged 78.3%, vs π0 61.7% and ACT 48.3%**. On SO-101 Lego pick-place it scored 90% in-distribution and 50% OOD, vs ACT 70% and 40%.
- Asynchronous inference cut task time by about 30% (13.75 s to 9.7 s), at slightly lower success (73.3% vs 78.3%). — [HF Papers 2506.01844](https://huggingface.co/papers/2506.01844)
- VRAM figures from secondary blogs, not official: about **10–16 GB for SmolVLA training at batch 8**, and about 1–2 GB for inference. — [OpenELab fine-tune guide](https://openelab.io/pl/blogs/learn/how-to-fine-tune-smolvla-on-so-101-with-lerobot); [Spheron blog](https://www.spheron.network/blog/smolvlm-smolvla-gpu-cloud-edge-ai-robotics/)

**π0 / π0.5 (openpi, official README)**
- Inference needs **more than 8 GB**, **LoRA fine-tuning more than 22.5 GB**, and full fine-tuning more than 70 GB (A100/H100). The README lists the RTX 4090 *desktop (24 GB)* as the example card for LoRA. In the PyTorch port, LoRA, mixed precision, FSDP and π0-FAST are not yet supported. — [openpi GitHub](https://github.com/Physical-Intelligence/openpi)

**GR00T (NVIDIA Isaac-GR00T, official README)**
- The current GA release is **GR00T N1.7-3B**; earlier releases are N1.6 and N1.5. Inference needs **16 GB+ VRAM** (RTX 4090 listed). Fine-tuning recommends **40 GB+ GPUs** (H100/L40; A6000 works but slowly). The repo includes an SO-100 walkthrough and a 5-episode demo dataset. — [Isaac-GR00T GitHub](https://github.com/NVIDIA/Isaac-GR00T)

**ACT** performed best on surgical subtasks in SRT and SutureBot (see §1). In SmolVLA's SO-100 comparison it was weaker than SmolVLA. — [arXiv 2510.20965](https://arxiv.org/html/2510.20965v1); [HF Papers 2506.01844](https://huggingface.co/papers/2506.01844)

**OpenVLA-OFT** scored 0/10 on every SutureBot subtask. — [arXiv 2510.20965](https://arxiv.org/html/2510.20965v1)

**Low-cost arms**
- SO-101 is the next generation of SO-100 (RobotStudio and Hugging Face, Apr–May 2025). It is 3D-printable and integrated with LeRobot. — [Gigazine](https://gigazine.net/gsc_news/en/20250501-hugging-face-robotic-arm); [SO-ARM100 GitHub](https://github.com/TheRobotStudio/SO-ARM100)
- A search for medical, surgical or ultrasound research on SO-100/LeRobot returned only hobby and general AI use. — [search result set incl. dupple.com](https://dupple.com/blog/how-to-make-a-robotic-arm)

**Assistive and eldercare (mostly older)**
- A 2022 review groups learning-based dressing assistance into supervised learning, LfD and RL **[older]**. A University of York bimanual dressing robot (2024) imitates care workers and found that two arms are needed and humans sometimes must intervene **[older]**. — [PMC9635144](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9635144/); [York news 2024](https://www.york.ac.uk/news-and-events/news/2024/research/dressing-robot-mimic-actions-of-care-workers)

### Inferences
- **Practical recipe for this laptop:** train ACT (tens of millions of parameters) and fine-tune SmolVLA-450M locally with mixed precision and batch size 4–8. Run π0/π0.5 or GR00T only as inference baselines; GR00T at 16 GB+ is borderline on a 16 GB laptop and may need quantization. For π0 LoRA or GR00T fine-tuning, rent a cloud A100 for a few hours.
- Laptop RTX 4090 GPUs are power-limited relative to desktop cards. The vendor numbers above use desktop or datacenter cards, so expect slower training.
- SO-100/101 hardware is not surgical-grade: it has no RCM, low precision and no force sensing. It is credible as a proxy for **non-sterile, low-precision medical tasks**: handing over instruments, holding a dummy ultrasound probe on a phantom, pick-and-place of medication or specimen tubes, assisted feeding, or teaching and demonstration rigs for trainees. It is not credible for surgery.

### Gaps
- I did not find official LeRobot hardware-guide VRAM tables (the SmolVLA training VRAM figures are second-hand), or exact ACT memory figures.
- I found no 2025–2026 VLA papers on feeding, dressing or rehab, though they likely exist (e.g., the feeding-robot literature); I did not search specifically for them.
- I found no peer-reviewed medical study on SO-100/SO-101.

---

## 4. Physical AI for trainee skill assessment (video, kinematics, force); OSATS-style accuracy

### Takeaway
On JIGSAWS **[older benchmark, 2014]**, kinematics-based classifiers report very high accuracy for expertise classes: 91–95% per short window, and close to 100% for whole trials or binary novice-vs-expert. A 2024 RA-L critique says these numbers are easily misinterpreted. Regressing actual OSATS/GRS scores from real operative video remains weak; one prostatectomy study reports Spearman ρ of about 0.36–0.37. Directions for 2025–2026 are multimodal (video, kinematics, force), explainable and VLM-based feedback, with real-time suturing assessment.

### Cited Findings
- A 2018 CNN on JIGSAWS kinematics achieved 92.5% (suturing), 95.4% (needle passing) and 91.3% (knot tying) from windows of about 1–3 s. Whole-trial entropy methods report 99.9–100% **[older]**. — [arXiv 1806.05796](https://arxiv.org/pdf/1806.05796)
- In a 2023 study, binary novice-vs-experienced classification on kinematics consistently reached 100% **[older]** *(snippet-level)*. — [Óbuda University archive](https://oda.uni-obuda.hu/handle/20.500.14044/38725)
- **Hendricks et al., 2024 (IEEE RA-L)** argue that JIGSAWS results "may be easily misinterpreted" because of metric and dataset limitations, and that some studies report only Spearman correlation and never recover OSATS *(snippet-level; the link is the likely NSF PAR copy, not verified)*. — [NSF PAR](https://par.nsf.gov/servlets/purl/10524243)
- A systematic review of deep networks for skill assessment, built with PRISMA and kinematics-focused, groups studies into JIGSAWS vs other datasets **[older, 2021]**. — [arXiv 2103.05113](https://arxiv.org/pdf/2103.05113)
- In robotic prostatectomy (54 videos), deep-learning OSATS estimates reached only Spearman ρ of **0.37 and 0.36**, with normalized MAE equal to a **17.92% prediction error** *(snippet-level; attribution to this Oxford record not verified by fetch)*. — [Oxford RDM publication 2350109](https://www.rdm.ox.ac.uk/publications/publication_modal/2350109)
- A multimodal (video plus kinematics) knot-tying model matched expert human raters on most GRS domains **[older, 2022]**. — [PMC9571767](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9571767/)
- In laparoscopic sleeve gastrectomy, Mask R-CNN instrument tracking showed that the top-quartile grasper-smoothness videos had higher OSATS (17.31±2.27 vs 15.69±2.93) **[2023 abstract]**. — [BJS abstract via CiteDrive](https://www.citedrive.com/en/discovery/sp118-deep-learning-for-performance-assessment-of-laparoscopic-sleeve-gastrectomy-lsg-validation-against-objective-structured-assessment-of-technical-skills-osats-and-clinical-outcomes)
- 2026 preprints: "Model selection and real-time skill assessment for suturing in robotic surgery" (arXiv 2601.12012) reports that multimodal learning gives more stable fine-grained evaluation. A second preprint (arXiv 2603.12787) combines a basic-action recognition foundation model with skill assessment in prostatectomy and VLM-based action planning. — [arXiv 2601.12012](https://arxiv.org/html/2601.12012v1); [arXiv 2603.12787](https://arxiv.org/abs/2603.12787)
- SurgXBench (arXiv 2505.10764, 2025) benchmarks VLMs on surgical instrument and action recognition and finds surgical VLM performance "remains limited and not well understood". — [arXiv 2505.10764](https://arxiv.org/pdf/2505.10764v3)

### Inferences
- **Concrete laptop-feasible gap:** most assessment work uses either da Vinci kinematics (JIGSAWS) or OR video. *Low-cost open-surgery or bench suturing assessment* is under-served, especially work that fuses inexpensive sensing (a webcam plus a hand-pose model, an instrumented needle driver, or a load cell under the suture pad) with an OSATS/GRS regression target and **natural-language feedback** from a local VLM. Reporting ICC or Spearman against 2+ blinded human raters, rather than classification accuracy, would answer the Hendricks critique directly.
- A second gap is **cross-domain reuse of the robot-learning datasets for assessment**. SutureBot and ImitateCholec include recovery or suboptimal demos, so they could be relabelled as "skill" or "error" data, and policy-learning representations (e.g., the SmolVLA encoder) could be tested as skill-assessment features. I found no paper that does this. Novelty is plausible but unverified.

### Gaps
- I found no 2025 systematic review with pooled accuracy figures for video OSATS prediction.
- I did not verify the details of the 2025 Scientific Reports paper on simulated laparoscopic skill assessment.
- I found no force-sensor-based assessment numbers from 2025–2026.

---

## 5. Named open problems and gaps stated in 2025–2026 papers and reviews

### Takeaway
The open problems that recur across 2025–2026 primary sources are data scarcity on real tissue, generalization (lighting, tools, tissue), long-horizon recovery, occlusion and memory, the lack of clinical metrics, manual target selection, expensive real-robot evaluation (which world models try to fix) and the poor performance of generalist VLAs on precision subtasks. Several of these can be attacked offline or in simulation on one laptop.

### Cited Findings
- SutureBot reports performance drops under lighting and tool changes, manual target-point selection, no clinical metrics (bite depth, tissue trauma, suture tension), no history or memory while the needle is occluded, an open question whether the bottleneck is data size or architecture, and that "clinical post-training did not significantly improve" results. — [arXiv 2510.20965](https://arxiv.org/html/2510.20965v1)
- SRT notes non-clinical wrist cameras, no language conditioning and mostly qualitative tissue generalization **[2024]**. — [arXiv 2407.12998](https://arxiv.org/html/2407.12998v1)
- SRT-H frames long-horizon dexterity and robustness to tissue variability as the core challenge and uses language correction to recover from low-level errors. It has been shown only ex vivo and only at step level. — [arXiv 2505.10251](https://arxiv.org/abs/2505.10251)
- SurgVIL states that clinical or realistic-tissue demos with synchronized video and actions are "exceedingly rare" and that phantom data lacks visual diversity. — [arXiv 2608.16058](https://arxiv.org/abs/2608.16058)
- Cosmos-Surg-dVRK is motivated by the cost of real-robot evaluation; world-model evaluation is offered as the fix. — [arXiv 2510.16240](https://arxiv.org/html/2510.16240v2)
- The robotic US survey names two gaps: surface-parallel force control, and real-time image feedback for path planning. — [KFUPM listing](https://pure.kfupm.edu.sa/en/publications/a-survey-of-autonomous-robotic-ultrasound-scanning-systems/)
- A PMC review lists data scarcity (public sets are mostly segmentation and phase data), lack of cross-scenario generalization and overly simple tasks. — [PMC12836364](https://pmc.ncbi.nlm.nih.gov/articles/PMC12836364)
- On skill assessment, JIGSAWS metrics are easily misinterpreted and OSATS is often not recovered (Hendricks 2024). — [NSF PAR](https://par.nsf.gov/servlets/purl/10524243)
- On education, there is limited patient- or hospital-level evidence for robotic-surgery simulation training (9 studies, 2025 review) *(snippet-level)*. — [Corewell Health](https://scholarlyworks.corewellhealth.org/pediatric_surgery_articles/65)

### Inferences: candidate master's projects ranked by feasibility on 16 GB laptop + SO-101 + 9 months
These are my synthesis, not claims from the sources.
1. **Offline benchmark study on the public surgical datasets (laptop only, high feasibility).** Train ACT and SmolVLA on SutureBot subtasks and/or ImitateCholec, then study one named gap: (a) history or memory for occluded needles, e.g. adding a temporal context window to ACT; (b) robustness to lighting and tool changes via augmentation; (c) an offline metric that predicts the real success rates already published for SutureBot. All datasets are in LeRobot/HF format. The risk is that real-robot validation is impossible without a dVRK, so the contribution is methods plus offline analysis.
2. **Low-cost robot-assisted skill training or assessment rig (SO-101 + webcam, high feasibility, strong education angle).** Use the arm as a *haptic or demonstrative tutor* or a *standardized task presenter* for bench suturing or ultrasound-probe handling on phantoms. Pair it with a video and kinematics skill-assessment model validated against 2+ raters (ICC/Spearman), add LLM or VLM narrative feedback, and run a small trainee study, e.g. with Thai medical students. This hits two stated gaps: thin educational-effectiveness evidence, and OSATS recovery rather than accuracy-only reporting.
3. **SO-101 "medical assistant" VLA tasks with Thai-language instructions (medium feasibility).** Fine-tune SmolVLA on a new LeRobot dataset of instrument handover, specimen-tube sorting, or holding a dummy US probe on a phantom with contact maintenance. Compare it against ACT, and against π0 in inference-only mode. A Thai-language-conditioned medical manipulation dataset would be novel; I found no prior instance. The risk is limited clinical realism.
4. **World-model-based policy evaluation, offline (medium-low feasibility).** Check whether Open-H/Cosmos-H checkpoints can run inference at 16 GB with quantization. If they can, study failure modes or calibration of world-model-predicted success. The risk is that the VRAM need is unknown and may be too high.
5. **Sim suturing or knot-tying task in LapGym (thread track) or ORBIT-Surgical aligned with SutureBot subtasks (medium feasibility, laptop GPU OK for SOFA/PyBullet).** ORBIT-Surgical needs Isaac Sim, which is heavy but runs on an RTX GPU. The contribution would be a sim-to-real-aligned benchmark, though without real-robot transfer.

### Gaps
- I found no single comprehensive 2025–2026 review of "open problems in surgical robot learning" (e.g., in Science Robotics or IEEE T-MRB) in these searches. The gap list above is assembled from primary papers.

---

## 6. Thai work: universities and hospital robot deployments

### Takeaway
Thai medical robotics consists of service and telemedicine robots (COVID-era deployments in 2020), rehabilitation exoskeletons and surgeon-in-the-loop assistive cobots. Clinical robotic surgery is imported da Vinci systems concentrated at Siriraj, Ramathibodi and King Chulalongkorn Memorial. I found **no Thai work on learning-based (imitation learning, VLA, world-model) medical robotics or robot-based skill assessment**. That is a clear local gap, though not proof of absence.

### Cited Findings
- **Mahidol BART LAB** (Center for Biomedical and Robotics Technology, Faculty of Engineering) works on medical robotics and computer-integrated surgery. Mahidol projects include "Doctosight" (a telemedicine diagnosis and treatment robot) and a laparoscopic surgery assistance robot. — [BART LAB page](https://www.eg.mahidol.ac.th/egmu_eng/research-and-services/research/centers-and-laboratories/research-centers/101-research-services/research/544-research-center-bartlab); [Doctosight](https://give.mahidol.ac.th/?p=1073)
- In March 2023 a Mahidol medical robotics seminar led to research cooperation and staff/student exchanges. There is also a Mahidol, Imperial College and IEEE RAS Thailand chapter link. — [Mahidol seminar news](https://eg.mahidol.ac.th/egmu_eng/about/news-events/previous-news/646-medical-robotics-seminar); [MU–Imperial news](https://eg.mahidol.ac.th/egmu_eng/about/news-events/previous-news/572-mu-imperial-college-london-ieee-robotics-automation-society-thailand-chapter)
- **Ramathibodi** presented the Assistive Cobot for Spinal Surgery (ACoSS) as a keynote project developed with Mahidol Engineering; the surgeon stays in control. — [Ramathibodi international news, Jul 2024](https://www.rama.mahidol.ac.th/international/news/event/10072024-1357)
- **Siriraj** received 2 fourth-generation da Vinci robots in 2019 and claims more than 3,000 robotic surgeries, "the most in Southeast Asia" (undated Bangkok Post). — [Siriraj case page](https://www2.si.mahidol.ac.th/en/case/the-4th-gen-robotic-surgery-da-vinci); [Bangkok Post](https://www.bangkokpost.com/thailand/general/2092807)
- Thailand had **8 surgical robots** across King Chulalongkorn Memorial, Siriraj and Ramathibodi according to a 2021 report, reposted in 2024, so the count is likely stale. — [OpenGov Asia 2021](https://archive.opengovasia.com/2021/01/20/thai-hospital-rolls-out-surgical-robot/)
- A 2018 Siriraj Medical Journal review says robotic surgery's high cost and lack of proven superiority over laparoscopy make it controversial in less affluent countries **[older]**. — [Mahidol repository](https://repository.li.mahidol.ac.th/handle/123456789/46379); [DOAJ](https://doaj.org/article/8ddbd6c8b9254664b6e3f00ab39c822b)
- **Chulalongkorn Engineering** built the "Ninja" telemedicine robots, normally used with stroke patients, and "Pinto" delivery robots for COVID-19. They were deployed at Ramathibodi, King Chulalongkorn Memorial and Vachira Phuket hospitals in 2020 **[older]**. The university also built the CUREs rehabilitation exoskeleton, piloted with stroke patients at the Thai Red Cross Rehabilitation Centre (2018) **[older]**. — [Bangkok Post 2020](https://bangkokpost.com/thailand/general/1895105/ninja-robots-to-help-treat-infected); [Open Development Mekong](https://opendevelopmentmekong.net/news/thai-hospitals-roll-out-ninja-robots-to-help-combat-covid-19/)
- **FIBO/KMUTT** built the FACO robots (renamed "Mod Boriraksa"): autonomous telemedicine and communication robots deployed at Ramathibodi Chakri Naruebodindra Hospital in May 2020 **[older]**. FIBO's founder Djitt Laowattana was profiled on automating Thai hospitals. KMUTT's 2025 research themes list medical, assistive and rehab robotics for elderly and disabled people. A 2016 FIBO page mentions a tele-operated IVF robot **[older]**. — [KMUTT news](https://www.kmutt.ac.th/internationalization/inter-news/mod-boriraksa-robots-by-fibo-kmutt-report-for-duty-at-ramathibodi-chakri-naruebodindra-hospital/); [Rest of World 2020](https://restofworld.org/2020/the-man-trying-to-automate-thailands-hospitals/); [KMUTT 8 Themes PDF](https://ripo.kmutt.ac.th/wp-content/uploads/2025/01/8-Themes-Eng.pdf); [FIBO 2016](https://fibo.kmutt.ac.th/ecdd-visit-fibo)
- A national advanced medical robotics programme (NSTDA/NANOTEC, around 2014–2017) aimed to make Thailand a regional medical-robot hub **[older]**. — [NANOTEC](https://nanotec.or.th/en/?p=4414); [NSTDA](https://nstda.or.th/blog/index.php/archives/21556.html)

### Inferences
- The local advantages are hospital access (Siriraj, Ramathibodi and Chula all run large robotic-surgery programmes and simulation centres), engineering partners (BART LAB, FIBO, Chula Engineering), and the lack of local learning-based work. A Thai master's project positioned as "the first open Thai LeRobot medical-manipulation or skill-training dataset plus baseline policies" would be locally novel and cheap.
- Because of the cost-effectiveness concern raised for robotic surgery in Thailand, a **low-cost (about US$300) robot training or assessment tool** fits the local context better than chasing surgical autonomy.

### Gaps
- I found no 2025–2026 news on Thai hospital robot deployments, and no current count of da Vinci systems in Thailand. Thai-language sources were not searched.
- I could not identify any Thai paper on imitation learning, VLAs or AI surgical skill assessment, nor any Thai paper using dVRK or LeRobot. Searching Thai-language sources and ThaiJO would be the next step.
- I did not determine whether Chulalongkorn or Siriraj simulation centres use robotic patient simulators.
