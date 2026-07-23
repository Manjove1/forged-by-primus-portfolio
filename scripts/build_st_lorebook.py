#!/usr/bin/env python3
"""Build SillyTavern World Info JSON from core-systems/*.md for release packaging."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "core-systems"
OUT = Path("forged-by-primus-core-systems.json")

# (filename, comment, constant, order, keys)
MANIFEST = [
    ("CORE_RULES.md", "Core Rules (Orchestrator)", True, 1, []),
    ("SESSION_MANAGEMENT_SAFETY.md", "Session Management & Safety", True, 2,
     ["state footer", "rezero", "end of session", "OOC: Verify state", "OOC: Rebuild state", "OOC: Reset state"]),
    ("ENERGON_CONDITION.md", "Energon & Condition", False, 20,
     ["energon", "condition", "damaged", "critical", "offline", "repair", "rest"]),
    ("STAT_GROWTH_DECAY.md", "Stat Growth & Decay", False, 25,
     ["XP", "stat growth", "level up", "spark trauma", "T-Cog"]),
    ("COMBAT_FLOW.md", "Combat Flow", False, 30,
     ["combat", "attack", "fight", "dodge", "firefight", "engagement"]),
    ("CASTING_RULES.md", "Casting Rules", False, 15,
     ["introduce", "arrive", "meets", "cast", "NPC", "core cast"]),
    ("COMBINER_MECHANICS.md", "Combiner Mechanics", False, 40,
     ["combine", "merge", "combiner", "Defensor", "Computron", "Superion", "Bruticus", "Devastator", "Menasor"]),
    ("CASSETTE_PROTOCOL.md", "Cassette Protocol", False, 45,
     ["cassette", "Soundwave", "Ravage", "Laserbeak", "Rumble", "Frenzy", "eject", "recall"]),
    ("GOLDEN_ERA.md", "Golden Era Special Conditions", False, 50,
     ["Golden Era", "Facade", "Prime Approval", "Quintesson", "caste"]),
    ("CYBERTRON_WAR.md", "Cybertron War Special Conditions", False, 50,
     ["Cybertron War", "Civil War", "energon scarcity", "Iacon"]),
    ("WAR_ON_EARTH.md", "War on Earth Special Conditions", False, 50,
     ["War on Earth", "Heat", "human", "Earth", "safe house", "exposure"]),
]

def extract_content(text: str) -> str:
    m = re.search(r"```(?:text)?\n(.*?)```", text, re.S)
    if m:
        return m.group(1).strip()
    lines = text.splitlines()
    while lines and (lines[0].startswith("#") or not lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines).strip()

def make_entry(uid, comment, content, keys, constant, order):
    return {
        "uid": uid,
        "key": keys,
        "keysecondary": [],
        "comment": comment,
        "content": content,
        "constant": constant,
        "vectorized": False,
        "selective": False,
        "selectiveLogic": 0,
        "addMemo": True,
        "order": order,
        "position": 0,
        "disable": False,
        "excludeRecursion": False,
        "probability": 100,
        "useProbability": False,
        "depth": 4,
        "group": "",
        "groupOverride": False,
        "groupWeight": 100,
        "scanDepth": None,
        "caseSensitive": False,
        "matchWholeWords": False,
        "useGroupScoring": False,
        "automationId": "",
        "role": None,
        "displayIndex": uid,
    }

entries = {}
for i, (fname, comment, constant, order, keys) in enumerate(MANIFEST):
    path = CORE / fname
    if not path.exists():
        raise SystemExit(f"Missing {path}")
    content = extract_content(path.read_text(encoding="utf-8"))
    entries[str(i)] = make_entry(i, comment, content, keys, constant, order)

lorebook = {
    "name": "Forged by Primus — Core Systems",
    "description": "Portfolio package: orchestrator, state integrity, casting, combat, eras, multi-body protocols. All Rights Reserved. Personal/educational review only. Unofficial non-commercial Transformers fan/portfolio work.",
    "scan_depth": 4,
    "token_budget": 2048,
    "recursive_scanning": False,
    "extensions": {},
    "entries": entries,
}

OUT.write_text(json.dumps(lorebook, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {OUT} with {len(entries)} entries")
