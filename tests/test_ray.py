
import pytest


from chess.position import Position
from chess.ray import Ray


def test_init():
    ray = Ray(p1=Position(1, 2), p2=Position(3, 6))
    assert ray
    assert ray.p1 == Position(1, 2)
    assert ray.p2 == Position(3, 6)

def test_contains_with_colinear_internal():
    assert Position(2, 4) in Ray(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_colinear_external_same_direction():
    assert Position(4, 8) in Ray(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_colinear_external_opposite_direction():
    assert Position(0, 0) not in Ray(p1=Position(1, 2), p2=Position(3, 6))

def test_contains_with_non_colinear_internal():
    assert Position(2, 5) not in Ray(p1=Position(1, 2), p2=Position(3, 6))



