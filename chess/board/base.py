from typing import List

import numpy as np

import chess.piece


class ChessBoard:
    def __init__(self, array: np.ndarray, *args, **kwargs):
        self._array: np.ndarray = array

    def __eq__(self, other):
        if isinstance(other, ChessBoard):
            return np.array_equal(self._array, other._array)
        elif isinstance(other, np.ndarray):
            return np.array_equal(self._array, other)
        else:
            return False

    def get_pieces(self) -> List[chess.piece.ChessPiece]:
        pieces = []
        for square in self._array.flatten():
            if square is not None:
                pieces.append(square)
        return pieces

    def get(self, row: int, col: int) -> chess.piece.ChessPiece:
        return self._array[row][col]

    def set(self, row: int, col: int, piece: chess.piece.ChessPiece | None):
        self._array[row][col] = piece

