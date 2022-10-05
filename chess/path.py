
from dataclasses import dataclass

from chess.offset import Offset


@dataclass(frozen=True)
class Path:
    offset: Offset
    max_steps: int | None = None

    def get_offsets(self):
        if self.max_steps is None:
            return {self.offset}




