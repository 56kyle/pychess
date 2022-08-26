
import chess.board
import chess.unit

from chess.move import Move
from chess.movement import Movement, INFINITE_STEPS
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

    def _fit_movement_max_steps_to_board(self, square: Square, movement: Movement):
        absolute_max_steps: int = max(self.board.get_height(), self.board.get_width())
        board_limited_max_steps: int = 0
        for _ in range(absolute_max_steps):
            square: Square = square.offset(movement.offset)
            if not self.board.is_valid_square(square=square):
                break
            board_limited_max_steps += 1
        return movement.with_limited_max_steps(max_steps=board_limited_max_steps)














