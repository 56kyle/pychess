from typing import TypeVar

from chess.color import Color
from chess.piece.factory import PieceFactory
from chess.piece.knight.data import T, KnightData
from chess.position import Position


class KnightFactory(PieceFactory[T]):
    data_type: T = KnightData

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


F = TypeVar('F', bound=KnightFactory)

