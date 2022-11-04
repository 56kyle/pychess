import math
from dataclasses import dataclass, replace

from chess.notation.position import PositionNotation


@dataclass(frozen=True)
class Position:
    file: int  # 1-indexed
    rank: int  # 1-indexed

    @classmethod
    def from_algebraic(cls, notation: str) -> 'Position':
        cls._validate_algebraic_length(notation)
        file: int = cls._get_file_from_algebraic(notation)
        rank: int = cls._get_rank_from_algebraic(notation)
        return cls(file=file, rank=rank)

    @classmethod
    def _validate_algebraic_length(cls, notation: str):
        if len(notation) != 2:
            raise ValueError(f'Invalid notation length: {notation}')

    @classmethod
    def _get_file_from_algebraic(cls, notation: str) -> int:
        if notation[0] not in 'abcdefgh':
            raise ValueError(f'Invalid file notation: {notation}')
        return ord(notation[0]) - ord('a') + 1

    @classmethod
    def _get_rank_from_algebraic(cls, notation: str) -> int:
        if notation[1] not in '12345678':
            raise ValueError(f'Invalid rank notation: {notation}')
        return int(notation[1])

    def offset(self, dx: int = 0, dy: int = 0) -> 'Position':
        return replace(self, file=self.file + dx, rank=self.rank + dy)

    def distance_to(self, position: 'Position') -> float:
        return ((self.file - position.file) ** 2 + (self.rank - position.rank) ** 2) ** 0.5

    def theta_to(self, position: 'Position') -> float:
        """Returns the angle in radians between the line from self to position and the x-axis"""
        return math.atan2(position.rank - self.rank, position.file - self.file)


ZERO = Position(0, 0)

