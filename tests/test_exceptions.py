
import pytest

from chess.exceptions import ValidationError


def test_validation_error():
    with pytest.raises(ValidationError):
        raise ValidationError
