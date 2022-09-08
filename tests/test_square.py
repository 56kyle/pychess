
import pytest

from chess.offset import Offset
from chess.square import Square


def test_init():
    assert Square(row=0, column=0)

def test_eq_with_same_row_and_same_column():
    assert Square(row=0, column=0) == Square(row=0, column=0)

def test_eq_with_same_row_and_different_column():
    assert not Square(row=0, column=0) == Square(row=0, column=1)

def test_eq_with_different_row_and_same_column():
    assert not Square(row=0, column=0) == Square(row=1, column=0)

def test_eq_with_different_row_and_different_column():
    assert not Square(row=0, column=0) == Square(row=1, column=1)

def test_eq_with_other_type():
    assert not Square(row=0, column=0) == 1

def test_offset():
    assert Square(row=0, column=0).offset(offset=Offset(dy=1, dx=1)) == Square(row=1, column=1)


