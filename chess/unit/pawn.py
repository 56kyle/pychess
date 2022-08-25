
import chess.unit.base as base
import chess.piece as piece

from chess.color import Color

class WhitePawn(base.Unit, piece.Pawn):
    color: Color = Color.WHITE

    def _get_unvalidated_move_coverage_offsets(self):
        pass


class BlackPawn(base.Unit, piece.Pawn):
    color: Color = Color.BLACK

    def _get_unvalidated_move_coverage_offsets(self):
        pass

