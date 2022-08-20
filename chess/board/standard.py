import numpy as np

import chess.board.base as base
import chess.piece as piece

from chess.color import Color

from typing import List

_a8_rook = piece.Rook(Color.BLACK)
_b8_knight = piece.Knight(Color.BLACK)
_c8_bishop = piece.Bishop(Color.BLACK)
_d8_queen = piece.Queen(Color.BLACK)
_e8_king = piece.King(Color.BLACK)
_f8_bishop = piece.Bishop(Color.BLACK)
_g8_knight = piece.Knight(Color.BLACK)
_h8_rook = piece.Rook(Color.BLACK)
_a7_pawn = piece.Pawn(Color.BLACK)
_b7_pawn = piece.Pawn(Color.BLACK)
_c7_pawn = piece.Pawn(Color.BLACK)
_d7_pawn = piece.Pawn(Color.BLACK)
_e7_pawn = piece.Pawn(Color.BLACK)
_f7_pawn = piece.Pawn(Color.BLACK)
_g7_pawn = piece.Pawn(Color.BLACK)
_h7_pawn = piece.Pawn(Color.BLACK)

_a2_pawn = piece.Pawn(Color.WHITE)
_b2_pawn = piece.Pawn(Color.WHITE)
_c2_pawn = piece.Pawn(Color.WHITE)
_d2_pawn = piece.Pawn(Color.WHITE)
_e2_pawn = piece.Pawn(Color.WHITE)
_f2_pawn = piece.Pawn(Color.WHITE)
_g2_pawn = piece.Pawn(Color.WHITE)
_h2_pawn = piece.Pawn(Color.WHITE)
_a1_rook = piece.Rook(Color.WHITE)
_b1_knight = piece.Knight(Color.WHITE)
_c1_bishop = piece.Bishop(Color.WHITE)
_d1_queen = piece.Queen(Color.WHITE)
_e1_king = piece.King(Color.WHITE)
_f1_bishop = piece.Bishop(Color.WHITE)
_g1_knight = piece.Knight(Color.WHITE)
_h1_rook = piece.Rook(Color.WHITE)


standard_black_pieces = [
    _a8_rook, _b8_knight, _c8_bishop, _d8_queen, _e8_king, _f8_bishop, _g8_knight, _h8_rook,
    _a7_pawn, _b7_pawn, _c7_pawn, _d7_pawn, _e7_pawn, _f7_pawn, _g7_pawn, _h7_pawn
]

standard_white_pieces = [
    _a2_pawn, _b2_pawn, _c2_pawn, _d2_pawn, _e2_pawn, _f2_pawn, _g2_pawn, _h2_pawn,
    _a1_rook, _b1_knight, _c1_bishop, _d1_queen, _e1_king, _f1_bishop, _g1_knight, _h1_rook
]

standard_pieces = [*standard_black_pieces, *standard_white_pieces]


standard_board_array = np.array(
    [[_a8_rook, _b8_knight, _c8_bishop, _d8_queen, _e8_king, _f8_bishop, _g8_knight, _h8_rook],
     [_a7_pawn, _b7_pawn, _c7_pawn, _d7_pawn, _e7_pawn, _f7_pawn, _g7_pawn, _h7_pawn],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [_a2_pawn, _b2_pawn, _c2_pawn, _d2_pawn, _e2_pawn, _f2_pawn, _g2_pawn, _h2_pawn],
     [_a1_rook, _b1_knight, _c1_bishop, _d1_queen, _e1_king, _f1_bishop, _g1_knight, _h1_rook]]
)


class Standard(base.ChessBoard):
    def __init__(self, array: np.ndarray = None, *args, **kwargs):
        array = array if array is not None else standard_board_array
        super().__init__(array=array, *args, **kwargs)

    def get(self, row: int, col: int) -> piece.ChessPiece:
        return self.array[row][col]



