from abc import ABC
from typing import TypeVar

from chess.game.data import T
from chess.factory import AbstractFactory


class GameFactory(AbstractFactory[T], ABC):
    pass


F = TypeVar('F', bound=GameFactory)

