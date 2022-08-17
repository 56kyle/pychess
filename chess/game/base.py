
import chess.board
import chess.piece


class ChessGame:
    def __init__(self, board: chess.board.ChessBoard, *args, **kwargs):
        self.board: chess.board.ChessBoard = board

    def add_piece(self, row: int, column: int, piece: chess.piece.ChessPiece):
        raise NotImplementedError()


