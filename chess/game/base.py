
import chess.board
import chess.unit

from chess.move import Move
from chess.path import Path, INFINITE_STEPS, AllowedMovementTypes
from chess.square import Square
from chess.unit import Unit

from typing import List


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, moves: List[Move] = None, *args, **kwargs):
        self.board: chess.board.ChessBoard = board
        self.moves: List[Move] = moves if moves is not None else []

    def add_piece(self, square: Square, unit: chess.unit.Unit):
        self.board.set(square=square, unit=unit)

    def remove_piece(self, square: Square):
        self.board.set(square=square, unit=None)



