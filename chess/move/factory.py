
from abc import ABC, abstractmethod
from typing import TypeVar

from chess.factory import AbstractFactory
from chess.move.data import T
from chess.offset import Offset
from chess.piece import Piece


class MoveFactory(AbstractFactory[T], ABC):
    pass


F = TypeVar('F', bound=MoveFactory)

