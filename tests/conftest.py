

import numpy as np
import pytest

import chess.board
import chess.piece
import chess.game

from chess.color import Color


@pytest.fixture
def standard_empty_board_array() -> np.ndarray:
    return np.empty((8, 8), dtype=chess.piece.ChessPiece)


@pytest.fixture
def base_empty_board(standard_empty_board_array) -> chess.board.ChessBoard:
    return chess.board.ChessBoard(array=standard_empty_board_array)


@pytest.fixture
def standard_empty_board(standard_empty_board_array) -> chess.board.Standard:
    return chess.board.Standard(array=standard_empty_board_array)


@pytest.fixture
def standard_board() -> chess.board.Standard:
    return chess.board.Standard()


@pytest.fixture
def base_empty_game(base_empty_board) -> chess.game.ChessGame:
    return chess.game.ChessGame(board=base_empty_board)


@pytest.fixture
def standard_empty_game(standard_empty_board) -> chess.game.Standard:
    return chess.game.Standard(board=standard_empty_board)


@pytest.fixture
def standard_game(standard_board) -> chess.game.Standard:
    return chess.game.Standard(board=standard_board)


@pytest.fixture
def fools_mate_game(standard_game):
    standard_game.make_move()




