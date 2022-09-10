import pytest


def test_init(dummy_validator):
    assert dummy_validator

def test_is_valid(dummy_validator, dummy_data):
    with pytest.raises(NotImplementedError):
        dummy_validator.is_valid(dummy_data)

def test_validate(dummy_validator, dummy_data):
    with pytest.raises(NotImplementedError):
        dummy_validator.validate(dummy_data)
