
import pytest

from chess.move.en_passant import EnPassantData, EnPassantValidator


def test_init(dummy_en_passant_validator):
    assert dummy_en_passant_validator

def test_is_valid(dummy_en_passant_validator, dummy_en_passant_data):
    assert EnPassantValidator.is_valid(dummy_en_passant_data)

def test_validate(dummy_en_passant_data):
    assert EnPassantValidator.validate(dummy_en_passant_data) is None


