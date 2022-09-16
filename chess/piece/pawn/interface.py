from abc import ABC
from typing import Set

from chess.color import Color
from chess.piece.interface import Piece
from chess.piece.pawn.data import PawnData, T
from chess.piece.pawn.factory import PawnFactory, F
from chess.piece.pawn.validator import PawnValidator, V
from chess.position import Position


class Pawn(Piece[T, F, V], ABC):
    factory: F = PawnFactory[T]
    validator: V = PawnValidator[T]

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



