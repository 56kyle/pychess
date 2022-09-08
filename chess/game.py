
import chess.board
import chess.unit

from chess.color import Color
from chess.move import Move
from chess.square import Square
from chess.turn import Turn

from typing import List

from chess.unit import Unit


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, moves: List[Move] = None, *args, **kwargs):
        self.board: chess.board.ChessBoard = board
        self.moves: List[Move] = moves if moves is not None else []
        self.turns: List[Turn] = []
        self.to_move: Color = Color.WHITE

    def add_piece(self, square: Square, unit: chess.unit.Unit):
        self.board.set(square=square, unit=unit)

    def remove_piece(self, square: Square):
        self.board.set(square=square, unit=None)
