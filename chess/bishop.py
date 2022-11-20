from dataclasses import dataclass
from typing import Set

from chess.line import Line
from chess.offset import DIAGONAL
from chess.piece import Piece
from chess.piece_type import PieceType


class BishopType(PieceType):
    name: str = 'Bishop'
    letter: str = 'B'
    value: int = 3
    symbol: str = '♝'
    html_decimal: str = '&#9821;'
    html_hex: str = '&#x265D;'

    move_lines: Set[Line] = {offset.as_ray() for offset in DIAGONAL}
    capture_lines: Set[Line] = {offset.as_ray() for offset in DIAGONAL}


@dataclass(frozen=True)
class Bishop(Piece):
    type: BishopType = BishopType


