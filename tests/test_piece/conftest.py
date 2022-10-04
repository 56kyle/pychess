import pytest

from dataclasses import dataclass, field
from typing import Set, Type

from chess.color import Color
from chess.piece import PieceData, PieceFactory, Piece, PieceValidator
from chess.piece import Piece
from chess.position import Position

@pytest.fixture
def dummy_piece_data() -> PieceData:
    return PieceData(
        position=Position(file=1, rank=1),
        color=Color.WHITE,
        has_moved=False,
    )

@pytest.fixture
def dummy_piece_factory(dummy_piece_data: PieceData) -> PieceFactory:
    return PieceFactory(dummy_piece_data)

@pytest.fixture
def dummy_piece(dummy_piece_data: PieceData) -> Piece:
    return Piece[PieceData, PieceFactory, PieceValidator](**dummy_piece_data.__dict__)

@pytest.fixture
def dummy_piece_validator(dummy_piece_data: PieceData) -> PieceValidator:
    return PieceValidator(dummy_piece_data)
