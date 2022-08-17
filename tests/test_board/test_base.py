
import pytest
import chess.board as board
import chess.piece as piece


def test_init_with_standard_empty_board_array(standard_empty_board_array):
    assert board.ChessBoard(standard_empty_board_array)

def test_eq_with_other_board(standard_empty_board):
    assert standard_empty_board == board.ChessBoard(standard_empty_board.array)

def test_eq_with_other_array(standard_empty_board):
    assert standard_empty_board == standard_empty_board.array

def test_eq_with_other_non_compatible_type(standard_empty_board):
    assert not standard_empty_board == 1

