# Forged by Primus

**Modular AI Dungeon Master system** for long-form roleplay with durable state, enforced multi-step processes, and recovery under context loss.

Built as a practical prompt-engineering portfolio piece — not a toy prompt pack.

[Case Study](docs/CASE_STUDY.md) · [Technical Systems](docs/TECHNICAL_SYSTEMS.md) · [Prompt Samples](docs/PROMPT_SAMPLES.md) · [Personal Statement](docs/PERSONAL_STATEMENT.md)

---

## Why this exists

Long-form AI roleplay usually breaks in the same ways:

- mechanical state drifts after summarization
- models skip structured multi-step processes
- large rule/character sets bloat context
- multi-body systems (combiners, deployable units) become incoherent

This project treats those as **design problems**, not user error.

---

## What it demonstrates

| Skill area | Evidence in this repo |
|------------|------------------------|
| **Orchestrator design** | Core Rules coordinates specialized systems instead of one monolithic prompt |
| **State integrity** | State Footer + Summary Integrity + ReZero recovery |
| **Process enforcement** | 12-step gated character creation with internal checkpoints |
| **Modular architecture** | Separated combat, era, casting, combiner, and cassette systems |
| **Constraint design** | Era gating, mission-scoped casting, capacity limits |
| **Iteration from failure modes** | Systems added only after observed breakage or operational gaps |
| **Documentation discipline** | Case study, technical writeup, samples, live metrics |

---

## System at a glance

- **Core Rules** — director/orchestrator
- **State Footer** — compact self-healing mechanical anchor
- **Casting Rules** — anti-bloat character introduction controls
- **Combiner Mechanics** — shared-state multi-body rules
- **Cassette Protocol** — deployment, recall, and capacity limits
- **Era scripts** — Golden Era, Cybertron War, War on Earth
- **Premade rosters** — Autobot + Decepticon operational depth, including mid-tier and 6 combiner teams

---

## Suggested reading order

1. [Case Study](docs/CASE_STUDY.md) — problem, approach, iteration, results  
2. [Technical Systems](docs/TECHNICAL_SYSTEMS.md) — architecture and design rationale  
3. [Prompt Samples](docs/PROMPT_SAMPLES.md) — concrete enforcement patterns  
4. `core-systems/` — full system scripts  
5. [Analytics](docs/ANALYTICS_AND_RESULTS.md) — early live deployment metrics  

---

## Live deployment

Published publicly with **no advertising** (July 13, 2026).

Early window metrics:

- 74 page views  
- 19 chats opened  
- 98 messages  
- 8 favorites  
- 6 min average time on page  

Read as early validation of deployability and organic interest, not scale proof.

Details: [Analytics & Results](docs/ANALYTICS_AND_RESULTS.md)

---

## Repository map

```text
forged-by-primus-portfolio/
├── docs/            Portfolio narrative and technical writeups
├── core-systems/    Orchestrator, recovery, combat, eras, combiners, cassettes
└── characters/      Faction rosters and combiner teams
```

---

## Contact

Professional inquiries via GitHub: [@Manjove1](https://github.com/Manjove1)  
LinkedIn is listed on the GitHub profile.

---

## License

Original systems design, prompt architecture, and documentation  
© 2026 Forged by Primus contributors. All Rights Reserved.

You may view this repository for personal and educational purposes.  
Reuse, modification, or commercial use of the original systems requires prior written permission.

---

## Intellectual Property Notice

*Transformers* and related characters, names, and likenesses are property of Hasbro, TakaraTomy, and/or their respective owners.

This is an **unofficial, non-commercial fan and portfolio work**. Not affiliated with or endorsed by any official rights holder.

The All Rights Reserved notice applies only to original systems design, prompt architecture, and documentation in this repository. It does not grant or claim rights to third-party intellectual property.
