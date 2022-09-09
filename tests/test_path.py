
import pytest

from chess.move import Move
from chess.offset import UP
from chess.path import Path, INFINITY


def test_path_init_with_defaults():
    path = Path(offset=UP)
    assert path
    assert path.offset == UP
    assert path.steps is INFINITY

def test_path_init_with_values():
    path = Path(offset=UP, steps=1)
    assert path
    assert path.offset == UP
    assert path.steps == 1

