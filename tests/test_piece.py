from dataclasses import replace

import pytest


from chess.piece import Piece
from chess.queen import Queen
from chess.position import Position
from chess.ray import Ray


def test_get_move_paths(dummy_piece):
    assert dummy_piece.get_move_paths() == set()

def test_get_capture_paths(dummy_piece):
    assert dummy_piece.get_capture_paths() == set()

def test_get_en_passant_paths(dummy_piece):
    assert dummy_piece.get_en_passant_paths() == set()

def test_get_castle_paths(dummy_piece):
    assert dummy_piece.get_castle_paths() == set()

def test_adjust_paths_to_position(dummy_piece):
    dummy_piece_at_2_2: Piece = replace(dummy_piece, position=Position(rank=2, file=2))
    path: Ray = Ray(p1=Position(rank=1, file=1), p2=Position(rank=3, file=3))
    assert dummy_piece_at_2_2.adjust_paths_to_position({path}) == {
        Ray(p1=Position(rank=3, file=3), p2=Position(rank=5, file=5))
    }

def test_move(dummy_piece):
    new_position: Position = Position(rank=2, file=2)
    assert dummy_piece.move(new_position) == replace(dummy_piece, position=new_position, has_moved=True)

def test_promote(dummy_piece):
    assert dummy_piece.promote(promotion=Queen) == replace(dummy_piece, meta=Queen.meta)



