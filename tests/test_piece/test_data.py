
import pytest


def test_all_paths(dummy_piece):
    assert dummy_piece.data.all_paths == dummy_piece.data.move_paths | dummy_piece.data.capture_paths

