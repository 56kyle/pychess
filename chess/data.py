
from dataclasses import dataclass
from typing import TypeVar


@dataclass(frozen=True)
class AbstractData:
    pass


T = TypeVar('T', bound=AbstractData)

