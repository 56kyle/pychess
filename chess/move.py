
from dataclasses import dataclass
import chess.piece


@dataclass
class Move:
    piece: chess.piece.ChessPiece
    from_column: int
    from_row: int
    to_column: int
    to_row: int
    captured_piece: chess.piece.ChessPiece = None
    promotion: chess.piece.ChessPiece = None
    check: bool = False


