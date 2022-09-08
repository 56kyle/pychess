
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

def test__is_move_color(empty_game, e2_to_e4_move):
    empty_game.to_move = Color.WHITE
    assert empty_game._is_move_color(move=e2_to_e4_move)
    empty_game.to_move = Color.BLACK
    assert not empty_game._is_move_color(move=e2_to_e4_move)

def test__is_capture_move_with_captured_unit(empty_game):
    empty_game.board._array[7][0] = unit.WhiteRook()
    empty_game.board._array[0][0] = unit.BlackRook()
    move = Move(
        unit=empty_game.board.get(Square(row=7, column=0)),
        from_square=Square(row=7, column=0),
        offset=UP*7,
    )
    assert empty_game._is_capture_move(move=move)

def test__is_capture_move_with_no_captured_unit(empty_game):
    empty_game.board._array[7][0] = unit.WhiteRook()
    move = Move(
        unit=empty_game.board.get(Square(row=7, column=0)),
        from_square=Square(row=7, column=0),
        offset=UP*7,
    )
    assert not empty_game._is_capture_move(move=move)

def test_add_piece(empty_game):
    empty_game.add_piece(Square(row=0, column=0), unit.BlackRook())
    assert empty_game.board._array[0][0] == unit.BlackRook()

def test_remove_piece(empty_game):
    empty_game.board._array[0][0] = unit.BlackRook()
    empty_game.remove_piece(Square(row=0, column=0))
    assert empty_game.board._array[0][0] is None


