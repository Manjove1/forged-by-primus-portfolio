# Case Study: Transformers: Forged by Primus

**Role:** Solo System Designer & Prompt Engineer  
**Platform:** Multi-script AI roleplay environment (SillyTavern / JanitorAI-style)

---

## 1. Project Overview

**Forged by Primus** is a long-form AI Dungeon Master system set in the Transformers universe. It supports multi-era campaigns and combines cinematic narrative roleplay with structured mechanical systems for character creation, combat, resource management, and persistent state tracking.

The project was built to solve a common failure mode of AI roleplay platforms: the inability to maintain mechanical consistency and structured processes across long sessions.

---

## 2. Key Contributions & Skills Demonstrated

This project demonstrates practical prompt engineering skills relevant to production AI systems:

- Designed a modular multi-script architecture with a clear orchestrator pattern
- Built robust state integrity systems to protect mechanical data against context loss and aggressive summarization
- Implemented strict sequential gating for complex multi-step processes (character creation)
- Developed self-healing mechanisms that allow the system to recover from corrupted context
- Balanced strong structural control with high-quality narrative generation
- Iteratively stress-tested the system against model failure modes and refined enforcement strategies

---

## 3. The Problem

Long-form AI roleplay systems frequently degrade for several reasons:

- Auto-summarization and context window pressure corrupt mechanical state (stats, resources, conditions)
- Models prefer free-form narration and routinely skip structured multi-step processes
- Maintaining lore and faction consistency across eras is difficult without explicit gating
- Large rule sets create token bloat and reduce response quality over time

The core design challenge was enforcing structure and state integrity without destroying narrative quality or requiring constant user intervention.

---

## 4. Goals & Constraints

**Goals:**
- Create a reliable long-form RPG experience with clear mechanical systems
- Enforce multi-step character creation without phase-skipping
- Protect mechanical state against summarization and context resets
- Support multiple eras while preventing anachronisms
- Maintain modularity for token efficiency and easier maintenance

**Constraints:**
- Had to function within existing AI chat platforms
- Preferred modular scripts over a single monolithic prompt
- Needed to preserve strong narrative quality
- Could not rely on the user constantly restating rules

---

## 5. System Architecture

The system uses a modular multi-script architecture:

- **Core Rules** — Central orchestrator. Handles high-level principles, character creation gating, event triggers, and state integrity.
- **Lore Book** — Always-active cosmological and setting reference.
- **Combat, Conditions & Growth** — Mechanical systems for combat resolution, condition tracking, and progression.
- **Session Management & Safety** — End-of-session handling, ReZero recovery, and summary integrity protocols.
- **Faction / Role Scripts** — Modular character and NPC definitions.

The Core Rules script functions as a director rather than a complete rulebook. It coordinates the other systems and only activates detailed rules when needed. This design improves both control and token efficiency.

---

## 6. Key Prompt Engineering Techniques

**Strict Sequential Gating**  
Character creation uses a 12-step locked process. The model is required to wait for explicit player input at each stage and includes internal checkpoints to reduce phase-skipping.

**State Footer (Self-Healing Anchor)**  
A compact mechanical status footer is automatically appended after significant events. The model is instructed to treat the most recent footer as the authoritative source of truth for stats, resources, and conditions.

**Summary Integrity Protocol**  
Auto-generated summaries are treated as narrative flavor only. Mechanical values must be reconstructed from the Master State, State Footer, and pinned character export rather than trusted from summaries.

**Era Gating & Mission-Scoped Casting**  
NPCs and lore are restricted by era. Premade characters are only introduced when they provide clear narrative value for the current mission, reducing bloat and anachronistic appearances.

**Orchestrator Pattern**  
The Core Rules script issues structured calls to specialized scripts when needed, keeping the primary context lean while preserving access to detailed systems.

**Hybrid Resolution System**  
A lightweight 1d20 + modifier system with narrative outcome tiers (“Yes, and…”, “Yes, but…”, etc.) provides mechanical structure without turning every interaction into a pure numbers exercise.

---

## 7. Iteration Process

Early versions of the system suffered from two recurring failures: the model frequently skipped character creation steps, and mechanical state would drift or become corrupted after summaries.

Several concrete changes were made in response:

- Character creation enforcement was strengthened from soft instructions to a strict gated protocol with internal checkpoints and in-character refusal language.
- The State Footer was introduced after observing that purely narrative memory was unreliable for tracking numbers across long sessions.
- Detailed mechanical rules were moved out of the Core Rules into specialized scripts once it became clear that a monolithic prompt was both token-expensive and harder to maintain.
- Era and casting restrictions were added after repeated anachronistic NPC appearances during testing.

Each major change was driven by observed model behavior rather than theoretical preference.

---

## 8. Challenges & Solutions

| Challenge | Solution |
|---------|----------|
| Model skipping structured steps | Strict sequential gating + internal checkpoints + in-character enforcement |
| Mechanical state corruption | State Footer + Summary Integrity Protocol that prioritizes mechanical anchors over summaries |
| Token bloat from large rule sets | Modular scripts with Core Rules acting as orchestrator |
| Anachronistic content | Era gating + mission-scoped casting limits |
| Maintaining narrative quality under structure | Explicit permission for free cinematic narration within defined constraints |

---

## 9. Results

The system was deployed publicly with no advertising. In the first **5 days** of public availability it recorded:

- 66 page views  
- 38 daily visitors  
- 18 chats opened  
- 97 messages sent  
- 12 daily chatters  

These early results indicate that a complex, structured AI RPG system can attract organic engagement and function under live usage pressure. The deployment successfully moved the project from internal development into real-world testing of its core prompt engineering systems.

---

## 10. What I Learned

- Structural enforcement is possible, but it must be designed against actual model failure modes rather than assumed compliance.
- Self-healing mechanisms are often more reliable than trying to prevent all forms of context corruption.
- Modular architectures improve maintainability and efficiency, but only if the orchestrating layer remains strong enough to prevent fragmentation.
- Balancing control and narrative freedom requires explicit design attention; over-structuring can suppress quality writing just as under-structuring can destroy consistency.
- Adversarial testing (actively trying to break the system) produces better results than optimistic prompting.
