from typing import List

import numpy as np

from chess import piece


class ChessBoard:
    def __init__(self, array: np.ndarray, *args, **kwargs):
        self.array: np.ndarray = array

    def __eq__(self, other):
        if isinstance(other, ChessBoard):
            return np.array_equal(self.array, other.array)
        elif isinstance(other, np.ndarray):
            return np.array_equal(self.array, other)
        else:
            return False

    def get_pieces(self) -> List[piece.ChessPiece]:
        pieces = []
        for square in self.array.flatten():
            if square is not None:
                pieces.append(square)
        return pieces

