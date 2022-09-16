from abc import ABC
from typing import Set

from chess.color import Color
from chess.piece.interface import Piece
from chess.piece.queen.data import QueenData, T
from chess.piece.queen.factory import QueenFactory, F
from chess.piece.queen.validator import QueenValidator, V
from chess.position import Position


class Queen(Piece[T, F, V], ABC):
    factory: F = QueenFactory[T]
    validator: V = QueenValidator[T]

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



