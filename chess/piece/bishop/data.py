
from dataclasses import dataclass
from typing import TypeVar

from chess.piece import PieceData


@dataclass(frozen=True)
class BishopData(PieceData):
    name: str = 'Bishop'
    letter: str = 'B'
    value: int = 3
    symbol: str = '♝'
    html_decimal: str = '&#9821;'
    html_hex: str = '&#x265D;'


T = TypeVar('T', bound=BishopData)

