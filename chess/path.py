
from dataclasses import dataclass

from chess.offset import Offset


@dataclass(frozen=True)
class Path:
    offset: Offset
    max_steps: int | None = None



