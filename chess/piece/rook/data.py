
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.offset import LINEAR
from chess.path import Path
from chess.piece import PieceData


def _get_all_move_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=None) for offset in LINEAR}

def _get_all_capture_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=None) for offset in LINEAR}


@dataclass(frozen=True)
class RookData(PieceData):
    name: str = field(init=False, default='Rook')
    letter: str = field(init=False, default='R')
    value: int = field(init=False, default=5)
    symbol: str = field(init=False, default='♜')
    html_decimal: str = field(init=False, default='&#9820;')
    html_hex: str = field(init=False, default='&#x265C;')
    move_paths: Set[Path] = field(default_factory=_get_all_move_paths)
    capture_paths: Set[Path] = field(default_factory=_get_all_capture_paths)


T = TypeVar('T', bound=RookData)

