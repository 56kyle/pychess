
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.move.capture import Capture
from chess.offset import Offset, UP, RIGHT, DOWN, LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT
from chess.path import Path
from chess.piece import PieceData


def _get_knight_offsets() -> Set[Offset]:
    return {
        UP_RIGHT + UP,
        UP_RIGHT + RIGHT,
        DOWN_RIGHT + RIGHT,
        DOWN_RIGHT + DOWN,
        DOWN_LEFT + DOWN,
        DOWN_LEFT + LEFT,
        UP_LEFT + LEFT,
        UP_LEFT + UP,
    }


def _get_all_move_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in _get_knight_offsets()}

def _get_all_capture_paths() -> Set[Path]:
    return {Path(offset=offset, max_steps=1) for offset in _get_knight_offsets()}


@dataclass(frozen=True)
class KnightData(PieceData):
    name: str = field(init=False, default='Knight')
    letter: str = field(init=False, default='N')
    value: int = field(init=False, default=3)
    symbol: str = field(init=False, default='\u2658')
    html_decimal: str = field(init=False, default='&#9822;')
    html_hex: str = field(init=False, default='&#x2658;')
    move_paths: Set[Path] = field(init=False, default_factory=_get_all_move_paths)
    capture_paths: Set[Path] = field(init=False, default_factory=_get_all_capture_paths)

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths


T = TypeVar('T', bound=KnightData)

