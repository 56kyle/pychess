
import chess.game.base as base
import chess.board
import chess.piece

from chess.color import Color
from chess.move import Move


class Standard(base.ChessGame):
    def add_piece(self, row: int, column: int, piece: chess.piece.ChessPiece):
        self.board.array[row][column]: chess.piece.ChessPiece = piece

    def remove_piece(self, row: int, column: int):
        self.board.array[row][column] = None

