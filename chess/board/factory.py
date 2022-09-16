
from typing import Set, TypeVar, Type

from chess.board.data import T, BoardData
from chess.castle_right import CastleRight
from chess.factory import AbstractFactory
from chess.piece import Piece
from chess.position import Position


class BoardFactory(AbstractFactory[T]):
    data_type: Type[T] = BoardData

    @classmethod
    def create(cls, pieces: Set[Piece],
               castling_rights: Set[CastleRight],
               en_passant_target_position: Position | None,
               half_move_draw_clock: int,
               full_move_number: int,
               width: int,
               height: int,
               *args,
               **kwargs) -> BoardData:
        return cls.data_type(
            pieces=pieces,
            castling_rights=castling_rights,
            en_passant_target_position=en_passant_target_position,
            half_move_draw_clock=half_move_draw_clock,
            full_move_number=full_move_number,
            width=width,
            height=height,
        )


F = TypeVar('F', bound=BoardFactory)

