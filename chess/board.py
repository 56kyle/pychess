

from .board_state import BoardState
from .board_validator import BoardValidator


class Board:
    def __init__(self, board_state: BoardState, validator: BoardValidator):
        self._current_state: BoardState = board_state
        self._validator: BoardValidator = validator
        self._validator.validate(self._current_state)

    def get_state(self) -> BoardState:
        return self._current_state











