
from dataclasses import dataclass
from typing import TypeVar

from chess.offset import Offset
from chess.piece import PieceData
from chess.data import AbstractData
from chess.position import Position


@dataclass(frozen=True)
class MoveData(AbstractData):
    piece_data: PieceData
    piece_start: Position
    offset: Offset


T = TypeVar('T', bound=MoveData)
