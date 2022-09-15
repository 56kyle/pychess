from abc import ABC
from typing import Generic, TypeVar

from chess.factory import AbstractFactory
from chess.piece.data import PieceData, T


class PieceFactory(AbstractFactory[T], ABC):
    data_type: T = PieceData


F = TypeVar('F', bound=PieceFactory)
