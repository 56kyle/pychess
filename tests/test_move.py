
import pytest

import chess.move as move
import chess.unit as unit

from chess.offset import RIGHT
from chess.square import Square


def test_move_init_with_no_removed_and_no_promotion():
    move.Move(unit.WhiteRook(), from_square=Square(row=0, column=0), offset=RIGHT)

def test_move_init_with_removed_and_no_promotion():
    move.Move(unit.WhiteRook(), from_square=Square(row=0, column=0), offset=RIGHT, captured=unit.BlackPawn())

def test_move_init_with_no_removed_and_promotion():
    move.Move(unit.WhiteRook(), from_square=Square(row=0, column=0), offset=RIGHT, promotion=unit.BlackPawn())

def test_move_init_with_removed_and_promotion():
    move.Move(
        unit=unit.WhiteRook(),
        from_square=Square(row=0, column=0),
        offset=RIGHT,
        captured=unit.BlackPawn(),
        promotion=unit.BlackPawn(),
    )





