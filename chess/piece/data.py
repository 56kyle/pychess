from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.color import Color
from chess.data import AbstractData
from chess.path import Path
from chess.position import Position


@dataclass(frozen=True)
class PieceData(AbstractData):
    position: Position
    color: Color
    has_moved: bool = False
    name: str = field(init=False)
    letter: str = field(init=False)
    value: int = field(init=False)
    symbol: str = field(init=False)
    html_decimal: str = field(init=False)
    html_hex: str = field(init=False)
    move_paths: Set[Path] = field(init=False)
    capture_paths: Set[Path] = field(init=False)

    @property
    def all_paths(self) -> Set[Path]:
        return self.move_paths | self.capture_paths


T = TypeVar('T', bound=PieceData)

