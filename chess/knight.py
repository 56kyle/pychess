
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.offset import Offset, UP, RIGHT, DOWN, LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT
from chess.path import Path
from chess.piece import Piece


class Knight(Piece):
    name: str = 'Knight'
    letter: str = 'N'
    value: int = 3
    symbol: str = '\u2658'
    html_decimal: str = '&#9822;'
    html_hex: str = '&#x2658;'
    offsets: Set[Offset] = {
        UP_RIGHT + UP,
        UP_RIGHT + RIGHT,
        DOWN_RIGHT + RIGHT,
        DOWN_RIGHT + DOWN,
        DOWN_LEFT + DOWN,
        DOWN_LEFT + LEFT,
        UP_LEFT + LEFT,
        UP_LEFT + UP,
    }

    @property
    def move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in self.offsets}

    @property
    def capture_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in self.offsets}


