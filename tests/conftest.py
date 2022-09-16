
import pytest

from chess.castle_right import CastleRight
from chess.color import Color
from chess.data import AbstractData, T
from chess.factory import AbstractFactory, F
from chess.interface import AbstractInterface
from chess.piece import Piece
from chess.position import Position
from chess.side import Side
from chess.validator import AbstractValidator, V


@pytest.fixture
def dummy_data():
    return AbstractData()

@pytest.fixture
def dummy_factory(dummy_data):
    return AbstractFactory[AbstractData](dummy_data)

@pytest.fixture
def dummy_interface(dummy_data):
    return AbstractInterface[AbstractData, AbstractFactory, AbstractValidator](**dummy_data.__dict__)

@pytest.fixture
def dummy_validator(dummy_data):
    return AbstractValidator[AbstractData](dummy_data)

@pytest.fixture
def dummy_piece():
    return Piece(
        position=Position(rank=1, file=1),
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_position():
    return Position(rank=1, file=1)

@pytest.fixture
def dummy_castle_right():
    return CastleRight(
        color=Color.WHITE,
        side=Side.KING,
    )


