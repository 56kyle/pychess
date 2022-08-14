
import pytest
import chess.board as board


def test_init_with_standard_empty_board(standard_empty_board_array):
    brd = board.Standard(array=standard_empty_board_array)
    assert brd.array.all() == standard_empty_board_array.all()



