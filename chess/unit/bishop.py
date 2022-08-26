from typing import Set

import chess.unit.base as base
import chess.piece as piece

from chess.color import Color
from chess.movement import Movement, INFINITE_STEPS
from chess.offset import Offset, DIAGONAL


BISHOP_MOVEMENTS: Set[Movement] = {Movement(offset=offset, max_steps=INFINITE_STEPS) for offset in DIAGONAL}

class WhiteBishop(base.Unit, piece.Bishop):
    color: Color = Color.WHITE
    movements: Set[Movement] = BISHOP_MOVEMENTS


class BlackBishop(base.Unit, piece.Bishop):
    color: Color = Color.BLACK
    movements: Set[Movement] = BISHOP_MOVEMENTS

