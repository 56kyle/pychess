

import numpy as np
import pytest

import chess.board
import chess.piece
import chess.game

from chess.color import Color
from chess.move import Move
from chess.square import Square


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


algebraic = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]
indexed = [
    ['00', '01', '02', '03', '04', '05', '06', '07'],
    ['10', '11', '12', '13', '14', '15', '16', '17'],
    ['20', '21', '22', '23', '24', '25', '26', '27'],
    ['30', '31', '32', '33', '34', '35', '36', '37'],
    ['40', '41', '42', '43', '44', '45', '46', '47'],
    ['50', '51', '52', '53', '54', '55', '56', '57'],
    ['60', '61', '62', '63', '64', '65', '66', '67'],
    ['70', '71', '72', '73', '74', '75', '76', '77']
]


@pytest.fixture
def fools_mate_game(standard_game):
    f2_pawn = standard_game.board.get(Square(row=6, column=5))
    e7_pawn = standard_game.board.get(Square(row=1, column=4))
    g2_pawn = standard_game.board.get(Square(row=6, column=6))
    d8_queen = standard_game.board.get(Square(row=0, column=3))
    return chess.game.ChessGame(
        board=standard_game.board,
        moves=[
            Move(piece=f2_pawn, from_column=5, from_row=6, to_column=5, to_row=5),
            Move(piece=e7_pawn, from_column=4, from_row=1, to_column=4, to_row=2),
            Move(piece=g2_pawn, from_column=6, from_row=6, to_column=6, to_row=4),
            Move(piece=d8_queen, from_column=3, from_row=0, to_column=7, to_row=4),
        ]
    )




