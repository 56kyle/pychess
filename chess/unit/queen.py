
import chess.unit.base as base
import chess.piece as piece

from typing import Set

from chess.color import Color
from chess.movement import (
    Movement,
    INFINITE_STEPS,
)
from chess.offset import (
    LINEAR,
    DIAGONAL,
)


QUEEN_MOVEMENTS: Set[Movement] = {Movement(offset=offset, max_steps=INFINITE_STEPS) for offset in LINEAR | DIAGONAL}


class WhiteQueen(base.Unit, piece.Queen):
    color: Color = Color.WHITE
    movements: Set[Movement] = QUEEN_MOVEMENTS


class BlackQueen(base.Unit, piece.Queen):
    color: Color = Color.BLACK
    movements: Set[Movement] = QUEEN_MOVEMENTS

