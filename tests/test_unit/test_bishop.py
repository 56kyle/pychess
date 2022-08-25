
import pytest

from chess.color import Color
from chess.move import Move
from chess.piece import Bishop
from chess.square import Square
from chess.unit import WhiteBishop, BlackBishop


def test_init():
    assert BlackBishop()

