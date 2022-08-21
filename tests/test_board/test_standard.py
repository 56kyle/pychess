
import pytest
import chess.board as board
import chess.piece as piece

from chess.color import Color
from collections import Counter


def test_init_with_standard_empty_board(standard_empty_board_array):
    brd = board.Standard(array=standard_empty_board_array)
    assert brd.array.all() == standard_empty_board_array.all()

def test_init_with_no_array():
    assert board.Standard().array.all() == board.standard.standard_board_array.all()

def test_get_pieces(standard_board):
    retrieved_pieces = standard_board.get_pieces()
    assert Counter(retrieved_pieces) == Counter(board.standard.standard_pieces)
