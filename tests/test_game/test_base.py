
import pytest
import chess.board
import chess.game as game
import chess.piece as piece

from chess.color import Color
from chess.move import Move
from chess.square import Square


def test_init(base_empty_game, base_empty_board):
    assert base_empty_game.board == base_empty_board


def test_add_piece(base_empty_game):
    base_empty_game.add_piece(Square(row=0, column=0), piece.BlackRook)
    assert base_empty_game.board._array[0][0] == piece.BlackRook


def test_remove_piece(base_empty_game):
    base_empty_game.board._array[0][0] = piece.BlackRook
    base_empty_game.remove_piece(Square(row=0, column=0))
    assert base_empty_game.board._array[0][0] is None

