
import pytest


def test_init(dummy_interface):
    assert dummy_interface

def test_is_valid(dummy_interface):
    with pytest.raises(NotImplementedError):
        dummy_interface.is_valid()

def test_validate(dummy_interface):
    with pytest.raises(NotImplementedError):
        dummy_interface.validate()

