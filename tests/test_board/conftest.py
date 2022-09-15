
import pytest

from chess.board import BoardData, BoardFactory, Board, BoardValidator


@pytest.fixture
def dummy_board_data() -> BoardData:
    return BoardData(
        pieces=set(),
        castling_rights=set(),
        en_passant_target_position=None,
        half_move_draw_clock=0,
        full_move_number=0,
        width=23,
        height=37,
    )

@pytest.fixture
def dummy_board_factory(dummy_board_data: BoardData) -> BoardFactory:
    return BoardFactory(dummy_board_data)

@pytest.fixture
def dummy_board_interface(dummy_board_data: BoardData) -> Board:
    return Board[BoardData, BoardFactory, BoardValidator](**dummy_board_data.__dict__)

@pytest.fixture
def dummy_board_validator(dummy_board_data: BoardData) -> BoardValidator:
    return BoardValidator(dummy_board_data)

