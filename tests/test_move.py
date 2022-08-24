
import pytest
import chess.piece as piece
import chess.move as move

from chess.color import Color
from chess.square import Square


def test_move_init_with_no_removed_and_no_promotion():
    move.Move(piece.WhitePawn, from_square=Square(row=0, column=0), to_square=Square(row=0, column=1))

def test_move_init_with_removed_and_no_promotion():
    move.Move(piece.WhitePawn, from_square=Square(row=0, column=0), to_square=Square(row=0, column=1), captured_piece=piece.BlackPawn)

def test_move_init_with_no_removed_and_promotion():
    move.Move(piece.WhitePawn, from_square=Square(row=0, column=0), to_square=Square(row=0, column=1), promotion=piece.BlackPawn)

def test_move_init_with_removed_and_promotion():
    move.Move(
        piece.WhitePawn,
        from_square=Square(row=0, column=0),
        to_square=Square(row=0, column=1),
        captured_piece=piece.BlackPawn,
        promotion=piece.BlackPawn
    )





