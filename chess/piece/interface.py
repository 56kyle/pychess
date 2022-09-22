from abc import ABC
from typing import Set

from chess.color import Color
from chess.interface import AbstractInterface
from chess.piece.data import PieceData, T
from chess.piece.factory import PieceFactory, F
from chess.piece.validator import PieceValidator, V
from chess.position import Position


class Piece(AbstractInterface[T, F, V], ABC):
    factory: F = PieceFactory[T]
    validator: V = PieceValidator[T]

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

