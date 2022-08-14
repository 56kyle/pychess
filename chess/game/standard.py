
import chess.game.base as base
import chess.board
import chess.piece

from chess.decorators import callback


class Standard(base.ChessGame):
    @callback
    def add_piece(self, row: int, column: int, piece: chess.piece.ChessPiece):
        self.board.array[row][column] = piece

