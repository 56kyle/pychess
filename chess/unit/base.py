

from abc import ABC, abstractmethod

from typing import Set

from chess.color import Color
from chess.piece import ChessPiece
from chess.movement import Movement


class Unit(ChessPiece, ABC):
    color: Color
    movements: Set[Movement]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_moved = False


