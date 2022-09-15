from dataclasses import dataclass, field
from typing import Set, Type

import pytest

from chess.game import GameData, GameFactory, Game, GameValidator


@dataclass(frozen=True)
class DummyGameData(GameData):
    pass


class DummyGameFactory(GameFactory[DummyGameData]):
    @classmethod
    def create(cls, *args, **kwargs):
        return super().create(*args, **kwargs)


class DummyGameValidator(GameValidator[DummyGameData]):
    @classmethod
    def validate(cls, data: DummyGameData):
        return super().validate(data=data)


class DummyGame(Game[DummyGameData], DummyGameFactory[DummyGameData], DummyGameValidator[DummyGameData]):
    pass


@pytest.fixture
def dummy_game_data() -> DummyGameData:
    return DummyGameData()

@pytest.fixture
def dummy_game_factory(dummy_game_data: DummyGameData) -> GameFactory:
    return DummyGameFactory(dummy_game_data)

@pytest.fixture
def dummy_game_interface(dummy_game_data: DummyGameData) -> Game:
    return DummyGame(dummy_game_data)

@pytest.fixture
def dummy_game_validator(dummy_game_data: DummyGameData) -> GameValidator:
    return DummyGameValidator(dummy_game_data)

