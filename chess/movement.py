
from dataclasses import dataclass

from chess.offset import Offset

INFINITE_STEPS = 0

@dataclass(frozen=True)
class Movement:
    offset: Offset = Offset(0, 0)
    max_steps: int = INFINITE_STEPS


