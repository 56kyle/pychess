from abc import ABC
from typing import TypeVar

from chess.piece.bishop.data import BishopData, T
from chess.position import Position
from chess.piece.validator import PieceValidator


class BishopValidator(PieceValidator[T], ABC):
    @classmethod
    def _validate_data(cls, data: T):
        cls._validate_position(data.position)


V = TypeVar('V', bound=BishopValidator)

