
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Square:
    row: int
    column: int

