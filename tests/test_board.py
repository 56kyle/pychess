

import pytest

from dataclasses import replace

from chess.bishop import WhiteBishop, BlackBishop
from chess.board import Board
from chess.color import Color
from chess.king import BlackKing
from chess.offset import Offset
from chess.pawn import Pawn, BlackPawn, WhitePawn
from chess.position import Position
from chess.position_constants import *
from chess.queen import Queen, WhiteQueen
from chess.segment import Segment


def test_move(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    dummy_board.move(piece=dummy_piece, destination=B2)
    assert dummy_board.pieces == {replace(dummy_piece, position=B2, has_moved=True)}

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
    assert dummy_board._validate_in_bounds(position=A1) is None

def test_promote(dummy_board, dummy_piece):
    dummy_board.pieces.add(dummy_piece)
    dummy_board.promote(piece=dummy_piece, promotion=Queen)
    assert dummy_board.pieces == {replace(dummy_piece, type=Queen.type)}

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

def test_is_promotion_position_with_white_promotion_position(dummy_board):
    assert dummy_board.is_promotion_position(position=Position(rank=8, file=1), color=Color.WHITE)

def test_is_promotion_position_with_black_promotion_position(dummy_board):
    assert dummy_board.is_promotion_position(position=A1, color=Color.BLACK)

def test_is_promotion_position_with_not_promotion_position(dummy_board):
    assert not dummy_board.is_promotion_position(position=A1, color=Color.WHITE)

def test_is_check_present_with_check():
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackKing(A3),
        }
    ).is_check_present() is True

def test_is_check_present_with_no_check():
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackKing(B3),
        }
    ).is_check_present() is False

def test_is_check_present_with_ally_blocked_check():
    assert Board(
        pieces={
            WhiteQueen(A1),
            WhiteBishop(A2),
            BlackKing(A3),
        }
    ).is_check_present() is False

def test_is_check_with_enemy_blocked_check():
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackBishop(A2),
            BlackKing(A3),
        }
    )

def test_is_check_with_color_filter():
    dummy_board: Board = Board(
        pieces={
            WhiteQueen(A1),
            BlackKing(A3),
        }
    )
    assert dummy_board.is_check_present(color=Color.WHITE) is False
    assert dummy_board.is_check_present(color=Color.BLACK) is True

def test__iter_line_positions_with_horizontal():
    assert list(Board(pieces=set())._iter_line_positions(
        line=Segment(A1, A8),
    )) == [A1, A2, A3, A4, A5, A6, A7, A8]

def test__iter_line_positions_with_vertical():
    assert list(Board(pieces=set())._iter_line_positions(
        line=Segment(A1, H1),
    )) == [A1, B1, C1, D1, E1, F1, G1, H1]

def test__iter_line_positions_with_diagonal():
    assert list(Board(pieces=set())._iter_line_positions(
        line=Segment(A1, H8),
    )) == [A1, B2, C3, D4, E5, F6, G7, H8]

def test_get_piece_movements_with_queen(dummy_board, dummy_a1_white_queen):
    assert Board(
        pieces={
            WhiteQueen(A1),
        }
    ).get_piece_movements(piece=WhiteQueen(A1)) == {
        A2, A3, A4, A5, A6, A7, A8,  # Rank
        B1, C1, D1, E1, F1, G1, H1,  # File
        B2, C3, D4, E5, F6, G7, H8,  # Diagonal
    }

def test_get_piece_movements_with_non_moved_white_pawn():
    assert Board(
        pieces={
            WhitePawn(A2),
        }
    ).get_piece_movements(piece=WhitePawn(A2)) == {
        A3, A4,
    }

def test_get_piece_movements_with_non_moved_black_pawn():
    assert Board(
        pieces={
            BlackPawn(A7),
        }
    ).get_piece_movements(piece=BlackPawn(A7)) == {
        A6, A5,
    }

def test_get_piece_movements_with_moved_white_pawn():
    assert Board(
        pieces={
            WhitePawn(A3, has_moved=True),
        }
    ).get_piece_movements(piece=WhitePawn(A3, has_moved=True)) == {
        A4,
    }

def test_get_piece_movements_with_moved_black_pawn():
    moved_pawn: Pawn = BlackPawn(A6, has_moved=True)
    assert Board(pieces={moved_pawn}).get_piece_movements(piece=moved_pawn) == {A5}

def test_get_piece_capture_targets_with_no_targets():
    assert Board(
        pieces={
            WhiteQueen(A1),
            WhitePawn(C2),
            BlackKing(A3),
        }
    ).get_piece_capture_targets(piece=BlackKing(A3)) == set()

def test_get_piece_capture_targets_with_normal_target(dummy_board, dummy_a1_white_queen, dummy_a3_black_king):
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackKing(A3),
        }
    ).get_piece_capture_targets(piece=WhiteQueen(A1)) == {BlackKing(A3)}

def test_get_piece_capture_targets_with_multiple_targets():
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackKing(A3),
            BlackPawn(C3),
        }
    ).get_piece_capture_targets(piece=WhiteQueen(A1)) == {BlackKing(A3), BlackPawn(C3)}


def test_get_piece_capture_targets_with_direct_target():
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackKing(A3),
        }
    ).get_piece_capture_targets(piece=WhiteQueen(A1)) == {BlackKing(A3)}

def test_get_piece_capture_targets_with_ally_blocked_target():
    assert Board(
        pieces={
            WhiteQueen(A1),
            WhitePawn(A2),
            BlackKing(A3),
        }
    ).get_piece_capture_targets(piece=WhiteQueen(A1)) == set()

def test_get_piece_capture_targets_with_enemy_blocked_target():
    assert Board(
        pieces={
            WhiteQueen(A1),
            BlackPawn(A2),
            BlackKing(A3),
        }
    ).get_piece_capture_targets(piece=WhiteQueen(A1)) == {BlackPawn(A2)}

def test_get_piece_en_passant_targets_with_no_targets():
    assert Board(
        pieces={
            WhiteQueen(A1),
        }
    ).get_piece_en_passant_targets(piece=WhiteQueen(A1)) == set()

def test_get_piece_en_passant_targets_with_direct_target(dummy_white_castle_right):
    dummy_board = Board(
        pieces={
            BlackPawn(D5),
            WhitePawn(E5),
        },
        castling_rights={dummy_white_castle_right},
        en_passant_target_position=D6,
    )
    assert dummy_board.get_piece_en_passant_targets(piece=WhitePawn(E5)) == {BlackPawn(D5)}







