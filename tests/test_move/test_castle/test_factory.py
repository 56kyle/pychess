import pytest

from chess.move.castle import CastleFactory


def test_init(dummy_castle_data):
    assert CastleFactory(data=dummy_castle_data)

def test_create(dummy_castle_data):
    assert CastleFactory.create(**dummy_castle_data.__dict__) == dummy_castle_data

