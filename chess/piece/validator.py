from abc import ABC
from typing import TypeVar

from chess.piece.data import PieceData, T
from chess.validator import AbstractValidator


class PieceValidator(AbstractValidator[T], ABC):
    pass


V = TypeVar('V', bound=PieceValidator)

