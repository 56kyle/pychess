
import pytest
import chess.game as game
import chess.piece as piece

from chess.color import Color
from chess.move import Move


def test_init(standard_empty_board):
    assert game.Standard(standard_empty_board)

def test_make_move(standard_game):
    standard_game.make_move(0, 1, 0, 2)


