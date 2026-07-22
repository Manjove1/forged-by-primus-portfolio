# Technical Systems Documentation
**Project:** Transformers: Forged by Primus

This document provides a technical overview of the core systems used in the project. It explains how the major prompt engineering patterns function and why they were designed this way.

---

## System Relationships Overview

The major systems are designed to reinforce each other:

- **Core Rules** acts as the central orchestrator. It controls high-level flow, triggers specialized systems, and enforces sequential processes.
- **State Footer** provides a persistent mechanical anchor that the Core Rules and recovery protocols reference.
- **Summary Integrity Protocol** protects mechanical state by treating auto-summaries as non-authoritative.
- **ReZero Recovery** reconstructs state from the Master State + State Footer + pinned character export after context loss.
- **Casting Rules** control who appears and prevent roster bloat.
- **Combiner Mechanics** and **Cassette Protocol** govern specialized multi-body systems with shared state and deployment limits.
- Era scripts and premade character files are activated only when needed via structured calls from Core Rules.

This design prioritizes recovery and coordination over trying to prevent all forms of context degradation.

---

## 1. Core Rules as Orchestrator

The Core Rules script functions as a central director rather than a complete rulebook. Its responsibilities are:

- Enforce high-level principles (user agency, lore consistency, narrative quality)
- Control sequential processes, especially character creation
- Trigger specialized systems only when needed
- Maintain state integrity through the State Footer and related protocols

Detailed mechanical rules are kept in separate scripts. The Core Rules references them using a structured calling convention when required.

**Current major call targets include:**
- Session Management & Safety (ReZero)
- Era Special Conditions
- Casting Rules
- Combiner Mechanics
- Cassette Protocol
- Combat / Energon / Stat systems

**Why this approach:**  
A monolithic prompt became both token-expensive and harder to maintain. Moving stable systems into specialized scripts while keeping fragile processes under strong central control improved both efficiency and reliability.

---

## 2. Character Creation Gating Protocol

Character creation uses a strict 12-step sequential process. The model must wait for explicit player input before advancing.

Key enforcement mechanisms:

- One question per message requirement
- Silent internal checkpoint (the model must confirm the current step before responding)
- In-character refusal language when the player attempts to skip ahead
- Final confirmation step (Spark Resonance Export) that must be explicitly accepted before the story begins

**Why this was necessary:**  
Earlier versions allowed the model to batch questions or jump into narrative. The combination of sequential locking and an internal checkpoint significantly reduced phase-skipping.

---

## 3. State Footer (Self-Healing Anchor)

The State Footer is a compact mechanical status block automatically appended after significant events (combat, condition changes, energon changes, or periodically during downtime).

Example format:

```
---
[STATUS: Energon: 85/100 | Condition: Optimal | Flags: none]
[XP: Strength+2, Speed+0, Endurance+1, Firepower+0, Intelligence+3, Skill+1, Courage+0]
---
```

**Key rules:**
- The most recent footer is treated as the authoritative source of truth for mechanical values
- Before generating a response, the model checks the latest footer and corrects its internal state if there is a conflict
- The footer is kept deliberately short to minimize token cost

**Why this was introduced:**  
Purely narrative memory proved unreliable for tracking numbers across long sessions and after summarization. The footer provides a low-cost, persistent mechanical anchor.

---

## 4. Summary Integrity Protocol & ReZero Recovery

AI platforms frequently generate summaries that alter or drop mechanical details. This protocol treats all auto-generated summaries as narrative flavor only.

Mechanical state must be reconstructed from:

1. The Master State Template
2. The most recent valid State Footer
3. The pinned Spark Resonance Export

After a context reset or major summary event, the system follows a structured recovery process:

1. Reconstruct mechanical state from the sources above
2. Re-establish the active era and relevant constraints
3. Resume play without inventing missing information

**Why this exists:**  
It is more reliable to design for recovery after summarization than to attempt to prevent all forms of context compression.

---

## 5. Casting Rules & Anti-Bloat Design

Premade characters are organized by faction and operational category (High Command, Frontline, Special Operations, Support, etc.). Casting Rules define:

- Preference for dynamic / mission-generated characters by default
- Limited introduction of premade canon characters only when narratively justified
- Core Cast retention and removal criteria
- Separation between supporting cast and campaign-critical cast

**Design intent:**  
Create the feeling of a full specialized world without loading the entire roster into every scene. Token efficiency and narrative focus are treated as first-class constraints.

---

## 6. Combiner Mechanics

Combiners are handled as a dedicated multi-body system rather than ordinary characters.

**Core rules cover:**
- Formation and separation triggers
- Shared Energon / Condition pools while combined
- Identity control (combined form deactivates component entries)
- Team-specific tension and limited independent thought while merged

**Implementation pattern:**
- Universal rules live in `COMBINER_MECHANICS.md`
- Each team file contains the combined form plus all components
- Core Rules issues a structured call when combination, separation, or combiner-specific questions arise

**Why formalized:**  
Without explicit rules, models either ignored combination constraints or treated combiners as ordinary large robots. Shared-state and identity-deactivation rules keep the fantasy coherent and prevent component double-acting.

---

## 7. Cassette Protocol

Soundwave’s cassettes use a lighter but parallel formal system.

**Core rules cover:**
- Deployment and recall
- Capacity limits (preferred max of 2 active; strain at 3+)
- Independence limits when operating away from Soundwave
- Behavior when Soundwave is incapacitated
- Casting guidance so cassettes do not replace independent mid-tier operatives by default

**Why formalized:**  
Narrative-only guidance was insufficient. Without capacity and recall rules, cassettes risked becoming free infinite mini-units. The protocol keeps them powerful, flavorful, and subordinate.

---

## 8. Mid-Tier Roster Architecture

Both factions include a deliberate mid-tier layer between High Command and combiners.

**Problem observed:**  
Decepticon content especially tended to jump from officers/cassettes straight to city-scale combiners, leaving ordinary missions without appropriate opposition.

**Solution:**  
A focused mid-tier package of independent enforcers, covert operators, and practical support (including a dedicated medic) so normal missions do not require combiner-scale force.

**Design principle:**  
Structural completeness beats completionism. Characters were added to close operational gaps, not to exhaust franchise lists.

---

## 9. Era Gating

NPC entries and certain lore elements are restricted by the active campaign era. Characters whose era does not match the current scene are treated as historically absent or not yet active. The model is instructed to narrate their absence logically.

Three fully developed era scripts provide distinct mechanical identities:

- **Golden Era** — Facade, status, political subversion
- **Cybertron War** — scarcity, planetary hazard, factional total war
- **War on Earth** — secrecy, human entanglement, heat/occupation pressure

---

## 10. Hybrid Resolution System

The system uses a lightweight resolution model:

- Roll: 1d20 + relevant stat modifier + situational bonuses
- Compare against a Difficulty Class (DC)
- Resolve using narrative outcome tiers:

| Result | Outcome |
|--------|---------|
| ≥ DC + 5 | Yes, and… (success + benefit) |
| ≥ DC | Yes, but… (success + complication) |
| < DC but ≥ DC – 5 | No, but… (failure + silver lining) |
| < DC – 5 | No, and… (failure + consequence) |

Natural 20 always produces “Yes, and…”. Natural 1 always produces “No, and…”.

Dice are used only for player actions that involve meaningful risk. NPCs express threat primarily through DC values rather than separate rolls.

---

## 11. Modular Script Calling Convention

When the Core Rules needs to activate a specialized system, it uses a consistent format:

```
[CALL: Script Name - Specific Section] → Incorporate the relevant rules, then continue.
```

Priority order (simplified):

1. State Footer
2. ReZero / Summary Integrity
3. Era-specific rules
4. Casting Rules
5. Combiner Mechanics
6. Cassette Protocol
7. Normal response

This keeps the Core Rules relatively lean while still giving the model clear instructions on where to pull detailed rules from.

---

## Design Principles

- **Assume degradation** — Context will eventually be summarized or truncated. Design recovery mechanisms accordingly.
- **Centralize fragile processes** — Sequential systems like character creation remain in the Core Rules for stronger enforcement.
- **Separate stable systems** — Mechanical details that do not require constant presence are moved to specialized scripts.
- **Prefer self-healing over prevention** — Detecting and correcting drift is more reliable than trying to prevent all corruption.
- **Close operational gaps, not franchise checklists** — Roster and system expansion is driven by playability holes.
- **Protect narrative quality** — Structural rules constrain process, not cinematic or emotional writing.

---

This documentation reflects the system as of the current Core Rules revision, Combiner Mechanics, Cassette Protocol, and completed faction rosters.
