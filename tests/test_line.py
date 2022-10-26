
import pytest


from chess.line import Line
from chess.position import Position


def test_init():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line
    assert line.p1 == Position(1, 2)
    assert line.p2 == Position(2, 4)


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

def test_offset():
    line = Line(p1=Position(1, 2), p2=Position(2, 4))
    assert line.offset(dx=1, dy=1) == Line(p1=Position(2, 3), p2=Position(3, 5))
