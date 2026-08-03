from typing import List, Any


def agent(observation: dict, configuration: dict) -> List[Any]:
    """
    Agent for the Pokémon TCG AI Battle Challenge.
    Parses the options and applies a heuristic decision tree:
    1. Submit deck at Step 0.
    2. Attack (type 13)
    3. Attach Energy (type 8)
    4. Pass (type 14)
    5. Default to [0] if no known types, or [] if no options.
    """
    step = observation.get("step")

    # Step 0: initialization, return a default valid deck
    if step == 0:
        return [
            721, 721, 722, 722, 722, 722, 723, 723, 723, 723, 
            1092, 1121, 1121, 1145, 1145, 1163, 1163, 1219, 1219, 1219, 
            1219, 1227, 1227, 1227, 1227, 1262, 1262, 3, 3, 3, 
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
        ]

    select = observation.get("select")
    if not select:
        return []

    options = select.get("option")
    if not options:
        return []

    # Map options to indices
    options_by_type = {}
    for idx, opt in enumerate(options):
        opt_type = opt.get("type")
        if opt_type not in options_by_type:
            options_by_type[opt_type] = []
        options_by_type[opt_type].append(idx)

    # Heuristic 1: Attack
    if 13 in options_by_type:
        return [options_by_type[13][0]]

    # Heuristic 2: Attach Energy
    if 8 in options_by_type:
        return [options_by_type[8][0]]

    # Heuristic 3: Pass
    if 14 in options_by_type:
        return [options_by_type[14][0]]

    # Fallback to the first available option
    return [0]
