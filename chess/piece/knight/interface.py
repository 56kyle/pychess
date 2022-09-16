from abc import ABC
from typing import Set

from chess.color import Color
from chess.piece.interface import Piece
from chess.piece.knight.data import KnightData, T
from chess.piece.knight.factory import KnightFactory, F
from chess.piece.knight.validator import KnightValidator, V
from chess.position import Position


class Knight(Piece[T, F, V], ABC):
    factory: F = KnightFactory[T]
    validator: V = KnightValidator[T]

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



