from typing import Set

from chess.line import Line


class PieceType:
    name: str
    letter: str
    value: int
    symbol: str
    html_decimal: str
    html_hex: str

    move_lines: Set[Line] = set()
    capture_lines: Set[Line] = set()
    en_passant_lines: Set[Line] = set()
    castle_lines: Set[Line] = set()


