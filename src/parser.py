from typing import Any


class GameState:
    """
    Parses the observation dictionary from the Kaggle environment
    into a more easily usable format.
    """

    def __init__(self, observation: dict[str, Any]):
        self.observation = observation
        self.player_id = observation.get("player_id", 0)
        self.players = observation.get("players", [])

    @property
    def my_state(self) -> dict[str, Any]:
        if len(self.players) > self.player_id:
            return self.players[self.player_id]
        return {}

    @property
    def opponent_state(self) -> dict[str, Any]:
        opponent_id = 1 - self.player_id
        if len(self.players) > opponent_id:
            return self.players[opponent_id]
        return {}

    @property
    def active_pokemon(self) -> str | None:
        return self.my_state.get("active_pokemon")

    @property
    def hand(self) -> list:
        return self.my_state.get("hand", [])
