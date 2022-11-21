
import pytest

from chess.board import Board
from chess.castle_right import CastleRight
from chess.color import Color
from chess.king import King
from chess.pawn import Pawn
from chess.piece import Piece
from chess.position_constants import *
from chess.queen import Queen
from chess.rook import Rook
from chess.size import Size


@pytest.fixture
def dummy_board():
    return Board(
        pieces=set(),
        castling_rights=set(),
    )

@pytest.fixture
def dummy_piece():
    return Piece(
        position=A1,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_size():
    return Size(width=8, height=8)

@pytest.fixture
def dummy_e4_white_pawn():
    return Pawn(
        position=E4,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_e5_black_pawn():
    return Pawn(
        position=E5,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_e5_white_pawn():
    return Pawn(
        position=E5,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_d5_black_pawn():
    return Pawn(
        position=D5,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_e1_white_king():
    return King(
        position=E1,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a1_white_rook():
    return Rook(
        position=A1,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a1_white_queen():
    return Queen(
        position=A1,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a2_white_pawn():
    return Pawn(
        position=A2,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a7_black_pawn():
    return Pawn(
        position=A7,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_a3_white_pawn():
    return Pawn(
        position=A3,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a6_black_pawn():
    return Pawn(
        position=A6,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_a3_white_king():
    return King(
        position=A3,
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a3_black_king():
    return King(
        position=A3,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_b3_black_king():
    return King(
        position=B3,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_c3_black_pawn():
    return Pawn(
        position=C3,
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_position():
    return A1

@pytest.fixture
def dummy_white_castle_right():
    return CastleRight(
        color=Color.WHITE,
        rook_origin=A8,
        rook_destination=A6,
        king_origin=A5,
        king_destination=A7,
    )


