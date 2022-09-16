from typing import TypeVar

from chess.color import Color
from chess.piece.factory import PieceFactory
from chess.piece.queen.data import T, QueenData
from chess.position import Position


class QueenFactory(PieceFactory[T]):
    data_type: T = QueenData

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


F = TypeVar('F', bound=QueenFactory)

