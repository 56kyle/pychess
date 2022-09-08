
from dataclasses import dataclass, field

import chess.unit
from chess.offset import Offset

from chess.square import Square


@dataclass(frozen=True)
class Move:
    unit: chess.unit.Unit = field(hash=False)
    from_square: Square
    offset: Offset
    captured: chess.unit.Unit = None
    promotion: chess.unit.Unit = None
    check: bool = False


