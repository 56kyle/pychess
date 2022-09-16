import pytest

from chess.piece.rook.data import RookData
from chess.piece.rook.exceptions import RookValidationError
from chess.piece.rook.validator import RookValidator, V


def test_init(dummy_rook_data):
    assert RookValidator[RookData](dummy_rook_data)


def test__validate_data(dummy_rook_data):
    assert RookValidator[RookData]._validate_data(dummy_rook_data) is None









