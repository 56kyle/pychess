
import pytest

from chess.line import Line
from chess.position import Position


def test_init():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line
    assert line.p1 == Position(1, 2)
    assert line.p2 == Position(2, 4)

def test_init_validates_with_valid():
    assert Line(p1=Position(1, 2), p2=Position(2, 4))

def test_init_validates_with_invalid():
    with pytest.raises(ValueError):
        Line(p1=Position(1, 2), p2=Position(1, 2))


def test_validate_with_valid():
    Line(p1=Position(1, 2), p2=Position(2, 4)).validate()

def test_validate_with_p1_eq_p2():
    with pytest.raises(ValueError):
        Line(p1=Position(1, 2), p2=Position(1, 2)).validate()

def test__validate_points_are_different():
    with pytest.raises(ValueError):
        Line(p1=Position(1, 2), p2=Position(1, 2))._validate_points_are_different()


def test_contains_with_colinear_external_left():
    assert Position(0, 0) in Line(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_colinear_p1():
    assert Position(1, 2) in Line(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_colinear_internal():
    assert Position(2, 4) in Line(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_colinear_p2():
    assert Position(3, 6) in Line(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_colinear_external_right():
    assert Position(4, 8) in Line(p1=Position(1, 2), p2=Position(3, 6))

def test_offset_with_positive():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.offset(dx=1, dy=1) == Line(p1=Position(2, 3), p2=Position(3, 5))

def test_offset_with_negative():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.offset(dx=-1, dy=-1) == Line(p1=Position(0, 1), p2=Position(1, 3))

def test_offset_with_zero():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.offset(dx=0, dy=0) == Line(p1=Position(1, 2), p2=Position(2, 4))

def test_parallel_to_with_same_line():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.parallel_to(line=line)

def test_parallel_to_with_colinear():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.parallel_to(line=Line(p1=Position(3, 6), p2=Position(4, 8)))

def test_parallel_to_with_parallel_non_colinear():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.parallel_to(line=Line(p1=Position(1, 3), p2=Position(2, 5)))








