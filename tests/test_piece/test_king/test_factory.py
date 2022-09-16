import pytest

from chess.piece.king.factory import KingFactory


def test_init(dummy_king_data):
    assert KingFactory(data=dummy_king_data)

def test_create(dummy_king_data):
    assert KingFactory.create(**dummy_king_data.__dict__) == dummy_king_data

