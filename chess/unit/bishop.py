
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteBishop(base.Unit, piece.Bishop):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.WHITE, *args, **kwargs)

class BlackBishop(base.Unit, piece.Bishop):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.BLACK, *args, **kwargs)
