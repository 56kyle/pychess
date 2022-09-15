
from abc import ABC, abstractmethod
from typing import Set

from chess.board import BoardFactory
from chess.castle_right import CastleRight
from chess.piece import Piece
from chess.position import Position
from chess.standard.board.data import StandardBoardData, T


class StandardBoardFactory(BoardFactory[T], ABC):
    @classmethod
    @abstractmethod
    def create(cls, pieces: Set[Piece],
               castling_rights: Set[CastleRight],
               en_passant_target_position: Position | None,
               half_move_draw_clock: int,
               full_move_number: int,
               width: int,
               height: int,
               *args,
               **kwargs) -> T:
        return StandardBoardData(
            pieces=pieces,
            castling_rights=castling_rights,
            en_passant_target_position=en_passant_target_position,
            half_move_draw_clock=half_move_draw_clock,
            full_move_number=full_move_number,
            width=width,
            height=height
        )


