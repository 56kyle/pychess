
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteQueen(base.Unit, piece.Queen):
    color: Color = Color.WHITE

class BlackQueen(base.Unit, piece.Queen):
    color: Color = Color.BLACK
