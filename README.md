# Thai Med AI Capstone

Exploration for a master's capstone (AI & Digital Healthcare, Chulalongkorn), October 2026.

## Contents
- `reports/Thai medical LLM landscape.md`: deep-research report on Thai medical LLMs, deployed products and benchmarks, with 12 research gaps.
- `research_notes/Thai medical LLM landscape/`: source notes from the Claude researchers and the two co-researchers (Codex GPT-6.1-Sol, Gemini 4 Argon).
- `full_debate.md`: council v1, the first three-agent idea debate.
- `full_council_v2.md`: council v2, where the only constraint was the laptop hardware.
- `full_council_v3_frontier.md`: council v3, on frontier paradigms (RSI, JEPA, SSM/TTT, diffusion LMs, physical AI).

## Handoff note (for a new Claude session, 2026-10-20)

**Student and constraints**
- Master's in AI & Digital Healthcare at Chulalongkorn, co-run by the Faculty of Medicine and the Faculty of Engineering. The committee mixes clinicians and engineers. About 9 months left.
- Laptop: i9-13980HX, 32 GB RAM, RTX 4090 Laptop (16 GB VRAM), about 1 TB free. All training happens there; cloud sessions have no GPU.
- Wants frontier ML as the core contribution (RSI, JEPA, SSM/TTT, diffusion LMs, physical AI, agents) with real Thai healthcare impact.
- **Rejected so far:** "safe" admin and claims ideas, and the v2 shortlist (VenomSight snake ID, dysarthria). They felt anchored on past history or lacked frontier depth.

**How we got here**
1. Council v1: rejected as too safe.
2. Council v2: hardware-only constraint; also rejected.
3. Council v3, frontier paradigms: all three agents converged on the same top 3:
   - dual-verifier RSI on Thai medical constraints;
   - gap-aware Mamba/TTT for wearable signals;
   - a JEPA that preserves pathology.
4. The student asked what the impact would be. RSI alone is a methods result, too weak for this committee, so it was reframed as **audit-first** (see below).
5. The deep-research report found:
   - every score for a Thai medical LLM is self-reported, and none has been independently benchmarked in Thai;
   - ThaiLLM-27B-Prescreen has F1 = 0 for "Observe at Home";
   - TMA-1 scores 27% or lower on drug–drug interactions;
   - no LLM product has a Thai FDA (อย.) registration or post-market data.

**Current direction (not final)**
- **Part 1 (months 1–4): audit.** Build an independent Thai safety benchmark with two independent rule-based verifiers. Run it on the open Thai medical LLMs: pai1/tma1-medgemma-4b, EIRAI-8B, ThaiLLM-8B-MedApp, ThaiLLM-30B-IQ and Typhoon-Si-Med. Two domain options:
  - **Option B, preferred:** a symptom chatbot, checked for red-flag escalation (calling 1669) and for triage (both under- and over-triage).
  - **Option A:** medication instructions (dose, units, before/after meals: ก่อน/หลังอาหาร).
- **Part 2 (months 4–8): RSI study.**
  - Setup: Proposer–Solver self-play with GRPO + QLoRA on a 1.5–4B model, e.g. pai1-medgemma-4b compared with a generic Qwen3-4B.
  - Method: train against verifier A, then evaluate against verifier B and a test set written by clinicians.
  - Research question: at which round does improvement turn into reward hacking (for example, "send everyone to the ER")? Also build an early-warning signal for it.
  - Prior art: STaR and ReST-EM already filter outputs by correctness, and Gao et al. (2022) studied reward hacking with *learned* reward models. The open gap is rule-based verifiers inside self-play, in an incomplete real-world domain.
- **Clinical partner:** a KCMH partner is essential, either ER/triage staff or a pharmacist. This is still undecided, and the choice decides Option A vs B.
- **Alternative:** if a rehab partner is easier to find, do Rehab-JEPA instead (pretrain on NTU RGB+D, evaluate on KIMORE).

**How the student likes to work**
- Concise tables, diagrams, and honest pushback rather than agreement.
- Runs three-model councils: Claude + Codex (gpt-6.1-sol, high) + Gemini (gemini-4-argon-high via `agy`), with the philosopher-council lenses and each agent isolated from its stored memories. **Codex and Gemini only work on the laptop**; no API keys are configured in the cloud.

## Open next steps
1. Novelty check (2025–2026): Thai medical LLM safety and triage benchmarks, and verifier-based reward hacking in self-play RSI.
2. One-page proposal to recruit a KCMH clinical partner.
3. Month-1 pilot plan: verifier design, a 300-item test set, and laptop throughput measurements.
4. Check the pai1-medgemma licence (gated, HAI-DEF terms) before relying on it.
