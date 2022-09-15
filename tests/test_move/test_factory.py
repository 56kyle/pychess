import pytest

from chess.move import MoveFactory


def test_init(dummy_move_data):
    assert MoveFactory(data=dummy_move_data)

def test_create(dummy_move_data):
    assert MoveFactory.create(**dummy_move_data.__dict__) == dummy_move_data

