# Transformers: Forged by Primus

A modular, long-form AI Dungeon Master system for structured Transformers roleplay. Built for mechanical consistency, lore integrity, and multi-step process control across extended sessions on platforms that aggressively summarize context.

---

## Overview

**Forged by Primus** combines cinematic narrative roleplay with lightweight mechanical systems. It supports multiple eras — Golden Era, Cybertron Civil War, and War on Earth — and prioritizes state integrity, player agency, and modular design.

The project focuses on a practical problem in long-form AI roleplay: keeping structured processes and mechanical state reliable after context pressure, summarization, and model drift.

---

## Technical Highlights

- **Orchestrator Pattern** — Core Rules coordinates specialized systems instead of containing all rules
- **Self-Healing State Management** — State Footer acts as a persistent mechanical anchor
- **Strict Sequential Gating** — Multi-step character creation with internal checkpoints
- **Summary Integrity Protocol** — Auto-summaries treated as narrative-only; mechanical state reconstructed from authoritative sources
- **Modular Script Architecture** — Separates concerns for token efficiency under strong central control
- **Era, Casting, Combiner & Cassette Controls** — Limits anachronism, roster bloat, and multi-body incoherence

---

## Key Features

- 12-step gated character creation that resists phase-skipping
- Self-healing mechanical tracking via State Footer
- Modular multi-script architecture with clear orchestration
- Era gating to prevent anachronistic content
- Mission-scoped NPC casting to reduce lore bloat
- Full Autobot and Decepticon premade rosters with mid-tier depth
- Six complete combiner teams (3 Autobot, 3 Decepticon)
- Soundwave Cassette Protocol for mini-operative deployment
- Hybrid dice + narrative outcome resolution
- ReZero recovery protocols for context resets

---

## Architecture

| Layer | Responsibility |
|-------|----------------|
| **Core Rules** | Central orchestrator: principles, creation gating, event triggers, state integrity |
| **Session Management & Safety** | End-of-session handling, ReZero recovery, summary integrity |
| **Combat, Conditions & Growth** | Combat resolution, Energon/Condition, progression |
| **Casting Rules** | Core Cast management, canon handling, anti-bloat |
| **Combiner Mechanics** | Formation, separation, shared state |
| **Cassette Protocol** | Soundwave deployment, recall, capacity, independence limits |
| **Era Special Conditions** | Golden Era, Cybertron War, War on Earth |
| **Premade Characters** | Faction-organized canon and supporting cast |

---

## Repository Structure

```text
forged-by-primus-portfolio/
├── README.md
├── docs/
│   ├── PERSONAL_STATEMENT.md
│   ├── CASE_STUDY.md
│   ├── TECHNICAL_SYSTEMS.md
│   ├── PROMPT_SAMPLES.md
│   └── ANALYTICS_AND_RESULTS.md
├── core-systems/
│   ├── CORE_RULES.md
│   ├── SESSION_MANAGEMENT_SAFETY.md
│   ├── ENERGON_CONDITION.md
│   ├── STAT_GROWTH_DECAY.md
│   ├── COMBAT_FLOW.md
│   ├── CASTING_RULES.md
│   ├── COMBINER_MECHANICS.md
│   ├── CASSETTE_PROTOCOL.md
│   ├── WAR_ON_EARTH.md
│   ├── GOLDEN_ERA.md
│   └── CYBERTRON_WAR.md
└── characters/
    ├── autobots/
    ├── decepticons/
    └── combiners/
```

---

## Current Status

**Core systems:** Complete  
**Era scripts:** Complete  
**Autobot roster:** Operational across major categories  
**Decepticon roster:** High Command, Seekers, Frontline, Spec Ops, Support, Soundwave Unit complete  
**Combiners:** Six complete teams  
**Cassette Protocol:** Implemented and linked from Core Rules  
**Documentation:** Aligned with current architecture

---

## Portfolio Documents

- [Personal Statement](docs/PERSONAL_STATEMENT.md)
- [Case Study](docs/CASE_STUDY.md)
- [Technical Systems Documentation](docs/TECHNICAL_SYSTEMS.md)
- [Prompt Samples](docs/PROMPT_SAMPLES.md)
- [Analytics & Results Summary](docs/ANALYTICS_AND_RESULTS.md)

---

## Notes

This project is a practical study in prompt engineering for long-form, stateful AI experiences. It prioritizes iterative testing against actual model behavior over purely theoretical prompt design.
