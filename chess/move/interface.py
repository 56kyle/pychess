
from chess.interface import AbstractInterface
from chess.move.data import MoveData, T
from chess.move.factory import MoveFactory, F
from chess.move.validator import MoveValidator, V


class Move(AbstractInterface[T, F, V]):
    def __init__(self, data: T, factory: F[T] = None, validator: V[T] = None, *args, **kwargs):
        super().__init__(data, factory, validator, *args, **kwargs)
        self.factory: F[T] = factory if factory else MoveFactory[T](data=data)
        self.validator: V[T] = validator if validator else MoveValidator[T](data=data)


