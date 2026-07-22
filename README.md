# Transformers: Forged by Primus

A modular, long-form AI Dungeon Master system designed for structured Transformers roleplay. Built to maintain mechanical consistency, lore integrity, and multi-step character creation across extended sessions on platforms that aggressively summarize context.

---

## Overview

**Forged by Primus** is a prompt-engineered RPG framework that combines cinematic narrative roleplay with lightweight mechanical systems. It supports multiple eras (Golden Era, Cybertron Civil War, War on Earth) and prioritizes state integrity, player agency, and modular design.

The project was developed to solve common failure modes in long-form AI roleplay: context drift, mechanical state corruption, and models skipping structured processes.

---

## Technical Highlights

- **Orchestrator Pattern** — Core Rules script acts as a director that coordinates specialized systems
- **Self-Healing State Management** — Compact State Footer serves as a persistent mechanical anchor
- **Strict Sequential Gating** — Multi-step character creation with internal checkpoints
- **Summary Integrity Protocol** — Treats auto-summaries as narrative-only; reconstructs mechanical state from authoritative sources
- **Modular Script Architecture** — Separates concerns for token efficiency while maintaining strong central control
- **Era, Casting, Combiner & Cassette Controls** — Prevents anachronisms and reduces narrative bloat

---

## Key Features

- Strict 12-step gated character creation that resists phase-skipping
- Self-healing mechanical tracking via State Footer
- Modular multi-script architecture with clear orchestration
- Era gating to prevent anachronistic content
- Mission-scoped NPC casting to reduce lore bloat
- Full Autobot and Decepticon premade rosters with mid-tier depth
- Six complete combiner teams (3 Autobot, 3 Decepticon)
- Soundwave Cassette Protocol for mini-operative deployment
- Hybrid dice + narrative outcome resolution system
- Summary integrity and ReZero recovery protocols

---

## Architecture

| Layer | Responsibility |
|-------|----------------|
| **Core Rules** | Central orchestrator. High-level principles, character creation gating, event triggers, state integrity. |
| **Session Management & Safety** | End-of-session handling, ReZero recovery, summary integrity. |
| **Combat, Conditions & Growth** | Combat resolution, Energon/Condition, progression. |
| **Casting Rules** | Core Cast management, canon handling, anti-bloat. |
| **Combiner Mechanics** | Formation, separation, shared state for all combiners. |
| **Cassette Protocol** | Soundwave deployment, recall, capacity, and independence limits. |
| **Era Special Conditions** | Golden Era, Cybertron War, War on Earth rules. |
| **Premade Characters** | Faction-organized canon and supporting cast. |

---

## Repository Structure

```text
forged-by-primus-portfolio/
├── README.md
├── docs/                       # Portfolio documents
│   ├── PERSONAL_STATEMENT.md
│   ├── CASE_STUDY.md
│   ├── TECHNICAL_SYSTEMS.md
│   ├── PROMPT_SAMPLES.md
│   └── ANALYTICS_AND_RESULTS.md
├── core-systems/               # Overarching mechanics & setting
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
└── characters/                 # Premade roster
    ├── autobots/
    ├── decepticons/
    └── combiners/
```

---

## Current Status

**Core systems:** Complete  
**Era scripts:** Complete (Golden Era, Cybertron War, War on Earth)  
**Autobot roster:** Operational across all major categories  
**Decepticon roster:** High Command, Seekers, Frontline, Spec Ops, Support, Soundwave Unit complete  
**Combiners:** 6 complete teams (Defensor, Computron, Superion, Bruticus, Menasor, Devastator)  
**Cassette Protocol:** Implemented and linked from Core Rules

---

## Portfolio Documents

- [Personal Statement](docs/PERSONAL_STATEMENT.md)
- [Case Study](docs/CASE_STUDY.md)
- [Technical Systems Documentation](docs/TECHNICAL_SYSTEMS.md)
- [Prompt Samples](docs/PROMPT_SAMPLES.md)
- [Analytics & Results Summary](docs/ANALYTICS_AND_RESULTS.md)

---

## Notes

This project was developed as a practical exploration of advanced prompt engineering techniques for long-form, stateful AI experiences. It emphasizes iterative testing against actual model behavior rather than purely theoretical prompt design.
