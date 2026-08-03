from src.parser import GameState


def test_game_state_parsing():
    obs = {
        "player_id": 0,
        "players": [
            {"active_pokemon": "Pikachu", "hand": ["Lightning Energy", "Potion"]},
            {"active_pokemon": "Squirtle", "hand": ["Water Energy"]},
        ],
    }

    state = GameState(obs)

    assert state.player_id == 0
    assert state.active_pokemon == "Pikachu"
    assert state.hand == ["Lightning Energy", "Potion"]
    assert state.opponent_state["active_pokemon"] == "Squirtle"


def test_game_state_missing_data():
    obs = {}
    state = GameState(obs)

    assert state.player_id == 0
    assert state.active_pokemon is None
    assert state.hand == []
    assert state.opponent_state == {}
