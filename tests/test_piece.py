


import pytest


from chess.piece import Piece
from chess.queen import Queen
from chess.position import Position


def test_move(dummy_piece):
    new_position: Position = Position(rank=2, file=2)
    assert dummy_piece.move(new_position) == Piece(
        position=new_position,
        color=dummy_piece.color,
        has_moved=True,
    )

def test_promote(dummy_piece):
    assert dummy_piece.promote(promotion=Queen) == Queen(
        position=dummy_piece.position,
        color=dummy_piece.color,
        has_moved=dummy_piece.has_moved,
    )



