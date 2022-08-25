from chess.color import Color
from chess.move import Move
from chess.piece import Rook
from chess.square import Square
from chess.unit import WhiteRook, BlackRook


def test_white_rook_init():
    rook = WhiteRook()
    assert rook.color == Color.WHITE
    assert isinstance(rook, Rook)

def test_black_rook_init():
    rook = BlackRook()
    assert rook.color == Color.BLACK
    assert isinstance(rook, Rook)
