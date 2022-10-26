
import pytest

from chess.position import Position


def test_init():
    position = Position(1, 2)
    assert position
    assert position.file == 1
    assert position.rank == 2

def test_offset():
    position = Position(1, 2)
    assert position.offset(dx=1, dy=2) == Position(2, 4)


def test_distance_to_with_whole_answer():
    position = Position(1, 1)
    assert position.distance_to(position=Position(4, 5)) == 5.0

def test_distance_to_with_fraction_answer():
    position = Position(1, 2)
    assert position.distance_to(position=Position(3, 4)) == 2.8284271247461903

