import pytest

from chess.piece.queen.factory import QueenFactory


def test_init(dummy_queen_data):
    assert QueenFactory(data=dummy_queen_data)

def test_create(dummy_queen_data):
    assert QueenFactory.create(**dummy_queen_data.__dict__) == dummy_queen_data

