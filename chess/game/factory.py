from abc import ABC
from typing import TypeVar, Set, Type

from chess.board import BoardData
from chess.game.data import T, GameData
from chess.factory import AbstractFactory
from chess.piece import Piece


class GameFactory(AbstractFactory[T], ABC):
    data_type: T = GameData

    @classmethod
    def create(cls,
               board_data: BoardData,
               allowed_pieces: Set[Type[Piece]],
               allowed_promotions: Set[Type[Piece]],
               *args,
               **kwargs) -> T:
        return cls.data_type(
            board_data=board_data,
            allowed_pieces=allowed_pieces,
            allowed_promotions=allowed_promotions,
        )


F = TypeVar('F', bound=GameFactory)

