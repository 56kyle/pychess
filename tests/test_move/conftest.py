import pytest
 
from dataclasses import dataclass, field
from typing import Set, Type

from chess.move import MoveData, MoveFactory, MoveInterface, MoveValidator
from chess.offset import Offset
from chess.piece import Piece
from chess.position import Position


@dataclass(frozen=True)
class DummyMoveData(MoveData):
    piece: Piece = Piece(
        position=Position(1, 1),
    )
    offset: Offset = Offset(1, 1)


class DummyMoveFactory(MoveFactory[DummyMoveData]):
    @classmethod
    def create(cls, *args, **kwargs):
        return MoveFactory[DummyMoveData].create(*args, **kwargs)


class DummyMoveInterface(MoveInterface[DummyMoveData]):
    pass


class DummyMoveValidator(MoveValidator[DummyMoveData]):
    @classmethod
    def is_valid(cls, data, *args, **kwargs):
        return MoveValidator[DummyMoveData].is_valid(data=data, *args, **kwargs)

    @classmethod
    def validate(cls, data, *args, **kwargs):
        return MoveValidator[DummyMoveData].validate(data=data, *args, **kwargs)


@pytest.fixture
def dummy_move_data(dummy_piece) -> DummyMoveData:
    return DummyMoveData(
        piece=dummy_piece,
        offset=Offset(1, 1),
    )

@pytest.fixture
def dummy_move_factory(dummy_move_data: DummyMoveData) -> MoveFactory:
    return DummyMoveFactory(dummy_move_data)

@pytest.fixture
def dummy_move_interface(dummy_move_data: DummyMoveData) -> MoveInterface:
    return DummyMoveInterface(dummy_move_data)

@pytest.fixture
def dummy_move_validator(dummy_move_data: DummyMoveData) -> MoveValidator:
    return DummyMoveValidator(dummy_move_data)

