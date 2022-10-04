import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece.bishop import BishopData, BishopFactory, Bishop, BishopValidator
from chess.piece.bishop import Bishop
from chess.position import Position

@pytest.fixture
def dummy_bishop_data() -> BishopData:
    return BishopData(
        position=Position(file=1, rank=1),
        color=Color.WHITE,
        has_moved=False,
    )

@pytest.fixture
def dummy_bishop_factory(dummy_bishop_data: BishopData) -> BishopFactory:
    return BishopFactory(dummy_bishop_data)

@pytest.fixture
def dummy_bishop(dummy_bishop_data: BishopData) -> Bishop:
    return Bishop[BishopData, BishopFactory, BishopValidator](**dummy_bishop_data.__dict__)

@pytest.fixture
def dummy_bishop_validator(dummy_bishop_data: BishopData) -> BishopValidator:
    return BishopValidator(dummy_bishop_data)
