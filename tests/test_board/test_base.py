
import pytest
import chess.board as board
import chess.piece as piece

from collections import Counter

from chess.color import Color


def test_init_with_standard_empty_board_array(standard_empty_board_array):
    assert board.ChessBoard(standard_empty_board_array)

def test_eq_with_other_board(standard_empty_board):
    assert standard_empty_board == board.ChessBoard(standard_empty_board.array)

def test_eq_with_other_array(standard_empty_board):
    assert standard_empty_board == standard_empty_board.array

def test_eq_with_other_non_compatible_type(standard_empty_board):
    assert not standard_empty_board == 1

def test_get_pieces_with_standard_board(standard_board):
    retrieved_pieces = standard_board.get_pieces()
    assert Counter(retrieved_pieces) == Counter(board.standard.standard_pieces)

def test_get_pieces_with_empty_board(standard_empty_board):
    retrieved_pieces = standard_empty_board.get_pieces()
    expected_pieces = []
    assert Counter(retrieved_pieces) == Counter(expected_pieces)

def test_get(standard_board):
    assert standard_board.get(0, 0) == piece.BlackRook

