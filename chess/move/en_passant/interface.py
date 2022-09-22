from typing import Type

from chess.move.capture.interface import Capture
from chess.move.en_passant.data import T
from chess.move.en_passant.factory import EnPassantFactory, F
from chess.move.en_passant.validator import EnPassantValidator, V
from chess.position import Position


class EnPassant(Capture[T, F, V]):
    factory: Type[F] = EnPassantFactory[T]
    validator: Type[V] = EnPassantValidator[T]

    def __init__(self,
                 target_position: Position,
                 *args,
                 **kwargs):
        super().__init__(
            target_position=target_position,
            *args,
            **kwargs
        )

