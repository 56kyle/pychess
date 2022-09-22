
from abc import ABC
from typing import TypeVar

from chess.move.capture.factory import CaptureFactory
from chess.move.en_passant.data import T, EnPassantData
from chess.position import Position


class EnPassantFactory(CaptureFactory[T], ABC):
    data_type: T = EnPassantData

    @classmethod
    def create(cls,
               target_position: Position,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            target_position=target_position,
            *args,
            **kwargs,
        )


F = TypeVar('F', bound=EnPassantFactory)

