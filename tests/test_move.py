
import pytest
import chess.piece as piece
import chess.move as move
import chess.unit as unit

from chess.color import Color
from chess.square import Square


def test_move_init_with_no_removed_and_no_promotion():
    move.Move(unit.WhitePawn(), from_square=Square(row=0, column=0), to_square=Square(row=0, column=1))

def test_move_init_with_removed_and_no_promotion():
    move.Move(unit.WhitePawn(), from_square=Square(row=0, column=0), to_square=Square(row=0, column=1), captured=unit.BlackPawn())

def test_move_init_with_no_removed_and_promotion():
    move.Move(unit.WhitePawn(), from_square=Square(row=0, column=0), to_square=Square(row=0, column=1), promotion=unit.BlackPawn())

def test_move_init_with_removed_and_promotion():
    move.Move(
        unit.WhitePawn(),
        from_square=Square(row=0, column=0),
        to_square=Square(row=0, column=1),
        captured=unit.BlackPawn(),
        promotion=unit.BlackPawn(),
    )





