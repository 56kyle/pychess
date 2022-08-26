
import pytest

from chess.offset import (
    Offset,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    UP_LEFT,
    UP_RIGHT,
    DOWN_LEFT,
    DOWN_RIGHT,
    VERTICAL,
    HORIZONTAL,
    LINEAR,
    DIAGONAL,
)


def test_with_no_offset():
    assert Offset() == Offset()

def test_eq_with_same_offset():
    assert Offset(dy=1, dx=1) == Offset(dy=1, dx=1)

def test_eq_with_different_dy_and_same_dx():
    assert not Offset(dy=1, dx=0) == Offset(dy=0, dx=0)

def test_eq_with_same_dy_and_different_dx():
    assert not Offset(dy=0, dx=1) == Offset(dy=0, dx=0)

def test_eq_with_different_dy_and_different_dx():
    assert not Offset(dy=1, dx=1) == Offset(dy=0, dx=0)

def test_eq_with_int():
    assert not Offset(dy=1, dx=1) == 1

def test_add_with_offset():
    assert Offset(dy=1, dx=1) + Offset(dy=1, dx=1) == Offset(dy=2, dx=2)

def test_add_with_int():
    assert Offset(dy=1, dx=1) + 1 == Offset(dy=2, dx=2)

def test_add_with_int_string():
    assert Offset(dy=1, dx=1) + '1' == Offset(dy=2, dx=2)

def test_add_with_non_int_string():
    with pytest.raises(ValueError):
        Offset(dy=1, dx=1) + 'a'

def test_sub_with_offset():
    assert Offset(dy=1, dx=1) - Offset(dy=1, dx=1) == Offset(dy=0, dx=0)

def test_sub_with_int():
    assert Offset(dy=1, dx=1) - 1 == Offset(dy=0, dx=0)

def test_sub_with_int_string():
    assert Offset(dy=1, dx=1) - '1' == Offset(dy=0, dx=0)

def test_sub_with_non_int_string():
    with pytest.raises(ValueError):
        Offset(dy=1, dx=1) - 'a'

def test_mul_with_offset():
    assert Offset(dy=1, dx=1) * Offset(dy=1, dx=1) == Offset(dy=1, dx=1)

def test_is_linear():
    assert UP.is_linear()
    assert DOWN.is_linear()
    assert LEFT.is_linear()
    assert RIGHT.is_linear()
    assert not UP_LEFT.is_linear()
    assert not UP_RIGHT.is_linear()
    assert not DOWN_LEFT.is_linear()
    assert not DOWN_RIGHT.is_linear()

def test_is_diagonal():
    assert UP_LEFT.is_diagonal()
    assert UP_RIGHT.is_diagonal()
    assert DOWN_LEFT.is_diagonal()
    assert DOWN_RIGHT.is_diagonal()
    assert not UP.is_diagonal()
    assert not DOWN.is_diagonal()
    assert not LEFT.is_diagonal()
    assert not RIGHT.is_diagonal()

def test_up():
    assert UP == Offset(dy=-1, dx=0)

def test_down():
    assert DOWN == Offset(dy=1, dx=0)

def test_left():
    assert LEFT == Offset(dy=0, dx=-1)

def test_right():
    assert RIGHT == Offset(dy=0, dx=1)

def test_up_left():
    assert UP_LEFT == Offset(dy=-1, dx=-1)

def test_up_right():
    assert UP_RIGHT == Offset(dy=-1, dx=1)

def test_down_left():
    assert DOWN_LEFT == Offset(dy=1, dx=-1)

def test_down_right():
    assert DOWN_RIGHT == Offset(dy=1, dx=1)

def test_vertical():
    assert UP in VERTICAL
    assert DOWN in VERTICAL

def test_horizontal():
    assert LEFT in HORIZONTAL
    assert RIGHT in HORIZONTAL

def test_linear():
    assert UP in LINEAR
    assert DOWN in LINEAR
    assert LEFT in LINEAR
    assert RIGHT in LINEAR

def test_diagonal():
    assert UP_LEFT in DIAGONAL
    assert UP_RIGHT in DIAGONAL
    assert DOWN_LEFT in DIAGONAL
    assert DOWN_RIGHT in DIAGONAL


