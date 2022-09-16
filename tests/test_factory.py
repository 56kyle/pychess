import pytest

from chess.factory import AbstractFactory

def test_init(dummy_factory):
    assert dummy_factory
    assert dummy_factory.data

def test_create(dummy_data):
    assert AbstractFactory.create(**dummy_data.__dict__) == dummy_data

def test_create_with_none_as_data_type(dummy_data):
    class DummyFactoryWithNoneDataType(AbstractFactory):
        data_type = None

    with pytest.raises(NotImplementedError):
        DummyFactoryWithNoneDataType.create(**dummy_data.__dict__)

