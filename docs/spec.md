# Spec: Pokémon TCG AI Battle Challenge

## Objective
Build a functional, competitive AI agent to play the Pokémon TCG on the `cabt` Engine for the Kaggle Simulation Category, and produce a 2000-word writeup detailing the strategy for the Strategy Category. Success means the agent successfully handles imperfect information and the writeup clearly communicates the technical and strategic logic to the judges.

## Tech Stack
- **Simulation Agent**: Python, `kaggle-environments` (cabt Engine), ADK 2.0
- **Libraries**: Standard library and heuristic logic preferred. ML libraries (e.g., PyTorch, scikit-learn) may be used *only* if strictly necessary to build the best possible agent, provided they are implemented cleanly and properly documented.
- **Scaffolding & Tools**: `google-agents-cli` for project setup and linting
- **Strategy Report**: Markdown (to be submitted as a Kaggle Writeup)
- **Frontend / UI**: Angular v21 (Optional, deferred until core simulation is stable)
- **Version Control**: Git / GitHub

## Commands
*Commands rely on the `google-agents-cli` for core ADK workflows:*
- Setup Project & Auth: `uvx google-agents-cli setup`
- Lint Agent Logic: `uvx google-agents-cli lint`
- Run local simulation: `python -m src.run_match`
- Test agent logic: `pytest tests/`
- Lint Python code: `flake8 src/` or `ruff check src/`
- Build/Serve optional UI: `ng serve` (if Angular is added)

## Project Structure
```
docs/           → Specifications, strategy reports, and intent documents
src/            → Python source code for the AI agent (using ADK 2.0)
src/agent.py    → Main entry point for the Kaggle submission
tests/          → Unit tests for agent logic and deck consistency
ui/             → (Optional) Angular v21 application for visualization
skills/         → Submodules and workflow skills (e.g., code-review-graph)
```

## Code Style
```python
# Naming conventions: snake_case for variables/functions, PascalCase for classes
# Type hinting is required for all function signatures.

from typing import Dict, Any

class TCGStrategyAgent:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def choose_action(self, observation: Dict[str, Any]) -> str:
        """
        Determines the next move based on the current board state and hidden information probabilities.
        """
        return "PASS"
```

## Testing Strategy
- **Framework**: `pytest` for Python logic.
- **Coverage**: Focus heavily on testing deterministic mechanics (damage calculation, win/loss state recognition) and probabilistic decision trees.
- **Test Locations**: All tests live in the `tests/` directory mirroring the `src/` structure.
- **Levels**: Unit tests for individual logic functions; integration tests running full mock matches against a random agent baseline.

## Boundaries
- **Always**: Type-hint Python code, write tests for core logic branches, document strategic choices in `docs/` as they are made, and keep all documents in the `docs/` folder. Use `google-agents-cli` for ADK 2.0 initialization and validation. Keep logic as simple and accessible as possible, even if ML is introduced.
- **Ask first**: Before adding large external dependencies (Kaggle limits what can be imported without internet access), or before starting the Angular UI implementation.
- **Never**: Introduce unnecessary complexity. Never hardcode assumptions about the opponent's deck composition unless running a specific meta-counter hypothesis.

## Success Criteria
- Agent can play a full game on the `cabt` Engine without crashing or throwing invalid action errors.
- Agent maintains a win rate > 50% against a baseline random agent, whether using heuristics or an ML model.
- A draft of the 2000-word Strategy Report is completed in `docs/`, covering model logic, deck construction, and hypothesis testing.

## Open Questions
- If we do introduce an ML model later, what architecture will best handle the state space of the Pokémon TCG within Kaggle's limits?
