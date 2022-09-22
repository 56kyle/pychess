
from abc import ABC, abstractmethod
from typing import TypeVar

from chess.move.factory import MoveFactory
from chess.move.capture.data import T, CaptureData
from chess.offset import Offset
from chess.piece import PieceData


class CaptureFactory(MoveFactory[T], ABC):
    data_type: T = CaptureData

    @classmethod
    def create(cls,
               captured_piece_data: PieceData,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            captured_piece_data=captured_piece_data,
            *args,
            **kwargs,
        )


F = TypeVar('F', bound=CaptureFactory)

