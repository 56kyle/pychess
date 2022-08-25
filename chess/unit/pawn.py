
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhitePawn(base.Unit, piece.Pawn):
    color: Color = Color.WHITE

class BlackPawn(base.Unit, piece.Pawn):
    color: Color = Color.BLACK
