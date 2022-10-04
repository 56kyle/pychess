import pytest


def test_all_paths(dummy_king_data):
    assert dummy_king_data.all_paths == dummy_king_data.move_paths | dummy_king_data.capture_paths | dummy_king_data.castle_paths

