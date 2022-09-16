from typing import Type

from chess.interface import AbstractInterface
from chess.move.data import MoveData, T
from chess.move.factory import MoveFactory, F
from chess.move.validator import MoveValidator, V
from chess.offset import Offset
from chess.piece import Piece, PieceData


class Move(AbstractInterface[T, F, V]):
    factory: Type[F] = MoveFactory[T]
    validator: Type[V] = MoveValidator[T]

    def __init__(self,
                 piece_data: PieceData,
                 offset: Offset,
                 *args,
                 **kwargs):
        super().__init__(
            piece_data=piece_data,
            offset=offset,
            *args,
            **kwargs
        )

