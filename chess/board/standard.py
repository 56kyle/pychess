import numpy as np

import chess.board.base as base
import chess.piece as piece

from chess.color import Color

from typing import List


standard_black_pieces = [
    piece.BlackRook, piece.BlackKnight, piece.BlackBishop, piece.BlackQueen, piece.BlackKing, piece.BlackBishop, piece.BlackKnight, piece.BlackRook,
    piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn,

]

standard_white_pieces = [
    piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn,
    piece.WhiteRook, piece.WhiteKnight, piece.WhiteBishop, piece.WhiteQueen, piece.WhiteKing, piece.WhiteBishop, piece.WhiteKnight, piece.WhiteRook,
]

standard_pieces = [*standard_black_pieces, *standard_white_pieces]


standard_board_array = np.array(
    [[piece.BlackRook, piece.BlackKnight, piece.BlackBishop, piece.BlackQueen, piece.BlackKing, piece.BlackBishop, piece.BlackKnight, piece.BlackRook],
     [piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn, piece.BlackPawn],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn, piece.WhitePawn],
     [piece.WhiteRook, piece.WhiteKnight, piece.WhiteBishop, piece.WhiteQueen, piece.WhiteKing, piece.WhiteBishop, piece.WhiteKnight, piece.WhiteRook]]
)


class Standard(base.ChessBoard):
    def __init__(self, array: np.ndarray = None, *args, **kwargs):
        array = array if array is not None else standard_board_array
        super().__init__(array=array, *args, **kwargs)

    def get(self, row: int, col: int) -> piece.ChessPiece:
        return self.array[row][col]



