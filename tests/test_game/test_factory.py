
import pytest

from chess.game import GameFactory


def test_init(dummy_game_data):
    assert GameFactory(data=dummy_game_data)

def test_create(dummy_game_data):
    assert GameFactory.create(**dummy_game_data.__dict__) == dummy_game_data




