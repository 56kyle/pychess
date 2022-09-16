import pytest

from chess.piece.pawn.factory import PawnFactory


def test_init(dummy_pawn_data):
    assert PawnFactory(data=dummy_pawn_data)

def test_create(dummy_pawn_data):
    assert PawnFactory.create(**dummy_pawn_data.__dict__) == dummy_pawn_data

