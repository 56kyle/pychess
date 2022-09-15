from abc import ABC, abstractmethod
from typing import Set

from chess.board.data import BoardData, T
from chess.board.factory import BoardFactory, F
from chess.board.validator import BoardValidator, V
from chess.interface import AbstractInterface
from chess.piece import Piece


class Board(AbstractInterface[T, F, V], ABC):
    factory: F = BoardFactory[T]
    validator: V = BoardValidator[T]

    def __init__(self,
                 pieces: Set[Piece],
                 castling_rights: Set[str],
                 en_passant_target_position: str,
                 half_move_draw_clock: int,
                 full_move_number: int,
                 width: int,
                 height: int,
                 *args,
                 **kwargs):
        super().__init__(
            pieces=pieces,
            castling_rights=castling_rights,
            en_passant_target_position=en_passant_target_position,
            half_move_draw_clock=half_move_draw_clock,
            full_move_number=full_move_number,
            width=width,
            height=height,
            *args,
            **kwargs
        )

