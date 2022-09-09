
from dataclasses import dataclass, field

from chess.offset import Offset

INFINITY = -1

@dataclass(frozen=True)
class Path:
    offset: Offset
    steps: int = INFINITY

    def get_step(self, step: int) -> Offset:
        return self.offset * step

