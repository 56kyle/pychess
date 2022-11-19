import datetime

from dataclasses import dataclass, field
from fractions import Fraction
from typing import List


@dataclass(frozen=True)
class Site:
    city: str
    region: str
    country: str


class Date(datetime.date):
    def __str__(self):
        return f'{self._year_str()}-{self._month_str()}-{self._day_str()}'

    def _year_str(self) -> str:
        return str(self.year) if self.year else '????'

    def _month_str(self) -> str:
        return str(self.month) if self.month else '??'

    def _day_str(self) -> str:
        return str(self.day) if self.day else '??'


@dataclass(frozen=True)
class PlayerName:
    first: str = None
    last: str = None
    middle_names: List[str] = field(default_factory=list)

    def __str__(self):
        return f'{self.last}, {self.first}'


@dataclass(frozen=True)
class Result:
    white: Fraction = None
    black: Fraction = None

    def __post_init__(self):
        if self.white is None and self.black is not None:
            raise ValueError(f'white must be set if black is set: {self.white} {self.black}')
        if self.black is None and self.white is not None:
            raise ValueError(f'black must be set if white is set: {self.white} {self.black}')

    def __str__(self):
        return f'{self.white}-{self.black}' if self.white is not None and self.black is not None else '*'


@dataclass(frozen=True)
class TimeControl:
    time: datetime.time =
    increment: datetime.time = None
    sudden_death_seconds: int

    def __str__(self):
        return f'{self.time}/{self.increment}' if self.time is not None and self.increment is not None else '*'


