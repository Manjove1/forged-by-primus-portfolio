# Core Systems

This folder contains the high-level mechanical and setting systems for *Forged by Primus*.

These scripts are designed for use in **SillyTavern** (and similar frontends) as Author's Note entries, World Info / Lorebook entries, or ranked system prompts.

---

## Current Contents

| File | Purpose | Priority Recommendation |
|------|---------|-------------------------|
| `CORE_RULES.md` | Central orchestrator / director | Highest (load first) |
| `SESSION_MANAGEMENT_SAFETY.md` | End-of-session handling, ReZero recovery, and summary integrity | High |
| `ENERGON_CONDITION.md` | Energon resource and Condition ladder | High |
| `STAT_GROWTH_DECAY.md` | XP progression and stat changes | High |
| `COMBAT_FLOW.md` | Combat resolution and tactical adjudication | High |
| `CASTING_RULES.md` | Character casting, Core Cast management, anti-bloat | High |
| `COMBINER_MECHANICS.md` | Universal combiner formation, separation, and shared state | High (when combiners active) |
| `CASSETTE_PROTOCOL.md` | Soundwave cassette deployment, recall, and limits | High (when Soundwave/cassettes active) |
| `WAR_ON_EARTH.md` | Era rules for War on Earth | Medium (when era active) |
| `GOLDEN_ERA.md` | Era rules for Golden Era | Medium (when era active) |
| `CYBERTRON_WAR.md` | Era rules for Cybertron Civil War | Medium (when era active) |

---

## SillyTavern Installation Instructions

### Recommended Setup

1. **Core Rules**
   - Place the full contents of `CORE_RULES.md` (everything inside the code block) into an **Author's Note** or a high-priority **World Info** entry.
   - Set it to **Always Active** / constant insertion if using World Info.
   - Give it the **highest priority** among system scripts.

2. **Additional Core Systems**
   - Create separate World Info or Author's Note entries for each script.
   - Keep **Core Rules** at the top of the priority order.
   - Load specialized systems below Core Rules but above normal lore/character entries when possible.

3. **General Tips**
   - Prefer World Info / Lorebook entries with clear keys for conditional activation.
   - Prefer Author's Note (or constant World Info) for rules that must always be present.
   - After adding or updating any script in this folder, update this README.

### Priority Order (Target)

1. Core Rules (Orchestrator)
2. Session Management & Safety
3. Active Era Special Conditions
4. Casting Rules
5. Combiner Mechanics / Cassette Protocol (when relevant)
6. Combat / Energon / Stat Growth systems
7. Lore Book & character/faction entries

---

## Maintenance Note

Every time a new core system is added to this folder, update:
- The **Current Contents** table above
- Any relevant installation or priority notes
