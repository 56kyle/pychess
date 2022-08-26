
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
    offset: Offset = Offset(dy=0, dx=0)
    max_steps: int = INFINITE_STEPS
    allowed_movement_types: AllowedMovementTypes = AllowedMovementTypes.BOTH

    def with_limited_max_steps(self, max_steps: int) -> 'Movement':
        new_max_steps: int = min(self.max_steps, max_steps) if self.max_steps != INFINITE_STEPS else max_steps
        return Movement(self.offset, new_max_steps, self.allowed_movement_types)


