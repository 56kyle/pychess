
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteRook(base.Unit, piece.Rook):
    color: Color = Color.WHITE

    def _get_unvalidated_move_coverage_offsets(self):
        pass


class BlackRook(base.Unit, piece.Rook):
    color: Color = Color.BLACK

    def _get_unvalidated_move_coverage_offsets(self):
        pass

