import pytest
 
from dataclasses import dataclass, field
from typing import Set, Type

from chess.move.en_passant import EnPassantData, EnPassantFactory, EnPassant, EnPassantValidator
from chess.offset import Offset
from chess.piece import Piece
from chess.position import Position

@pytest.fixture
def dummy_en_passant_data(dummy_e5_white_pawn, dummy_d5_black_pawn) -> EnPassantData:
    return EnPassantData(
        piece_data=dummy_e5_white_pawn.data,
        piece_start=dummy_e5_white_pawn.data.position,
        offset=Offset(1, 1),
        captured_piece_data=dummy_d5_black_pawn,
        captured_piece_start=dummy_d5_black_pawn.data.position,
        target_position=Position(file=4, rank=6),
    )

@pytest.fixture
def dummy_en_passant_factory(dummy_en_passant_data: EnPassantData) -> EnPassantFactory:
    return EnPassantFactory(dummy_en_passant_data)

@pytest.fixture
def dummy_en_passant(dummy_en_passant_data: EnPassantData) -> EnPassant:
    return EnPassant[EnPassantData, EnPassantFactory, EnPassantValidator](**dummy_en_passant_data.__dict__)

@pytest.fixture
def dummy_en_passant_validator(dummy_en_passant_data: EnPassantData) -> EnPassantValidator:
    return EnPassantValidator(dummy_en_passant_data)

