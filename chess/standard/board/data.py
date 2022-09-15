
from dataclasses import dataclass
from typing import TypeVar

from chess.board import BoardData


@dataclass(frozen=True)
class StandardBoardData(BoardData):
    pass


T = TypeVar('T', bound=StandardBoardData)
