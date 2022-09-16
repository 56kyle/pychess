from abc import ABC
from typing import Set

from chess.color import Color
from chess.piece.interface import Piece
from chess.piece.king.data import KingData, T
from chess.piece.king.factory import KingFactory, F
from chess.piece.king.validator import KingValidator, V
from chess.position import Position


class King(Piece[T, F, V], ABC):
    factory: F = KingFactory[T]
    validator: V = KingValidator[T]

    def __init__(self,
                 position: Position,
                 color: Color,
                 *args,
                 **kwargs):
        super().__init__(
            position=position,
            color=color,
            *args,
            **kwargs
        )



