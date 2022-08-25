from chess.color import Color
from chess.move import Move
from chess.piece import Knight
from chess.square import Square
from chess.unit import WhiteKnight, BlackKnight


def test_white_knight_init():
    knight = WhiteKnight()
    assert knight.color == Color.WHITE
    assert isinstance(knight, Knight)

def test_black_knight_init():
    knight = BlackKnight()
    assert knight.color == Color.BLACK
    assert isinstance(knight, Knight)
