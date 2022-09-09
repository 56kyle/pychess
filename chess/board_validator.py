

from abc import ABC, abstractmethod

from .board_state import BoardState


class BoardValidator(ABC):
    @abstractmethod
    def validate(self, board: BoardState) -> bool:
        raise NotImplementedError

