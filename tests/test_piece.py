from dataclasses import replace

import pytest


from chess.piece import Piece
from chess.queen import Queen
from chess.position import Position


def test_move(dummy_piece):
    new_position: Position = Position(rank=2, file=2)
    assert dummy_piece.move(new_position) == replace(dummy_piece, position=new_position, has_moved=True)

def test_promote(dummy_piece):
    assert dummy_piece.promote(promotion=Queen) == replace(dummy_piece, meta=Queen.meta)



