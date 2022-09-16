from typing import TypeVar

from chess.color import Color
from chess.piece.factory import PieceFactory
from chess.piece.pawn.data import T, PawnData
from chess.position import Position


class PawnFactory(PieceFactory[T]):
    data_type: T = PawnData

    @classmethod
    def create(cls,
               position: Position,
               color: Color,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            position=position,
            color=color,
            **kwargs,
        )


F = TypeVar('F', bound=PawnFactory)

