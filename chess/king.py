from dataclasses import dataclass
from typing import Set

from chess.move import Move
from chess.offset import HORIZONTAL, OMNI
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta


class KingMeta(PieceMeta):
    name: str = 'King'
    letter: str = 'K'
    value: int = 0
    symbol: str = '♚'
    html_decimal: str = '&#9818;'
    html_hex: str = '&#x265A;'

    def get_move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in OMNI}

    def get_capture_paths(self) -> Set[Path]:
        return self.get_move_paths()

    def get_castle_paths(self) -> Set[Path]:
        return {Path(offset=offset*2, max_steps=1) for offset in HORIZONTAL} \
               | {Path(offset=offset*3, max_steps=1) for offset in HORIZONTAL}


@dataclass(frozen=True)
class King(Piece):
    meta: KingMeta = KingMeta


