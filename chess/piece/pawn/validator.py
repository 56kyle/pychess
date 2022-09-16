from abc import ABC
from typing import TypeVar

from chess.piece.pawn.data import PawnData, T
from chess.position import Position
from chess.piece.validator import PieceValidator


class PawnValidator(PieceValidator[T], ABC):
    @classmethod
    def _validate_data(cls, data: T):
        cls._validate_position(data.position)


V = TypeVar('V', bound=PawnValidator)

