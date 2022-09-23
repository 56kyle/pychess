
from abc import ABC
from dataclasses import dataclass, field
from typing import TypeVar, Set, Type

from chess.board import BoardData
from chess.data import AbstractData
from chess.piece import Piece


@dataclass(frozen=True)
class GameData(AbstractData):
    board_data: BoardData
    allowed_pieces: Set[Type[Piece]]
    allowed_promotions: Set[Type[Piece]]


T = TypeVar('T', bound=GameData)

