from abc import ABC
from typing import Set

from chess.color import Color
from chess.offset import UP, RIGHT, DOWN, LEFT, UP_LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, ALL, HORIZONTAL
from chess.path import Path
from chess.piece.interface import Piece
from chess.piece.king.data import KingData, T
from chess.piece.king.factory import KingFactory, F
from chess.piece.king.validator import KingValidator, V
from chess.position import Position


class King(Piece[T, F, V], ABC):
    factory: F = KingFactory[T]
    validator: V = KingValidator[T]

    castling_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in HORIZONTAL}
    standard_movement_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in ALL}
    movement_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in ALL} | castling_paths
    capture_paths: Set[Path] = standard_movement_paths

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



