from abc import ABC
from typing import Set

from chess.color import Color
from chess.offset import UP_LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT
from chess.path import Path
from chess.piece.interface import Piece
from chess.piece.bishop.data import BishopData, T
from chess.piece.bishop.factory import BishopFactory, F
from chess.piece.bishop.validator import BishopValidator, V
from chess.position import Position


class Bishop(Piece[T, F, V], ABC):
    factory: F = BishopFactory[T]
    validator: V = BishopValidator[T]

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






