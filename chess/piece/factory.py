from abc import ABC
from typing import Generic, TypeVar

from chess.factory import AbstractFactory
from chess.piece.data import PieceData, T


class PieceFactory(AbstractFactory[T], ABC):
    pass


F = TypeVar('F', bound=PieceFactory)
