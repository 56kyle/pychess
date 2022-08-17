
import chess.board
import chess.piece

from chess.move import Move


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, *args, **kwargs):
        self.board: chess.board.ChessBoard = board

    def make_move(self, move: Move):
        raise NotImplementedError()

    def add_piece(self, row: int, column: int, piece: chess.piece.ChessPiece):
        raise NotImplementedError()

    def remove_piece(self, row: int, column: int):
        raise NotImplementedError()

