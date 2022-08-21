
import numpy as np
from chess.color import Color
from typing import SupportsInt


class ChessPiece:
    value: int = 0
    letter: str = ''

    def __init__(self, color: Color, *args, **kwargs):
        self.color: Color = color
        self.has_moved: bool = False

    def __str__(self):
        return f'{self.color.name.capitalize()} {self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color.__class__.__name__}.{self.color.name})'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.color == other.color

    def __hash__(self):
        return hash(self.__class__) & hash(self.color)













