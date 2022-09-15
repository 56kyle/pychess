
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type

from chess.data import AbstractData, T


class AbstractFactory(Generic[T]):
    data_type: Type[T] = AbstractData

    def __init__(self, data: T, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data: T = data

    @classmethod
    def create(cls, *args, **kwargs) -> T:
        if not cls.data_type:
            raise NotImplementedError
        return cls.data_type(*args, **kwargs)


F = TypeVar('F', bound=AbstractFactory)

