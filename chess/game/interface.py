
from abc import ABC
from typing import Set, Type

from chess.game.data import T
from chess.game.factory import GameFactory, F
from chess.game.validator import GameValidator, V
from chess.interface import AbstractInterface
from chess.piece import Piece


class Game(AbstractInterface[T, F, V], ABC):
    factory: F = GameFactory[T]
    validator: V = GameValidator[T]


