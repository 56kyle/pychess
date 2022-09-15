import pytest
 
from dataclasses import dataclass, field
from typing import Set, Type

from chess.move import MoveData, MoveFactory, Move, MoveValidator
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


class DummyMove(Move[DummyMoveData]):
    pass


class DummyMoveValidator(MoveValidator[DummyMoveData]):
    def validate(self):
        return super().validate()


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
def dummy_move_interface(dummy_move_data: DummyMoveData) -> Move:
    return DummyMove(dummy_move_data)

@pytest.fixture
def dummy_move_validator(dummy_move_data: DummyMoveData) -> MoveValidator:
    return DummyMoveValidator(dummy_move_data)

