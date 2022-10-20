
from dataclasses import dataclass, replace

from chess.position import Position


@dataclass(frozen=True)
class Line:
    p1: Position
    p2: Position

    @property
    def slope(self) -> float:
        return (self.p2.rank - self.p1.rank) / (self.p2.file - self.p1.file)

    @property
    def y_intercept(self) -> float:
        return self.p1.rank - self.slope * self.p1.file

    def __contains__(self, position: Position) -> bool:
        return self.is_colinear(position=position)

    def offset(self, dx: int = 0, dy: int = 0) -> 'Line':
        return replace(self, p1=self.p1.offset(dx=dx, dy=dy), p2=self.p2.offset(dx=dx, dy=dy))

    def is_colinear(self, position: Position) -> bool:
        return position.rank == self.slope * position.file + self.y_intercept

    def is_closer_to_p2_than_p1(self, position: Position) -> bool:
        return self.p1.distance_to(position=position) > self.p2.distance_to(position=position)

    def is_between_p1_and_p2(self, position: Position) -> bool:
        return (self.p1.file <= position.file <= self.p2.file) and (self.p1.rank <= position.rank <= self.p2.rank)




