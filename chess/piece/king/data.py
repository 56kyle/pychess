
from dataclasses import dataclass
from typing import TypeVar

from chess.piece import PieceData


@dataclass(frozen=True)
class KingData(PieceData):
    name: str = 'King'
    letter: str = 'K'
    value: int = 0
    symbol: str = '♚'
    html_decimal: str = '&#9818;'
    html_hex: str = '&#x265A;'


T = TypeVar('T', bound=KingData)

