
import chess.board
import chess.piece

from chess.decorators import callback


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, *args, **kwargs):
        self.board: chess.board.ChessBoard = board

    @callback
    def add_piece(self, row: int, column: int, piece: chess.piece.ChessPiece):
        pass


