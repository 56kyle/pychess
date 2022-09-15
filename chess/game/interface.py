
from abc import ABC

from chess.game.data import T
from chess.game.factory import GameFactory, F
from chess.game.validator import GameValidator, V
from chess.interface import AbstractInterface


class Game(AbstractInterface[T, F, V], ABC):
    factory: F = GameFactory[T]
    validator: V = GameValidator[T]



