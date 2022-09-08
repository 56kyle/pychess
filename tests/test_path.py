
import pytest


from chess.color import Color
from chess.move import Move
from chess.path import Path, INFINITE_STEPS, AllowedPathTypes
from chess.offset import Offset


def test_init():
    path = Path()
    assert path.offset == Offset(0, 0)
    assert path.max_steps == INFINITE_STEPS
    assert path.allowed_path_types == AllowedPathTypes.BOTH



