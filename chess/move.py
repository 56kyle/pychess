

from dataclasses import dataclass, field
from typing import Set

from chess.position import Position
from piece import Piece


@dataclass(frozen=True)
class Move:
    piece: Piece
    start: Position
    end: Position
    captures: Set[Piece] = field(default_factory=set)
    promotes: Set[Piece] = field(default_factory=set)
    moves: Set['Move'] = field(default_factory=set)


