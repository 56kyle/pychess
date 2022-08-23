
import pytest
import chess.game as game
import chess.piece as piece

from chess.color import Color
from chess.move import Move


def test_init(standard_empty_board):
    assert game.Standard(standard_empty_board)

def test_make_move(standard_game):
    standard_game.make_move(0, 1, 0, 2)

def test_add_piece(standard_empty_game):
    standard_empty_game.add_piece(0, 0, piece.BlackRook)
    assert standard_empty_game.board._array[0][0] == piece.BlackRook


def test_remove_piece(standard_game):
    standard_game.remove_piece(0, 0)
    assert standard_game.board._array[0][0] is None

