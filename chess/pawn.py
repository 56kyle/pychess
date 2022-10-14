from dataclasses import dataclass
from typing import Set

from chess.offset import VERTICAL, DIAGONAL
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta


class PawnMeta(PieceMeta):
    name: str = 'Pawn'
    letter: str = 'P'
    value: int = 1
    symbol: str = '\u2659'
    html_decimal: str = '&#9817;'
    html_hex: str = '&#x2659;'

    def get_move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in VERTICAL}

    def get_capture_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in DIAGONAL}

    def get_en_passant_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in DIAGONAL}


@dataclass(frozen=True)
class Pawn(Piece):
    meta: PawnMeta = PawnMeta


