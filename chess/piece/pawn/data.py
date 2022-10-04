
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.move.capture import Capture
from chess.move.en_passant import EnPassant
from chess.offset import VERTICAL, DIAGONAL
from chess.path import Path
from chess.piece import PieceData


def _get_all_move_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in VERTICAL}

def _get_all_capture_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in DIAGONAL}

def _get_all_en_passant_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in DIAGONAL}


@dataclass(frozen=True)
class PawnData(PieceData):
    name: str = field(init=False, default='Pawn')
    letter: str = field(init=False, default='P')
    value: int = field(init=False, default=1)
    symbol: str = field(init=False, default='\u2659')
    html_decimal: str = field(init=False, default='&#9817;')
    html_hex: str = field(init=False, default='&#x2659;')
    move_paths: Set[Path] = field(default_factory=_get_all_move_paths)
    capture_paths: Set[Path] = field(default_factory=_get_all_capture_paths)
    en_passant_paths: Set[Path] = field(default_factory=_get_all_en_passant_paths)

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths | self.en_passant_paths


T = TypeVar('T', bound=PawnData)

