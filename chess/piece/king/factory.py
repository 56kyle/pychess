from typing import TypeVar

from chess.color import Color
from chess.piece.factory import PieceFactory
from chess.piece.king.data import T, KingData
from chess.position import Position


class KingFactory(PieceFactory[T]):
    data_type: T = KingData

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


F = TypeVar('F', bound=KingFactory)

