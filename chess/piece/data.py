from dataclasses import dataclass
from typing import TypeVar

from chess.color import Color
from chess.data import AbstractData
from chess.position import Position


@dataclass(frozen=True)
class PieceData(AbstractData):
    position: Position
    color: Color
    name: str
    letter: str
    value: int
    symbol: str
    html_decimal: str
    html_hex: str
    has_moved: bool = False


T = TypeVar('T', bound=PieceData)

