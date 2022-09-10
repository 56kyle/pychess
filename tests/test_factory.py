import pytest


def test_init(dummy_factory):
    assert dummy_factory
    assert dummy_factory.data

def test_create(dummy_factory):
    with pytest.raises(NotImplementedError):
        dummy_factory.create()

