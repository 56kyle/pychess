import pytest

from chess.piece.knight.factory import KnightFactory


def test_init(dummy_knight_data):
    assert KnightFactory(data=dummy_knight_data)

def test_create(dummy_knight_data):
    assert KnightFactory.create(**dummy_knight_data.__dict__) == dummy_knight_data

