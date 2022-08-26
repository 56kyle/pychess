
import chess.unit.base as base
import chess.piece as piece

from typing import Set

from chess.color import Color
from chess.movement import Movement
from chess.offset import (
    UP,
    DOWN,
    UP_RIGHT,
    UP_LEFT,
    DOWN_RIGHT,
    DOWN_LEFT,
)


WHITE_PAWN_FIRST_MOVEMENT = Movement(offset=UP*2, max_steps=1)
WHITE_PAWN_STANDARD_MOVEMENT = Movement(offset=UP, max_steps=1)
WHITE_PAWN_CAPTURE_MOVEMENTS = {Movement(offset=offset, max_steps=1) for offset in {UP_RIGHT, UP_LEFT}}
WHITE_PAWN_MOVEMENTS = {WHITE_PAWN_FIRST_MOVEMENT, WHITE_PAWN_STANDARD_MOVEMENT} | WHITE_PAWN_CAPTURE_MOVEMENTS

BLACK_PAWN_FIRST_MOVEMENT = Movement(offset=DOWN*2, max_steps=1)
BLACK_PAWN_STANDARD_MOVEMENT = Movement(offset=DOWN, max_steps=1)
BLACK_PAWN_CAPTURE_MOVEMENTS = {Movement(offset=offset, max_steps=1) for offset in {DOWN_RIGHT, DOWN_LEFT}}
BLACK_PAWN_MOVEMENTS = {BLACK_PAWN_FIRST_MOVEMENT, BLACK_PAWN_STANDARD_MOVEMENT} | BLACK_PAWN_CAPTURE_MOVEMENTS


class WhitePawn(base.Unit, piece.Pawn):
    color: Color = Color.WHITE
    movements: Set[Movement] = WHITE_PAWN_MOVEMENTS


class BlackPawn(base.Unit, piece.Pawn):
    color: Color = Color.BLACK
    movements: Set[Movement] = BLACK_PAWN_MOVEMENTS

