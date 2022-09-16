
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type

from chess.data import T
from chess.exceptions import ValidationError


class AbstractValidator(Generic[T]):
    validation_error: Type[ValidationError] = ValidationError

    def __init__(self, data: T, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data: T = data

    @classmethod
    def is_valid(cls, data: T) -> bool:
        try:
            cls.validate(data=data)
        except ValidationError:
            return False
        return True

    @classmethod
    def validate(cls, data: T):
        cls._validate_data(data=data)

    @classmethod
    def _validate_data(cls, data: T):
        raise NotImplementedError


V = TypeVar('V', bound=AbstractValidator)
