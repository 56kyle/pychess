
from abc import ABC

from chess.game.data import T
from chess.game.factory import GameFactory, F
from chess.game.validator import GameValidator, V
from chess.interface import AbstractInterface


class Game(AbstractInterface[T, F, V], ABC):
    def __init__(self, data: T, factory: F = None, validator: V = None, *args, **kwargs):
        super().__init__(data, factory, validator, *args, **kwargs)
        self.factory: F = factory if factory else GameFactory[T](data=data)
        self.validator: V = validator if validator else GameValidator[T](data=data)

