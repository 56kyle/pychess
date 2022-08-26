from typing import Set

from chess.color import Color
from chess.movement import Movement, INFINITE_STEPS
from chess.offset import DIAGONAL
from chess.piece import Bishop
from chess.unit import Unit


BISHOP_MOVEMENTS: Set[Movement] = {Movement(offset=offset, max_steps=INFINITE_STEPS) for offset in DIAGONAL}

class WhiteBishop(Unit, Bishop):
    color: Color = Color.WHITE
    movements: Set[Movement] = BISHOP_MOVEMENTS


class BlackBishop(Unit, Bishop):
    color: Color = Color.BLACK
    movements: Set[Movement] = BISHOP_MOVEMENTS

