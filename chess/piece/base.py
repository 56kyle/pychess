
import numpy as np
from chess.color import Color


class ChessPiece:
    def __init__(self, color: Color, *args, **kwargs):
        self.color: Color = color
        self.has_moved = False








