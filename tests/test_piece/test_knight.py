import pytest
import chess.piece as piece

from chess.color import Color


def test_init():
    assert piece.Knight(Color.WHITE)
