import pytest

from chess.piece.knight.data import KnightData
from chess.piece.knight.exceptions import KnightValidationError
from chess.piece.knight.validator import KnightValidator, V


def test_init(dummy_knight_validator):
    assert dummy_knight_validator


def test__validate_data(dummy_knight_data):
    assert KnightValidator[KnightData]._validate_data(dummy_knight_data) is None









