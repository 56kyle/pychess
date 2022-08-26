
from typing import Set

from chess.color import Color
from chess.movement import Movement, AllowedMovementTypes
from chess.offset import RIGHT, LEFT, LINEAR, DIAGONAL
from chess.piece import King
from chess.unit import Unit


KING_SIDE_CASTLE_MOVEMENT = Movement(offset=RIGHT*2, max_steps=1, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
QUEEN_SIDE_CASTLE_MOVEMENT = Movement(offset=LEFT*3, max_steps=1, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
CASTLE_MOVEMENTS = {KING_SIDE_CASTLE_MOVEMENT, QUEEN_SIDE_CASTLE_MOVEMENT}

STANDARD_KING_MOVEMENTS = {Movement(offset=offset, max_steps=1) for offset in LINEAR | DIAGONAL}
KING_MOVEMENTS = STANDARD_KING_MOVEMENTS | CASTLE_MOVEMENTS


class WhiteKing(Unit, King):
    color: Color = Color.WHITE
    movements: Set[Movement] = KING_MOVEMENTS


class BlackKing(Unit, King):
    color: Color = Color.BLACK
    movements: Set[Movement] = KING_MOVEMENTS

