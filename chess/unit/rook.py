
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteRook(base.Unit, piece.Rook):
    color: Color = Color.WHITE

class BlackRook(base.Unit, piece.Rook):
    color: Color = Color.BLACK
