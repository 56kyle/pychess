import pytest

from chess.data import T
from chess.exceptions import ValidationError
from chess.validator import AbstractValidator


class DummyValidatorPassingImpl(AbstractValidator):
    @classmethod
    def _validate_data(cls, data: T):
        pass

class DummyValidatorFailingImpl(AbstractValidator):
    @classmethod
    def _validate_data(cls, data: T):
        raise ValidationError('DummyValidatorFailingImpl._validate_data() failed.')


@pytest.fixture
def dummy_validator_passing_impl(dummy_data):
    return DummyValidatorPassingImpl(dummy_data)

@pytest.fixture
def dummy_validator_failing_impl(dummy_data):
    return DummyValidatorFailingImpl(dummy_data)


def test_init(dummy_validator):
    assert dummy_validator

class TestIsValid:
    def test_is_valid_with_no_impl(self, dummy_data):
        with pytest.raises(NotImplementedError):
            AbstractValidator.is_valid(dummy_data)

    def test_is_valid_with_passing_impl(self, dummy_validator_passing_impl, dummy_data):
        assert dummy_validator_passing_impl.is_valid(dummy_data)

    def test_is_valid_with_failing_impl(self, dummy_validator_failing_impl, dummy_data):
        assert not dummy_validator_failing_impl.is_valid(dummy_data)


class TestValidate:
    def test_validate_with_no_impl(self, dummy_data):
        with pytest.raises(NotImplementedError):
            AbstractValidator.validate(dummy_data)

    def test_validate_with_passing_impl(self, dummy_validator_passing_impl, dummy_data):
        assert dummy_validator_passing_impl.validate(dummy_data) is None

    def test_validate_with_failing_impl(self, dummy_validator_failing_impl, dummy_data):
        with pytest.raises(ValidationError):
            dummy_validator_failing_impl.validate(dummy_data)


class TestValidateData:
    def test__validate_data_with_no_impl(self, dummy_data):
        with pytest.raises(NotImplementedError):
            AbstractValidator._validate_data(dummy_data)

    def test__validate_data_with_passing_impl(self, dummy_validator_passing_impl, dummy_data):
        assert dummy_validator_passing_impl._validate_data(dummy_data) is None

    def test__validate_data_with_failing_impl(self, dummy_validator_failing_impl, dummy_data):
        with pytest.raises(ValidationError):
            dummy_validator_failing_impl._validate_data(dummy_data)

