
from abc import ABC, abstractmethod
from typing import TypeVar

from chess.factory import AbstractFactory
from chess.move.data import T, MoveData


class MoveFactory(AbstractFactory[T], ABC):
    data_type: T = MoveData


F = TypeVar('F', bound=MoveFactory)

