
from typing import Generic

from chess.data import T
from chess.factory import AbstractFactory, F
from chess.validator import AbstractValidator, V


class AbstractInterface(Generic[T, F, V]):
    def __init__(self, data: T, factory: F = None, validator: V = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data: T = data
        self.factory: F = factory if factory else AbstractFactory[T](data=data)
        self.validator: V = validator if validator else AbstractValidator[T](data=data)

    def is_valid(self) -> bool:
        return self.validator.is_valid()

    def validate(self):
        self.validator.validate()
