from typing import List

import numpy as np

from chess.color import Color
from chess.piece import (
    King,
    Queen,
    Rook,
    Bishop,
    Knight,
    Pawn,
    ChessPiece
)
from chess.unit import (
    Unit,
    BlackKing,
    BlackQueen,
    BlackRook,
    BlackBishop,
    BlackKnight,
    BlackPawn,
    WhiteKing,
    WhiteQueen,
    WhiteRook,
    WhiteBishop,
    WhiteKnight,
    WhitePawn,
)
from chess.square import Square


standard_black_pieces = [
    BlackRook, BlackKnight, BlackBishop, BlackQueen, BlackKing, BlackBishop, BlackKnight, BlackRook,
    BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn,

]

standard_white_pieces = [
    WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn,
    WhiteRook, WhiteKnight, WhiteBishop, WhiteQueen, WhiteKing, WhiteBishop, WhiteKnight, WhiteRook,
]

standard_pieces = [*standard_black_pieces, *standard_white_pieces]


standard_board_array = np.array(
    [[BlackRook, BlackKnight, BlackBishop, BlackQueen, BlackKing, BlackBishop, BlackKnight, BlackRook],
     [BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn],
     [WhiteRook, WhiteKnight, WhiteBishop, WhiteQueen, WhiteKing, WhiteBishop, WhiteKnight, WhiteRook]]
)
class ChessBoard:
    def __init__(self, array: np.ndarray = standard_board_array, *args, **kwargs):
        self._array: np.ndarray = array

    def __eq__(self, other):
        if isinstance(other, ChessBoard):
            return np.array_equal(self._array, other._array)
        elif isinstance(other, np.ndarray):
            return np.array_equal(self._array, other)
        else:
            return False

    def get_pieces(self) -> List[ChessPiece]:
        pieces = []
        for square in self._array.flatten():
            if square is not None:
                pieces.append(square)
        return pieces

    def get(self, square: Square) -> ChessPiece:
        return self._array[square.row][square.column]

    def set(self, square: Square, unit: Unit | None):
        self._array[square.row][square.column] = unit

