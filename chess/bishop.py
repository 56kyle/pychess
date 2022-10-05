
from typing import Set

from chess.offset import DIAGONAL
from chess.path import Path
from chess.piece import Piece


class Bishop(Piece):
    name: str = 'Bishop'
    letter: str = 'B'
    value: int = 3
    symbol: str = '♝'
    html_decimal: str = '&#9821;'
    html_hex: str = '&#x265D;'

    def move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=None) for offset in DIAGONAL}

    def capture_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=None) for offset in DIAGONAL}


