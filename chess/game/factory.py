from abc import ABC
from typing import TypeVar

from chess.game.data import T, GameData
from chess.factory import AbstractFactory


class GameFactory(AbstractFactory[T], ABC):
    data_type: T = GameData


F = TypeVar('F', bound=GameFactory)

