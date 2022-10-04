
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.move.capture import Capture
from chess.offset import DIAGONAL
from chess.path import Path
from chess.piece import PieceData


@dataclass(frozen=True)
class BishopData(PieceData):
    name: str = field(init=False, default='Bishop')
    letter: str = field(init=False, default='B')
    value: int = field(init=False, default=3)
    symbol: str = field(init=False, default='♝')
    html_decimal: str = field(init=False, default='&#9821;')
    html_hex: str = field(init=False, default='&#x265D;')
    move_paths: Set[Path] = field(default_factory=lambda: {Path(offset=offset, max_steps=None) for offset in DIAGONAL})
    capture_paths: Set[Path] = field(default_factory=lambda: {Path(offset=offset, max_steps=None) for offset in DIAGONAL})


T = TypeVar('T', bound=BishopData)

