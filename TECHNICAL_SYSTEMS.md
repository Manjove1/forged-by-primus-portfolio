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
- Specialized scripts (Combat, Golden Era conditions, etc.) are activated only when needed via structured calls from Core Rules.

This design prioritizes recovery and coordination over trying to prevent all forms of context degradation.

---

## 1. Core Rules as Orchestrator

The Core Rules script functions as a central director rather than a complete rulebook. Its responsibilities are:

- Enforce high-level principles (user agency, lore consistency, narrative quality)
- Control sequential processes, especially character creation
- Trigger specialized systems only when needed
- Maintain state integrity through the State Footer and related protocols

Detailed mechanical rules are kept in separate scripts. The Core Rules references them using a structured calling convention when required.

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

## 4. Summary Integrity Protocol

AI platforms frequently generate summaries that alter or drop mechanical details. This protocol treats all auto-generated summaries as narrative flavor only.

Mechanical state must be reconstructed from:

1. The Master State Template
2. The most recent valid State Footer
3. The pinned Spark Resonance Export

The model is explicitly instructed not to trust numerical values from summaries.

**Why this exists:**  
It is more reliable to design for recovery after summarization than to attempt to prevent all forms of context compression.

---

## 5. ReZero Recovery

After a context reset or major summary event, the system follows a structured recovery process:

1. Reconstruct mechanical state from the Master State + State Footer + pinned character export
2. Re-establish the active era and relevant constraints
3. Resume play without inventing missing information

This process can be triggered automatically or via explicit player command.

---

## 6. Era Gating & Mission-Scoped Casting

**Era Gating**  
NPC entries and certain lore elements are restricted by the active campaign era. Characters whose era does not match the current scene are treated as historically absent or not yet active. The model is instructed to narrate their absence logically.

**Mission-Scoped Casting**  
At the start of a new mission, the system evaluates whether any premade NPCs provide significantly superior narrative value. Only 0–2 premade NPCs may be selected per mission. All other introductions default to procedural generation.

These controls reduce anachronisms and prevent over-reliance on a small set of named characters.

---

## 7. Hybrid Resolution System

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

**Design choice:**  
Narrative outcome tiers were selected to preserve story flow and dramatic interest while still providing mechanical structure.

---

## 8. Modular Script Calling Convention

When the Core Rules needs to activate a specialized system, it uses a consistent format:

```
[CALL: Script Name - Specific Section] → Incorporate the relevant rules, then continue.
```

This keeps the Core Rules relatively lean while still giving the model clear instructions on where to pull detailed rules from. It also makes the system easier to maintain and extend.

---

## Design Principles

Several principles guided the technical design:

- **Assume degradation** — Context will eventually be summarized or truncated. Design recovery mechanisms accordingly.
- **Centralize fragile processes** — Sequential systems like character creation remain in the Core Rules for stronger enforcement.
- **Separate stable systems** — Mechanical details that do not require constant presence are moved to specialized scripts.
- **Prefer self-healing over prevention** — Detecting and correcting drift is more reliable than trying to prevent all corruption.
- **Protect narrative quality** — Structural rules constrain process, not cinematic or emotional writing.

---

This documentation reflects the system as of the current Core Rules revision and supporting scripts.
