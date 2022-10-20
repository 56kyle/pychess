
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.line import Line
from chess.offset import OMNI
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta
from chess.ray import Ray


class QueenMeta(PieceMeta):
    name: str = 'Queen'
    letter: str = 'Q'
    value: int = 9
    symbol: str = '♛'
    html_decimal: str = '&#9819;'
    html_hex: str = '&#x265B;'

    move_paths: Set[Line] = {offset.as_ray() for offset in OMNI}
    capture_paths: Set[Line] = {offset.as_ray() for offset in OMNI}


@dataclass(frozen=True)
class Queen(Piece):
    meta: QueenMeta = QueenMeta


