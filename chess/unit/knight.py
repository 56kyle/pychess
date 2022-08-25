
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteKnight(base.Unit, piece.Knight):

    def __init__(self, *args, **kwargs):
        super().__init__(Color.WHITE, *args, **kwargs)

class BlackKnight(base.Unit, piece.Knight):
    color: Color = Color.BLACK
