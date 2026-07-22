# Case Study: Transformers: Forged by Primus

**Role:** Solo System Designer & Prompt Engineer  
**Platform:** Multi-script AI roleplay environment (SillyTavern / JanitorAI-style / Rfab-compatible)

---

## 1. Project Overview

**Forged by Primus** is a long-form AI Dungeon Master system set in the Transformers universe. It supports multi-era campaigns and combines cinematic narrative roleplay with structured mechanical systems for character creation, combat, resource tracking, persistent state management, combiner operations, and specialized unit deployment.

The project was built to keep long-session AI roleplay reliable: coherent state, enforceable process, and recoverable structure under real platform constraints.

---

## 2. Skills Demonstrated

- Modular multi-script architecture with a clear orchestrator pattern
- State integrity systems that protect mechanical data against context loss and aggressive summarization
- Strict sequential gating for multi-step processes
- Self-healing recovery after corrupted or compressed context
- Formal multi-body systems (combiners and cassette deployment) with shared-state and capacity rules
- Faction roster design driven by operational completeness rather than franchise completionism
- Structural control balanced with high-quality narrative generation
- Iterative refinement based on observed model behavior

---

## 3. Problem Space

Long-form AI roleplay systems commonly degrade for several reasons:

- Auto-summarization and context pressure corrupt mechanical state
- Models prefer free-form narration and skip structured multi-step processes
- Cross-era lore consistency breaks without explicit gating
- Oversized rule sets and character lists create token bloat
- Multi-body fantasy elements collapse without formal constraints

The design challenge was to enforce structure and protect state without suppressing narrative quality or requiring constant user intervention.

---

## 4. Goals & Constraints

**Goals**
- Reliable long-form RPG play with clear mechanical systems
- Multi-step character creation that resists phase-skipping
- Mechanical state that survives summarization and context resets
- Multi-era support without anachronism
- Modular architecture for maintainability and token efficiency
- Operational completeness for both Autobot and Decepticon play at normal mission scale

**Constraints**
- Had to function inside existing AI chat platforms
- Modular scripts preferred over a single monolithic prompt
- Narrative quality had to remain high
- Users could not be expected to constantly restate rules
- Expansion needed justification by playability gaps, not checklist completion

---

## 5. System Architecture

| Layer | Responsibility |
|-------|----------------|
| **Core Rules** | Central orchestrator: principles, creation gating, event triggers, state integrity |
| **Session Management & Safety** | End-of-session handling, ReZero recovery, summary integrity |
| **Combat, Conditions & Growth** | Resolution, Energon/Condition, progression |
| **Casting Rules** | Core Cast management, canon introduction limits, anti-bloat |
| **Combiner Mechanics** | Formation, separation, shared state |
| **Cassette Protocol** | Deployment, recall, capacity, independence limits |
| **Era Special Conditions** | Golden Era, Cybertron War, War on Earth |
| **Premade Characters** | Faction- and role-organized roster, including six complete combiner teams |

Core Rules acts as a director, not a complete rulebook. Detailed systems are activated only when needed.

---

## 6. Key Techniques

**Strict Sequential Gating**  
Twelve-step character creation with internal checkpoints and in-character refusal when players attempt to skip ahead.

**State Footer**  
Compact mechanical status block treated as the authoritative source of truth after significant events.

**Summary Integrity & ReZero**  
Auto-summaries are narrative-only. Mechanical values are reconstructed from Master State, State Footer, and pinned character export.

**Era Gating & Mission-Scoped Casting**  
NPCs and lore are restricted by era. Premade characters appear only when they clearly serve the current mission.

**Orchestrator Pattern**  
Structured calls keep primary context lean while preserving access to specialized systems.

**Multi-Body Formalization**  
Combiners and cassettes received dedicated protocols so identity, capacity, and recall behavior remain coherent under model pressure.

**Operational Roster Design**  
Mid-tier enforcers, covert operators, and support roles were added specifically so ordinary missions did not require combiner-scale force.

**Hybrid Resolution**  
Lightweight 1d20 + modifier resolution with narrative outcome tiers.

---

## 7. Iteration

Major changes were driven by observed behavior:

- Soft character-creation guidance was replaced with strict gated protocol after repeated phase-skipping
- State Footer was introduced when narrative memory proved unreliable for numbers
- Mechanical detail was moved out of Core Rules once the monolithic prompt became expensive and hard to maintain
- Era and casting limits were added after anachronistic NPC appearances
- Combiner identity and shared-state rules were formalized after components continued acting while combined
- Cassette capacity and recall rules were formalized after narrative-only guidance failed to prevent overdeployment
- Decepticon mid-tier content was built after analysis showed the roster jumped from officers/cassettes to combiners with too little ordinary opposition in between

---

## 8. Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Skipped structured steps | Sequential gating + internal checkpoints + in-character enforcement |
| Mechanical state corruption | State Footer + Summary Integrity Protocol |
| Token bloat | Modular scripts under a strong orchestrator |
| Anachronistic content | Era gating + mission-scoped casting |
| Combiner identity collapse | Universal Combiner Mechanics + per-team files |
| Cassette overdeployment | Cassette Protocol with capacity and recall limits |
| Faction operational imbalance | Mid-tier roster focused on enforcers, covert ops, and support |
| Structure vs. narrative quality | Explicit permission for cinematic narration within defined constraints |

---

## 9. Early Deployment Results

Public deployment with no advertising produced, in the first five days:

- 66 page views  
- 38 daily visitors  
- 18 chats opened  
- 97 messages sent  
- 12 daily chatters  

These figures are early and limited, but they show the system was deployable, usable, and able to attract organic engagement under live conditions. Later development expanded the system from core reliability into full faction operational completeness, formal multi-body systems, and documentation suitable for external review.

---

## 10. Takeaways

- Enforcement works when designed against real model failure modes, not assumed compliance
- Recovery mechanisms are often more reliable than perfect prevention
- Modular systems only stay coherent if the orchestrating layer remains strong
- Multi-body systems need explicit capacity and identity rules
- Roster design should close operational gaps before chasing franchise completeness
- Control and narrative freedom both require deliberate design attention
- Structural gap analysis and adversarial testing outperform optimistic prompting
