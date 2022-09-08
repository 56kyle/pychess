
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

    def _is_move_color(self, move: Move) -> bool:
        return move.unit.color == self.to_move

    def _is_capture_move(self, move: Move) -> bool:
        opposing_unit: Unit | None = self.board.get(move.get_end_square())
        if opposing_unit is not None:
            return opposing_unit.color != move.unit.color
        return False

    def add_piece(self, square: Square, unit: chess.unit.Unit):
        self.board.set(square=square, unit=unit)

    def remove_piece(self, square: Square):
        self.board.set(square=square, unit=None)
