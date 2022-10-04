import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece.rook import RookData, RookFactory, Rook, RookValidator
from chess.piece.rook import Rook
from chess.position import Position

@pytest.fixture
def dummy_rook_data() -> RookData:
    return RookData(
        position=Position(file=1, rank=1),
        color=Color.WHITE,
        has_moved=False,
    )

@pytest.fixture
def dummy_rook_factory(dummy_rook_data: RookData) -> RookFactory:
    return RookFactory(dummy_rook_data)

@pytest.fixture
def dummy_rook(dummy_rook_data: RookData) -> Rook:
    return Rook[RookData, RookFactory, RookValidator](**dummy_rook_data.__dict__)

@pytest.fixture
def dummy_rook_validator(dummy_rook_data: RookData) -> RookValidator:
    return RookValidator(dummy_rook_data)
