from typing import Type

from chess.interface import AbstractInterface
from chess.move.data import MoveData, T
from chess.move.factory import MoveFactory, F
from chess.move.validator import MoveValidator, V


class Move(AbstractInterface[T, F, V]):
    factory: Type[F] = MoveFactory[T]
    validator: Type[V] = MoveValidator[T]

