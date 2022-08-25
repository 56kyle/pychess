from chess.color import Color
from chess.move import Move
from chess.piece import Queen
from chess.square import Square
from chess.unit import WhiteQueen, BlackQueen


def test_white_queen_init():
    queen = WhiteQueen()
    assert queen.color == Color.WHITE
    assert isinstance(queen, Queen)

def test_black_queen_init():
    queen = BlackQueen()
    assert queen.color == Color.BLACK
    assert isinstance(queen, Queen)
