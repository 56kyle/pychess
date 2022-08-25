
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteRook(base.Unit, piece.Rook):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.WHITE, *args, **kwargs)

class BlackRook(base.Unit, piece.Rook):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.BLACK, *args, **kwargs)
