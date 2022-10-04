
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.offset import OMNI
from chess.path import Path
from chess.piece import PieceData


def _get_all_move_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=None) for offset in OMNI}

def _get_all_capture_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=None) for offset in OMNI}


@dataclass(frozen=True)
class QueenData(PieceData):
    name: str = field(init=False, default='Queen')
    letter: str = field(init=False, default='Q')
    value: int = field(init=False, default=9)
    symbol: str = field(init=False, default='♛')
    html_decimal: str = field(init=False, default='&#9819;')
    html_hex: str = field(init=False, default='&#x265B;')
    move_paths: Set[Path] = field(init=False, default_factory=_get_all_move_paths)
    capture_paths: Set[Path] = field(init=False, default_factory=_get_all_capture_paths)


T = TypeVar('T', bound=QueenData)

