
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
        return super().create(*args, **kwargs)

class DummyValidator(AbstractValidator[DummyData]):
    @classmethod
    def validate(cls, data: DummyData):
        AbstractValidator[DummyData].validate(data=data)

class DummyInterface(AbstractInterface[DummyData, DummyFactory, DummyValidator]):
    pass

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


