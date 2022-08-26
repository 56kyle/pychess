from typing import Set

from chess.color import Color
from chess.movement import Movement, INFINITE_STEPS
from chess.offset import LINEAR
from chess.piece import Rook
from chess.unit import Unit


ROOK_MOVEMENTS: Set[Movement] = {Movement(offset=offset, max_steps=INFINITE_STEPS) for offset in LINEAR}


class WhiteRook(Unit, Rook):
    color: Color = Color.WHITE
    movements: Set[Movement] = ROOK_MOVEMENTS


class BlackRook(Unit, Rook):
    color: Color = Color.BLACK
    movements: Set[Movement] = ROOK_MOVEMENTS

