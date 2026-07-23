# Forged by Primus

[![Latest release](https://img.shields.io/github/v/release/Manjove1/forged-by-primus-portfolio)](https://github.com/Manjove1/forged-by-primus-portfolio/releases/latest)

**Modular AI Dungeon Master system** for long-form roleplay with durable state, enforced multi-step processes, and recovery under context loss.

Built as a practical prompt-engineering portfolio piece — not a toy prompt pack.

**Download:** [Latest package](https://github.com/Manjove1/forged-by-primus-portfolio/releases/latest) · or use **Code → Download ZIP**

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
├── docs/                 Portfolio narrative and technical writeups
├── core-systems/         Orchestrator, recovery, combat, eras, combiners, cassettes
├── characters/           Faction rosters and combiner teams
├── packages/sillytavern/ Install notes for ST import
└── scripts/              Release helpers (e.g. build ST lorebook)
```

---

## Download

### Recommended: portfolio package
Download the curated systems + docs archive from the latest release:

- **[Latest package](https://github.com/Manjove1/forged-by-primus-portfolio/releases/latest)**

The package zip contains:

- `core-systems/` and `docs/`
- `sillytavern/forged-by-primus-core-systems.json` — ready for SillyTavern World Info import
- `sillytavern/INSTALL_SILLYTAVERN.md`
- `LICENSE` and README

### SillyTavern import
1. Unzip the release package  
2. SillyTavern → **World Info** → **Import**  
3. Select `sillytavern/forged-by-primus-core-systems.json`  
4. Attach the lorebook to the chat or character  

Details: [packages/sillytavern/INSTALL_SILLYTAVERN.md](packages/sillytavern/INSTALL_SILLYTAVERN.md)

### Full repository
Use GitHub’s built-in archive:

1. Click the green **Code** button at the top of this repository  
2. Select **Download ZIP**

That includes character rosters and the complete repo.

### Publishing releases (maintainers)
Releases are automated via GitHub Actions:

- **Manual:** Actions → **Portfolio Release** → Run workflow → enter tag (e.g. `v0.1.0-portfolio`)
- **Tag push:** `git tag v0.1.0-portfolio && git push origin v0.1.0-portfolio`

Both paths:
1. Build the SillyTavern lorebook from `core-systems/`
2. Package systems + docs + ST import files
3. Publish a GitHub Release with the zip attached

### Usage note
Original systems design, prompt architecture, and documentation are **All Rights Reserved**.

You may download and review this material for personal and educational purposes.  
Reuse, modification, redistribution, or commercial use requires prior written permission.

*Transformers* and related characters/names remain the property of their respective owners. This repository is an unofficial, non-commercial portfolio work.

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
