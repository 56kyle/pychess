
from dataclasses import dataclass
from enum import Enum

from chess.offset import Offset


INFINITE_STEPS = -999


class AllowedPathTypes(Enum):
    MOVE_ONLY = 1
    CAPTURE_ONLY = 2
    BOTH = 3
    EN_PASSANT = 4
    CASTLE = 5


@dataclass(frozen=True)
class Path:
    offset: Offset = Offset(dy=0, dx=0)
    max_steps: int = INFINITE_STEPS
    allowed_path_types: AllowedPathTypes = AllowedPathTypes.BOTH


