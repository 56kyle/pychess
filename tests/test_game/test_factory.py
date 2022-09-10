
import pytest


def test_init(dummy_game_factory):
    assert dummy_game_factory

def test_create(dummy_game_factory):
    with pytest.raises(NotImplementedError):
        dummy_game_factory.__class__.create()




