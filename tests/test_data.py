
import pytest

from dataclasses import dataclass

from chess.data import AbstractData


@dataclass(frozen=True)
class DummyData(AbstractData):
    pass


class TestDummyData:
    def test_init(self):
        assert DummyData()

