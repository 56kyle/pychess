
from typing import TypeVar

from chess.move.castle.data import CastleData, T
from chess.move.validator import MoveValidator


class CastleValidator(MoveValidator[T]):
    @classmethod
    def _validate_data(cls, data: T):
        pass


V = TypeVar('V', bound=CastleValidator)

