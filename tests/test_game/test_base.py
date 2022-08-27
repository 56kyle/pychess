
import pytest
import chess.board
import chess.unit as unit

from chess.movement import Movement, INFINITE_STEPS, AllowedMovementTypes
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

def test__fit_movement_max_steps_to_blocked_path_with_piece_in_way_and_capturing_allowed(base_empty_game):
    base_empty_game.board._array[0][0] = unit.BlackQueen()
    base_empty_game.board._array[1][1] = unit.WhitePawn()
    queen_down_right_diagonal_movement = Movement(offset=DOWN_RIGHT, max_steps=10)
    assert base_empty_game._fit_movement_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_movement
    ) == Movement(offset=DOWN_RIGHT, max_steps=1)

def test__fit_movement_max_steps_to_blocked_path_with_piece_in_way_and_no_capturing_allowed(base_empty_game):
    base_empty_game.board._array[0][0] = unit.BlackQueen()
    base_empty_game.board._array[1][1] = unit.WhitePawn()
    queen_down_right_diagonal_movement = Movement(offset=DOWN_RIGHT, max_steps=10, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)
    assert base_empty_game._fit_movement_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_movement
    ) == Movement(offset=DOWN_RIGHT, max_steps=0, allowed_movement_types=AllowedMovementTypes.MOVE_ONLY)

def test__fit_movement_max_steps_to_blocked_path_with_piece_in_way_part_way(base_empty_game):
    base_empty_game.board._array[0][0] = unit.BlackQueen()
    base_empty_game.board._array[4][4] = unit.WhitePawn()
    queen_down_right_diagonal_movement = Movement(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert base_empty_game._fit_movement_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_movement
    ) == Movement(offset=DOWN_RIGHT, max_steps=4)

def test__fit_movement_max_steps_to_blocked_path_with_invalid_movements_present(base_empty_game):
    base_empty_game.board._array[5][5] = unit.BlackQueen()
    queen_down_right_diagonal_movement = Movement(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert base_empty_game._fit_movement_max_steps_to_blocked_path(
        Square(row=5, column=5),
        queen_down_right_diagonal_movement,
    ) == Movement(offset=DOWN_RIGHT, max_steps=2)




