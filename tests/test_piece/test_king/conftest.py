import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece.king import KingData, KingFactory, King, KingValidator
from chess.piece.king import King
from chess.position import Position

@pytest.fixture
def dummy_king_data() -> KingData:
    return KingData(
        position=Position(file=1, rank=1),
        color=Color.WHITE,
        has_moved=False,
    )

@pytest.fixture
def dummy_king_factory(dummy_king_data: KingData) -> KingFactory:
    return KingFactory(dummy_king_data)

@pytest.fixture
def dummy_king(dummy_king_data: KingData) -> King:
    return King[KingData, KingFactory, KingValidator](**dummy_king_data.__dict__)

@pytest.fixture
def dummy_king_validator(dummy_king_data: KingData) -> KingValidator:
    return KingValidator(dummy_king_data)
