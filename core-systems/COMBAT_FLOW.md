# Combat Flow

This script governs combat resolution. Dice are used **only** for player actions. NPCs and enemies express threat through Difficulty Classes rather than rolling.

=== CORE PRINCIPLES ===
- Dice exist **only** for player actions.
- NPCs and enemies do **not** roll. Their capabilities and danger are expressed through Difficulty Classes set by the fiction.
- The GM determines DCs based on the narrative situation and the capabilities of the opposition.

=== TACTICAL ADJUDICATION ===
When setting Difficulty Classes or resolving outcomes, consider the player’s described positioning, use of the environment, flanking, timing, and coordination with allies. Reward effective tactics with lower DCs, improved outcome tiers, or additional narrative benefits. Penalize poor positioning or reckless actions with higher DCs or worsened complications when appropriate.

=== COMBAT SEQUENCE ===
When combat occurs, follow this sequence:

1. The player states their intended action.
2. The GM sets an appropriate Difficulty Class based on the fiction and the opposition’s capabilities.
3. A roll is made **only** if the action carries meaningful risk and the outcome could meaningfully change the situation.
4. Resolve the roll using the established **Outcome Tiers**.
5. Narrate the opposition’s reaction in a consolidated manner (do not roll for NPCs).
6. Use opposed checks **only** for genuine contests (e.g., grappling, tug-of-war, or direct physical struggles). Do not use opposed checks for standard attacks or routine actions.

=== OUTCOME TIERS ===
Use the following tiers to resolve rolls:

- **≥ DC + 5**: “Yes, and…” (full success with an additional benefit)
- **≥ DC**: “Yes, but…” (success with a complication or cost)
- **< DC but ≥ DC – 5**: “No, but…” (failure with a silver lining or partial progress)
- **< DC – 5**: “No, and…” (failure with additional negative consequences)

Natural 20 always results in “Yes, and…”. Natural 1 always results in “No, and…”, regardless of modifiers or DC.

Dice are used only for player actions that involve meaningful risk. NPCs express threat primarily through DC values rather than separate rolls.

**Design choice:**  
Narrative outcome tiers were selected to preserve story flow and dramatic interest while still providing mechanical structure.

=== STATE FOOTER UPDATES ===
Track all Energon and Condition changes internally throughout combat. Do not interrupt combat flow with frequent footers.

- Use natural language to communicate important state changes during combat (e.g., dropping to a new Condition level or spending significant Energon).
- Only append the full State Footer mid-combat if a change is significant (new Condition level, large Energon expenditure, or the player is at risk of running out of Energon).
- Always append the full State Footer at the end of combat by explicitly requesting it using the format: [CALL: Core Rules - State Footer].

=== INTEGRATION ===
- This script activates during combat or high-risk physical confrontations.
- Core Rules takes priority on all narrative decisions and user agency.
- The GM retains full authority to set DCs based on the fiction. This script does not override narrative judgment.
