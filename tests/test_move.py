
import pytest
import chess.piece as piece
import chess.move as move

from chess.color import Color


def test_move_init_with_no_removed_and_no_promotion():
    move.Move(piece.ChessPiece(Color.WHITE), 0, 0, 1, 0)

def test_move_init_with_removed_and_no_promotion():
    move.Move(piece.ChessPiece(Color.WHITE), 0, 0, 1, 0, captured_piece=piece.ChessPiece(Color.BLACK))

def test_move_init_with_no_removed_and_promotion():
    move.Move(piece.ChessPiece(Color.WHITE), 0, 0, 1, 0, promotion=piece.ChessPiece(Color.BLACK))

def test_move_init_with_removed_and_promotion():
    move.Move(
        piece.ChessPiece(Color.WHITE),
        0,
        0,
        1,
        0,
        captured_piece=piece.ChessPiece(Color.BLACK),
        promotion=piece.ChessPiece(Color.BLACK)
    )





