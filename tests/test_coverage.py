
import pytest

from chess.coverage import Coverage
from chess.position import Position


def test_init_with_defaults():
    coverage = Coverage()
    assert coverage
    assert coverage.positions == set()

def test_init_with_values():
    positions = {Position(file=1, rank=1)}
    coverage = Coverage(positions=positions)
    assert coverage
    assert coverage.positions == positions

