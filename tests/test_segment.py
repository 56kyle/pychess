

import pytest

from chess.position import Position
from chess.segment import Segment


def test_init():
    assert Segment(p1=Position(1, 2), p2=Position(2, 4))


def test_contains_with_colinear_internal():
    assert Position(1, 2) in Segment(p1=Position(1, 2), p2=Position(2, 4))

def test_contains_with_colinear_external_left():
    assert Position(0, 0) not in Segment(p1=Position(1, 2), p2=Position(2, 4))

def test_contains_with_colinear_external_right():
    assert Position(3, 6) not in Segment(p1=Position(1, 2), p2=Position(2, 4))




