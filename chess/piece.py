
from dataclasses import dataclass, field
from chess.color import Color


@dataclass(frozen=True)
class ChessPiece:
    color: Color
    name: str
    value: int
    letter: str
    symbol: str


WhiteKing = ChessPiece(Color.WHITE, 'King', 0, 'K', '\u2654')
WhiteQueen = ChessPiece(Color.WHITE, 'Queen', 9, 'Q', '\u2655')
WhiteRook = ChessPiece(Color.WHITE, 'Rook', 5, 'R', '\u2656')
WhiteBishop = ChessPiece(Color.WHITE, 'Bishop', 3, 'B', '\u2657')
WhiteKnight = ChessPiece(Color.WHITE, 'Knight', 3, 'N', '\u2658')
WhitePawn = ChessPiece(Color.WHITE, 'Pawn', 1, 'P', '\u2659')

BlackKing = ChessPiece(Color.BLACK, 'King', 0, 'K', '\u265A')
BlackQueen = ChessPiece(Color.BLACK, 'Queen', 9, 'Q', '\u265B')
BlackRook = ChessPiece(Color.BLACK, 'Rook', 5, 'R', '\u265C')
BlackBishop = ChessPiece(Color.BLACK, 'Bishop', 3, 'B', '\u265D')
BlackKnight = ChessPiece(Color.BLACK, 'Knight', 3, 'N', '\u265E')
BlackPawn = ChessPiece(Color.BLACK, 'Pawn', 1, 'P', '\u265F')









