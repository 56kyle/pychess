
import pytest
from chess.unit import Unit

class DummyUnit(Unit):
    def _get_unvalidated_move_coverage_offsets(self):
        return super()._get_unvalidated_move_coverage_offsets()


def test_get_unvalidated_move_coverage_offsets():
    dummy_unit = DummyUnit()
    assert not dummy_unit._get_unvalidated_move_coverage_offsets()

