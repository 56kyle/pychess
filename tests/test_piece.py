from dataclasses import replace

import pytest


from chess.piece import Piece
from chess.queen import Queen
from chess.position import Position
from chess.ray import Ray


def test_get_move_lines(dummy_piece):
    assert dummy_piece.get_move_lines() == set()

def test_get_capture_lines(dummy_piece):
    assert dummy_piece.get_capture_lines() == set()

def test_get_en_passant_lines(dummy_piece):
    assert dummy_piece.get_en_passant_lines() == set()

def test_get_castle_lines(dummy_piece):
    assert dummy_piece.get_castle_lines() == set()

def test_adjust_lines_to_position(dummy_piece):
    dummy_piece_at_2_2: Piece = replace(dummy_piece, position=Position(rank=2, file=2))
    line: Ray = Ray(p1=Position(rank=1, file=1), p2=Position(rank=3, file=3))
    assert dummy_piece_at_2_2.adjust_lines_to_position({line}) == {
        Ray(p1=Position(rank=3, file=3), p2=Position(rank=5, file=5))
    }

def test_move(dummy_piece):
    new_position: Position = Position(rank=2, file=2)
    assert dummy_piece.move(new_position) == replace(dummy_piece, position=new_position, has_moved=True)

def test_promote(dummy_piece):
    assert dummy_piece.promote(promotion=Queen) == replace(dummy_piece, type=Queen.type)

def test_is_enemy_with_enemy(dummy_a1_white_queen, dummy_a3_black_king):
    assert dummy_a1_white_queen.is_enemy(piece=dummy_a3_black_king)

def test_is_enemy_with_ally(dummy_a1_white_queen, dummy_a3_white_king):
    assert not dummy_a1_white_queen.is_enemy(piece=dummy_a3_white_king)

def test_is_ally_with_ally(dummy_a1_white_queen, dummy_a3_white_king):
    assert dummy_a1_white_queen.is_ally(piece=dummy_a3_white_king)

def test_is_ally_with_enemy(dummy_a1_white_queen, dummy_a3_black_king):
    assert not dummy_a1_white_queen.is_ally(piece=dummy_a3_black_king)

