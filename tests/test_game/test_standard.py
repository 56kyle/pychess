
import pytest
import chess.game as game
import chess.piece as piece

from chess.color import Color
from chess.move import Move
from chess.square import Square


def test_init(standard_empty_board):
    assert game.Standard(standard_empty_board)



