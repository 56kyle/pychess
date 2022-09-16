
from dataclasses import dataclass
from typing import TypeVar

from chess.piece import PieceData


@dataclass(frozen=True)
class QueenData(PieceData):
    name: str = 'Queen'
    letter: str = 'Q'
    value: int = 9
    symbol: str = '♛'
    html_decimal: str = '&#9819;'
    html_hex: str = '&#x265B;'


T = TypeVar('T', bound=QueenData)

