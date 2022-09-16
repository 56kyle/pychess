from typing import TypeVar

from chess.color import Color
from chess.piece.factory import PieceFactory
from chess.piece.rook.data import T, RookData
from chess.position import Position


class RookFactory(PieceFactory[T]):
    data_type: T = RookData

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


F = TypeVar('F', bound=RookFactory)

