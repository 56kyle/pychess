
import pytest

from chess.color import Color
from chess.unit import WhiteBishop, BlackBishop, BISHOP_PATHS


def test_white_bishop_init():
    bishop = WhiteBishop()
    assert bishop.color == Color.WHITE

def test_black_bishop_init():
    bishop = BlackBishop()
    assert bishop.color == Color.BLACK
    assert bishop.paths == BISHOP_PATHS

