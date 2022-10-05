
from typing import Set

from chess.castle_right import CastleRight
from chess.color import Color
from chess.move import Move
from chess.offset import Offset
from chess.piece import Piece
from chess.position import Position


class Board:
    width: int
    height: int

    def __init__(self,
                 pieces: Set[Piece],
                 castling_rights: Set[CastleRight],
                 en_passant_target_position: Position = None,
                 half_move_draw_clock: int = 0,
                 full_move_number: int = 0):
        self.pieces: Set[Piece] = pieces
        self.castling_rights: Set[CastleRight] = castling_rights
        self.en_passant_target_position: Position = en_passant_target_position
        self.half_move_draw_clock: int = half_move_draw_clock
        self.full_move_number: int = full_move_number

    def get_colored_pieces(self, color: Color) -> Set[Piece]:
        return {piece for piece in self.pieces if piece.color == color}

    def get_piece(self, position: Position) -> Piece | None:
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_valid_position(self, position: Position) -> bool:
        return self.is_valid_file(position.file) and self.is_valid_rank(position.rank)

    def is_valid_file(self, file: int) -> bool:
        return 1 <= file <= self.width

    def is_valid_rank(self, rank: int) -> bool:
        return 1 <= rank <= self.height













