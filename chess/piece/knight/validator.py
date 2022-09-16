from abc import ABC
from typing import TypeVar

from chess.piece.knight.data import KnightData, T
from chess.position import Position
from chess.piece.validator import PieceValidator


class KnightValidator(PieceValidator[T], ABC):
    @classmethod
    def _validate_data(cls, data: T):
        cls._validate_position(data.position)


V = TypeVar('V', bound=KnightValidator)

