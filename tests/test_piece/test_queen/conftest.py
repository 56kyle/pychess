import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece.queen import QueenData, QueenFactory, Queen, QueenValidator
from chess.piece.queen import Queen
from chess.position import Position

@pytest.fixture
def dummy_queen_data() -> QueenData:
    return QueenData(
        position=Position(file=1, rank=1),
        color=Color.WHITE,
        name='dummy',
        letter='d',
        value=99,
        symbol='d',
        html_decimal='d',
        html_hex='d',
        has_moved=False,
    )

@pytest.fixture
def dummy_queen_factory(dummy_queen_data: QueenData) -> QueenFactory:
    return QueenFactory(dummy_queen_data)

@pytest.fixture
def dummy_queen(dummy_queen_data: QueenData) -> Queen:
    return Queen[QueenData, QueenFactory, QueenValidator](**dummy_queen_data.__dict__)

@pytest.fixture
def dummy_queen_validator(dummy_queen_data: QueenData) -> QueenValidator:
    return QueenValidator(dummy_queen_data)
