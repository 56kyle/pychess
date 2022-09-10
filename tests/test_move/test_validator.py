
import pytest


def test_init(dummy_move_validator):
    assert dummy_move_validator

def test_is_valid(dummy_move_validator, dummy_move_data):
    with pytest.raises(NotImplementedError):
        dummy_move_validator.is_valid(dummy_move_data)

def test_validate(dummy_move_validator, dummy_move_data):
    with pytest.raises(NotImplementedError):
        dummy_move_validator.validate(dummy_move_data)

