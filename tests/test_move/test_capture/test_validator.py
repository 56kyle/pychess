
import pytest

from chess.move.capture import CaptureData, CaptureValidator


def test_init(dummy_capture_validator):
    assert dummy_capture_validator

def test_is_valid(dummy_capture_validator, dummy_capture_data):
    assert CaptureValidator.is_valid(dummy_capture_data)

def test_validate(dummy_capture_data):
    assert CaptureValidator.validate(dummy_capture_data) is None


