import pytest


def test_init(dummy_move_factory):
    assert dummy_move_factory

def test_create(dummy_move_factory, dummy_move_data):
    with pytest.raises(NotImplementedError):
        dummy_move_factory.__class__.create(
            piece=dummy_move_data.piece,
            offset=dummy_move_data.offset,
        )

