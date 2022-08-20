

import pytest
import chess.piece as piece

from chess.color import Color


def test_init():
    assert piece.ChessPiece(Color.WHITE)

def test_str():
    assert str(piece.ChessPiece(Color.WHITE)) == 'White ChessPiece'

def test_repr():
    assert repr(piece.ChessPiece(Color.WHITE)) == 'ChessPiece(Color.WHITE)'

def test_eq_with_same_class_and_same_color():
    assert piece.ChessPiece(Color.WHITE) == piece.ChessPiece(Color.WHITE)

def test_eq_with_different_class_and_same_color():
    assert piece.ChessPiece(Color.WHITE) != piece.Pawn(Color.BLACK)

def test_eq_with_same_class_and_different_color():
    assert piece.ChessPiece(Color.WHITE) != piece.ChessPiece(Color.BLACK)

def test_eq_with_different_class_and_different_color():
    assert piece.ChessPiece(Color.WHITE) != piece.Pawn(Color.BLACK)

def test_hash_with_same_value():
    assert hash(piece.ChessPiece(Color.WHITE)) == hash(piece.ChessPiece(Color.WHITE))

def test_hash_with_different_value_same_color():
    assert hash(piece.ChessPiece(Color.WHITE)) != hash(piece.ChessPiece(Color.BLACK))

def test_hash_with_same_value_different_color():
    assert hash(piece.ChessPiece(Color.WHITE)) != hash(piece.ChessPiece(Color.BLACK))

def test_hash_with_different_value_different_color():
    assert hash(piece.ChessPiece(Color.WHITE)) != hash(piece.ChessPiece(Color.BLACK))

