
from dataclasses import dataclass
from typing import TypeVar

from chess.piece import PieceData


@dataclass(frozen=True)
class RookData(PieceData):
    name: str = 'Rook'
    letter: str = 'R'
    value: int = 5
    symbol: str = '♜'
    html_decimal: str = '&#9820;'
    html_hex: str = '&#x265C;'


T = TypeVar('T', bound=RookData)

