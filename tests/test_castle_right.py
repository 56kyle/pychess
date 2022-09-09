
import pytest

from chess.castle_right import CastleRight
from chess.color import Color
from chess.side import Side


def test_castle_right_init():
    castle_right = CastleRight(color=Color.WHITE, side=Side.KING)
    assert castle_right
    assert castle_right.color == Color.WHITE
    assert castle_right.side == Side.KING


