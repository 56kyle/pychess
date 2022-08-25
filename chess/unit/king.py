
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhiteKing(base.Unit, piece.King):
    color: Color = Color.WHITE

    def _get_unvalidated_move_coverage_offsets(self):
        pass


class BlackKing(base.Unit, piece.King):
    color: Color = Color.BLACK

    def _get_unvalidated_move_coverage_offsets(self):
        pass

