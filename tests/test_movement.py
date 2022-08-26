
import pytest


from chess.color import Color
from chess.move import Move
from chess.movement import Movement, INFINITE_STEPS
from chess.offset import Offset


def test_init():
    movement = Movement()
    assert movement.offset == Offset(0, 0)
    assert movement.max_steps == INFINITE_STEPS
    assert not movement.move_only
    assert not movement.capture_only



