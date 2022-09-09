
from dataclasses import dataclass

from .offset import Offset


@dataclass(frozen=True)
class Position:
    file: int  # 1-indexed
    rank: int  # 1-indexed

    def __post_init__(self):
        if self.file <= 0:
            raise ValueError(f'File must be a positive integer: {self.file}')
        if self.rank <= 0:
            raise ValueError(f'Rank must be a positive integer: {self.rank}')

    @classmethod
    def from_fen(cls, fen: str) -> 'Position':
        return cls(int(fen[1]), ord(fen[0]) - ord('a') + 1)

    def to_fen(self) -> str:
        return chr(ord('a') + self.file - 1) + str(self.rank)

    def offset(self, offset: Offset) -> 'Position':
        return Position(self.rank + offset.dy, self.file + offset.dx)

