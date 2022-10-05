
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.offset import LINEAR
from chess.path import Path
from chess.piece import Piece


def _get_all_move_paths() -> Set[Path]:
    return

def _get_all_capture_paths() -> Set[Path]:
    return


class Rook(Piece):
    name: str = 'Rook'
    letter: str = 'R'
    value: int = 5
    symbol: str = '♜'
    html_decimal: str = '&#9820;'
    html_hex: str = '&#x265C;'
    move_paths: Set[Path] = {Path(offset=offset, max_steps=None) for offset in LINEAR}
    capture_paths: Set[Path] = {Path(offset=offset, max_steps=None) for offset in LINEAR}



