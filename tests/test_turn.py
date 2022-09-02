
import pytest

from chess.color import Color
from chess.move import Move
from chess.square import Square
from chess.turn import Turn
from chess.unit import WhitePawn


def test_turn_init():
    e2: Square = Square(row=6, column=4)
    e4: Square = Square(row=4, column=4)
    move: Move = Move(unit=WhitePawn(), from_square=e2, to_square=e4)
    turn = Turn(
        color=Color.WHITE,
        move=move,
        time_spent=10.5,
    )
    assert turn.color == Color.WHITE
    assert turn.move == move
    assert turn.time_spent == 10.5




