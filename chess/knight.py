
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.offset import Offset, UP, RIGHT, DOWN, LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta



class KnightMeta(PieceMeta):
    name: str = 'Knight'
    letter: str = 'N'
    value: int = 3
    symbol: str = '\u2658'
    html_decimal: str = '&#9822;'
    html_hex: str = '&#x2658;'
    offsets: Set[Offset] = field(default_factory=lambda: {
        UP * 2 + RIGHT,
        UP * 2 + LEFT,
        DOWN * 2 + RIGHT,
        DOWN * 2 + LEFT,
        RIGHT * 2 + UP,
        RIGHT * 2 + DOWN,
        LEFT * 2 + UP,
        LEFT * 2 + DOWN,
    })

    def get_move_paths(self) -> Set[Path]:
        return {Path(offset=offset, max_steps=1) for offset in self.offsets}

    def get_capture_paths(self) -> Set[Path]:
        return self.get_move_paths()


@dataclass(frozen=True)
class Knight(Piece):
    meta: KnightMeta = KnightMeta


