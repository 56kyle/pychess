from dataclasses import dataclass
from typing import Set

from chess.line import Line
from chess.move import Move
from chess.offset import HORIZONTAL, OMNI

from chess.piece import Piece
from chess.piece_meta import PieceMeta
from chess.position import Position
from chess.segment import Segment

ZERO_POSITION = Position(rank=0, file=0)

class KingMeta(PieceMeta):
    name: str = 'King'
    letter: str = 'K'
    value: int = 0
    symbol: str = '♚'
    html_decimal: str = '&#9818;'
    html_hex: str = '&#x265A;'

    move_lines: Set[Line] = {offset.as_segment() for offset in OMNI}
    capture_lines: Set[Line] = move_lines
    castle_lines: Set[Line] = {(offset*2).as_segment() for offset in HORIZONTAL} |\
                              {(offset*3).as_segment() for offset in HORIZONTAL}


@dataclass(frozen=True)
class King(Piece):
    meta: KingMeta = KingMeta


