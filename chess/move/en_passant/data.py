
from dataclasses import dataclass
from typing import TypeVar

from chess.move.capture import CaptureData
from chess.position import Position


@dataclass(frozen=True)
class EnPassantData(CaptureData):
    target_position: Position


T = TypeVar('T', bound=EnPassantData)
