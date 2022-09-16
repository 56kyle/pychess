import pytest

from chess.piece.bishop.factory import BishopFactory


def test_init(dummy_bishop_data):
    assert BishopFactory(data=dummy_bishop_data)

def test_create(dummy_bishop_data):
    assert BishopFactory.create(**dummy_bishop_data.__dict__) == dummy_bishop_data

