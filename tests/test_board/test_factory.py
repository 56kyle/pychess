import pytest

from chess.board import BoardFactory


def test_init(dummy_board_data):
    assert BoardFactory(data=dummy_board_data)

def test_create(dummy_board_data):
    assert BoardFactory.create(
        pieces=dummy_board_data.pieces,
        castling_rights=dummy_board_data.castling_rights,
        en_passant_target_position=dummy_board_data.en_passant_target_position,
        half_move_draw_clock=dummy_board_data.half_move_draw_clock,
        full_move_number=dummy_board_data.full_move_number,
        width=dummy_board_data.width,
        height=dummy_board_data.height
    ) == dummy_board_data
