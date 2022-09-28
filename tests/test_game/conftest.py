from dataclasses import dataclass, field
from typing import Set, Type

import pytest

from chess.board import BoardData
from chess.game import GameData, GameFactory, Game, GameValidator


@pytest.fixture
def dummy_game_data() -> GameData:
    return GameData(
        board_data=BoardData(
            pieces=set(),
            castling_rights=set(),
            en_passant_target_position=None,
            half_move_draw_clock=0,
            full_move_number=0,
            width=23,
            height=37,
        ),
        allowed_pieces=set(),
        allowed_promotions=set(),
    )

@pytest.fixture
def dummy_game_factory(dummy_game_data: GameData) -> GameFactory:
    return GameFactory(dummy_game_data)

@pytest.fixture
def dummy_game(dummy_game_data: GameData) -> Game:
    return Game[GameData, GameFactory, GameValidator](**dummy_game_data.__dict__)

@pytest.fixture
def dummy_game_validator(dummy_game_data: GameData) -> GameValidator:
    return GameValidator(dummy_game_data)

