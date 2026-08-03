## Task 1: Scaffold Project Structure
## Task 1: Scaffold Project Structure
**Description:** Initialize the basic directory structure (`src/`, `tests/`) and create the entry point `src/agent.py` containing a dummy agent that always returns a "PASS" action.
**Acceptance criteria:**
- [x] `src/agent.py` exists with a function matching Kaggle's agent signature.
- [x] `tests/` directory exists.
**Verification:**
- [x] Manual check: Files exist.
**Dependencies:** None
**Files likely touched:** `src/agent.py`
**Estimated scope:** Small

## Task 2: Setup Testing Harness
**Description:** Set up `pytest` and write a baseline unit test for the dummy agent to ensure it can receive a mock state and return a valid action.
**Acceptance criteria:**
- [ ] `tests/test_agent.py` exists.
- [ ] Test passes when running `pytest tests/`.
**Verification:**
- [ ] Tests pass: `pytest tests/`
**Dependencies:** Task 1
**Files likely touched:** `tests/test_agent.py`
**Estimated scope:** Small

## Task 3: Implement State Parser
**Description:** Create helper functions to safely parse the `observation` dictionary provided by the Kaggle `cabt` engine, abstracting away the complexity.
**Acceptance criteria:**
- [ ] Functions exist to get the active Pokémon, hand, and energy.
- [ ] Functions do not throw KeyErrors on missing data.
**Verification:**
- [ ] Tests pass: `pytest tests/`
**Dependencies:** Task 1, Task 2
**Files likely touched:** `src/parser.py`, `tests/test_parser.py`
**Estimated scope:** Medium

## Task 4: Implement Rule-based Action Selection
**Description:** Replace the dummy "PASS" logic with a simple heuristic decision tree (Attack > Attach Energy > Pass).
**Acceptance criteria:**
- [ ] Agent returns valid attack actions when possible.
- [ ] Agent returns valid attach energy actions when possible.
- [ ] Agent defaults to "PASS".
**Verification:**
- [ ] Build succeeds: `uvx google-agents-cli lint`
**Dependencies:** Task 3
**Files likely touched:** `src/agent.py`
**Estimated scope:** Medium

## Task 5: Test Logic Branches
**Description:** Write unit tests simulating different board states to ensure the heuristic logic triggers in the correct priority order.
**Acceptance criteria:**
- [ ] Test covers the attack branch.
- [ ] Test covers the energy attachment branch.
- [ ] Test covers the fallback pass branch.
**Verification:**
- [ ] Tests pass: `pytest tests/`
**Dependencies:** Task 4
**Files likely touched:** `tests/test_agent.py`
**Estimated scope:** Small

## Task 6: Local Mock Match Execution
**Description:** Create a runner script to execute a full match using `kaggle-environments` against a random baseline agent.
**Acceptance criteria:**
- [ ] `src/run_match.py` exists.
- [ ] Script successfully plays a match to completion without agent crashes.
**Verification:**
- [ ] Manual check: Run `python -m src.run_match` and observe a completed match.
**Dependencies:** Task 4, Task 5
**Files likely touched:** `src/run_match.py`
**Estimated scope:** Medium

## Task 7: Draft Strategy Report
**Description:** Write the required Kaggle Writeup detailing the non-ML, simple heuristic approach.
**Acceptance criteria:**
- [ ] `docs/strategy_report.md` exists and is ~2000 words (or extensively detailed).
- [ ] Explains logic clearly without assuming ML knowledge.
**Verification:**
- [ ] Manual check: Read document for clarity.
**Dependencies:** Task 4
**Files likely touched:** `docs/strategy_report.md`
**Estimated scope:** Large
