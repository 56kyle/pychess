
import pytest
import chess.game as game
import chess.piece as piece


def test_init(standard_board):
    assert game.Standard(standard_board)


def test_add_piece(standard_game):
    chess_piece = piece.ChessPiece()
    standard_game.add_piece(0, 0, chess_piece)
    assert standard_game.board.array[0][0] == chess_piece



