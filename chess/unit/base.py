

from chess.color import Color
from chess.move import Move
from chess.piece import ChessPiece
from chess.square import Square


class Unit(ChessPiece):
    color: Color

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_moved = False




