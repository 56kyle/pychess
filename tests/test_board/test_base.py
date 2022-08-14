
import pytest
import chess.board as board
import chess.piece as piece


def test_init_with_standard_empty_board_array(standard_empty_board_array):
    assert board.ChessBoard(standard_empty_board_array)


