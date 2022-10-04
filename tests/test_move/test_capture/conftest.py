import pytest
 
from dataclasses import dataclass, field
from typing import Set, Type

from chess.move.capture import CaptureData, CaptureFactory, Capture, CaptureValidator
from chess.offset import Offset
from chess.piece import Piece
from chess.position import Position

@pytest.fixture
def dummy_capture_data(dummy_piece) -> CaptureData:
    return CaptureData(
        piece_data=dummy_piece.data,
        piece_start=dummy_piece.data.position,
        offset=Offset(1, 1),
        captured_piece_data=dummy_piece,
        captured_piece_start=dummy_piece.data.position,
    )

@pytest.fixture
def dummy_capture_factory(dummy_capture_data: CaptureData) -> CaptureFactory:
    return CaptureFactory(dummy_capture_data)

@pytest.fixture
def dummy_capture(dummy_capture_data: CaptureData) -> Capture:
    return Capture[CaptureData, CaptureFactory, CaptureValidator](**dummy_capture_data.__dict__)

@pytest.fixture
def dummy_capture_validator(dummy_capture_data: CaptureData) -> CaptureValidator:
    return CaptureValidator(dummy_capture_data)

