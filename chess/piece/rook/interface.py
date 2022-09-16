from abc import ABC
from typing import Set

from chess.color import Color
from chess.piece.interface import Piece
from chess.piece.rook.data import RookData, T
from chess.piece.rook.factory import RookFactory, F
from chess.piece.rook.validator import RookValidator, V
from chess.position import Position


class Rook(Piece[T, F, V], ABC):
    factory: F = RookFactory[T]
    validator: V = RookValidator[T]

    def __init__(self,
                 position: Position,
                 color: Color,
                 has_moved: bool = False,
                 *args,
                 **kwargs):
        super().__init__(
            position=position,
            color=color,
            has_moved=has_moved,
            *args,
            **kwargs
        )



