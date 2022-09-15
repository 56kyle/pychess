
import pytest

from chess.move import MoveData, MoveValidator


def test_init(dummy_move_validator):
    assert dummy_move_validator

def test_is_valid(dummy_move_validator, dummy_move_data):
    assert MoveValidator.is_valid(dummy_move_data)

def test_validate(dummy_move_data):
    assert MoveValidator.validate(dummy_move_data) is None


