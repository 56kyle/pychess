
from abc import ABC, abstractmethod


from chess.board import BoardValidator
from chess.standard.board.data import StandardBoardData, T
from chess.standard.board.exceptions import StandardBoardValidationError


class StandardBoardValidator(BoardValidator[StandardBoardData], ABC):
    def validate(self):
        pass








