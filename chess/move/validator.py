
from abc import ABC
from typing import TypeVar

from chess.move.data import MoveData, T
from chess.validator import AbstractValidator


class MoveValidator(AbstractValidator[T]):
    @classmethod
    def validate(cls, data: T):
        pass


V = TypeVar('V', bound=MoveValidator)

