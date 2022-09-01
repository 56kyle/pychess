
import pytest

from collections import Counter

from chess.board import ChessBoard, standard_pieces
from chess.offset import UP_LEFT, DOWN_RIGHT
from chess.path import Path, INFINITE_STEPS, AllowedMovementTypes
from chess.square import Square
from chess.unit import BlackRook, BlackQueen, WhitePawn


def test_init_with_empty_board_array(empty_board_array):
    assert ChessBoard(empty_board_array)

def test_eq_with_other_board(empty_board):
    assert empty_board == ChessBoard(empty_board._array)

def test_eq_with_other_array(empty_board):
    assert empty_board == empty_board._array

def test_eq_with_other_non_compatible_type(empty_board):
    assert not empty_board == 1

def test_get_with_piece(standard_board):
    assert standard_board.get(Square(row=0, column=0)) == BlackRook

def test_get_with_none(empty_board):
    assert empty_board.get(Square(row=0, column=0)) is None

def test_get_with_out_of_range_row(standard_board):
    with pytest.raises(IndexError):
        standard_board.get(Square(row=8, column=0))

def test_get_with_out_of_range_column(standard_board):
    with pytest.raises(IndexError):
        standard_board.get(Square(row=0, column=8))

def test_set_with_piece(empty_board):
    empty_board.set(Square(row=0, column=0), BlackRook())
    assert empty_board.get(Square(row=0, column=0)) == BlackRook()

def test_set_with_none(empty_board):
    empty_board.set(Square(row=0, column=0), None)
    assert empty_board.get(Square(row=0, column=0)) is None

def test_set_with_out_of_range_row(empty_board):
    with pytest.raises(IndexError):
        empty_board.set(Square(row=8, column=0), None)

def test_set_with_out_of_range_column(empty_board):
    with pytest.raises(IndexError):
        empty_board.set(Square(row=0, column=8), None)

def test_get_height(empty_board):
    assert empty_board.get_height() == 8

def test_get_width(empty_board):
    assert empty_board.get_width() == 8

def test_get_max_y_index(empty_board):
    assert empty_board.get_max_y_index() == 7

def test_get_max_x_index(empty_board):
    assert empty_board.get_max_x_index() == 7

def test_get_pieces_with_standard_board(standard_board):
    retrieved_pieces = standard_board.get_units()
    assert Counter(retrieved_pieces) == Counter(standard_pieces)

def test_get_pieces_with_empty_board(empty_board):
    retrieved_pieces = empty_board.get_units()
    expected_pieces = []
    assert Counter(retrieved_pieces) == Counter(expected_pieces)

def test_get_absolute_max_path_steps(empty_board):
    assert empty_board.get_absolute_max_path_steps() == 8

def test_is_valid_square_with_min_row_and_min_column(empty_board):
    assert empty_board.is_valid_square(Square(row=0, column=0))

def test_is_valid_square_with_max_row_and_max_column(empty_board):
    assert empty_board.is_valid_square(Square(row=7, column=7))

def test_is_valid_square_with_out_of_range_row(empty_board):
    assert not empty_board.is_valid_square(Square(row=8, column=0))

def test_is_valid_square_with_out_of_range_column(empty_board):
    assert not empty_board.is_valid_square(Square(row=0, column=8))

def test_is_valid_square_with_out_range_row_and_column(empty_board):
    assert not empty_board.is_valid_square(Square(row=8, column=8))

def test_is_valid_square_with_invalid_row(empty_board):
    assert not empty_board.is_valid_square(Square(row=-1, column=0))

def test_is_valid_square_with_invalid_column(empty_board):
    assert not empty_board.is_valid_square(Square(row=0, column=-1))

def test_is_valid_square_with_invalid_row_and_column(empty_board):
    assert not empty_board.is_valid_square(Square(row=-1, column=-1))

def test__fit_path_max_steps_to_board_with_diagonal_against_edge(empty_board):
    empty_board._array[0][0] = BlackQueen()
    queen_up_left_diagonal_path = Path(offset=UP_LEFT, max_steps=INFINITE_STEPS)
    assert empty_board._fit_path_max_steps_to_board(
        Square(row=0, column=0),
        queen_up_left_diagonal_path
    ) == Path(offset=UP_LEFT, max_steps=0)

def test__fit_path_max_steps_to_board_with_open_diagonal(empty_board):
    empty_board._array[0][0] = BlackQueen()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert empty_board._fit_path_max_steps_to_board(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=7)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_and_capturing_allowed(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[1][1] = WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=1)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_and_no_capturing_allowed(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[1][1] = WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10, allowed_path_types=AllowedMovementTypes.MOVE_ONLY)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=0, allowed_path_types=AllowedMovementTypes.MOVE_ONLY)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_part_way(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[4][4] = WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=4)

def test__fit_path_max_steps_to_blocked_path_with_invalid_paths_present(empty_board):
    empty_board._array[5][5] = BlackQueen()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=INFINITE_STEPS)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=5, column=5),
        queen_down_right_diagonal_path,
    ) == Path(offset=DOWN_RIGHT, max_steps=2)
