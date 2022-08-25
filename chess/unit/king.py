
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteKing(base.Unit, piece.King):
    color: Color = Color.WHITE

class BlackKing(base.Unit, piece.King):
    color: Color = Color.BLACK
