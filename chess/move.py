
from dataclasses import dataclass, field
import chess.piece


@dataclass
class Move:
    row_start: int
    column_start: int
    row_end: int
    column_end: int
    removed_piece: chess.piece.ChessPiece = None
    promotion: chess.piece.ChessPiece = None

