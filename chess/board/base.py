
import numpy as np

import chess.piece


class ChessBoard:
    def __init__(self, array: np.ndarray, *args, **kwargs):
        self.array: np.ndarray = array

