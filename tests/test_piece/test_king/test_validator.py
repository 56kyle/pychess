import pytest

from chess.piece.king.data import KingData
from chess.piece.king.exceptions import KingValidationError
from chess.piece.king.validator import KingValidator, V


def test_init(dummy_king_data):
    assert KingValidator[KingData](dummy_king_data)


def test__validate_data(dummy_king_data):
    assert KingValidator[KingData]._validate_data(dummy_king_data) is None









