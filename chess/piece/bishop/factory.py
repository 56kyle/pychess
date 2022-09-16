from typing import TypeVar

from chess.color import Color
from chess.piece.factory import PieceFactory
from chess.piece.bishop.data import T, BishopData
from chess.position import Position


class BishopFactory(PieceFactory[T]):
    data_type: T = BishopData

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


F = TypeVar('F', bound=BishopFactory)

