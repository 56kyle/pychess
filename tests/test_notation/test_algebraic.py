import pytest
import chess.notation as notation


def test_init(fools_mate_game):
    assert notation.AlgebraicNotation(move=fools_mate_game.moves[0])

def test_get_indexes_from_square_with_min():
    assert notation.AlgebraicNotation.get_indexes_from_square('a1') == (0, 0)

def test_get_indexes_from_square_with_max():
    assert notation.AlgebraicNotation.get_indexes_from_square('h8') == (7, 7)

def test_get_indexes_from_square_with_invalid_square_column():
    with pytest.raises(ValueError):
        notation.AlgebraicNotation.get_indexes_from_square('i8')

def test_get_indexes_from_square_with_invalid_square_row():
    with pytest.raises(ValueError):
        notation.AlgebraicNotation.get_indexes_from_square('a9')


