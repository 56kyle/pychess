
import pytest
import chess.board
import chess.unit as unit
from chess.color import Color
from chess.move import Move

from chess.path import Path, INFINITE_STEPS, AllowedPathTypes
from chess.offset import UP_LEFT, DOWN_RIGHT, Offset, DOWN, UP
from chess.square import Square


def test_init(empty_game, empty_board):
    assert empty_game.board == empty_board
    assert empty_game.moves == []
    assert empty_game.turns == []
    assert empty_game.to_move == Color.WHITE

def test_add_piece(empty_game):
    empty_game.add_piece(Square(row=0, column=0), unit.BlackRook())
    assert empty_game.board._array[0][0] == unit.BlackRook()

def test_remove_piece(empty_game):
    empty_game.board._array[0][0] = unit.BlackRook()
    empty_game.remove_piece(Square(row=0, column=0))
    assert empty_game.board._array[0][0] is None


