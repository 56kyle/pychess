
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.move.capture import Capture
from chess.move.castle import Castle
from chess.offset import UP_LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, HORIZONTAL, OMNI
from chess.path import Path
from chess.piece import PieceData


def _get_all_paths() -> Set[Path]:
    return _get_all_move_paths() | _get_all_capture_paths() | _get_all_castle_paths()

def _get_all_move_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in OMNI}

def _get_all_capture_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in OMNI}

def _get_all_castle_paths() -> Set[Path]:
    return {Path(offset=offset*2, max_steps=1) for offset in HORIZONTAL} | \
           {Path(offset=offset*3, max_steps=1) for offset in HORIZONTAL}


@dataclass(frozen=True)
class KingData(PieceData):
    name: str = field(init=False, default='King')
    letter: str = field(init=False, default='K')
    value: int = field(init=False, default=0)
    symbol: str = field(init=False, default='♚')
    html_decimal: str = field(init=False, default='&#9818;')
    html_hex: str = field(init=False, default='&#x265A;')
    move_paths: Set[Path] = field(init=False, default_factory=_get_all_move_paths)
    capture_paths: Set[Path] = field(init=False, default_factory=_get_all_capture_paths)
    castle_paths: Set[Path] = field(init=False, default_factory=_get_all_castle_paths)

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths | self.castle_paths


T = TypeVar('T', bound=KingData)

