
import pytest

from collections import Counter

from chess.board import ChessBoard, standard_pieces
from chess.move import Move
from chess.offset import UP_LEFT, DOWN_RIGHT, RIGHT, DOWN, UP, LEFT
from chess.path import Path, INFINITE_STEPS, AllowedPathTypes
from chess.square import Square
from chess.unit import BlackRook, BlackQueen, WhitePawn, BlackPawn


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

def test_get_path_moves_with_no_unit(empty_board):
    assert empty_board.get_path_moves(
        square=Square(row=0, column=0),
        path=Path(offset=RIGHT, max_steps=7)
    ) == set()

def test_get_path_moves_with_king_a8(empty_board):
    empty_board._array[0][0] = BlackQueen()
    queen = empty_board.get(Square(row=0, column=0))
    expected_moves = set()
    for i in range(1, 8):
        expected_moves.add(Move(unit=queen, from_square=Square(row=0, column=0), offset=RIGHT * i))
    assert empty_board.get_path_moves(
        square=Square(row=0, column=0),
        path=Path(offset=RIGHT, max_steps=7)
    ) == expected_moves

def test_get_path_squares_with_no_unit(empty_board):
    assert empty_board.get_path_offsets(
        square=Square(row=0, column=0),
        path=Path(offset=RIGHT, max_steps=7)
    ) == set()

def test_get_path_squares_with_infinite_path(empty_board):
    empty_board._array[0][0] = BlackQueen()
    with pytest.raises(ValueError):
        empty_board.get_path_offsets(
            square=Square(row=0, column=0),
            path=Path(offset=RIGHT, max_steps=INFINITE_STEPS)
        )
def test_get_path_squares_with_unit(empty_board):
    empty_board._array[0][0] = BlackQueen()
    initial_square = Square(row=0, column=0)
    assert empty_board.get_path_offsets(
        square=initial_square,
        path=Path(offset=RIGHT, max_steps=7)
    ) == {
        RIGHT,
        RIGHT * 2,
        RIGHT * 3,
        RIGHT * 4,
        RIGHT * 5,
        RIGHT * 6,
        RIGHT * 7,
    }

def test_get_valid_paths_with_no_unit(empty_board):
    assert empty_board.get_valid_paths(Square(row=0, column=0)) == set()

def test_get_valid_paths_with_unit_and_no_valid_paths(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[0][1] = BlackRook()
    empty_board._array[1][0] = BlackRook()
    empty_board._array[1][1] = BlackRook()
    assert empty_board.get_valid_paths(Square(row=0, column=0)) == set()

def test_get_valid_paths_with_queen_a8(empty_board):
    empty_board._array[0][0] = BlackQueen()
    assert empty_board.get_valid_paths(Square(row=0, column=0)) == {
        Path(offset=RIGHT, max_steps=7),
        Path(offset=DOWN_RIGHT, max_steps=7),
        Path(offset=DOWN, max_steps=7),
    }

def test_get_valid_paths_with_queen_h1(empty_board):
    empty_board._array[7][7] = BlackQueen()
    assert empty_board.get_valid_paths(Square(row=7, column=7)) == {
        Path(offset=LEFT, max_steps=7),
        Path(offset=UP_LEFT, max_steps=7),
        Path(offset=UP, max_steps=7),
    }


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

def test__fit_path_max_steps_to_blocked_path_with_no_unit(empty_board):
    assert empty_board._fit_path_max_steps_to_blocked_path(
        square=Square(row=0, column=0),
        path=Path(offset=RIGHT, max_steps=7)
    ) == Path(offset=RIGHT, max_steps=0)

def test__fit_path_max_steps_to_blocked_path_with_enemy_piece_in_way_and_capturing_allowed(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[1][1] = WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=1)

def test__fit_path_max_steps_to_blocked_path_with_ally_piece_in_way_and_capturing_allowed(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[1][1] = BlackPawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=0)

def test__fit_path_max_steps_to_blocked_path_with_piece_in_way_and_no_capturing_allowed(empty_board):
    empty_board._array[0][0] = BlackQueen()
    empty_board._array[1][1] = WhitePawn()
    queen_down_right_diagonal_path = Path(offset=DOWN_RIGHT, max_steps=10, allowed_path_types=AllowedPathTypes.MOVE_ONLY)
    assert empty_board._fit_path_max_steps_to_blocked_path(
        Square(row=0, column=0),
        queen_down_right_diagonal_path
    ) == Path(offset=DOWN_RIGHT, max_steps=0, allowed_path_types=AllowedPathTypes.MOVE_ONLY)

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

