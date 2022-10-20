from dataclasses import dataclass
from typing import Set

from chess.line import Line
from chess.offset import VERTICAL, DIAGONAL

from chess.piece import Piece
from chess.piece_meta import PieceMeta
from chess.position import ZERO
from chess.segment import Segment


class PawnMeta(PieceMeta):
    name: str = 'Pawn'
    letter: str = 'P'
    value: int = 1
    symbol: str = '\u2659'
    html_decimal: str = '&#9817;'
    html_hex: str = '&#x2659;'

    move_lines: Set[Line] = {offset.as_segment() for offset in VERTICAL}
    capture_lines: Set[Line] = {offset.as_segment() for offset in DIAGONAL}
    en_passant_lines: Set[Line] = {offset.as_segment() for offset in DIAGONAL}


@dataclass(frozen=True)
class Pawn(Piece):
    meta: PawnMeta = PawnMeta


