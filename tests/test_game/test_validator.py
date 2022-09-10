
import pytest


def test_init(dummy_game_validator):
    assert dummy_game_validator

def test_is_valid(dummy_game_validator, dummy_game_data):
    with pytest.raises(NotImplementedError):
        dummy_game_validator.__class__.is_valid(dummy_game_data)

def test_validate(dummy_game_validator, dummy_game_data):
    with pytest.raises(NotImplementedError):
        dummy_game_validator.__class__.validate(dummy_game_data)

