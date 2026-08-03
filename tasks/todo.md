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
- [x] `tests/test_agent.py` exists.
- [x] Test passes when running `pytest tests/`.
**Verification:**
- [x] Tests pass: `pytest tests/`
**Dependencies:** Task 1
**Files likely touched:** `tests/test_agent.py`
**Estimated scope:** Small

## Task 3: Implement State Parser
**Description:** Build helper functions to parse Kaggle `observation` dicts.
**Acceptance criteria:**
- [x] `src/parser.py` (or similar) created.
- [x] Unit tests for parsing logic exist and pass.
**Verification:**
- [x] Run `pytest tests/test_parser.py`
**Dependencies:** Task 1, Task 2
**Files likely touched:** `src/parser.py`, `tests/test_parser.py`
**Estimated scope:** Medium

## Task 4: Implement Rule-based Action Selection
**Description:** Replace the dummy "PASS" logic with a simple heuristic decision tree (Attack > Attach Energy > Pass).
**Acceptance criteria:**
- [x] Agent returns valid attack actions when possible.
- [x] Agent returns valid attach energy actions when possible.
- [x] Agent defaults to "PASS".
**Verification:**
- [x] Build succeeds: `uvx google-agents-cli lint` (Skipped due to ty external error, tests passed)
**Dependencies:** Task 3
**Files likely touched:** `src/agent.py`
**Estimated scope:** Medium

## Task 5: Test Logic Branches
**Description:** Write unit tests simulating different board states to ensure the heuristic logic triggers in the correct priority order.
**Acceptance criteria:**
- [x] Test covers the attack branch.
- [x] Test covers the energy attachment branch.
- [x] Test covers the fallback pass branch.
**Verification:**
- [x] Tests pass: `pytest tests/`
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
