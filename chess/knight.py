
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.line import Line
from chess.move import Move
from chess.offset import Offset, UP, RIGHT, DOWN, LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT

from chess.piece import Piece
from chess.piece_type import PieceType
from chess.position import ZERO
from chess.segment import Segment


class KnightType(PieceType):
    name: str = 'Knight'
    letter: str = 'N'
    value: int = 3
    symbol: str = '\u2658'
    html_decimal: str = '&#9822;'
    html_hex: str = '&#x2658;'
    offsets: Set[Offset] = {
        UP * 2 + RIGHT,
        UP * 2 + LEFT,
        DOWN * 2 + RIGHT,
        DOWN * 2 + LEFT,
        RIGHT * 2 + UP,
        RIGHT * 2 + DOWN,
        LEFT * 2 + UP,
        LEFT * 2 + DOWN,
    }
    move_lines: Set[Line] = {offset.as_segment() for offset in offsets}
    capture_lines: Set[Line] = {offset.as_segment() for offset in offsets}


@dataclass(frozen=True)
class Knight(Piece):
    type: KnightType = KnightType


