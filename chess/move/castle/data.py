
from dataclasses import dataclass
from typing import TypeVar

from chess.castle_right import CastleRight
from chess.move import MoveData
from chess.piece.rook import RookData


@dataclass(frozen=True)
class CastleData(MoveData):
    rook_data: RookData
    castle_right: CastleRight


T = TypeVar('T', bound=CastleData)
