from dataclasses import dataclass
from typing import TypeVar

from chess.color import Color
from chess.position import Position


@dataclass(frozen=True)
class PieceData:
    position: Position
    color: Color = Color.WHITE
    name: str = ''
    letter: str = ''
    value: int = 0
    symbol: str = ''
    html_decimal: str = ''
    html_hex: str = ''
    has_moved: bool = False


T = TypeVar('T', bound=PieceData)

