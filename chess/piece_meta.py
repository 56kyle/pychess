
from typing import Set

from chess.line import Line


class PieceMeta:
    name: str
    letter: str
    value: int
    symbol: str
    html_decimal: str
    html_hex: str

    move_paths: Set[Line] = set()
    capture_paths: Set[Line] = set()
    en_passant_paths: Set[Line] = set()
    castle_paths: Set[Line] = set()


