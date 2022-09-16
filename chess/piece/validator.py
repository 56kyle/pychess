from abc import ABC
from typing import TypeVar

from chess.piece.data import PieceData, T
from chess.piece.exceptions import PieceValidationError
from chess.position import Position
from chess.validator import AbstractValidator


class PieceValidator(AbstractValidator[T], ABC):
    @classmethod
    def _validate_data(cls, data: T):
        cls._validate_position(data.position)

    @classmethod
    def _validate_position(cls, position: Position):
        cls._validate_position_file(file=position.file)
        cls._validate_position_rank(rank=position.rank)

    @classmethod
    def _validate_position_file(cls, file):
        if file < 1:
            raise PieceValidationError(f'File must be greater than 0, not {file}.')

    @classmethod
    def _validate_position_rank(cls, rank):
        if rank < 1:
            raise PieceValidationError(f'Rank must be greater than 0, not {rank}.')


V = TypeVar('V', bound=PieceValidator)

