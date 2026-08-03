from src.agent import agent

def test_dummy_agent():
    """
    Ensure the dummy agent returns 'PASS' given empty mock dicts.
    """
    mock_observation = {}
    mock_configuration = {}
    
    action = agent(mock_observation, mock_configuration)
    assert action == "PASS"
