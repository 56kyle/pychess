import pytest

from chess.validator import AbstractValidator


def test_init(dummy_validator):
    assert dummy_validator

def test_is_valid(dummy_data):
    with pytest.raises(NotImplementedError):
        AbstractValidator.is_valid(dummy_data)

def test_validate(dummy_data):
    with pytest.raises(NotImplementedError):
        AbstractValidator.validate(dummy_data)
