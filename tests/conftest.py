
import pytest

from chess.board import Board
from chess.castle_right import CastleRight
from chess.color import Color
from chess.king import King
from chess.pawn import Pawn
from chess.piece import Piece
from chess.position import Position
from chess.rook import Rook
from chess.side import Side


@pytest.fixture
def dummy_board():
    return Board(
        pieces=set(),
        castling_rights=set(),
    )

@pytest.fixture
def dummy_piece():
    return Piece(
        position=Position(rank=1, file=1),
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_e4_white_pawn():
    return Pawn(
        position=Position(rank=4, file=5),
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_e5_black_pawn():
    return Pawn(
        position=Position(rank=5, file=5),
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_e5_white_pawn():
    return Pawn(
        position=Position(rank=5, file=5),
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_d5_black_pawn():
    return Pawn(
        position=Position(rank=5, file=4),
        color=Color.BLACK,
    )

@pytest.fixture
def dummy_e1_white_king():
    return King(
        position=Position(file=5, rank=1),
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_a1_white_rook():
    return Rook(
        position=Position(rank=1, file=1),
        color=Color.WHITE,
    )

@pytest.fixture
def dummy_position():
    return Position(rank=1, file=1)

@pytest.fixture
def dummy_castle_right():
    return CastleRight(
        color=Color.WHITE,
        side=Side.KING,
    )


