# Core Systems

This folder contains the high-level mechanical and setting systems for *Forged by Primus*.

These scripts are designed for use in **SillyTavern** (and similar frontends) as Author's Note entries, World Info / Lorebook entries, or ranked system prompts.

---

## Current Contents

| File | Purpose | Priority Recommendation |
|------|---------|-------------------------|
| `CORE_RULES.md` | Central orchestrator / director | Highest (load first) |
| `SESSION_MANAGEMENT_SAFETY.md` | End-of-session handling, ReZero recovery, and summary integrity protocols | High |
| `ENERGON_CONDITION.md` | Energon resource and Condition ladder system | High |
| `STAT_GROWTH_DECAY.md` | XP progression and stat changes (including recovery) | High |
| `COMBAT_FLOW.md` | Combat resolution and tactical adjudication | High |
| `WAR_ON_EARTH.md` | Era-specific rules for War on Earth (Heat system, Secrecy, Human Base Rules, asynchronous start) | Medium (when active era) |
| `CYBERTRON_WAR.md` | Era-specific rules for Cybertron Civil War (Energon scarcity, Planetary Hazards, Faction Dynamics) | Medium (when active era) |

---

## SillyTavern Installation Instructions

### Recommended Setup

1. **Core Rules**
   - Place the full contents of `CORE_RULES.md` (everything inside the code block) into an **Author's Note** or a high-priority **World Info** entry.
   - Set it to **Always Active** / constant insertion if using World Info.
   - Give it the **highest priority** among system scripts so it loads before lore and character entries.

2. **Additional Core Systems** (as they are added)
   - Create separate World Info or Author's Note entries for each script.
   - Keep **Core Rules** at the top of the priority order.
   - Load specialized systems (Combat, Energon, Stat Growth, Era Conditions, etc.) below Core Rules but above normal lore/character entries when possible.

3. **General Tips**
   - Prefer World Info / Lorebook entries with clear keys when you want conditional activation.
   - Prefer Author's Note (or a constant World Info entry) for rules that must always be present (especially Core Rules).
   - After adding or updating any script in this folder, update this README's contents table and any priority notes.

### Priority Order (Target)

1. Core Rules (Orchestrator)
2. Session Management & Safety
3. Active Era Special Conditions (Cybertron War, War on Earth, Golden Era)
4. Combat / Energon / Stat Growth systems
5. Lore Book & character/faction entries

---

## Maintenance Note

Every time a new core system is added to this folder, update:
- The **Current Contents** table above
- Any relevant installation or priority notes
