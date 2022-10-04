
import pytest



def test_all_paths(dummy_rook_data):
    assert dummy_rook_data.all_paths == dummy_rook_data.move_paths | dummy_rook_data.capture_paths
