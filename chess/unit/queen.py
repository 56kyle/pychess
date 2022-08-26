

from typing import Set

from chess.color import Color
from chess.movement import Movement, INFINITE_STEPS
from chess.offset import LINEAR, DIAGONAL
from chess.piece import Queen
from chess.unit import Unit


QUEEN_MOVEMENTS: Set[Movement] = {Movement(offset=offset, max_steps=INFINITE_STEPS) for offset in LINEAR | DIAGONAL}


class WhiteQueen(Unit, Queen):
    color: Color = Color.WHITE
    movements: Set[Movement] = QUEEN_MOVEMENTS


class BlackQueen(Unit, Queen):
    color: Color = Color.BLACK
    movements: Set[Movement] = QUEEN_MOVEMENTS

