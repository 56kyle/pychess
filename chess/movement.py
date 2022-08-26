
from dataclasses import dataclass
from enum import Enum

from chess.offset import Offset

INFINITE_STEPS = 0


class AllowedMovementTypes(Enum):
    MOVE_ONLY = 1
    CAPTURE_ONLY = 2
    BOTH = 3


@dataclass(frozen=True)
class Movement:
    offset: Offset = Offset(0, 0)
    max_steps: int = INFINITE_STEPS
    allowed_movement_types: AllowedMovementTypes = AllowedMovementTypes.BOTH


