
from abc import ABC, abstractmethod
from typing import TypeVar

from chess.factory import AbstractFactory
from chess.move.data import T, MoveData
from chess.offset import Offset
from chess.piece import PieceData
from chess.position import Position


class MoveFactory(AbstractFactory[T], ABC):
    data_type: T = MoveData

    @classmethod
    def create(cls,
               piece_data: PieceData,
               piece_start: Position,
               offset: Offset,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            piece_data=piece_data,
            piece_start=piece_start,
            offset=offset,
        )


F = TypeVar('F', bound=MoveFactory)

