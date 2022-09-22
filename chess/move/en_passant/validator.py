
from typing import TypeVar

from chess.move.en_passant.data import EnPassantData, T
from chess.move.capture.validator import CaptureValidator


class EnPassantValidator(CaptureValidator[T]):
    @classmethod
    def _validate_data(cls, data: T):
        pass


V = TypeVar('V', bound=EnPassantValidator)

