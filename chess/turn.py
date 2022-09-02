

from dataclasses import dataclass, field

from chess.color import Color
from chess.move import Move


@dataclass(frozen=True)
class Turn:
    color: Color
    move: Move
    time_spent: float = 0








