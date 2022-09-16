
from dataclasses import dataclass
from typing import TypeVar

from chess.piece import PieceData


@dataclass(frozen=True)
class PawnData(PieceData):
    name: str = 'Pawn'
    letter: str = 'P'
    value: int = 1
    symbol: str = '\u2659'
    html_decimal: str = '&#9817;'
    html_hex: str = '&#x2659;'


T = TypeVar('T', bound=PawnData)

