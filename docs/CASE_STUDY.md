# Case Study: Transformers: Forged by Primus

**Role:** Solo System Designer & Prompt Engineer  
**Platform:** Multi-script AI roleplay environment (SillyTavern / JanitorAI-style / Rfab-compatible)

---

## 1. Project Overview

**Forged by Primus** is a long-form AI Dungeon Master system set in the Transformers universe. It supports multi-era campaigns and combines cinematic narrative roleplay with structured mechanical systems for character creation, combat, resource management, persistent state tracking, combiner operations, and specialized unit deployment.

The project was built to solve a common failure mode of AI roleplay platforms: the inability to maintain mechanical consistency and structured processes across long sessions.

---

## 2. Key Contributions & Skills Demonstrated

This project demonstrates practical prompt engineering skills relevant to production AI systems:

- Designed a modular multi-script architecture with a clear orchestrator pattern
- Built robust state integrity systems to protect mechanical data against context loss and aggressive summarization
- Implemented strict sequential gating for complex multi-step processes (character creation)
- Developed self-healing mechanisms that allow the system to recover from corrupted context
- Created specialized multi-body systems (combiners and cassette deployment) with shared-state and capacity rules
- Designed faction rosters around operational completeness rather than franchise completionism
- Balanced strong structural control with high-quality narrative generation
- Iteratively stress-tested the system against model failure modes and refined enforcement strategies

---

## 3. The Problem

Long-form AI roleplay systems frequently degrade for several reasons:

- Auto-summarization and context window pressure corrupt mechanical state (stats, resources, conditions)
- Models prefer free-form narration and routinely skip structured multi-step processes
- Maintaining lore and faction consistency across eras is difficult without explicit gating
- Large rule sets and oversized character lists create token bloat and reduce response quality
- Multi-body fantasy elements (combiners, mini-operatives) collapse without formal constraints

The core design challenge was enforcing structure and state integrity without destroying narrative quality or requiring constant user intervention.

---

## 4. Goals & Constraints

**Goals:**
- Create a reliable long-form RPG experience with clear mechanical systems
- Enforce multi-step character creation without phase-skipping
- Protect mechanical state against summarization and context resets
- Support multiple eras while preventing anachronisms
- Maintain modularity for token efficiency and easier maintenance
- Make both Autobot and Decepticon sides operationally complete at normal mission scale

**Constraints:**
- Had to function within existing AI chat platforms
- Preferred modular scripts over a single monolithic prompt
- Needed to preserve strong narrative quality
- Could not rely on the user constantly restating rules
- Expansion had to be justified by playability gaps, not checklist completion

---

## 5. System Architecture

The system uses a modular multi-script architecture:

- **Core Rules** — Central orchestrator. Handles high-level principles, character creation gating, event triggers, and state integrity.
- **Session Management & Safety** — End-of-session handling, ReZero recovery, and summary integrity protocols.
- **Combat, Conditions & Growth** — Mechanical systems for combat resolution, condition tracking, and progression.
- **Casting Rules** — Core Cast management, canon introduction limits, and anti-bloat controls.
- **Combiner Mechanics** — Universal formation, separation, and shared-state rules for all combiner teams.
- **Cassette Protocol** — Soundwave deployment, recall, capacity, and independence limits.
- **Era Special Conditions** — Golden Era, Cybertron War, and War on Earth mechanical identities.
- **Premade Characters** — Faction- and role-organized canon/supporting cast, including six complete combiner teams.

The Core Rules script functions as a director rather than a complete rulebook. It coordinates the other systems and only activates detailed rules when needed.

---

## 6. Key Prompt Engineering Techniques

**Strict Sequential Gating**  
Character creation uses a 12-step locked process with internal checkpoints and in-character refusal language when players attempt to skip ahead.

**State Footer (Self-Healing Anchor)**  
A compact mechanical status footer is automatically appended after significant events. The model treats the most recent footer as the authoritative source of truth for resources and conditions.

**Summary Integrity Protocol**  
Auto-generated summaries are treated as narrative flavor only. Mechanical values are reconstructed from Master State, State Footer, and pinned character export.

**Era Gating & Mission-Scoped Casting**  
NPCs and lore are restricted by era. Premade characters are introduced only when they provide clear narrative value for the current mission.

**Orchestrator Pattern**  
Core Rules issues structured calls to specialized scripts when needed, keeping primary context lean while preserving access to detailed systems.

**Multi-Body System Formalization**  
Combiners and cassettes received dedicated protocols so shared identity, capacity, and recall behavior remain coherent under model pressure.

**Operational Roster Design**  
Faction content was expanded to close mid-tier gaps (independent enforcers, covert options, practical support) rather than adding more high-spectacle units.

**Hybrid Resolution System**  
A lightweight 1d20 + modifier system with narrative outcome tiers provides mechanical structure without turning every interaction into pure numbers.

---

## 7. Iteration Process

Early versions of the system suffered from recurring failures: the model frequently skipped character creation steps, mechanical state drifted after summaries, and specialized units behaved inconsistently.

Concrete changes made in response:

- Character creation enforcement was strengthened from soft instructions to a strict gated protocol with internal checkpoints.
- The State Footer was introduced after observing that purely narrative memory was unreliable for tracking numbers.
- Detailed mechanical rules were moved out of Core Rules into specialized scripts once a monolithic prompt became token-expensive and harder to maintain.
- Era and casting restrictions were added after repeated anachronistic NPC appearances.
- Combiner identity and shared-state rules were formalized after models either ignored combination constraints or double-acted components.
- Cassette capacity and recall rules were formalized after narrative-only guidance failed to prevent infinite mini-unit deployment.
- Decepticon mid-tier content was deliberately built after analysis showed the roster jumped from officers/cassettes to combiners with too little ordinary opposition in between.

Each major change was driven by observed model or structural behavior rather than theoretical preference.

---

## 8. Challenges & Solutions

| Challenge | Solution |
|---------|----------|
| Model skipping structured steps | Strict sequential gating + internal checkpoints + in-character enforcement |
| Mechanical state corruption | State Footer + Summary Integrity Protocol |
| Token bloat from large rule sets | Modular scripts with Core Rules as orchestrator |
| Anachronistic content | Era gating + mission-scoped casting limits |
| Combiner identity collapse | Universal Combiner Mechanics + per-team files |
| Cassette overdeployment | Cassette Protocol with capacity and recall limits |
| Faction operational imbalance | Mid-tier roster design focused on enforcers, covert ops, and support |
| Maintaining narrative quality under structure | Explicit permission for free cinematic narration within defined constraints |

---

## 9. Results

The system was deployed publicly with no advertising. In the first **5 days** of public availability it recorded:

- 66 page views  
- 38 daily visitors  
- 18 chats opened  
- 97 messages sent  
- 12 daily chatters  

These early results show that a complex, structured AI RPG system can attract organic engagement and function under live usage pressure. Subsequent development expanded the system from core mechanical reliability into full faction operational completeness, formal multi-body systems, and documentation suitable for external review.

---

## 10. What I Learned

- Structural enforcement is possible, but it must be designed against actual model failure modes rather than assumed compliance.
- Self-healing mechanisms are often more reliable than trying to prevent all forms of context corruption.
- Modular architectures improve maintainability and efficiency only if the orchestrating layer remains strong enough to prevent fragmentation.
- Multi-body systems (combiners, deployable mini-units) need explicit capacity and identity rules; narrative flavor alone is not enough.
- Roster design should close operational gaps before chasing franchise completeness.
- Balancing control and narrative freedom requires explicit design attention; over-structuring can suppress quality writing just as under-structuring can destroy consistency.
- Adversarial testing and structural gap analysis produce better systems than optimistic prompting or pure content expansion.
