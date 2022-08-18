

import pytest
import chess.piece as piece

from chess.color import Color


def test_init():
    assert piece.ChessPiece(Color.WHITE)


def test_str():
    assert str(piece.ChessPiece(Color.WHITE)) == 'White ChessPiece'


def test_repr():
    assert repr(piece.ChessPiece(Color.WHITE)) == 'ChessPiece(Color.WHITE)'

def test_int():
    assert int(piece.ChessPiece(Color.WHITE)) == 0

def test_eq():
    assert piece.ChessPiece(Color.WHITE) == piece.ChessPiece(Color.WHITE)

def test_hash_with_same_value_same_color():
    assert hash(piece.ChessPiece(Color.WHITE)) == hash(piece.ChessPiece(Color.WHITE))

def test_hash_with_different_value_same_color():
    assert hash(piece.ChessPiece(Color.WHITE)) != hash(piece.ChessPiece(Color.BLACK))

def test_hash_with_same_value_different_color():
    assert hash(piece.ChessPiece(Color.WHITE)) != hash(piece.ChessPiece(Color.BLACK))

def test_hash_with_different_value_different_color():
    assert hash(piece.ChessPiece(Color.WHITE)) != hash(piece.ChessPiece(Color.BLACK))

def test_gt_with_greater():
    assert (piece.ChessPiece(Color.WHITE) > -1) is True

def test_gt_with_equal():
    assert (piece.ChessPiece(Color.WHITE) > 0) is False

def test_gt_with_less():
    assert (piece.ChessPiece(Color.WHITE) > 1) is False

def test_lt_with_less():
    assert (piece.ChessPiece(Color.WHITE) < -1) is False

def test_lt_with_equal():
    assert (piece.ChessPiece(Color.WHITE) < 0) is False

def test_lt_with_greater():
    assert (piece.ChessPiece(Color.WHITE) < 1) is True

def test_ge_with_greater():
    assert (piece.ChessPiece(Color.WHITE) >= -1) is True

def test_ge_with_equal():
    assert (piece.ChessPiece(Color.WHITE) >= 0) is True

def test_ge_with_less():
    assert (piece.ChessPiece(Color.WHITE) >= 1) is False

def test_le_with_less():
    assert (piece.ChessPiece(Color.WHITE) <= -1) is False

def test_le_with_equal():
    assert (piece.ChessPiece(Color.WHITE) <= 0) is True

def test_le_with_greater():
    assert (piece.ChessPiece(Color.WHITE) <= 1) is True
















