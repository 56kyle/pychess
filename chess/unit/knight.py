
from typing import Set

from chess.color import Color
from chess.movement import Movement
from chess.offset import UP, DOWN, RIGHT, LEFT
from chess.piece import Knight
from chess.unit import Unit


UP_UP_RIGHT = Movement(offset=UP*2 + RIGHT, max_steps=1)
UP_RIGHT_RIGHT = Movement(offset=UP + RIGHT*2, max_steps=1)
DOWN_RIGHT_RIGHT = Movement(offset=DOWN + RIGHT*2, max_steps=1)
DOWN_DOWN_RIGHT = Movement(offset=DOWN*2 + RIGHT, max_steps=1)
DOWN_DOWN_LEFT = Movement(offset=DOWN*2 + LEFT, max_steps=1)
DOWN_LEFT_LEFT = Movement(offset=DOWN + LEFT*2, max_steps=1)
UP_LEFT_LEFT = Movement(offset=UP + LEFT*2, max_steps=1)
UP_UP_LEFT = Movement(offset=UP*2 + LEFT, max_steps=1)

KNIGHT_MOVEMENTS = {
    UP_UP_RIGHT,
    UP_RIGHT_RIGHT,
    DOWN_RIGHT_RIGHT,
    DOWN_DOWN_RIGHT,
    DOWN_DOWN_LEFT,
    DOWN_LEFT_LEFT,
    UP_LEFT_LEFT,
    UP_UP_LEFT,
}


class WhiteKnight(Unit, Knight):
    color: Color = Color.WHITE
    movements: Set[Movement] = KNIGHT_MOVEMENTS


class BlackKnight(Unit, Knight):
    color: Color = Color.BLACK
    movements: Set[Movement] = KNIGHT_MOVEMENTS

