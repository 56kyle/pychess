import pytest
 
from dataclasses import dataclass, field
from typing import Set, Type

from chess.castle_right import CastleRight
from chess.color import Color
from chess.move.castle import CastleData, CastleFactory, Castle, CastleValidator
from chess.offset import Offset
from chess.side import Side


@pytest.fixture
def dummy_castle_data(dummy_e1_white_king, dummy_a1_white_rook) -> CastleData:
    return CastleData(
        piece_data=dummy_e1_white_king.data,
        piece_start=dummy_e1_white_king.data.position,
        offset=Offset(1, 1),
        rook_data=dummy_a1_white_rook.data,
        rook_start=dummy_a1_white_rook.data.position,
        castle_right=CastleRight(
            color=Color.WHITE,
            side=Side.QUEEN,
        )
    )

@pytest.fixture
def dummy_castle_factory(dummy_castle_data: CastleData) -> CastleFactory:
    return CastleFactory(dummy_castle_data)

@pytest.fixture
def dummy_castle(dummy_castle_data: CastleData) -> Castle:
    return Castle[CastleData, CastleFactory, CastleValidator](**dummy_castle_data.__dict__)

@pytest.fixture
def dummy_castle_validator(dummy_castle_data: CastleData) -> CastleValidator:
    return CastleValidator(dummy_castle_data)

