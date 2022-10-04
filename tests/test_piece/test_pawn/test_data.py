
import pytest

def test_all_paths(dummy_pawn_data):
    assert dummy_pawn_data.all_paths == dummy_pawn_data.move_paths | dummy_pawn_data.capture_paths | dummy_pawn_data.en_passant_paths

