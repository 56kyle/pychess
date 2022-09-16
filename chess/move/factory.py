
from abc import ABC, abstractmethod
from typing import TypeVar

from chess.factory import AbstractFactory
from chess.move.data import T, MoveData
from chess.offset import Offset
from chess.piece import PieceData


class MoveFactory(AbstractFactory[T], ABC):
    data_type: T = MoveData

    @classmethod
    def create(cls,
               piece_data: PieceData,
               offset: Offset,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            piece_data=piece_data,
            offset=offset,
        )


F = TypeVar('F', bound=MoveFactory)

