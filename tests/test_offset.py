
from chess.offset import Offset


def test_with_no_offset():
    assert Offset() == Offset()

def test_eq_with_same_offset():
    assert Offset(dy=1, dx=1) == Offset(dy=1, dx=1)

def test_eq_with_different_dy_and_same_dx():
    assert not Offset(dy=1, dx=0) == Offset(dy=0, dx=0)

def test_eq_with_same_dy_and_different_dx():
    assert not Offset(dy=0, dx=1) == Offset(dy=0, dx=0)

