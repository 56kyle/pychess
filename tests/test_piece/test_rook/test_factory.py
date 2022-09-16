import pytest

from chess.piece.rook.factory import RookFactory


def test_init(dummy_rook_data):
    assert RookFactory(data=dummy_rook_data)

def test_create(dummy_rook_data):
    assert RookFactory.create(**dummy_rook_data.__dict__) == dummy_rook_data

