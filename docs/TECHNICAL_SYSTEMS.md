# Technical Systems Documentation
**Project:** Transformers: Forged by Primus

Technical overview of the core systems in the project: how the major prompt engineering patterns function, and why they were designed this way.

---

## System Relationships

- **Core Rules** is the central orchestrator. It controls high-level flow, triggers specialized systems, and enforces sequential processes.
- **State Footer** is the persistent mechanical anchor referenced by Core Rules and recovery protocols.
- **Summary Integrity Protocol** treats auto-summaries as non-authoritative for mechanical values.
- **ReZero Recovery** reconstructs state from Master State + State Footer + pinned character export after context loss.
- **Casting Rules** control who appears and limit roster bloat.
- **Combiner Mechanics** and **Cassette Protocol** govern multi-body systems with shared state and deployment limits.
- Era scripts and premade character files activate only when needed through structured calls from Core Rules.

The architecture prioritizes coordination and recovery over attempting to prevent every form of context degradation.

---

## 1. Core Rules as Orchestrator

Core Rules functions as a director, not a complete rulebook. It:

- Enforces high-level principles (user agency, lore consistency, narrative quality)
- Controls sequential processes, especially character creation
- Triggers specialized systems only when needed
- Maintains state integrity through the State Footer and related protocols

**Major call targets include:**
- Session Management & Safety (ReZero)
- Era Special Conditions
- Casting Rules
- Combiner Mechanics
- Cassette Protocol
- Combat / Energon / Stat systems

**Design rationale:**  
A monolithic prompt became token-expensive and difficult to maintain. Specialized scripts for stable systems, under strong central control for fragile processes, improved both efficiency and reliability.

---

## 2. Character Creation Gating Protocol

Character creation uses a strict 12-step sequential process. The model must wait for explicit player input before advancing.

Enforcement mechanisms:

- One question per message
- Silent internal checkpoint before each response
- In-character refusal when the player attempts to skip ahead
- Final Spark Resonance Export confirmation before the story may begin

**Design rationale:**  
Earlier versions allowed batching and early narrative entry. Sequential locking plus an internal checkpoint substantially reduced phase-skipping.

---

## 3. State Footer

A compact mechanical status block is appended after significant events.

```
---
[STATUS: Energon: 85/100 | Condition: Optimal | Flags: none]
[XP: Strength+2, Speed+0, Endurance+1, Firepower+0, Intelligence+3, Skill+1, Courage+0]
---
```

Rules:
- Most recent footer is authoritative for mechanical values
- Model corrects internal state to match the footer when conflict appears
- Format stays short to minimize token cost

**Design rationale:**  
Narrative memory alone was unreliable for numbers across long sessions and after summarization.

---

## 4. Summary Integrity & ReZero

Auto-generated summaries are treated as narrative flavor only.

Mechanical state is reconstructed from:

1. Master State Template
2. Most recent valid State Footer
3. Pinned Spark Resonance Export

After reset or major summary events:

1. Reconstruct mechanical state
2. Re-establish active era and constraints
3. Resume without inventing missing information

**Design rationale:**  
Recovery after summarization is more reliable than attempting to prevent all context compression.

---

## 5. Casting Rules & Anti-Bloat

Premade characters are organized by faction and operational category. Casting Rules define:

- Preference for dynamic / mission-generated characters by default
- Limited premade canon introduction when narratively justified
- Core Cast retention and removal criteria
- Separation between supporting cast and campaign-critical cast

**Design rationale:**  
Create the feeling of a specialized world without loading the full roster into every scene.

---

## 6. Combiner Mechanics

Combiners are a dedicated multi-body system.

Covered rules:
- Formation and separation triggers
- Shared Energon / Condition pools while combined
- Identity control (combined form deactivates component entries)
- Team-specific tension while merged

Implementation:
- Universal rules in `COMBINER_MECHANICS.md`
- Team files contain combined form plus components
- Core Rules issues structured calls on combination, separation, or combiner-specific questions

**Design rationale:**  
Without explicit rules, models ignored combination constraints or treated combiners as ordinary large robots.

---

## 7. Cassette Protocol

Soundwave’s cassettes use a lighter parallel system.

Covered rules:
- Deployment and recall
- Capacity limits (preferred max of 2 active; strain at 3+)
- Independence limits away from Soundwave
- Behavior when Soundwave is incapacitated
- Casting guidance so cassettes do not replace independent mid-tier operatives by default

**Design rationale:**  
Narrative-only guidance was insufficient. Capacity and recall rules keep cassettes powerful, flavorful, and subordinate.

---

## 8. Mid-Tier Roster Architecture

Both factions include a deliberate mid-tier layer between High Command and combiners.

**Problem:**  
Especially on the Decepticon side, content tended to jump from officers/cassettes to city-scale combiners, leaving ordinary missions without appropriate opposition.

**Solution:**  
Independent enforcers, covert operators, and practical support (including a dedicated medic) so normal missions do not require combiner-scale force.

**Design principle:**  
Structural completeness over franchise completionism. Characters are added to close operational gaps.

---

## 9. Era Gating

NPC entries and certain lore elements are restricted by active campaign era. Mismatched characters are treated as historically absent or not yet active.

Three era scripts provide distinct mechanical identities:

- **Golden Era** — Facade, status, political subversion
- **Cybertron War** — scarcity, planetary hazard, total war
- **War on Earth** — secrecy, human entanglement, occupation pressure

---

## 10. Hybrid Resolution System

- Roll: 1d20 + relevant modifier + situational bonuses
- Compare against DC
- Resolve with narrative outcome tiers:

| Result | Outcome |
|--------|---------|
| ≥ DC + 5 | Yes, and… |
| ≥ DC | Yes, but… |
| < DC but ≥ DC – 5 | No, but… |
| < DC – 5 | No, and… |

Natural 20 → Yes, and…  
Natural 1 → No, and…

Dice are reserved for meaningful risk. NPCs express threat primarily through DC values.

---

## 11. Script Calling Convention

```
[CALL: Script Name - Specific Section] → Incorporate the relevant rules, then continue.
```

Priority order:

1. State Footer  
2. ReZero / Summary Integrity  
3. Era-specific rules  
4. Casting Rules  
5. Combiner Mechanics  
6. Cassette Protocol  
7. Normal response

---

## Design Principles

- Assume degradation and design recovery
- Centralize fragile sequential processes
- Separate stable systems into modular scripts
- Prefer self-healing over perfect prevention
- Close operational gaps rather than franchise checklists
- Constrain process, not cinematic or emotional writing

---

Documentation current as of the live Core Rules revision, Combiner Mechanics, Cassette Protocol, and completed faction rosters.
