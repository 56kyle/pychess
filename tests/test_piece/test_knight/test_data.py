import pytest


def test_all_paths(dummy_knight_data):
    assert dummy_knight_data.all_paths == dummy_knight_data.move_paths | dummy_knight_data.capture_paths

