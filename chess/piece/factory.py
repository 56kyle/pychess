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
               name: str = '',
               letter: str = '',
               value: int = 0,
               symbol: str = '',
               html_decimal: str = '',
               html_hex: str = '',
               has_moved=False,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            position=position,
            color=color,
            name=name,
            letter=letter,
            value=value,
            symbol=symbol,
            html_decimal=html_decimal,
            html_hex=html_hex,
            has_moved=has_moved,
        )


F = TypeVar('F', bound=PieceFactory)

