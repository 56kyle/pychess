from chess.color import Color
from chess.move import Move
from chess.piece import Pawn
from chess.square import Square
from chess.unit import WhitePawn, BlackPawn


def test_white_pawn_init():
    pawn = WhitePawn()
    assert pawn.color == Color.WHITE
    assert isinstance(pawn, Pawn)

def test_black_pawn_init():
    pawn = BlackPawn()
    assert pawn.color == Color.BLACK
    assert isinstance(pawn, Pawn)
