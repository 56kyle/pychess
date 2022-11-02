
import pytest

from chess.position import Position


def test_init():
    position = Position(1, 2)
    assert position
    assert position.file == 1
    assert position.rank == 2

def test_from_algebraic_with_valid_algebraic():
    assert Position.from_algebraic('a1') == Position(1, 1)

def test_from_algebraic_with_invalid_algebraic_length():
    with pytest.raises(ValueError):
        Position.from_algebraic('a')

def test_from_algebraic_with_invalid_algebraic_character():
    with pytest.raises(ValueError):
        Position.from_algebraic('a0')

def test__get_file_from_algebraic_with_valid_algebraic():
    assert Position._get_file_from_algebraic('a1') == 1

def test__get_file_from_algebraic_with_invalid_algebraic():
    with pytest.raises(ValueError):
        Position._get_file_from_algebraic('01')

def test__get_rank_from_algebraic_with_valid_algebraic():
    assert Position._get_rank_from_algebraic('a1') == 1

def test__get_rank_from_algebraic_with_invalid_algebraic():
    with pytest.raises(ValueError):
        Position._get_rank_from_algebraic('a0')

def test__validate_algebraic_length_with_valid_algebraic_length():
    assert Position._validate_algebraic_length(notation='a1') is None

def test__validate_algebraic_length_with_invalid_algebraic_length():
    with pytest.raises(ValueError):
        Position._validate_algebraic_length(notation='a1x')

def test_offset():
    position = Position(1, 2)
    assert position.offset(dx=1, dy=2) == Position(2, 4)

def test_distance_to_with_whole_answer():
    position = Position(1, 1)
    assert position.distance_to(position=Position(4, 5)) == 5.0

def test_distance_to_with_fraction_answer():
    position = Position(1, 2)
    assert position.distance_to(position=Position(3, 4)) == 2.8284271247461903

