

import pytest

from chess.offset import Offset
from chess.position import Position


def test_get_max_steps(dummy_board):
    assert dummy_board.get_max_steps(position=Position(rank=1, file=1), offset=Offset(1, 1)) == 7


