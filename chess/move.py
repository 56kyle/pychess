
from dataclasses import dataclass

import chess.unit

from chess.square import Square


@dataclass(frozen=True)
class Move:
    unit: chess.unit.Unit
    from_square: Square
    to_square: Square
    captured: chess.unit.Unit = None
    promotion: chess.unit.Unit = None
    check: bool = False


