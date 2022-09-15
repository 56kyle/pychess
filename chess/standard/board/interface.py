
from abc import ABC

from chess.board.interface import Board
from chess.standard.board.data import T


class StandardBoard(Board[T], ABC):
    pass
