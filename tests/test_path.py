
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

def test_limit_to_shape_with_infinite_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path.limit_to_shape(height=10, width=10) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test_limit_to_shape_with_limited_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=20)
    assert path.limit_to_shape(height=10, width=10) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test__get_shape_limited_steps_with_infinite_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path._get_shape_limited_steps(height=10, width=10) == 10

def test__get_shape_limited_steps_with_limited_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=20)
    assert path._get_shape_limited_steps(height=10, width=10) == 10

def test__get_shape_limited_steps_with_limited_max_steps_due_to_height():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path._get_shape_limited_steps(height=10, width=1000) == 10

def test__get_shape_limited_steps_with_limited_max_steps_due_to_width():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path._get_shape_limited_steps(height=1000, width=10) == 10

def test_limit_to_height_with_infinite_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path.limit_to_height(height=10) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test_limit_to_height_with_limited_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=20)
    assert path.limit_to_height(height=10) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test_limit_to_height_with_limited_max_steps_and_height_steps_larger_than_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=10)
    assert path.limit_to_height(height=1000) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test__get_height_limited_steps_with_infinite_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path._get_height_limited_steps(height=10) == 10

def test__get_height_limited_steps_with_limited_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=20)
    assert path._get_height_limited_steps(height=10) == 10

def test__get_height_limited_steps_with_limited_max_steps_and_height_steps_larger_than_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=10)
    assert path._get_height_limited_steps(height=1000) == 10

def test_limit_to_width_with_infinite_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path.limit_to_width(width=10) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test_limit_to_width_with_limited_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=20)
    assert path.limit_to_width(width=10) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test_limit_to_width_with_limited_max_steps_and_width_steps_larger_than_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=10)
    assert path.limit_to_width(width=1000) == Path(offset=Offset(dy=1, dx=1), max_steps=10)

def test__get_width_limited_steps_with_infinite_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=INFINITE_STEPS)
    assert path._get_width_limited_steps(width=10) == 10

def test__get_width_limited_steps_with_limited_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=20)
    assert path._get_width_limited_steps(width=10) == 10

def test__get_width_limited_steps_with_limited_max_steps_and_width_steps_larger_than_max_steps():
    path = Path(offset=Offset(dy=1, dx=1), max_steps=10)
    assert path._get_width_limited_steps(width=1000) == 10


