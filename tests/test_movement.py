
import pytest


from chess.color import Color
from chess.move import Move
from chess.movement import Movement
from chess.offset import Offset


def test_init():
    movement = Movement()
    assert movement.offset == Offset(0, 0)


