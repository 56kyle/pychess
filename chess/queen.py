
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.offset import OMNI
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta


class QueenMeta(PieceMeta):
    name: str = 'Queen'
    letter: str = 'Q'
    value: int = 9
    symbol: str = '♛'
    html_decimal: str = '&#9819;'
    html_hex: str = '&#x265B;'

    def get_move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=None) for offset in OMNI}

    def get_capture_paths(self) -> Set[Path]:
        return self.get_move_paths()


@dataclass(frozen=True)
class Queen(Piece):
    meta: QueenMeta = QueenMeta


