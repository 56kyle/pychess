import pytest

import chess.move
import chess.notation


@pytest.fixture
def notated_move(fools_mate_game):
    return chess.notation.Notation(move=fools_mate_game.moves[0])


def test_init(fools_mate_game, notated_move):
    assert notated_move.move == fools_mate_game.moves[0]

def test_str(fools_mate_game, notated_move):
    with pytest.raises(NotImplementedError):
        str(notated_move)

def test_get_move_from_string(fools_mate_game, notated_move):
    with pytest.raises(NotImplementedError):
        chess.notation.Notation.get_move_from_string(notation='e4')

def test__get_notation_string(fools_mate_game, notated_move):
    with pytest.raises(NotImplementedError):
        notated_move._get_notation_string()






