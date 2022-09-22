
from abc import ABC, abstractmethod
from typing import TypeVar

from chess.castle_right import CastleRight
from chess.move.factory import MoveFactory
from chess.move.castle.data import T, CastleData
from chess.offset import Offset
from chess.piece import PieceData
from chess.piece.rook import RookData


class CastleFactory(MoveFactory[T], ABC):
    data_type: T = CastleData

    @classmethod
    def create(cls,
               rook_data: RookData,
               castle_right: CastleRight,
               *args,
               **kwargs) -> T:
        return cls.data_type(
            rook_data=rook_data,
            castle_right=castle_right,
            *args,
            **kwargs,
        )


F = TypeVar('F', bound=CastleFactory)

