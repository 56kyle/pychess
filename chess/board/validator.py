from typing import Set, TypeVar

from chess.board.data import BoardData, T
from chess.board.exceptions import BoardValidationError
from chess.castle_right import CastleRight
from chess.piece import Piece
from chess.validator import AbstractValidator


class BoardValidator(AbstractValidator[T]):
    @classmethod
    def validate(cls, data: T):
        cls._validate_data(data=data)

    @classmethod
    def _validate_data(cls, data: T):
        cls._validate_pieces(pieces=data.pieces)
        cls._validate_castling_rights(castling_rights=data.castling_rights)
        cls._validate_en_passant_target_position(en_passant_target_position=data.en_passant_target_position)
        cls._validate_half_move_draw_clock(half_move_draw_clock=data.half_move_draw_clock)
        cls._validate_full_move_number(full_move_number=data.full_move_number)
        cls._validate_width(width=data.width)
        cls._validate_height(height=data.height)

    @classmethod
    def _validate_pieces(cls, pieces: Set[Piece]):
        pass

    @classmethod
    def _validate_castling_rights(cls, castling_rights: Set[CastleRight]):
        pass

    @classmethod
    def _validate_en_passant_target_position(cls, en_passant_target_position: Piece | None):
        pass

    @classmethod
    def _validate_half_move_draw_clock(cls, half_move_draw_clock: int):
        pass

    @classmethod
    def _validate_full_move_number(cls, full_move_number: int):
        pass

    @classmethod
    def _validate_width(cls, width: int):
        pass

    @classmethod
    def _validate_height(cls, height: int):
        pass


V = TypeVar('V', bound=BoardValidator)

