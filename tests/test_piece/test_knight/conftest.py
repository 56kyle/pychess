import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece.knight import KnightData, KnightFactory, Knight, KnightValidator
from chess.piece.knight import Knight
from chess.position import Position

@pytest.fixture
def dummy_knight_data() -> KnightData:
    return KnightData(
        position=Position(file=1, rank=1),
        color=Color.WHITE,
        has_moved=False,
    )

@pytest.fixture
def dummy_knight_factory(dummy_knight_data: KnightData) -> KnightFactory:
    return KnightFactory(dummy_knight_data)

@pytest.fixture
def dummy_knight(dummy_knight_data: KnightData) -> Knight:
    return Knight[KnightData, KnightFactory, KnightValidator](**dummy_knight_data.__dict__)

@pytest.fixture
def dummy_knight_validator(dummy_knight_data: KnightData) -> KnightValidator:
    return KnightValidator(dummy_knight_data)
