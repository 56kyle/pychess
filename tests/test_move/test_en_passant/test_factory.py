import pytest

from chess.move.en_passant import EnPassantFactory


def test_init(dummy_en_passant_data):
    assert EnPassantFactory(data=dummy_en_passant_data)

def test_create(dummy_en_passant_data):
    assert EnPassantFactory.create(**dummy_en_passant_data.__dict__) == dummy_en_passant_data

