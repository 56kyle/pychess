
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhitePawn(base.Unit, piece.Pawn):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.WHITE, *args, **kwargs)

class BlackPawn(base.Unit, piece.Pawn):
    def __init__(self, *args, **kwargs):
        super().__init__(Color.BLACK, *args, **kwargs)
