
from typing import Set

from chess.offset import HORIZONTAL, OMNI
from chess.path import Path
from chess.piece import Piece


class King(Piece):
    name: str = 'King'
    letter: str = 'K'
    value: int = 0
    symbol: str = '♚'
    html_decimal: str = '&#9818;'
    html_hex: str = '&#x265A;'

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths | self.castle_paths

    @property
    def move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in OMNI}

    @property
    def capture_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in OMNI}

    @property
    def castle_paths(self) -> Set[Path]:
        return {Path(offset=offset*2, max_steps=1) for offset in HORIZONTAL} |\
               {Path(offset=offset*3, max_steps=1) for offset in HORIZONTAL}



