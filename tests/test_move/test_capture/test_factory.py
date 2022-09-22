import pytest

from chess.move.capture import CaptureFactory


def test_init(dummy_capture_data):
    assert CaptureFactory(data=dummy_capture_data)

def test_create(dummy_capture_data):
    assert CaptureFactory.create(**dummy_capture_data.__dict__) == dummy_capture_data

