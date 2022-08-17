
import pytest
import chess.game as game
import chess.piece as piece
from chess.color import Color


def test_init(base_game, base_board):
    assert base_game.board == base_board


def test_add_piece(base_game):
    with pytest.raises(NotImplementedError):
        base_game.add_piece(0, 0, piece.ChessPiece(Color.WHITE))

