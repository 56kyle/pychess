import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece.pawn import PawnData, PawnFactory, Pawn, PawnValidator
from chess.piece.pawn import Pawn
from chess.position import Position

@pytest.fixture
def dummy_pawn_data() -> PawnData:
    return PawnData(
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
def dummy_pawn_factory(dummy_pawn_data: PawnData) -> PawnFactory:
    return PawnFactory(dummy_pawn_data)

@pytest.fixture
def dummy_pawn(dummy_pawn_data: PawnData) -> Pawn:
    return Pawn[PawnData, PawnFactory, PawnValidator](**dummy_pawn_data.__dict__)

@pytest.fixture
def dummy_pawn_validator(dummy_pawn_data: PawnData) -> PawnValidator:
    return PawnValidator(dummy_pawn_data)
