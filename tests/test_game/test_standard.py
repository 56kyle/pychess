
import pytest
import chess.game as game
import chess.piece as piece

from chess.color import Color


def test_init(standard_empty_board):
    assert game.Standard(standard_empty_board)


def test_add_piece(standard_empty_game):
    chess_piece = piece.ChessPiece(Color.WHITE)
    standard_empty_game.add_piece(0, 0, chess_piece)
    assert standard_empty_game.board.array[0][0] == chess_piece


def test_remove_piece(standard_game):
    standard_game.remove_piece(0, 0)
    assert standard_game.board.array[0][0] is None


