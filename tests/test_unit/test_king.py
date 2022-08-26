

from chess.color import Color
from chess.move import Move
from chess.piece import King
from chess.square import Square
from chess.unit import WhiteKing, BlackKing


def test_white_king_init():
    king = WhiteKing()
    assert king.color == Color.WHITE
    assert isinstance(king, King)

def test_black_king_init():
    king = BlackKing()
    assert king.color == Color.BLACK
    assert isinstance(king, King)

