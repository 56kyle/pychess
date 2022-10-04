
from dataclasses import dataclass
from typing import TypeVar

from chess.castle_right import CastleRight
from chess.move import MoveData
from chess.piece.rook import RookData
from chess.position import Position


@dataclass(frozen=True)
class CastleData(MoveData):
    rook_data: RookData
    rook_start: Position
    castle_right: CastleRight


T = TypeVar('T', bound=CastleData)
