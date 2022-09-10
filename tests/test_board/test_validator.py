import pytest


def test_init(dummy_board_validator):
    assert dummy_board_validator

def test_is_valid(dummy_board_validator, dummy_board_data):
    with pytest.raises(NotImplementedError):
        dummy_board_validator.__class__.is_valid(data=dummy_board_data)

def test_validate(dummy_board_validator, dummy_board_data):
    with pytest.raises(NotImplementedError):
        dummy_board_validator.__class__.validate(data=dummy_board_data)

