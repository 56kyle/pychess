from typing import Type

from chess.interface import AbstractInterface
from chess.move.interface import Move
from chess.move.capture.data import CaptureData, T
from chess.move.capture.factory import CaptureFactory, F
from chess.move.capture.validator import CaptureValidator, V
from chess.offset import Offset
from chess.piece import Piece, PieceData


class Capture(Move[T, F, V]):
    factory: Type[F] = CaptureFactory[T]
    validator: Type[V] = CaptureValidator[T]

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

