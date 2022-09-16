import pytest

from chess.piece.bishop.data import BishopData
from chess.piece.bishop.exceptions import BishopValidationError
from chess.piece.bishop.validator import BishopValidator, V


def test_init(dummy_bishop_data):
    assert BishopValidator[BishopData](dummy_bishop_data)


def test__validate_data(dummy_bishop_data):
    assert BishopValidator[BishopData]._validate_data(dummy_bishop_data) is None













