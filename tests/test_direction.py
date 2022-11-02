
import pytest
import math

from chess.direction import Direction


def test__eq_same_theta_with_same():
    direction1 = Direction(radians=1)
    direction2 = Direction(radians=1)
    assert direction1._eq_same_theta(direction2)

def test__eq_same_theta_with_different():
    direction1 = Direction(radians=1)
    direction2 = Direction(radians=2)
    assert not direction1._eq_same_theta(direction2)

def test__eq_same_theta_with_opposite():
    direction1 = Direction(radians=1)
    direction2 = Direction(radians=math.pi + 1)
    assert not direction1._eq_same_theta(direction2)

def test__eq_opposite_theta_with_same():
    direction1 = Direction(radians=1)
    direction2 = Direction(radians=1)
    assert not direction1._eq_opposite_theta(direction2)

def test__eq_opposite_theta_with_different():
    direction1 = Direction(radians=1)
    direction2 = Direction(radians=2)
    assert not direction1._eq_opposite_theta(direction2)

def test__eq_opposite_theta_with_opposite():
    direction1 = Direction(radians=1)
    direction2 = Direction(radians=math.pi + 1)
    assert direction1._eq_opposite_theta(direction2)


