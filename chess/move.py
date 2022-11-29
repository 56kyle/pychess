

from dataclasses import dataclass, field

from chess.piece_type import PieceType
from chess.position import Position
from chess.piece import Piece


@dataclass(frozen=True)
class Move:
    piece: Piece
    origin: Position
    destination: Position
    promotion: PieceType = None
    captures: set[Piece] = field(default_factory=set)

    def is_promotion(self) -> bool:
        return self.promotion is not None

    def is_capture(self) -> bool:
        return len(self.captures) > 0


