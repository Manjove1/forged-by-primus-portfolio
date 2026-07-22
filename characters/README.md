# Premade Characters

This folder contains structured, premade canon characters for *Forged by Primus*.

These characters are intended to be used selectively according to the **Casting Rules**. The system should prefer Dynamic Core Cast characters and newly generated characters by default. Premade canon characters should only be introduced when they have clear narrative justification.

The goal of this structure is to create the feeling of a fuller, more specialized world while remaining token-efficient.

---

## Structure

```text
characters/
├── autobots/
│   ├── high_command.md
│   ├── frontline_combat.md
│   ├── aerial_naval.md
│   ├── special_operations.md
│   ├── science_medical.md
│   ├── support_logistics.md
│   └── earth_resistance.md
├── decepticons/
│   ├── high_command.md
│   ├── frontline.md
│   ├── aerial_naval.md
│   ├── special_operations.md
│   └── support_logistics.md
└── README.md
```

Each file is intended to hold approximately 5–8 characters.

---

## Category Guide

| Category | Purpose |
|----------|---------|
| **High Command** | Strategic leaders and high-level decision makers. Use sparingly and with weight. |
| **Frontline / Frontline Combat** | Primary combat personnel who commonly appear in active missions. |
| **Aerial & Naval** | Characters specialized in air or sea operations. |
| **Special Operations** | Covert, infiltration, sabotage, and high-skill specialist roles. |
| **Science & Medical** | Scientific, technical, and medical specialists. |
| **Support & Logistics** | Repair, supply, communications, intelligence support, and general logistics. |
| **Earth Resistance** | Autobot characters and cells specifically focused on operations on Earth. |

---

## Usage Notes

- Prefer loading only the relevant faction and category for the current mission.
- Use short summaries first. Expand to full detail only when a character becomes actively involved.
- Follow the priority order defined in `CASTING_RULES.md`.
- Keep character entries relatively concise to maintain token efficiency.
- High Command characters should feel significant when they appear.

---

## Character Entry Format

```text
### [Character Name]

**Role / Tier:** [Faction] – [Category]  
**Era Availability:** [Golden Era / Cybertron War / War on Earth / Multiple]  
**Alt-Mode:** [Cybertronian form] (Earth: [Earth form if applicable])  
**Stats (1–10):** STR:[X] | SPD:[X] | END:[X] | FIRE:[X] | INT:[X] | SKL:[X] | COU:[X]

**Personality & Voice:**  
[2–3 sentences covering core personality, speech style, and notable quirks.]

**Combat / Action Style:**  
[How they typically fight or operate. Focus on approach and priorities.]

**Key Relationships:**  
- [Important relationship 1]  
- [Important relationship 2]

**Hidden Agenda / Pressure Point:**  
[One clear secret, fear, or internal conflict.]

**When to Use:**  
[Clear guidance on when this character should appear.]

**AI Notes:**  
- Never speak, act, or think for {{user}}.  
- Stay consistent with the voice and personality above.  
- When describing this character in action, use at least two non-visual senses.  
- Prefer this character only when they serve a clear narrative purpose.
```
