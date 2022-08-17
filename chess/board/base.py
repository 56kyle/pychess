
import numpy as np

import chess.piece


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

