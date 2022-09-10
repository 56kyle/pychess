
import pytest


from chess.offset import Offset
from chess.position import Position


def test_init():
    position = Position(1, 2)
    assert position
    assert position.file == 1
    assert position.rank == 2

def test_init_with_negative_file():
    with pytest.raises(ValueError):
        Position(-1, 2)

def test_init_with_negative_rank():
    with pytest.raises(ValueError):
        Position(1, -2)

def test_offset():
    position = Position(1, 2)
    offset = Offset(1, 2)
    assert position.offset(offset) == Position(2, 4)
