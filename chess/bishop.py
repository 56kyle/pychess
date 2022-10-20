
from typing import Set

from chess.line import Line
from chess.offset import DIAGONAL
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta
from chess.position import Position
from chess.ray import Ray


class BishopMeta(PieceMeta):
    name: str = 'Bishop'
    letter: str = 'B'
    value: int = 3
    symbol: str = '♝'
    html_decimal: str = '&#9821;'
    html_hex: str = '&#x265D;'

    move_paths: Set[Line] = {offset.as_ray() for offset in DIAGONAL}
    capture_paths: Set[Line] = {offset.as_ray() for offset in DIAGONAL}

class Bishop(Piece):
    meta: BishopMeta = BishopMeta


