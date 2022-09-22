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

    movement_paths: Set[Path] = {
        Path(offset=UP_LEFT),
        Path(offset=UP_RIGHT),
        Path(offset=DOWN_RIGHT),
        Path(offset=DOWN_LEFT),
    }
    capture_paths: Set[Path] = movement_paths

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






