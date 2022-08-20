
import pytest
from chess.notation import FIDE


def test_init(fools_mate_game):
    assert FIDE(fools_mate_game.moves[0])

