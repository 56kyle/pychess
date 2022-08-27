
import pytest
import chess.board
import chess.unit as unit

from chess.path import Path, INFINITE_STEPS, AllowedMovementTypes
from chess.offset import UP_LEFT, DOWN_RIGHT
from chess.square import Square


def test_init(empty_game, empty_board):
    assert empty_game.board == empty_board


def test_add_piece(empty_game):
    empty_game.add_piece(Square(row=0, column=0), unit.BlackRook())
    assert empty_game.board._array[0][0] == unit.BlackRook()


def test_remove_piece(empty_game):
    empty_game.board._array[0][0] = unit.BlackRook()
    empty_game.remove_piece(Square(row=0, column=0))
    assert empty_game.board._array[0][0] is None

def test__fit_path_max_steps_to_board_with_diagonal_against_edge(empty_game):
    empty_game.board._array[0][0] = unit.BlackQueen()
    queen_up_left_diagonal_path = Path(offset=UP_LEFT, max_steps=INFINITE_STEPS)
    assert empty_game._fit_path_max_steps_to_board(
        Square(row=0, column=0),
        queen_up_left_diagonal_path
    ) == Path(offset=UP_LEFT, max_steps=0)

def test__fit_path_max_steps_to_board_with_open_diagonal(empty_game):
    empty_game.board._array[0][0] = unit.BlackQueen()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert empty_game._fit_path_max_steps_to_board(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=7)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_and_capturing_allowed(empty_game):
    empty_game.board._array[0][0] = unit.BlackQueen()
    empty_game.board._array[1][1] = unit.WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10)
    assert empty_game._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=1)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_and_no_capturing_allowed(empty_game):
    empty_game.board._array[0][0] = unit.BlackQueen()
    empty_game.board._array[1][1] = unit.WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10, allowed_path_types=AllowedMovementTypes.MOVE_ONLY)
    assert empty_game._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=0, allowed_path_types=AllowedMovementTypes.MOVE_ONLY)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_part_way(empty_game):
    empty_game.board._array[0][0] = unit.BlackQueen()
    empty_game.board._array[4][4] = unit.WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert empty_game._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=4)

def test__fit_path_max_steps_to_blocked_path_with_invalid_paths_present(empty_game):
    empty_game.board._array[5][5] = unit.BlackQueen()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert empty_game._fit_path_max_steps_to_blocked_path(
        Square(row=5, column=5),
        queen_down_right_diagonal_path,
    ) == Path(offset=DOWN_RIGHT, max_steps=2)




