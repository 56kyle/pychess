
from typing import TypeVar

from chess.move.capture.data import CaptureData, T
from chess.move.validator import MoveValidator


class CaptureValidator(MoveValidator[T]):
    @classmethod
    def _validate_data(cls, data: T):
        pass


V = TypeVar('V', bound=CaptureValidator)

