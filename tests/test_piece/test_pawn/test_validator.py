import pytest

from chess.piece.pawn.data import PawnData
from chess.piece.pawn.exceptions import PawnValidationError
from chess.piece.pawn.validator import PawnValidator, V


def test_init(dummy_pawn_data):
    assert PawnValidator[PawnData](dummy_pawn_data)


def test__validate_data(dummy_pawn_data):
    assert PawnValidator[PawnData]._validate_data(dummy_pawn_data) is None









