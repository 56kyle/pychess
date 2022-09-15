
import pytest

from chess.board import Board


def test_init(dummy_board_data):
    assert Board(**dummy_board_data.__dict__)


