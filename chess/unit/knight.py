
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteKnight(base.Unit, piece.Knight):
    color: Color = Color.WHITE

    def _get_unvalidated_move_coverage_offsets(self):
        pass


class BlackKnight(base.Unit, piece.Knight):
    color: Color = Color.BLACK

    def _get_unvalidated_move_coverage_offsets(self):
        pass

