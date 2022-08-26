
import pytest


from chess.color import Color
from chess.move import Move
from chess.movement import Movement, INFINITE_STEPS, AllowedMovementTypes
from chess.offset import Offset


def test_init():
    movement = Movement()
    assert movement.offset == Offset(0, 0)
    assert movement.max_steps == INFINITE_STEPS
    assert movement.allowed_movement_types == AllowedMovementTypes.BOTH

def test_with_limited_max_steps_with_infinite_starting_max_steps():
    movement = Movement(offset=Offset(dy=5, dx=5), max_steps=INFINITE_STEPS)
    assert movement.with_limited_max_steps(max_steps=10) == Movement(Offset(dy=5, dx=5), max_steps=10)

def test_with_limited_max_steps_with_limited_starting_max_steps():
    movement = Movement(offset=Offset(dy=5, dx=5), max_steps=20)
    assert movement.with_limited_max_steps(max_steps=10) == Movement(Offset(dy=5, dx=5), max_steps=10)



