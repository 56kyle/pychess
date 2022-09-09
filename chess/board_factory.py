

from abc import ABC, abstractmethod

from .board_state import BoardState


class BoardFactory(ABC):
    @abstractmethod
    def create(self) -> BoardState:
        raise NotImplementedError

    @abstractmethod
    def create_from_fen(self, fen: str) -> BoardState:
        raise NotImplementedError


