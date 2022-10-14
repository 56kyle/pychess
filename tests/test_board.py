

import pytest

from dataclasses import replace

from chess.color import Color
from chess.offset import Offset
from chess.pawn import Pawn
from chess.position import Position
from chess.queen import Queen


def test_move(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    dummy_board.move(piece=dummy_piece, destination=Position(rank=2, file=2))
    assert dummy_board.pieces == {replace(dummy_piece, position=Position(rank=2, file=2), has_moved=True)}

def test__validate_destination_is_empty_with_occupied_destination(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    with pytest.raises(ValueError):
        dummy_board._validate_destination_is_empty(dummy_piece.position)

def test__validate_destination_is_empty_with_empty_destination(dummy_board, dummy_piece):
    assert dummy_board._validate_destination_is_empty(dummy_piece.position) is None

def test__validate_in_bounds_with_out_of_bounds(dummy_board):
    with pytest.raises(ValueError):
        dummy_board._validate_in_bounds(position=Position(rank=9, file=9))

def test__validate_in_bounds_with_in_bounds(dummy_board):
    assert dummy_board._validate_in_bounds(position=Position(rank=1, file=1)) is None

def test_promote(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    dummy_board.promote(piece=dummy_piece, promotion=Queen)
    assert dummy_board.pieces == {replace(dummy_piece, meta=Queen.meta)}

def test__validate_is_allowed_promotion_with_allowed(dummy_board):
    assert dummy_board._validate_is_allowed_promotion(promotion=Queen) is None

def test__validate_is_allowed_promotion_with_not_allowed(dummy_board):
    with pytest.raises(ValueError):
        dummy_board._validate_is_allowed_promotion(promotion=Pawn)

def test_get_colored_pieces(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    wrong_color_dummy_piece = replace(dummy_piece, position=Position(rank=4, file=4), color=Color.BLACK)
    dummy_board.pieces.add(wrong_color_dummy_piece)
    colored_pieces = dummy_board.get_colored_pieces(color=dummy_piece.color)
    assert colored_pieces == {dummy_piece}
    assert wrong_color_dummy_piece not in colored_pieces

def test_get_piece(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    assert dummy_board.get_piece(position=dummy_piece.position) == dummy_piece

def test_get_max_steps(dummy_board):
    assert dummy_board.get_max_steps(position=Position(rank=1, file=1), offset=Offset(1, 1)) == 7

def test_is_promotion_position_with_white_promotion_position(dummy_board):
    assert dummy_board.is_promotion_position(position=Position(rank=8, file=1), color=Color.WHITE)

def test_is_promotion_position_with_black_promotion_position(dummy_board):
    assert dummy_board.is_promotion_position(position=Position(rank=1, file=1), color=Color.BLACK)

def test_is_promotion_position_with_not_promotion_position(dummy_board):
    assert not dummy_board.is_promotion_position(position=Position(rank=1, file=1), color=Color.WHITE)

def test_is_promotion_position_with_invalid(dummy_board):
    with pytest.raises(ValueError):
        dummy_board.is_promotion_position(position=Position(rank=0, file=0), color=Color.WHITE)

def test_in_bounds_with_min(dummy_board):
    assert dummy_board.in_bounds(position=Position(rank=1, file=1))

def test_in_bounds_with_max(dummy_board):
    assert dummy_board.in_bounds(position=Position(rank=8, file=8))

def test_in_bounds_with_out_of_bounds(dummy_board):
    assert not dummy_board.in_bounds(position=Position(rank=9, file=9))

def test_in_bounds_with_invalid(dummy_board):
    with pytest.raises(ValueError):
        dummy_board.in_bounds(position=Position(rank=0, file=0))





