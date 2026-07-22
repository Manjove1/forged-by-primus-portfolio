# Premade Characters

This folder contains structured, premade canon characters for *Forged by Primus*.

These characters are intended to be used selectively according to the **Casting Rules**. The system should prefer Dynamic Core Cast characters and newly generated characters by default. Premade canon characters should only be introduced when they have clear narrative justification.

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
│   ├── seekers.md
│   ├── special_operations.md
│   ├── support_logistics.md
│   └── soundwave_unit.md
├── combiners/
│   ├── defensor.md          (Protectobots)
│   ├── computron.md         (Technobots)
│   ├── superion.md          (Aerialbots)
│   ├── bruticus.md          (Combaticons)
│   ├── menasor.md           (Stunticons)
│   └── devastator.md        (Constructicons)
└── README.md
```

---

## Category Guide

| Category | Purpose |
|----------|---------|
| **High Command** | Strategic leaders. Use sparingly and with weight. |
| **Frontline** | Independent combat personnel for active missions. |
| **Seekers / Aerial & Naval** | Air (and limited sea) specialists. |
| **Special Operations** | Covert, infiltration, sabotage, bounty, and high-skill roles. |
| **Science & Medical** | Scientific, technical, and medical specialists. |
| **Support & Logistics** | Repair, supply, communications, medical support. |
| **Soundwave Unit** | Cassette operatives. Governed by Cassette Protocol. |
| **Earth Resistance** | Human allies and Earth-focused Autobot cells. |
| **Combiners** | Full teams + combined forms. Governed by Combiner Mechanics. |

---

## Deprecated Stubs

These files are empty placeholders and should not be used:

- `autobots/frontline.md` → use `frontline_combat.md`
- `autobots/logistics.md` → use `support_logistics.md`
- `decepticons/aerial_naval.md` → use `seekers.md`
- `decepticons/logistics.md` → use `support_logistics.md`

---

## Usage Notes

- Prefer loading only the relevant faction and category for the current mission.
- Use short summaries first. Expand to full detail only when a character becomes actively involved.
- Follow the priority order defined in `CASTING_RULES.md`.
- High Command and combiners should feel significant when they appear.
- Cassettes require Soundwave presence or explicit deployment (see Cassette Protocol).

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
[How they typically fight or operate.]

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
- Prefer this character only when they serve a clear narrative purpose.
```
