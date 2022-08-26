
import chess.unit.base as base
import chess.piece as piece

from typing import Set

from chess.color import Color
from chess.movement import (
    Movement,
    INFINITE_STEPS,
)
from chess.offset import LINEAR


ROOK_MOVEMENTS: Set[Movement] = {Movement(offset=offset, max_steps=INFINITE_STEPS) for offset in LINEAR}


class WhiteRook(base.Unit, piece.Rook):
    color: Color = Color.WHITE
    movements: Set[Movement] = ROOK_MOVEMENTS


class BlackRook(base.Unit, piece.Rook):
    color: Color = Color.BLACK
    movements: Set[Movement] = ROOK_MOVEMENTS

