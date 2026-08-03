# Pokémon TCG AI Battle Challenge: Heuristic Strategy Report

## 1. Introduction

The Pokémon TCG AI Battle Challenge on Kaggle, powered by the bespoke `cabt` engine developed by the University of Tokyo's Matsuo Institute, represents a fascinating intersection of combinatorial complexity, imperfect information, and turn-based strategic decision-making. The goal of this challenge is not simply to develop an agent that follows the rules of the Pokémon Trading Card Game (TCG), but to build one that makes optimal or near-optimal decisions given a hidden game state and a mathematically vast action space.

Our approach explicitly bypasses the temptation to dive headfirst into complex Machine Learning (ML) or Deep Reinforcement Learning (DRL) algorithms right away. Instead, we recognized that the structural complexity of a TCG requires a stable, interpretable, and mathematically sound heuristic baseline. We sought to answer a fundamental question: **How far can a rigid, rule-based decision tree go against a random baseline, and what architectural lessons does it teach us for subsequent ML integrations?**

This report details the theoretical foundation, implementation strategy, deck construction philosophy, and future trajectory of our initial heuristic agent.

---

## 2. Architectural Philosophy: Why Heuristics First?

In many Kaggle simulation challenges (such as Halite or Lux AI), participants often rush to train reinforcement learning agents (e.g., Proximal Policy Optimization) before understanding the nuances of the game mechanics. This frequently leads to "black-box" agents that learn local optima—such as moving back and forth aimlessly—rather than engaging with the core objective of the game.

The Pokémon TCG exacerbates this problem. The state space includes not just the board (Active Pokémon, Bench, Discard Pile), but also the player's Hand, the deck composition, and the hidden state of the opponent's Hand and Prize cards. A random agent will almost always execute illegal or sub-optimal moves. An ML agent trained against a random agent will simply learn how to not lose by invalid moves, rather than how to win through strategic play.

By building a deterministic heuristic agent first, we achieve three critical milestones:
1. **A Reliable Baseline:** We establish a benchmark win rate that any future ML model must surpass to justify its complexity.
2. **State Space Parsing Validation:** We verify our understanding of the `cabt` engine's observation structures, specifically the complex array-based action formatting and `select.option` API.
3. **Behavioral Logging:** A heuristic agent generates predictable, high-quality match logs that can later be used for imitation learning (Behavioral Cloning).

---

## 3. The `cabt` Engine API and Action Mapping

To implement a heuristic agent, one must first decode the complex observation schema provided by the `cabt` engine. Unlike simpler environments where actions are discrete strings (e.g., "UP", "DOWN", "ATTACK"), `cabt` actions are contextual indices representing selections from a dynamically generated list of valid options at any given step.

At each step where a decision is required, the engine provides a `select` object containing an `option` array. Each option contains a `type` ID, mapped internally by the engine to specific mechanics:

- **Type 13 (Attack):** The agent declares an attack using an `attackId`.
- **Type 8 (Attach Energy):** The agent takes an energy card from the hand and attaches it to a Pokémon in play.
- **Type 14 (Pass):** The agent ends its turn or declines an optional action.

Our implementation maps the provided options to their indices and selects the index corresponding to the most advantageous action type available on that step.

---

## 4. The Decision Tree Logic

Our current heuristic agent utilizes a strict, top-down priority queue for decision making. When presented with a list of valid options, it evaluates them against the following decision tree:

### Priority 1: Offensive Action (Attack - Type 13)
The ultimate objective in the Pokémon TCG is to take all Prize cards by Knocking Out the opponent's Pokémon. Therefore, if a valid attack is available, it is always the optimal move in a vacuum. The agent scans the `options` array for any object with `type == 13`. If found, it immediately returns the index of this option. 

*Strategic limitation:* This logic does not currently evaluate board state context. It will attack even if the attack deals negligible damage while a better setup play is available. However, for a baseline agent, ensuring consistent damage output is paramount.

### Priority 2: Resource Allocation (Attach Energy - Type 8)
Pokémon require Energy cards to use their attacks. If the agent cannot attack (either because it is the first turn, or the Active Pokémon lacks sufficient energy), the next most important action is to attach energy. The agent scans for `type == 8`.

*Strategic limitation:* The agent currently attaches energy to the first valid target it finds, which may not be the optimal attacker. Advanced heuristics will require evaluating the energy cost of attacks versus the current energy attached to each Pokémon.

### Priority 3: Board Development (Play Cards - Type 7/10)
While not yet explicitly prioritized in the current build, playing Supporter cards, Item cards, and placing Basic Pokémon onto the bench are the next logical steps in the hierarchy. Currently, these are handled by the fallback mechanism, but future iterations will isolate them to prioritize card draw engines (e.g., Professor's Research) over minor board adjustments.

### Priority 4: Pass / End Turn (Type 14)
If no proactive moves are available, the agent must gracefully end its turn. Attempting to force an invalid action will result in an immediate `INVALID` status, forfeiting the match. The agent scans for `type == 14` and selects it, ensuring the match continues smoothly.

### Fallback: Safe Default
In the rare event that the `select` options do not contain any of our explicitly mapped heuristics (e.g., forced discarding, prize card selection, or complex card effects), the agent defaults to selecting the first available option `[0]`. This guarantees the agent never crashes due to an empty response when an action is mandated.

---

## 5. Deck Construction Strategy

In the `cabt` engine, the deck is submitted at `step == 0` as an array of 60 integers representing card IDs. 

For our baseline agent, we reverse-engineered a valid 60-card deck structure from the engine's default random agent. This ensures our deck passes the engine's strict validation rules (e.g., containing at least one Basic Pokémon, adhering to the 4-card copy limit for non-basic energy). 

The deck is heavily skewed toward consistency:
- **High Basic Pokémon Count:** Minimizes the risk of "mulligans" (starting the game without a Basic Pokémon in hand).
- **High Energy Density:** Ensures the heuristic agent's Priority 2 (Attach Energy) triggers consistently every turn, enabling rapid deployment of attacks.

*Future Deck Enhancements:* Once the heuristic logic is expanded to differentiate between specific card IDs, we will transition to a targeted meta-deck (e.g., a high-aggro deck utilizing low-energy attacks) that perfectly synergizes with a rigid decision tree.

---

## 6. Local Testing and Validation Framework

A core tenant of our development process is the "Incremental Implementation" methodology. Before executing matches on the Kaggle servers, we established a robust local testing harness.

1. **Unit Testing (`pytest`):** We built deterministic tests to mock the `cabt` observation dictionary. By injecting mocked `select.option` arrays containing different combinations of Attack, Attach Energy, and Pass types, we computationally verified that the agent consistently returns the correct index according to our priority queue.
2. **Integration Testing (`run_match.py`):** We created a local runner script utilizing `kaggle_environments.make("cabt")`. This script executes a full match between our heuristic agent and a random baseline agent. 

Our integration tests prove that the agent successfully navigates the complex API without throwing `INVALID` actions, meaning the parsing engine successfully translates our heuristic priorities into valid engine commands.

---

## 7. Next Steps: Evolving the Baseline

With a stable, non-crashing baseline established, we have a foundation to iterate upon. The evolution of this agent will occur in three distinct phases:

### Phase A: Context-Aware Heuristics
The immediate next step is to expand the parser to evaluate the board state (`obs["current"]`) rather than just the action types. 
- **Target Selection:** Instead of attacking randomly, the agent will calculate exact damage output and select attacks that result in a Knock Out.
- **Energy Optimization:** The agent will prioritize attaching energy to the Active Pokémon until its best attack is powered up, and then funnel remaining energy to a designated "sweeper" on the Bench.

### Phase B: Game Tree Search algorithms
Because the TCG involves hidden information, traditional Minimax algorithms fall short. We plan to implement **Information Set Monte Carlo Tree Search (IS-MCTS)**. By sampling random permutations of the opponent's hidden hand and deck, the agent can simulate thousands of turns ahead and select the action that yields the highest expected win probability across all possible hidden states.

### Phase C: Reinforcement Learning Integration
Once we have pushed heuristics and IS-MCTS to their computational limits (constrained by Kaggle's timeout rules), we will use the heuristic agent to generate massive datasets of high-level play. We will then train a Neural Network to predict the expected value (Value Network) of board states, replacing the expensive rollout phase of MCTS with a near-instantaneous neural evaluation.

## 8. Conclusion

The Pokémon TCG AI Battle Challenge requires a methodical, layered approach to complexity. By resisting the urge to immediately implement ML, we have built a robust, tested, and strategically sound heuristic agent. This agent correctly interacts with the obscure `cabt` API, never throws invalid actions, and executes a logical priority sequence of attacking and powering up Pokémon. 

This stable baseline is the launchpad. From here, we transition from merely playing the game, to mastering it.
