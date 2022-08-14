
import pytest
import chess.game as game
import chess.piece as piece


def test_init():
    assert game


def test_add_piece(base_game):
    base_game.add_piece(0, 0, piece.ChessPiece())

