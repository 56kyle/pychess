
from dataclasses import dataclass, field
from chess.color import Color


@dataclass(frozen=True)
class ChessPiece:
    color: Color
    symbol: str
    name: str
    value: int
    letter: str

@dataclass(frozen=True)
class King(ChessPiece):
    name: str = 'King'
    value: int = 0
    letter: str = 'K'

@dataclass(frozen=True)
class Queen(ChessPiece):
    name: str = 'Queen'
    value: int = 9
    letter: str = 'Q'

@dataclass(frozen=True)
class Rook(ChessPiece):
    name: str = 'Rook'
    value: int = 5
    letter: str = 'R'

@dataclass(frozen=True)
class Bishop(ChessPiece):
    name: str = 'Bishop'
    value: int = 3
    letter: str = 'B'

@dataclass(frozen=True)
class Knight(ChessPiece):
    name: str = 'Knight'
    value: int = 3
    letter: str = 'N'

@dataclass(frozen=True)
class Pawn(ChessPiece):
    name: str = 'Pawn'
    value: int = 1
    letter: str = 'P'


WhiteKing = King(Color.WHITE, '\u2654')
WhiteQueen = Queen(Color.WHITE, '\u2655')
WhiteRook = Rook(Color.WHITE, '\u2656')
WhiteBishop = Bishop(Color.WHITE, '\u2657')
WhiteKnight = Knight(Color.WHITE, '\u2658')
WhitePawn = Pawn(Color.WHITE, '\u2659')

BlackKing = King(Color.BLACK, '\u265A')
BlackQueen = Queen(Color.BLACK, '\u265B')
BlackRook = Rook(Color.BLACK, '\u265C')
BlackBishop = Bishop(Color.BLACK, '\u265D')
BlackKnight = Knight(Color.BLACK, '\u265E')
BlackPawn = Pawn(Color.BLACK, '\u265F')









