
from dataclasses import dataclass
from enum import Enum

from chess.offset import Offset


INFINITE_STEPS = 0


class AllowedMovementTypes(Enum):
    MOVE_ONLY = 1
    CAPTURE_ONLY = 2
    BOTH = 3


@dataclass(frozen=True)
class Path:
    offset: Offset = Offset(dy=0, dx=0)
    max_steps: int = INFINITE_STEPS
    allowed_path_types: AllowedMovementTypes = AllowedMovementTypes.BOTH

    def with_limited_max_steps(self, max_steps: int) -> 'Path':
        new_max_steps: int = min(self.max_steps, max_steps) if self.max_steps != INFINITE_STEPS else max_steps
        return Path(self.offset, new_max_steps, self.allowed_path_types)


