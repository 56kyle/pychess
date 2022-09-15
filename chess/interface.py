
from typing import Generic

from chess.data import T
from chess.factory import AbstractFactory, F
from chess.validator import AbstractValidator, V


class AbstractInterface(Generic[T, F, V]):
    factory: F = AbstractFactory[T]
    validator: V = AbstractValidator[T]

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = self.factory.create(*args, **kwargs)

    def is_valid(self) -> bool:
        return self.validator.is_valid(data=self.data)

    def validate(self):
        self.validator.validate(data=self.data)
