# SillyTavern Import

## Lorebook package

File: `forged-by-primus-core-systems.json`

This file is **built automatically into the GitHub Release package** from `core-systems/` when a release is published.

### Import steps

1. Download the latest **Release** package zip
2. Open SillyTavern → **World Info** (Lorebook)
3. Click **Import**
4. Select `sillytavern/forged-by-primus-core-systems.json` from the unzipped package
5. Attach the lorebook to your chat or character
6. Start a new chat

### What is included

| Entry | Mode |
|-------|------|
| Core Rules (Orchestrator) | Always on |
| Session Management & Safety | Always on |
| Energon & Condition | Keyword |
| Stat Growth & Decay | Keyword |
| Combat Flow | Keyword |
| Casting Rules | Keyword |
| Combiner Mechanics | Keyword |
| Cassette Protocol | Keyword |
| Golden Era | Keyword |
| Cybertron War | Keyword |
| War on Earth | Keyword |

### Local rebuild (optional)

From the repo root:

```bash
python3 scripts/build_st_lorebook.py
```

This writes `forged-by-primus-core-systems.json` using the current `core-systems/*.md` files.

### Notes

- Core Rules enforces gated character creation and state integrity.
- Session Management handles ReZero / recovery after summarization.
- Era and specialist systems inject when their keys appear in context.
- Original systems design is All Rights Reserved. Personal and educational review only.

Unofficial, non-commercial Transformers fan / portfolio work.
