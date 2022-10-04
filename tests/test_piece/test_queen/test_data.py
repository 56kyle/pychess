
import pytest


def test_all_paths(dummy_queen_data):
    assert dummy_queen_data.all_paths == dummy_queen_data.move_paths | dummy_queen_data.capture_paths

