
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteKnight(base.Unit, piece.Knight):
    color: Color = Color.WHITE

class BlackKnight(base.Unit, piece.Knight):
    color: Color = Color.BLACK
