
from dataclasses import dataclass
from typing import List, Set

from .castle_right import CastleRight
from .color import Color
from .position import Position
from .piece import Piece


STANDARD_BOARD_WIDTH = 8
STANDARD_BOARD_HEIGHT = 8


@dataclass(frozen=True)
class BoardState:
    pieces: List[Piece]
    castling_rights: Set[CastleRight]
    en_passant_target_position: Position | None
    half_move_draw_clock: int
    full_move_number: int
    width: int = STANDARD_BOARD_WIDTH
    height: int = STANDARD_BOARD_HEIGHT

    def get_piece_at(self, position: Position) -> Piece | None:
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def get_pieces_of_color(self, color: Color) -> List[Piece]:
        return [piece for piece in self.pieces if piece.color == color]

    def get_piece_coverage(self, piece: Piece) -> List[Position]:
        pass








