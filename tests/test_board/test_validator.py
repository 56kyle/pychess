import pytest

from chess.board import BoardValidator


def test_init(dummy_board_validator):
    assert dummy_board_validator

def test_is_valid(dummy_board_validator):
    with pytest.raises(NotImplementedError):
        dummy_board_validator.is_valid()

def test_validate(dummy_board_validator):
    dummy_board_validator.validate()


class TestValidatePieces:
    def test__validate_pieces_with_empty_set(self):
        BoardValidator._validate_pieces(
            pieces=set(),
        )

    def test__validate_pieces_with

