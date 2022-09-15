from abc import ABC

from chess.interface import AbstractInterface
from chess.piece.data import PieceData, T
from chess.piece.factory import PieceFactory, F
from chess.piece.validator import PieceValidator, V


class Piece(AbstractInterface[T, F, V], ABC):
    factory: F = PieceFactory[T]
    validator: V = PieceValidator[T]

