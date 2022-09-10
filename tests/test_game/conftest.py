from dataclasses import dataclass, field
from typing import Set, Type

import pytest

from chess.game import GameData, GameFactory, GameInterface, GameValidator


@dataclass(frozen=True)
class DummyGameData(GameData):
    pass


class DummyGameFactory(GameFactory[DummyGameData]):
    @classmethod
    def create(cls, *args, **kwargs):
        return GameFactory[DummyGameData].create(*args, **kwargs)


class DummyGameInterface(GameInterface[DummyGameData]):
    pass


class DummyGameValidator(GameValidator[DummyGameData]):
    @classmethod
    def is_valid(cls, data, *args, **kwargs):
        return GameValidator[DummyGameData].is_valid(data=data, *args, **kwargs)

    @classmethod
    def validate(cls, data, *args, **kwargs):
        return GameValidator[DummyGameData].validate(data=data, *args, **kwargs)


@pytest.fixture
def dummy_game_data() -> DummyGameData:
    return DummyGameData()

@pytest.fixture
def dummy_game_factory(dummy_game_data: DummyGameData) -> GameFactory:
    return DummyGameFactory(dummy_game_data)

@pytest.fixture
def dummy_game_interface(dummy_game_data: DummyGameData) -> GameInterface:
    return DummyGameInterface(dummy_game_data)

@pytest.fixture
def dummy_game_validator(dummy_game_data: DummyGameData) -> GameValidator:
    return DummyGameValidator(dummy_game_data)

