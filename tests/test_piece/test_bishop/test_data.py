import pytest


def test_all_paths(dummy_bishop_data):
    assert dummy_bishop_data.all_paths == dummy_bishop_data.move_paths | dummy_bishop_data.capture_paths


