import pytest
 
from dataclasses import dataclass, field
from typing import Set, Type

from chess.move import MoveData, MoveFactory, Move, MoveValidator
from chess.offset import Offset
from chess.piece import Piece
from chess.position import Position

@pytest.fixture
def dummy_move_data(dummy_piece) -> MoveData:
    return MoveData(
        piece=dummy_piece,
        offset=Offset(1, 1),
    )

@pytest.fixture
def dummy_move_factory(dummy_move_data: MoveData) -> MoveFactory:
    return MoveFactory(dummy_move_data)

@pytest.fixture
def dummy_move(dummy_move_data: MoveData) -> Move:
    return Move[MoveData, MoveFactory, MoveValidator](dummy_move_data)

@pytest.fixture
def dummy_move_validator(dummy_move_data: MoveData) -> MoveValidator:
    return MoveValidator(dummy_move_data)

