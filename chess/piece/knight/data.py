
from dataclasses import dataclass
from typing import TypeVar

from chess.piece import PieceData


@dataclass(frozen=True)
class KnightData(PieceData):
    name: str = 'Knight'
    letter: str = 'N'
    value: int = 3
    symbol: str = '\u2658'
    html_decimal: str = '&#9822;'
    html_hex: str = '&#x2658;'


T = TypeVar('T', bound=KnightData)

