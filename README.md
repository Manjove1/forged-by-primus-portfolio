# Transformers: Forged by Primus

A modular, long-form AI Dungeon Master system designed for structured Transformers roleplay. Built to maintain mechanical consistency, lore integrity, and multi-step character creation across extended sessions on platforms that aggressively summarize context.

---

## Overview

**Forged by Primus** is a prompt-engineered RPG framework that combines cinematic narrative roleplay with lightweight mechanical systems. It supports multiple eras (Golden Era, Cybertron Civil War, War on Earth) and prioritizes state integrity, player agency, and modular design.

The project was developed to solve common failure modes in long-form AI roleplay: context drift, mechanical state corruption, and models skipping structured processes.

---

## Technical Highlights

This project demonstrates several advanced prompt engineering techniques:

- **Orchestrator Pattern** — Core Rules script acts as a director that coordinates specialized systems rather than containing all rules
- **Self-Healing State Management** — Compact State Footer serves as a persistent mechanical anchor against context loss and summarization
- **Strict Sequential Gating** — Multi-step character creation with internal checkpoints and enforcement against phase-skipping
- **Summary Integrity Protocol** — Treats auto-summaries as narrative-only; reconstructs mechanical state from authoritative sources
- **Modular Script Architecture** — Separates concerns for token efficiency while maintaining strong central control
- **Era & Casting Controls** — Prevents anachronisms and reduces narrative bloat through structured limits

---

## Key Features

- Strict 12-step gated character creation that resists phase-skipping
- Self-healing mechanical tracking via State Footer
- Modular multi-script architecture with clear orchestration
- Era gating to prevent anachronistic content
- Mission-scoped NPC casting to reduce lore bloat
- Hybrid dice + narrative outcome resolution system
- Summary integrity and ReZero recovery protocols
- Designed for long-session reliability under context pressure

---

## Architecture

The system uses a layered, modular design:

| Layer | Responsibility |
|-------|----------------|
| **Core Rules** | Central orchestrator. Handles high-level principles, character creation gating, event triggers, and state integrity. |
| **Lore Book** | Always-active reference for cosmology, eras, and core setting concepts. |
| **Combat, Conditions & Growth** | Mechanical systems for combat resolution, condition tracking, and progression. |
| **Session Management & Safety** | End-of-session handling, ReZero recovery, and summary integrity protocols. |
| **Faction / Role Scripts** | Modular character and NPC definitions organized by faction and function. |

The Core Rules script functions as a director rather than a complete rulebook. It activates detailed systems only when needed, improving both control and token efficiency.

---

## Core Systems

**Character Creation**  
A strict 12-step sequential process that requires explicit player input at each stage. Includes internal checkpoints and in-character enforcement when the player attempts to skip ahead.

**State Footer**  
A compact mechanical status block automatically appended after significant events. The model is instructed to treat the most recent footer as the authoritative source of truth for resources, conditions, and progression.

**Summary Integrity Protocol**  
Auto-generated summaries are treated as narrative flavor only. Mechanical values are reconstructed from the Master State, State Footer, and pinned character export.

**Era & Casting Controls**  
NPCs and lore entries are restricted by active era. Premade characters are only introduced when they provide clear narrative value for the current mission.

**Resolution System**  
Uses a lightweight 1d20 + modifier approach with narrative outcome tiers (Yes and…, Yes but…, No but…, No and…).

---

## Design Philosophy

The system prioritizes three principles:

1. **Structure without rigidity** — Strong enforcement of critical processes while preserving narrative freedom within defined bounds.
2. **Self-healing over prevention** — Assume context will eventually degrade and design recovery mechanisms accordingly.
3. **Modularity with strong orchestration** — Keep detailed systems separate for efficiency, but maintain a powerful central director script.

---

## Current Status

The system was deployed publicly with no advertising. In the first **5 days** it generated 66 page views, 18 chat sessions, and 97 messages. This early organic engagement provided real-world testing of the core prompt systems under actual usage conditions.

---

## Repository Structure

```text
forged-by-primus-portfolio/
├── README.md
├── docs/                  # Portfolio documents
│   ├── PERSONAL_STATEMENT.md
│   ├── CASE_STUDY.md
│   ├── TECHNICAL_SYSTEMS.md
│   ├── PROMPT_SAMPLES.md
│   └── ANALYTICS_AND_RESULTS.md
└── core-systems/          # Overarching mechanics & setting (in progress)
    └── README.md
```

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
