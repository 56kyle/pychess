
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteBishop(base.Unit, piece.Bishop):
    color: Color = Color.WHITE

class BlackBishop(base.Unit, piece.Bishop):
    color: Color = Color.BLACK
