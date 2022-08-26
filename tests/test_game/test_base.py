
import pytest
import chess.board
import chess.unit as unit

from chess.movement import Movement, INFINITE_STEPS
from chess.offset import UP_LEFT, DOWN_RIGHT
from chess.square import Square


def test_init(base_empty_game, base_empty_board):
    assert base_empty_game.board == base_empty_board


def test_add_piece(base_empty_game):
    base_empty_game.add_piece(Square(row=0, column=0), unit.BlackRook())
    assert base_empty_game.board._array[0][0] == unit.BlackRook()


def test_remove_piece(base_empty_game):
    base_empty_game.board._array[0][0] = unit.BlackRook()
    base_empty_game.remove_piece(Square(row=0, column=0))
    assert base_empty_game.board._array[0][0] is None

def test__fit_movement_max_steps_to_board_with_diagonal_against_edge(base_empty_game):
    base_empty_game.board._array[0][0] = unit.BlackQueen()
    queen_up_left_diagonal_movement = Movement(offset=UP_LEFT, max_steps=INFINITE_STEPS)
    assert base_empty_game._fit_movement_max_steps_to_board(
        Square(row=0, column=0),
        queen_up_left_diagonal_movement
    ) == Movement(offset=UP_LEFT, max_steps=0)

def test__fit_movement_max_steps_to_board_with_open_diagonal(base_empty_game):
    base_empty_game.board._array[0][0] = unit.BlackQueen()
    queen_down_right_diagonal_movement = Movement(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert base_empty_game._fit_movement_max_steps_to_board(
        Square(row=0, column=0),
        queen_down_right_diagonal_movement
    ) == Movement(offset=DOWN_RIGHT, max_steps=7)






