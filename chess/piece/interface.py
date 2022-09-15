from abc import ABC

from chess.interface import AbstractInterface
from chess.piece.data import PieceData, T
from chess.piece.factory import PieceFactory, F
from chess.piece.validator import PieceValidator, V


class Piece(AbstractInterface[T, F, V], ABC):
    def __init__(self, data: T, factory: F = None, validator: V = None, *args, **kwargs):
        super().__init__(data, factory, validator, *args, **kwargs)
        self.factory: F[T] = factory if factory else PieceFactory[T](data=data)
        self.validator: V[T] = validator if validator else PieceValidator[T](data=data)




