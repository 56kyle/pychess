from dataclasses import dataclass

from chess.move import Move
from chess.piece import Piece
from chess.position import Position


@dataclass(frozen=True)
class Castle(Move):
    rook: Piece = None
    rook_origin: Position = None
    rook_destination: Position = None

    def __post_init__(self):
        if self.rook is None:
            raise ValueError('Castle must have a rook')
        if self.rook_origin is None:
            raise ValueError('Castle must have a rook origin')
        if self.rook_destination is None:
            raise ValueError('Castle must have a rook destination')


