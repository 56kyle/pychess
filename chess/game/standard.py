
import chess.game.base as base
import chess.board
import chess.piece

from chess.color import Color
from chess.move import Move


class Standard(base.ChessGame):
    def make_move(self, from_column: int, from_row: int, to_column: int, to_row: int):
        pass

    def add_piece(self, column: int, row: int, piece: chess.piece.ChessPiece):
        self.board._array[row][column]: chess.piece.ChessPiece = piece

    def remove_piece(self, column: int, row: int):
        self.board._array[row][column] = None

