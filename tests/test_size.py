
import pytest


from chess.position import Position


def test__contains__with_within_bounds(dummy_size):
    assert Position(rank=1, file=1) in dummy_size

def test__contains__with_out_of_bounds(dummy_size):
    assert Position(rank=9, file=9) not in dummy_size

def test__is_within_width_with_within_bounds(dummy_size):
    assert dummy_size._is_within_width(position=Position(rank=1, file=1)) is True

def test__is_within_width_with_out_of_bounds(dummy_size):
    assert dummy_size._is_within_width(position=Position(rank=1, file=9)) is False

def test__is_within_height_with_within_bounds(dummy_size):
    assert dummy_size._is_within_height(position=Position(rank=1, file=1)) is True

def test__is_within_height_with_out_of_bounds(dummy_size):
    assert dummy_size._is_within_height(position=Position(rank=9, file=1)) is False

