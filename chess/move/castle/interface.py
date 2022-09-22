from typing import Type

from chess.castle_right import CastleRight
from chess.move.interface import Move
from chess.move.castle.data import CastleData, T
from chess.move.castle.factory import CastleFactory, F
from chess.move.castle.validator import CastleValidator, V
from chess.piece.rook import RookData


class Castle(Move[T, F, V]):
    factory: Type[F] = CastleFactory[T]
    validator: Type[V] = CastleValidator[T]

    def __init__(self,
                 rook_data: RookData,
                 castle_right: CastleRight,
                 *args,
                 **kwargs):
        super().__init__(
            rook_data=rook_data,
            castle_right=castle_right,
            *args,
            **kwargs
        )

