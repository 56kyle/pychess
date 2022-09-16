import pytest

from chess.piece.queen.data import QueenData
from chess.piece.queen.exceptions import QueenValidationError
from chess.piece.queen.validator import QueenValidator, V


def test_init(dummy_queen_data):
    assert QueenValidator[QueenData](dummy_queen_data)


def test__validate_data(dummy_queen_data):
    assert QueenValidator[QueenData]._validate_data(dummy_queen_data) is None









