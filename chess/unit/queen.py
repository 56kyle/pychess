
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteQueen(base.Unit, piece.Queen):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.WHITE, *args, **kwargs)

class BlackQueen(base.Unit, piece.Queen):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.BLACK, *args, **kwargs)
