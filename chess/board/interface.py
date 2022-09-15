from abc import ABC, abstractmethod

from chess.board.data import BoardData, T
from chess.board.factory import BoardFactory, F
from chess.board.validator import BoardValidator, V
from chess.interface import AbstractInterface


class Board(AbstractInterface[T, F, V], ABC):
    def __init__(self, data: T, factory: F = None, validator: V = None, *args, **kwargs):
        super().__init__(data, factory, validator, *args, **kwargs)
        self.factory: F = factory if factory else BoardFactory[T](data=data)
        self.validator: V = validator if validator else BoardValidator[T](data=data)









