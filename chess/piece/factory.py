from typing import TypeVar

from chess.color import Color
from chess.factory import AbstractFactory
from chess.piece.data import PieceData, T
from chess.position import Position


class PieceFactory(AbstractFactory[T]):
    data_type: T = PieceData

    @classmethod
    def create(cls,
               position: Position,
               color: Color,
               has_moved=False,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            position=position,
            color=color,
            has_moved=has_moved,
        )


F = TypeVar('F', bound=PieceFactory)

