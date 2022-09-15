
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type

from chess.data import T
from chess.exceptions import ValidationError


class AbstractValidator(Generic[T], ABC):
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
    @abstractmethod
    def validate(cls, data: T):
        raise NotImplementedError


V = TypeVar('V', bound=AbstractValidator)
