
from abc import ABC
from typing import TypeVar

from chess.game.data import T
from chess.validator import AbstractValidator


class GameValidator(AbstractValidator[T], ABC):
    @classmethod
    def validate(cls, data: T):
        pass


V = TypeVar('V', bound=GameValidator)

