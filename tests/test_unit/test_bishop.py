
import pytest

from chess.color import Color
from chess.move import Move
from chess.piece import Bishop
from chess.square import Square
from chess.unit import WhiteBishop, BlackBishop


def test_white_bishop_init():
    bishop = WhiteBishop()
    assert bishop.color == Color.WHITE
    assert isinstance(bishop, Bishop)

def test_black_bishop_init():
    bishop = BlackBishop()
    assert bishop.color == Color.BLACK
    assert isinstance(bishop, Bishop)


