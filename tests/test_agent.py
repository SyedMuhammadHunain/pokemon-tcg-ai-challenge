from src.agent import agent


def test_agent_initialization():
    """Step 0 should return a default deck."""
    obs = {"step": 0}
    action = agent(obs, {})
    assert len(action) == 60
    assert 721 in action
    assert 1092 in action


def test_agent_attack_priority():
    """Agent should prioritize attack (type 13) over attach (type 8) and pass (type 14)."""
    obs = {
        "step": 1,
        "select": {
            "option": [
                {"type": 14},
                {"type": 8, "area": 2},
                {"type": 13, "attackId": 1046}
            ]
        }
    }
    action = agent(obs, {})
    assert action == [2]  # Index of type 13


def test_agent_attach_priority():
    """Agent should prioritize attach (type 8) over pass (type 14) if no attack."""
    obs = {
        "step": 1,
        "select": {
            "option": [
                {"type": 14},
                {"type": 8, "area": 2}
            ]
        }
    }
    action = agent(obs, {})
    assert action == [1]  # Index of type 8


def test_agent_pass_fallback():
    """Agent should fallback to pass (type 14) if no better option."""
    obs = {
        "step": 1,
        "select": {
            "option": [
                {"type": 7, "index": 0},
                {"type": 14}
            ]
        }
    }
    action = agent(obs, {})
    assert action == [1]  # Index of type 14


def test_agent_empty_fallback():
    """Agent should return [0] if no known types, and [] if no options."""
    obs_options = {"step": 1, "select": {"option": [{"type": 99}]}}
    assert agent(obs_options, {}) == [0]

    obs_no_options = {"step": 1, "select": {"option": []}}
    assert agent(obs_no_options, {}) == []

    obs_no_select = {"step": 1}
    assert agent(obs_no_select, {}) == []
