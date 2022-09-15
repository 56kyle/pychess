
import pytest

from chess.game import GameValidator


def test_init(dummy_game_data):
    assert GameValidator(dummy_game_data)

def test_is_valid(dummy_game_data):
    assert GameValidator.is_valid(data=dummy_game_data)

def test_validate(dummy_game_data):
    assert GameValidator.validate(data=dummy_game_data) is None

