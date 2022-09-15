from dataclasses import dataclass, field
from typing import Set, Type

import pytest

from chess.game import GameData, GameFactory, Game, GameValidator


@pytest.fixture
def dummy_game_data() -> GameData:
    return GameData()

@pytest.fixture
def dummy_game_factory(dummy_game_data: GameData) -> GameFactory:
    return GameFactory(dummy_game_data)

@pytest.fixture
def dummy_game(dummy_game_data: GameData) -> Game:
    return Game[GameData, GameFactory, GameValidator](**dummy_game_data.__dict__)

@pytest.fixture
def dummy_game_validator(dummy_game_data: GameData) -> GameValidator:
    return GameValidator(dummy_game_data)

