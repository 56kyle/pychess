
from dataclasses import dataclass
import chess.piece


@dataclass
class Move:
    piece: chess.piece.ChessPiece
    from_row: int
    from_column: int
    to_row: int
    to_column: int
    captured_piece: chess.piece.ChessPiece = None
    promotion: chess.piece.ChessPiece = None


