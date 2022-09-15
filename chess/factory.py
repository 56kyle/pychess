
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.data import T


class AbstractFactory(Generic[T], ABC):
    data_type: T

    def __init__(self, data: T, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data: T = data

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs) -> T:
        raise NotImplementedError


F = TypeVar('F', bound=AbstractFactory)
