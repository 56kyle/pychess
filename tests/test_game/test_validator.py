
import pytest


def test_init(dummy_game_validator):
    assert dummy_game_validator

def test_is_valid(dummy_game_validator):
    with pytest.raises(NotImplementedError):
        dummy_game_validator.is_valid()

def test_validate(dummy_game_validator):
    with pytest.raises(NotImplementedError):
        dummy_game_validator.validate()

