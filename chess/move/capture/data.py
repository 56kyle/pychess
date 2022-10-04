
from dataclasses import dataclass
from typing import TypeVar

from chess.move import MoveData
from chess.piece import PieceData


@dataclass(frozen=True)
class CaptureData(MoveData):
    captured_piece_data: PieceData
    captured_piece_start: PieceData


T = TypeVar('T', bound=CaptureData)
