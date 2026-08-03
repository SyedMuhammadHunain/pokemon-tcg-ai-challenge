# Implementation Plan: Pokémon TCG AI Battle Challenge

## Overview
We are building a lightweight, simple Python-based AI agent to compete in the Kaggle Pokémon TCG AI Battle Challenge. The agent will run on the `cabt` Engine using `kaggle-environments`. Because we are constrained to non-ML, simple libraries and must assume no prior domain knowledge of the game, the agent will rely on a straightforward, rule-based heuristic system (e.g., attach energy if possible, attack if possible, otherwise pass). We will also produce a 2000-word Strategy Report explaining this logic.

## Architecture Decisions
- **Framework**: ADK 2.0 / `google-agents-cli` for scaffolding and validation.
- **Logic Design**: Start with a pure heuristic (if-then-else) approach in `src/agent.py` to establish a strong baseline. ML frameworks may be introduced later if they provably create a better, more competitive agent and follow all Kaggle constraints.
- **State Parsing**: We will build helper functions to parse the raw `observation` dictionary from Kaggle into simple, understandable concepts (e.g., `get_active_pokemon()`, `get_hand()`).
- **Testing**: `pytest` for unit testing the logic branches (ensuring the agent doesn't crash on edge cases).

## Task List

### Phase 1: Foundation
- [ ] **Task 1: Scaffold Project Structure**
  - Use ADK 2.0 / `google-agents-cli` or manually create `src/` and `tests/` directories. Create the initial `src/agent.py` with a dummy agent that always returns "PASS".
- [ ] **Task 2: Setup Testing Harness**
  - Create `tests/test_agent.py`. Write a basic test passing a mock observation state to the agent and asserting it returns a valid action.

### Checkpoint: Foundation
- [ ] `pytest tests/` runs successfully.
- [ ] `uvx google-agents-cli lint` passes on the codebase.

### Phase 2: Core Features (Simple Heuristics)
- [ ] **Task 3: Implement State Parser**
  - Add functions to safely extract data from the Kaggle `observation` (e.g., current active Pokémon, cards in hand, available energy).
- [ ] **Task 4: Implement Rule-based Action Selection**
  - Replace the "PASS" dummy logic with sequential heuristic checks: 
    1. If a winning attack is available, use it.
    2. If an energy card can be attached to the active Pokémon, attach it.
    3. If a regular attack is available, use it.
    4. Otherwise, PASS.
- [ ] **Task 5: Test Logic Branches**
  - Write unit tests in `tests/test_agent.py` simulating specific board states to verify the heuristics fire in the correct priority order.

### Checkpoint: Core Features
- [ ] Agent correctly attaches energy and attacks in unit tests.
- [ ] All tests pass and linting is clean.

### Phase 3: Integration & Polish
- [ ] **Task 6: Local Mock Match Execution**
  - Create a script (e.g., `src/run_match.py`) to run a full simulation match against a random agent using `kaggle-environments` locally. Verify the agent doesn't crash mid-game.
- [ ] **Task 7: Draft Strategy Report**
  - Write the `docs/strategy_report.md` covering the heuristic logic, how we handle lack of game knowledge, and why the simple rule-based system is robust.

### Checkpoint: Complete
- [ ] Agent can complete a full local match without crashing.
- [ ] Strategy report is drafted and ready for review.

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| Complex Kaggle state dict | High | Write robust parser functions with defensive checks (e.g., `dict.get()`) to avoid KeyErrors. |
| Agent gets stuck in invalid action loop | High | Always fallback to "PASS" if heuristic rules fail or error out. |
| Unforeseen game mechanics | Medium | Since we lack domain knowledge, we will stick to the absolute simplest mechanics (attack, attach energy) and ignore complex card abilities unless specifically requested. |

## Open Questions
- None at this time.
