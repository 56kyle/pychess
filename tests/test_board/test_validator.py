import pytest

from chess.board import BoardValidator, BoardValidationError, BoardFactory, BoardData
from chess.piece import Piece, PieceData, PieceFactory
from chess.position import Position


def test_init(dummy_board_data):
    assert BoardValidator(data=dummy_board_data)

def test_is_valid(dummy_board_data):
    assert BoardValidator.is_valid(data=dummy_board_data)

def test_validate(dummy_board_data):
    assert BoardValidator.validate(data=dummy_board_data) is None

class TestValidateData:
    def test__validate_data(self, dummy_board_data):
        assert BoardValidator._validate_data(data=dummy_board_data) is None

class TestValidatePieces:
    def test__validate_pieces__empty(self):
        assert BoardValidator._validate_pieces(set()) is None

    def test__validate_pieces_with_pieces(self, dummy_piece):
        assert BoardValidator._validate_pieces({dummy_piece}) is None

class TestValidateCastlingRights:
    def test__validate_castling_rights__empty(self):
        assert BoardValidator._validate_castling_rights(set()) is None

    def test__validate_castling_rights_with_castling_rights(self, dummy_castle_right):
        assert BoardValidator._validate_castling_rights({dummy_castle_right}) is None

class TestValidateEnPassantTargetPosition:
    def test__validate_en_passant_target_position__none(self):
        assert BoardValidator._validate_en_passant_target_position(None, 99, 99) is None

    def test__validate_en_passant_target_position_with_position(self, dummy_position):
        assert BoardValidator._validate_en_passant_target_position(dummy_position, 99, 99) is None

class TestValidateEnPassantTargetPositionFile:
    def test__validate_en_passant_target_position_file__below_one(self):
        with pytest.raises(BoardValidationError):
            BoardValidator._validate_en_passant_target_position_file(0, 99)

    def test__validate_en_passant_target_position_file__above_width(self):
        with pytest.raises(BoardValidationError):
            BoardValidator._validate_en_passant_target_position_file(100, 99)

    def test__validate_en_passant_target_position_file__valid(self):
        assert BoardValidator._validate_en_passant_target_position_file(1, 99) is None

class TestValidateEnPassantTargetPositionRank:
    def test__validate_en_passant_target_position_rank_with_below_one(self):
        with pytest.raises(BoardValidationError):
            BoardValidator._validate_en_passant_target_position_rank(0, 99)

    def test__validate_en_passant_target_position_rank_with_above_height(self):
        with pytest.raises(BoardValidationError):
            BoardValidator._validate_en_passant_target_position_rank(100, 99)

    def test__validate_en_passant_target_position_rank_with_valid(self):
        assert BoardValidator._validate_en_passant_target_position_rank(1, 99) is None


class TestValidateHalfMoveDrawClock:
    def test__validate_half_move_draw_clock_with_negative_int(self):
        with pytest.raises(BoardValidationError) as e:
            BoardValidator._validate_half_move_draw_clock(-2)

    def test__validate_half_move_draw_clock_with_zero(self):
        assert BoardValidator._validate_half_move_draw_clock(0) is None

    def test__validate_half_move_draw_clock_with_positive_int(self):
        assert BoardValidator._validate_half_move_draw_clock(2) is None

class TestValidateFullMoveNumber:
    def test__validate_full_move_number_with_negative_int(self):
        with pytest.raises(BoardValidationError) as e:
            BoardValidator._validate_full_move_number(-2)

    def test__validate_full_move_number_with_zero(self):
        assert BoardValidator._validate_full_move_number(0) is None

    def test__validate_full_move_number_with_positive_int(self):
        assert BoardValidator._validate_full_move_number(2) is None

class TestValidateWidth:
    def test__validate_width_with_negative_int(self):
        with pytest.raises(BoardValidationError) as e:
            BoardValidator._validate_width(-2)

    def test__validate_width_with_zero(self):
        with pytest.raises(BoardValidationError) as e:
            BoardValidator._validate_width(0)

    def test__validate_width_with_positive_int(self):
        assert BoardValidator._validate_width(2) is None

class TestValidateHeight:
    def test__validate_height_with_negative_int(self):
        with pytest.raises(BoardValidationError) as e:
            BoardValidator._validate_height(-2)

    def test__validate_height_with_zero(self):
        with pytest.raises(BoardValidationError) as e:
            BoardValidator._validate_height(0)

    def test__validate_height_with_positive_int(self):
        assert BoardValidator._validate_height(2) is None


