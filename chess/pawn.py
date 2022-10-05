
from typing import Set

from chess.offset import VERTICAL, DIAGONAL
from chess.path import Path
from chess.piece import Piece


class Pawn(Piece):
    name: str = 'Pawn'
    letter: str = 'P'
    value: int = 1
    symbol: str = '\u2659'
    html_decimal: str = '&#9817;'
    html_hex: str = '&#x2659;'

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths | self.en_passant_paths

    @property
    def move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in VERTICAL}

    @property
    def capture_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in DIAGONAL}

    @property
    def en_passant_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in DIAGONAL}


