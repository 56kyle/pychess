
import chess.board
import chess.piece

from chess.move import Move
from typing import List


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, moves: List[Move] = None, *args, **kwargs):
        self.board: chess.board.ChessBoard = board
        self.moves: List[Move] = moves if moves is not None else []

    def make_move(self, from_column: int, from_row: int, to_column: int, to_row: int):
        raise NotImplementedError()

    def add_piece(self, column: int, row: int, piece: chess.piece.ChessPiece):
        self.board.set(column, row, piece)

    def remove_piece(self, column: int, row: int):
        self.board.set(column, row, None)


