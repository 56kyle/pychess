
import chess.board
import chess.piece

from chess.move import Move
from chess.square import Square

from typing import List


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, moves: List[Move] = None, *args, **kwargs):
        self.board: chess.board.ChessBoard = board
        self.moves: List[Move] = moves if moves is not None else []

    def make_move(self, from_column: int, from_row: int, to_column: int, to_row: int):
        raise NotImplementedError()

    def add_piece(self, square: Square, piece: chess.piece.ChessPiece):
        self.board.set(square=square, piece=piece)

    def remove_piece(self, square: Square):
        self.board.set(square=square, piece=None)


