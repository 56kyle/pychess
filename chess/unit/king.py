
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteKing(base.Unit, piece.King):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.WHITE, *args, **kwargs)

class BlackKing(base.Unit, piece.King):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.BLACK, *args, **kwargs)
