
import pytest
import chess.piece as piece
import chess.move as move

from chess.color import Color


def test_move_init_with_no_removed_and_no_promotion():
    move.Move(piece.WhitePawn, 0, 0, 1, 0)

def test_move_init_with_removed_and_no_promotion():
    move.Move(piece.WhitePawn, 0, 0, 1, 0, captured_piece=piece.BlackPawn)

def test_move_init_with_no_removed_and_promotion():
    move.Move(piece.WhitePawn, 0, 0, 1, 0, promotion=piece.BlackPawn)

def test_move_init_with_removed_and_promotion():
    move.Move(
        piece.WhitePawn,
        0,
        0,
        1,
        0,
        captured_piece=piece.BlackPawn,
        promotion=piece.BlackPawn
    )





