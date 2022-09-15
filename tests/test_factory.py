import pytest

from chess.factory import AbstractFactory

def test_init(dummy_factory):
    assert dummy_factory
    assert dummy_factory.data

def test_create(dummy_data):
    assert AbstractFactory.create(**dummy_data.__dict__) == dummy_data

