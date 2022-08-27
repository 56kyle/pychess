
import pytest


from chess.color import Color
from chess.move import Move
from chess.path import Path, INFINITE_STEPS, AllowedMovementTypes
from chess.offset import Offset


def test_init():
    path = Path()
    assert path.offset == Offset(0, 0)
    assert path.max_steps == INFINITE_STEPS
    assert path.allowed_path_types == AllowedMovementTypes.BOTH

def test_with_limited_max_steps_with_infinite_starting_max_steps():
    path = Path(offset=Offset(dy=5, dx=5), max_steps=INFINITE_STEPS)
    assert path.with_limited_max_steps(max_steps=10) == Path(Offset(dy=5, dx=5), max_steps=10)

def test_with_limited_max_steps_with_limited_starting_max_steps():
    path = Path(offset=Offset(dy=5, dx=5), max_steps=20)
    assert path.with_limited_max_steps(max_steps=10) == Path(Offset(dy=5, dx=5), max_steps=10)



