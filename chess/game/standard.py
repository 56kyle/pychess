
import chess.game.base as base
import chess.board
import chess.piece


class Standard(base.ChessGame):
    def add_piece(self, row: int, column: int, piece: chess.piece.ChessPiece):
        self.board.array[row][column] = piece

