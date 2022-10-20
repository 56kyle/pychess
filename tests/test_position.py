
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
