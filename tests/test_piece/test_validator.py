import pytest

from chess.piece.data import PieceData
from chess.piece.exceptions import PieceValidationError
from chess.piece.validator import PieceValidator, V


def test_init(dummy_piece_data):
    assert PieceValidator[PieceData](dummy_piece_data)


class TestValidatePosition:
    def test__validate_position_with_valid(self, dummy_piece_data):
        assert PieceValidator[PieceData]._validate_position(dummy_piece_data.position) is None


class TestValidatePositionFile:
    def test__validate_position_file_with_negative_int(self):
        with pytest.raises(PieceValidationError):
            PieceValidator[PieceData]._validate_position_file(-1)

    def test__validate_position_file_with_zero(self):
        with pytest.raises(PieceValidationError):
            PieceValidator[PieceData]._validate_position_file(0)

    def test__validate_position_file_with_positive_int(self):
        assert PieceValidator[PieceData]._validate_position_file(1) is None


class TestValidatePositionRank:
    def test__validate_position_rank_with_negative_int(self):
        with pytest.raises(PieceValidationError):
            PieceValidator[PieceData]._validate_position_rank(-1)

    def test__validate_position_rank_with_zero(self):
        with pytest.raises(PieceValidationError):
            PieceValidator[PieceData]._validate_position_rank(0)

    def test__validate_position_rank_with_positive_int(self):
        assert PieceValidator[PieceData]._validate_position_rank(1) is None






