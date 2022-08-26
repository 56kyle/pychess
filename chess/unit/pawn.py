
from typing import Set

from chess.color import Color
from chess.movement import Movement, AllowedMovementTypes
from chess.offset import UP, DOWN, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT
from chess.piece import Pawn
from chess.unit import Unit


WHITE_PAWN_FIRST_MOVEMENT = Movement(offset=UP*2, max_steps=1, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
WHITE_PAWN_STANDARD_MOVEMENT = Movement(offset=UP, max_steps=1, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
WHITE_PAWN_CAPTURE_MOVEMENTS = {
    Movement(
        offset=offset,
        max_steps=1,
        allowed_movement_types=AllowedMovementTypes.CAPTURE_ONLY,
    ) for offset in {UP_RIGHT, UP_LEFT}
}
WHITE_PAWN_MOVEMENTS = {WHITE_PAWN_FIRST_MOVEMENT, WHITE_PAWN_STANDARD_MOVEMENT} | WHITE_PAWN_CAPTURE_MOVEMENTS

BLACK_PAWN_FIRST_MOVEMENT = Movement(offset=DOWN*2, max_steps=1, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
BLACK_PAWN_STANDARD_MOVEMENT = Movement(offset=DOWN, max_steps=1, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
BLACK_PAWN_CAPTURE_MOVEMENTS = {
    Movement(
        offset=offset,
        max_steps=1,
        allowed_movement_types=AllowedMovementTypes.CAPTURE_ONLY
    ) for offset in {DOWN_RIGHT, DOWN_LEFT}
}
BLACK_PAWN_MOVEMENTS = {BLACK_PAWN_FIRST_MOVEMENT, BLACK_PAWN_STANDARD_MOVEMENT} | BLACK_PAWN_CAPTURE_MOVEMENTS


class WhitePawn(Unit, Pawn):
    color: Color = Color.WHITE
    movements: Set[Movement] = WHITE_PAWN_MOVEMENTS


class BlackPawn(Unit, Pawn):
    color: Color = Color.BLACK
    movements: Set[Movement] = BLACK_PAWN_MOVEMENTS

