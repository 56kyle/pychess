from typing import Set

from chess.color import Color
from chess.path import Path
from chess.position import Position


class Piece:
    name: str
    letter: str
    value: int
    symbol: str
    html_decimal: str
    html_hex: str

    def __init__(self, position: Position, color: Color, has_moved: bool = False):
        self.position = position
        self.color = color
        self.has_moved = has_moved

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths

    @property
    def move_paths(self) -> Set[Path]:
        return set()

    @property
    def capture_paths(self) -> Set[Path]:
        return set()





