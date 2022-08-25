
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color
from chess.offset import Offset
from chess.square import Square


class WhiteBishop(base.Unit, piece.Bishop):
    color: Color = Color.WHITE

    def _get_unvalidated_move_coverage_offsets(self):
        pass

class BlackBishop(base.Unit, piece.Bishop):
    color: Color = Color.BLACK

    def _get_unvalidated_move_coverage_offsets(self):
        pass
