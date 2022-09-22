
import pytest

from chess.move.castle import CastleData, CastleValidator


def test_init(dummy_castle_validator):
    assert dummy_castle_validator

def test_is_valid(dummy_castle_validator, dummy_castle_data):
    assert CastleValidator.is_valid(dummy_castle_data)

def test_validate(dummy_castle_data):
    assert CastleValidator.validate(dummy_castle_data) is None


