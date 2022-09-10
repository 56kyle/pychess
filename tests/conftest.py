
import pytest

from dataclasses import dataclass

from chess.data import AbstractData
from chess.factory import AbstractFactory
from chess.interface import AbstractInterface
from chess.piece import Piece
from chess.position import Position
from chess.validator import AbstractValidator


@dataclass(frozen=True)
class DummyData(AbstractData):
    pass

class DummyFactory(AbstractFactory[DummyData]):
    @classmethod
    def create(cls, *args, **kwargs):
        return AbstractFactory[DummyData].create(*args, **kwargs)

class DummyInterface(AbstractInterface[DummyData]):
    pass

class DummyValidator(AbstractValidator[DummyData]):
    @classmethod
    def is_valid(cls, data, *args, **kwargs):
        return AbstractValidator[DummyData].is_valid(data=data, *args, **kwargs)

    @classmethod
    def validate(cls, data, *args, **kwargs):
        return AbstractValidator[DummyData].validate(data=data, *args, **kwargs)

@pytest.fixture
def dummy_data():
    return DummyData()

@pytest.fixture
def dummy_factory(dummy_data):
    return DummyFactory(dummy_data)

@pytest.fixture
def dummy_interface(dummy_data):
    return DummyInterface(dummy_data)

@pytest.fixture
def dummy_validator(dummy_data):
    return DummyValidator(dummy_data)

@pytest.fixture
def dummy_piece():
    return Piece(position=Position(1, 1))


