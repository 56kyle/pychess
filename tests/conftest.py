

import numpy as np
import pytest

import chess.board
import chess.piece
import chess.game


@pytest.fixture
def standard_empty_board_array() -> np.ndarray:
    return np.empty((8, 8), dtype=chess.piece.ChessPiece)


@pytest.fixture
def standard_filled_board_array(standard_empty_board_array) -> np.ndarray:
    return np.array([[chess.piece.ChessPiece() for _ in range(8)] for _ in range(8)])


@pytest.fixture
def base_board(standard_empty_board_array) -> chess.board.ChessBoard:
    return chess.board.ChessBoard(array=standard_empty_board_array)


@pytest.fixture
def standard_board(standard_empty_board_array) -> chess.board.Standard:
    return chess.board.Standard(array=standard_empty_board_array)


@pytest.fixture
def base_game(base_board) -> chess.game.ChessGame:
    return chess.game.ChessGame(board=base_board)


@pytest.fixture
def standard_game(standard_board) -> chess.game.Standard:
    return chess.game.Standard(board=standard_board)




