from typing import Set, TypeVar

from chess.board.data import BoardData, T
from chess.board.exceptions import BoardValidationError
from chess.castle_right import CastleRight
from chess.piece import Piece
from chess.position import Position
from chess.validator import AbstractValidator


class BoardValidator(AbstractValidator[T]):
    @classmethod
    def validate(cls, data: T):
        cls._validate_data(data=data)

    @classmethod
    def _validate_data(cls, data: T):
        cls._validate_pieces(pieces=data.pieces)
        cls._validate_castling_rights(castling_rights=data.castling_rights)
        cls._validate_en_passant_target_position(
            en_passant_target_position=data.en_passant_target_position, width=data.width, height=data.height)
        cls._validate_half_move_draw_clock(half_move_draw_clock=data.half_move_draw_clock)
        cls._validate_full_move_number(full_move_number=data.full_move_number)
        cls._validate_width(width=data.width)
        cls._validate_height(height=data.height)

    @classmethod
    def _validate_pieces(cls, pieces: Set[Piece]):
        for piece in pieces:
            piece.validate()

    @classmethod
    def _validate_castling_rights(cls, castling_rights: Set[CastleRight]):
        pass

    @classmethod
    def _validate_en_passant_target_position(cls, en_passant_target_position: Position | None, width: int, height: int):
        if en_passant_target_position is not None:
            cls._validate_en_passant_target_position_file(
                en_passant_target_position_file=en_passant_target_position.file, width=width)
            cls._validate_en_passant_target_position_rank(
                en_passant_target_position_rank=en_passant_target_position.rank, height=height)

    @classmethod
    def _validate_en_passant_target_position_file(cls, en_passant_target_position_file: int, width: int):
        cls._validate_en_passant_target_position_file_above_zero(
            en_passant_target_position_file=en_passant_target_position_file)
        cls._validate_en_passant_target_position_file_below_width(
            en_passant_target_position_file=en_passant_target_position_file, width=width)

    @classmethod
    def _validate_en_passant_target_position_file_above_zero(cls, en_passant_target_position_file: int):
        if en_passant_target_position_file < 1:
            raise BoardValidationError(
                f'En passant target position file must be greater than 0, not {en_passant_target_position_file}.'
            )

    @classmethod
    def _validate_en_passant_target_position_file_below_width(cls, en_passant_target_position_file: int, width: int):
        if en_passant_target_position_file > width:
            raise BoardValidationError(
                f'En passant target position file must be less than the board width of {width},'
                f' not {en_passant_target_position_file}.'
            )

    @classmethod
    def _validate_en_passant_target_position_rank(cls, en_passant_target_position_rank: int, height: int):
        cls._validate_en_passant_target_position_rank_above_zero(
            en_passant_target_position_rank=en_passant_target_position_rank)
        cls._validate_en_passant_target_position_rank_below_height(
            en_passant_target_position_rank=en_passant_target_position_rank, height=height)

    @classmethod
    def _validate_en_passant_target_position_rank_above_zero(cls, en_passant_target_position_rank: int):
        if en_passant_target_position_rank < 1:
            raise BoardValidationError(
                f'En passant target position rank must be greater than 0, not {en_passant_target_position_rank}.'
            )

    @classmethod
    def _validate_en_passant_target_position_rank_below_height(cls, en_passant_target_position_rank: int, height: int):
        if en_passant_target_position_rank > height:
            raise BoardValidationError(
                f'En passant target position rank must be less than the board height of {height},'
                f' not {en_passant_target_position_rank}.'
            )

    @classmethod
    def _validate_half_move_draw_clock(cls, half_move_draw_clock: int):
        if half_move_draw_clock < 0:
            raise BoardValidationError(f'Half move draw clock must be greater than or equal to 0, not {half_move_draw_clock}.')

    @classmethod
    def _validate_full_move_number(cls, full_move_number: int):
        if full_move_number < 0:
            raise BoardValidationError(f'Full move number must be greater than or equal to 0, not {full_move_number}.')

    @classmethod
    def _validate_width(cls, width: int):
        if width < 1:
            raise BoardValidationError(f'Width must be greater than or equal to 1, not {width}.')

    @classmethod
    def _validate_height(cls, height: int):
        if height < 1:
            raise BoardValidationError(f'Height must be greater than or equal to 1, not {height}.')


V = TypeVar('V', bound=BoardValidator)

