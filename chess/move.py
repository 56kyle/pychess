from dataclasses import dataclass

from .castle_right import CastleRight
from .offset import Offset
from .piece import Piece, Rook
from .position import Position


@dataclass(frozen=True)
class Move:
    piece: Piece
    offset: Offset

@dataclass(frozen=True)
class Capture(Move):
    captured: Piece

@dataclass(frozen=True)
class Promotion(Move):
    promoted: Piece

@dataclass(frozen=True)
class EnPassant(Capture):
    target_position: Position

@dataclass(frozen=True)
class CapturePromotion(Capture, Promotion):
    pass

@dataclass(frozen=True)
class EnPassantPromotion(EnPassant, Promotion):
    pass

@dataclass(frozen=True)
class Castling(Move):
    rook: Rook
    rook_offset: Offset
    castling_right: CastleRight


def from_fen(fen: str) -> Move:
    pass

def to_fen(move: Move) -> str:
    pass

