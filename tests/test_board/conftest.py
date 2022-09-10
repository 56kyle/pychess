from dataclasses import dataclass, field
from typing import Set, Type

import pytest

from chess.board import BoardData, BoardFactory, BoardInterface, BoardValidator
from chess.castle_right import CastleRight
from chess.piece import Piece
from chess.position import Position


@dataclass(frozen=True)
class DummyBoardData(BoardData):
    pieces: Set[Piece] = field(default_factory=set)
    castling_rights: Set[CastleRight] = field(default_factory=set)
    en_passant_target_position: Position | None = None
    half_move_draw_clock: int = 0
    full_move_number: int = 0
    width: int = 23
    height: int = 37


class DummyBoardFactory(BoardFactory[DummyBoardData]):
    @classmethod
    def create(cls, *args, **kwargs):
        return BoardFactory[DummyBoardData].create(*args, **kwargs)


class DummyBoardInterface(BoardInterface[DummyBoardData]):
    pass


class DummyBoardValidator(BoardValidator[DummyBoardData]):
    @classmethod
    def is_valid(cls, data, *args, **kwargs):
        return BoardValidator[DummyBoardData].is_valid(data=data, *args, **kwargs)

    @classmethod
    def validate(cls, data, *args, **kwargs):
        return BoardValidator[DummyBoardData].validate(data=data, *args, **kwargs)


@pytest.fixture
def dummy_board_data() -> DummyBoardData:
    return DummyBoardData()

@pytest.fixture
def dummy_board_factory(dummy_board_data: DummyBoardData) -> BoardFactory:
    return DummyBoardFactory(dummy_board_data)

@pytest.fixture
def dummy_board_interface(dummy_board_data: DummyBoardData) -> BoardInterface:
    return DummyBoardInterface(dummy_board_data)

@pytest.fixture
def dummy_board_validator(dummy_board_data: DummyBoardData) -> BoardValidator:
    return DummyBoardValidator(dummy_board_data)

